# Improvement Plan: Research Quality, Completeness Assurance, and Token Efficiency

**Repository:** `DWestobyGeo/uas-ai-regulatory-summary`  
**Plan date:** August 2, 2026  
**Intended use:** GitHub improvement issue and implementation roadmap

## Summary

Improve the reliability and efficiency of the state UAS regulatory research workflow without rebuilding the repository or abandoning its four-perspective product design.

The work will:

- distinguish legacy packets from current-method packets;
- make state research completeness machine-readable;
- evaluate semantic correctness in addition to file structure;
- prevent unsupported agency, legal, and operational boilerplate;
- route interpretation work only to materially relevant roles;
- measure token use and cost before setting reduction targets;
- eliminate duplicate drafting between the register and printable summaries;
- and retrofit existing states according to regulatory risk.

## Problem statement

The repository has strong governance, structured data, role ownership, and publication tooling. However:

1. current validators mainly prove structural completeness, not factual or semantic correctness;
2. GitHub Actions does not run every validator required by governance;
3. legacy and current-method states appear equally current on the public site;
4. research checklists are useful but not uniformly machine-readable or enforced;
5. requiring substantive AEC and legal commentary for every record encourages boilerplate;
6. the same authority content is maintained in both the source register and Markdown;
7. state `last_updated` is based on filesystem modification time rather than explicit research currency;
8. token, cost, retry, and cache-use data are not measured;
9. one objective change can cause unnecessary full-state regeneration.

## Goals

- Increase evidence fidelity and source-status accuracy.
- Demonstrate category-level research completeness.
- Detect unsupported process, permissions, fees, and legal recommendations.
- Preserve useful role-specific interpretation while removing filler.
- Reduce repeated prompt and output tokens.
- Support incremental currency updates.
- Provide transparent state-level maturity and freshness information.
- Preserve the existing website, data model, and AI-only disclaimer framework where practical.

## Non-goals

- Do not add municipal, county, tribal, federal-baseline, property-specific, or live-airspace research.
- Do not create a human publication-approval workflow.
- Do not redesign the website before the research pipeline is stabilized.
- Do not begin a nationwide burden ranking until the included states pass a common evidence gate.
- Do not immediately re-research all fifty states.
- Do not claim a token-reduction percentage before establishing a baseline.

# Workstream 0 — Establish the baseline

## Tasks

- [ ] Add run telemetry for every research, interpretation, and QA call.
- [ ] Record model provider and exact model ID.
- [ ] Record governance, role, prompt-template, and workflow versions.
- [ ] Record input, cached input, output, and reasoning tokens where available.
- [ ] Record cost, retries, latency, tool calls, and sources opened.
- [ ] Record state, phase, role, and record IDs.
- [ ] Add an objective-packet content hash.
- [ ] Add an interpretation-input hash.
- [ ] Capture the current cost and quality baseline for the pilot states.

## Suggested artifact

`runs/{run_id}.json`

## Acceptance criteria

- Every new agent run produces a machine-readable telemetry record.
- Token and cost totals can be summarized by state, phase, role, and record.
- Unchanged objective records can be identified by hash.

# Workstream 1 — Create a gold-standard pilot set

## Core pilot states

| State | Purpose |
|---|---|
| Washington | Legacy retrofit, obsolete or failed-authority detection, scope-gate cleanup |
| Oklahoma | Current-method sparse state; permission, consent, and agency-process distinctions |
| California | High-complexity statutes, agencies, permits, pending legislation |
| Minnesota | State registration/licensing, mixed public/private rules, citation ambiguity |
| Florida or Texas | Procurement/preemption and another distinctive regulatory pattern |

## Tasks

- [ ] Select the fifth pilot state based on the desired procurement/preemption test.
- [ ] Re-verify all retained objective records against current primary sources.
- [ ] Document inclusion and exclusion decisions.
- [ ] Create expected role-applicability results.
- [ ] Create expected controlled no-impact dispositions.
- [ ] Create known bad examples from actual repository failure modes.
- [ ] Create scoring rubrics for objective fidelity, status, scope, and interpretation.
- [ ] Preserve Washington’s historical provenance while marking corrected content as retrofit work.

## Acceptance criteria

- At least five states have a verified benchmark packet.
- The benchmark contains examples of current, future-effective, proposed, failed, repealed, secondary, negative, public-only, permit, consent, and no-process records.
- The benchmark is versioned and usable by automated evals.

# Workstream 2 — Make research completeness machine-readable

## Recommended approach

Create one state manifest per state rather than expanding the 33-field authority schema immediately.

## Suggested file

`States/XX_State/XX_UAS_Research_Manifest.yaml`

## Suggested fields

```yaml
state: Oklahoma
state_abbr: OK
method_version: 1.0.0
research_status: current_method_complete
last_full_research_date: 2026-08-02
last_currency_check: 2026-08-02
source_cutoff_date: 2026-08-02
legacy_retrofit_status: not_applicable
coverage:
  statutes:
    status: applicable_source_found
    sources_searched:
      - official state code
      - completed session laws
    unresolved: false
  administrative_rules:
    status: applicable_source_found
    unresolved: false
  executive_orders:
    status: reviewed_no_applicable_source
    unresolved: false
unresolved_count: 0
low_confidence_record_count: 0
primary_source_percentage: 100
```

## Tasks

- [ ] Define controlled values for category status and state research status.
- [ ] Convert the existing Markdown checklist content into manifests.
- [ ] Generate the human-readable checklist from the manifest, or validate exact agreement.
- [ ] Add state status to `docs/data/v1/index.json`.
- [ ] Display research status and currency on the website.
- [ ] Prevent `current_method_complete` unless every required category is resolved.

## Acceptance criteria

- All pilot states have valid manifests.
- The state index reports research status independently of record count.
- A state with an unresolved category cannot be presented as fully complete.
- Legacy status is visible to users.

# Workstream 3 — Expand deterministic validation

## New validator

`scripts/validate_research_semantics.py`

## Initial rules

- [ ] Fail when governance-required validators are omitted from CI.
- [ ] Flag a legislature or code publisher described as an application office.
- [ ] Flag “fee,” “application,” “permit,” “approval,” or “reviewer” language when the objective record establishes no such process.
- [ ] Flag a source classified as pending after the applicable legislative session has expired unless current status is explicitly verified.
- [ ] Flag negative findings or “none found” records in the authority register.
- [ ] Flag general statutes without a direct-UAS or official-UAS-application basis.
- [ ] Flag low-confidence records containing unqualified mandatory operating language.
- [ ] Flag agency or procurement commentary inconsistent with controlled N/A routing.
- [ ] Flag public-agency-only authorities interpreted as direct private-operator duties.
- [ ] Flag duplicate or highly similar interpretations across unrelated records.
- [ ] Validate manifest, register, generated JSON, and summary agreement.
- [ ] Validate explicit research dates rather than filesystem modification dates.

## CI changes

Update `.github/workflows/site-quality.yml` to run:

```text
python scripts/validate_roles.py
python scripts/validate_methodologies.py
python scripts/validate_phase2.py
python scripts/validate_research_manifests.py
python scripts/validate_research_semantics.py
python scripts/validate_site.py
```

## Acceptance criteria

- Actual known-bad Oklahoma-style boilerplate fixtures fail.
- Correct permit and no-process examples pass.
- CI runs all required checks on every relevant pull request.
- Warnings and errors are distinguished and not silently suppressed.

# Workstream 4 — Add layered agent evaluations

## Evaluation layers

### A. Deterministic grading

Use exact expected values for:

- source status;
- role applicability;
- public/private scope;
- permit/approval classification;
- effective dates;
- source type;
- controlled no-impact values.

### B. Rubric-based model grading

Grade:

- fidelity to objective evidence;
- unsupported inference;
- role relevance;
- conservative wording;
- distinction between mandatory and prudent actions;
- cross-role consistency;
- omission of material exceptions.

### C. Adversarial challenge pass

Require a separate context/model pass to challenge:

- proposed or failed bills;
- old unresolved records;
- secondary-source authorities;
- general laws with questionable UAS scope;
- criminal or felony restrictions;
- registration and permit rules;
- procurement/manufacturer restrictions;
- “no law found” conclusions.

### D. Sampled primary-source verification

Require:

- 100% challenge review of high-risk categories;
- a fixed sample of ordinary high-confidence records;
- rotating sample coverage across states.

## Suggested directory

```text
evals/
  README.md
  fixtures/
  pilot_states/
  rubrics/
  expected/
  results/
```

## Acceptance criteria

- At least twenty known failure-mode fixtures exist before nationwide retrofit.
- No pilot state has a blocking unsupported-process or wrong-status error.
- Eval results are versioned and comparable between workflow versions.

# Workstream 5 — Route interpretation roles by material relevance

## Routing output

For each record, classify:

```json
{
  "record_id": "OK-002",
  "aec_relevant": true,
  "agency_process_relevant": false,
  "procurement_relevant": false,
  "legal_analysis_relevant": true,
  "reasons": {
    "agency_process_relevant": "No government-administered application, registration, permit, waiver, or approval process."
  }
}
```

## Governance changes

Allow exact controlled no-material-impact values for AEC and legal roles in addition to the existing agency and procurement N/A values.

Suggested values:

- `No material AEC operational implication identified beyond the objective requirement.`
- `N/A — no agency process involved`
- `N/A — no procurement or equipment-selection implication identified`
- `No separate legal-risk implication identified beyond compliance with the stated authority.`

## Model allocation

- Use deterministic rules or a low-cost model for routing.
- Use the stronger research model only for materially relevant role outputs.
- Run a cross-role QA pass after all role outputs are assembled.

## Acceptance criteria

- Every substantive role output has a documented applicability reason.
- No role invents a process merely to avoid an empty field.
- Controlled no-impact values are used consistently and only when justified.
- Product presentation continues to show all four perspectives.

# Workstream 6 — Compile compact evidence packets and prompts

## Evidence packet

Provide each role only the necessary record-level input:

```json
{
  "record_id": "OK-002",
  "citation": "Okla. Stat. tit. 21, § 1743",
  "status": "Current / in force",
  "regulated_party": "Any UAS or drone operator",
  "regulated_activity": "Intentional surveillance, recording, private-property entry, or landing",
  "permit_or_approval_required": "Owner or lessee consent only for intentional landing",
  "public_agency_only": "No",
  "objective_summary": "...",
  "evidence_locator": "Official Title 21 PDF, pp. 813-814",
  "confidence_level": "High",
  "unresolved_questions": []
}
```

## Prompt construction

- Place stable governance and role rules at the beginning.
- Keep dynamic record content at the end.
- Use exact output schemas.
- Reuse stable prompt prefixes to support provider prompt caching.
- Do not pass website files, unrelated states, or unrelated role documents.
- Skip regeneration when the objective-packet hash is unchanged.

## Acceptance criteria

- Prompt size and cost are measured against the baseline.
- Quality on the pilot eval set does not decline.
- Cache-use data is captured where supported.
- Unchanged records are not regenerated.

# Workstream 7 — Make the source register the publication source of truth

## Tasks

- [ ] Generate authority headings, metadata, objective summaries, and four role bullets from the register.
- [ ] Keep state overview, cross-record synthesis, unresolved questions, and limited context as authored sections.
- [ ] Remove duplicated authority prose from manually maintained source Markdown.
- [ ] Add a generated-file warning to generated Markdown.
- [ ] Validate that website JSON and downloadable Markdown are produced from the same record set.

## Acceptance criteria

- Each authority fact and interpretation is maintained once.
- Editing a register record and rebuilding updates every publication format.
- Manual edits to generated authority sections fail validation.
- The public site and downloadable files cannot drift semantically.

# Workstream 8 — Correct currency metadata

## Tasks

- [ ] Stop using CSV filesystem modification time as substantive `last_updated`.
- [ ] Populate explicit research and review dates from the state manifest.
- [ ] Add `next_currency_review` based on risk.
- [ ] Add automatic recheck triggers for future-effective statutes and pending legislation.
- [ ] Add URL-health checks without treating URL availability as proof of current legal status.

## Suggested review frequency

| Record type | Review cadence |
|---|---|
| Future-effective or pending | Event-triggered plus monthly |
| Procurement/manufacturer/security | Quarterly |
| Registration, licensing, permits | Semiannual |
| Stable codified criminal/civil statutes | Annual |
| Low-confidence or secondary-source | Until resolved, then normal cadence |
| Negative finding | Annual and after legislative session |

## Acceptance criteria

- Public freshness dates correspond to research activity.
- Future-effective records create a scheduled recheck.
- Pending and low-confidence records cannot silently age indefinitely.

# Workstream 9 — Retrofit the national dataset by risk

## Tier 1 — Immediate

- Legacy states
- Proposed/pending/failed/superseded records
- Low-confidence records
- Criminal/felony restrictions
- Registration, licensing, permit, and procurement restrictions
- Secondary-source controlling records
- States with unresolved checklist categories

## Tier 2 — High complexity

- States with many authorities
- States lacking broad preemption
- States with multiple agency permit systems
- States with significant public-agency or procurement restrictions

## Tier 3 — Recent clean states

- Recent current-method states with high primary-source coverage and no unresolved categories

## Tasks

- [x] Generate a retrofit-risk score. (`scripts/compute_retrofit_risk.py`)
- [x] Publish a transparent retrofit queue. (`planning/national_retrofit_queue.md`, regenerate after any register/checklist change)
- [ ] Process one state per substantive research commit.
- [ ] Preserve stable record IDs when the same authority remains.
- [ ] Re-run dependent interpretations only when objective meaning changes.

## Acceptance criteria

- Retrofit order is risk-based and documented.
- Legacy states are visibly distinguished until reviewed.
- Corrections preserve record-level change history.
- No full national rerun is required for isolated record updates.

# Proposed implementation phases

## Phase A — Baseline and pilot

Complete Workstreams 0 and 1. Do not alter all fifty states.

## Phase B — Quality gates

Complete Workstreams 2, 3, and 4 for pilot states. Update CI.

## Phase C — Efficiency changes

Complete Workstreams 5 and 6. Compare cost and quality with the baseline.

## Phase D — Publication normalization

Complete Workstreams 7 and 8.

## Phase E — National retrofit

Apply Workstream 9 according to the risk queue.

# Definition of done

This improvement request is complete when:

- [ ] all pilot states have structured research manifests;
- [ ] legacy and current-method status is visible;
- [ ] CI runs all required validators;
- [ ] known unsupported-process examples fail automated evaluation;
- [ ] role applicability is recorded before interpretation;
- [ ] controlled no-impact values are authorized and validated;
- [ ] token and cost telemetry exists;
- [ ] compact evidence-packet prompts pass the pilot eval set;
- [ ] authority sections are generated from the register;
- [ ] substantive freshness dates no longer use file modification time;
- [ ] the national retrofit queue is published and underway;
- [ ] burden-index publication is gated on states meeting the common evidence standard.

# Recommended issue title

**Improve research quality, completeness assurance, and token efficiency**

# Recommended labels

- `enhancement`
- `research-quality`
- `agent-workflow`
- `technical-debt`
