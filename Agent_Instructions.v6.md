# State UAS Research Governance

**Purpose:** Repository-wide governance for AI-generated, state-level commercial UAS research and interpretation serving architecture, engineering, environmental consulting, surveying, GIS, construction, infrastructure inspection, and aerial-mapping users.

**Status:** Active. Research or revision begins only when assigned.

**Governance version:** 6.2.0 — August 2, 2026

**Compatibility note:** The filename remains `Agent_Instructions.v6.md` so existing state provenance, links, and automation continue to work. Role-specific operating instructions now live in [`agents/roles/`](agents/roles/).

---

## 1. Governance hierarchy

Apply instructions in this order:

1. the user's current assignment and explicit product decisions;
2. this governance document;
3. the active role document in [`agents/roles/`](agents/roles/);
4. repository data contracts, design-system rules, and validators; and
5. task-specific implementation judgment that does not conflict with the above.

If two documents conflict, stop the conflicting action, identify both instructions, and resolve the conflict at the highest applicable level. Do not silently choose the more convenient rule.

## 2. Product purpose and priorities

This repository is an **AI research and interpretation tool only**. It is not legal advice, flight clearance, mission approval, or a human-reviewed compliance system.

The product should help an experienced commercial UAS program user:

- identify state and state-agency requirements relevant to UAS work;
- distinguish authority, status, applicability, and confidence;
- trace material conclusions to cited evidence;
- compare four clearly labeled AI interpretation perspectives;
- print or download a state reference; and
- maintain structured records for national aggregation and later GIS use.

When priorities compete, use this order:

1. objective accuracy, evidence integrity, and completeness;
2. conservative and useful interpretation grounded in the objective packet;
3. reproducible updates, provenance, and revision transparency;
4. consistent structured data and publication artifacts;
5. efficient token and maintenance cost;
6. accessibility, navigation, and readability; and
7. visual polish.

Do not add human-review gates, approval queues, signoff states, or claims that a professional reviewed the output. Users may independently choose any external review appropriate to their work.

Do not name or tailor the repository to a specific AEC company, client, or employer. Use organization-neutral language such as `commercial AEC consultant`.

## 3. Research scope

### 3.1 In scope

Research state-level and state-agency authorities that specifically regulate, authorize, restrict, guide, or materially affect UAS use, including:

- statutes, session laws, and administrative rules;
- UAS-specific executive orders, state decisions, and attorney general opinions;
- state aviation, transportation, parks, public-land, wildlife, forestry, and natural-resource requirements;
- corrections, public-safety, emergency-scene, and critical-infrastructure restrictions;
- UAS-specific privacy, surveillance, harassment, trespass, interference, hunting, or fishing provisions;
- state permits, registrations, notices, approvals, and agency procedures;
- state and public-agency procurement, manufacturer, country-of-origin, component, equipment, or cybersecurity restrictions;
- UAS-specific professional-licensing-board material; and
- state preemption provisions defining the state/local regulatory boundary.

The AEC use context includes surveying, photogrammetry, LiDAR, mapping, construction documentation, quantities, corridor work, inspection, thermal imaging, environmental monitoring, emergency documentation, and public-agency projects.

### 3.2 Scope gate

Include a generally worded authority only when its text contains a direct UAS provision or an official source expressly applies it to UAS. General theoretical relevance to photography, privacy, property, contracting, cybersecurity, surveying, engineering, or professional practice is insufficient.

### 3.3 Deferred scope

The current program does not research municipal, county, tribal, property-specific, federal-baseline, or live-airspace requirements. State preemption remains in scope because it is a state authority, but it does not authorize local-ordinance research.

FAA rules are the nationwide baseline. Do not restate routine Part 107 requirements unless a state source expressly relies on them or changes their practical application.

## 4. Roles and ownership

Every active role has a versioned operating document with common ownership and change-control metadata.

| Role | Owns | Operating instructions |
|---|---|---|
| Research Expert | Objective evidence, checklist, source-register metadata, objective summary, contextual items | [`agents/roles/research-expert.md`](agents/roles/research-expert.md) |
| AEC Industry UAS Expert | AEC program and field interpretation | [`agents/roles/aec-industry-uas-expert.md`](agents/roles/aec-industry-uas-expert.md) |
| Agency Practitioner | Agency process interpretation or governed N/A disposition | [`agents/roles/agency-practitioner.md`](agents/roles/agency-practitioner.md) |
| UAS Procurement Expert | Equipment, software, service, security, acquisition, and fleet interpretation or governed N/A disposition | [`agents/roles/uas-procurement-expert.md`](agents/roles/uas-procurement-expert.md) |
| AEC Industry Legal Counsel | AI-generated legal-risk, contract, documentation, liability, and escalation interpretation | [`agents/roles/aec-industry-legal-counsel.md`](agents/roles/aec-industry-legal-counsel.md) |
| State UAS Regulatory Burden Analyst | Cross-state, scenario-based compliance-burden assessment and calibration | [`agents/roles/state-uas-regulatory-burden-analyst.md`](agents/roles/state-uas-regulatory-burden-analyst.md) |
| Editorial and QA Reviewer | Independent review, issue ownership, schema and publication consistency | [`agents/roles/editorial-qa-reviewer.md`](agents/roles/editorial-qa-reviewer.md) |
| Web UX/UI and Editorial Agent | Static-site presentation, navigation, hyperlinks, accessibility, and print behavior | [`agents/roles/web-ux-ui-editor.md`](agents/roles/web-ux-ui-editor.md) |

The role directory and reusable metadata template are documented in [`agents/roles/README.md`](agents/roles/README.md).

An agent may perform more than one role in a task only when the assignment permits it. The agent must still respect field ownership, run each role as a distinct pass, and document the role version used. QA should be independent of drafting reasoning when practical.

## 5. Authoritative repository artifacts

### 5.1 Source of truth

For each state, the authoritative research files live under `States/XX_State_Name/`:

```text
XX_UAS_Research_Checklist.md
XX_UAS_Source_Register.csv
XX_UAS_Regulatory_Summary.md
Sources/                         # optional, only when useful and permitted
```

The source register is the structured research source of truth. The printable summary must agree with it.

`build_data.py` creates JSON and downloadable mirrors under `docs/data/v1/`. Generated JSON and mirrors are never edited by hand.

The public site uses one shared presentation layer under `docs/`; states provide data, not state-specific HTML or CSS.

### 5.2 Coverage checklist

The Research Expert records a result for each required category:

- `Applicable source found`
- `Reviewed — no applicable UAS-specific source located`
- `Unresolved — additional verification required`
- `Not applicable`

Negative research findings normally belong in the checklist, not as source-register records or authority sections.

### 5.3 Source register schema

All records use these 33 fields in this order:

`record_id, state, state_abbr, state_fips, jurisdiction_name, jurisdiction_type, geographic_scope, issuing_authority, source_title, citation, source_type, effective_date, revision_date, status, binding_level, uas_topic, regulated_party, regulated_activity, requirement_type, permit_or_approval_required, public_agency_only, commercial_operator_relevance, aec_relevance, summary, practical_interpretation_aec_expert, practical_interpretation_agency_practitioner, practical_interpretation_uas_procurement_expert, practical_interpretation_legal_counsel, source_url, date_accessed, confidence_level, verification_status, notes`

One record represents one distinct authority or materially separate official policy. Do not combine unrelated authorities or split repeated pointer pages into separate records.

## 6. Program phases and gates

### Phase 1 — Objective Research

The Research Expert completes the coverage checklist and every objective field. The four interpretation fields contain the exact placeholder `PENDING — Phase 2`.

Phase 1 is complete only when all coverage categories are resolved or explicitly marked unresolved, material sources are verified and deduplicated, and the state files pass the schema and site-data validators.

### Phase 2 — Practical Interpretation

After the objective packet is complete, the four interpretation roles each perform one batched state pass. They replace every placeholder without changing objective fields.

Each interpretation is normally one to three sentences. A longer opinion is allowed when a material ambiguity, multi-step process, phased requirement, or competing operational consideration cannot be responsibly explained within that norm. Length alone never substitutes for substance.

Only these exact N/A dispositions are governed:

- Agency Practitioner: `N/A — no agency process involved`
- UAS Procurement Expert: `N/A — no procurement or equipment-selection implication identified`

The AEC and legal roles provide a substantive disposition for every retained record.

### Phase 3 — QA and Retrofit

The Editorial and QA Reviewer checks evidence-to-summary fidelity, role applicability, field ownership, schema, provenance, generated artifacts, and publication consistency. A nonempty field or N/A marker is not sufficient proof of quality.

QA identifies the owning role for substantive corrections. If an objective change affects an interpretation, all dependent role fields must be reconsidered.

### Phase 4 — Comparative Assessment

After the objective and interpretation work reaches a common national research cutoff, the State UAS Regulatory Burden Analyst may apply the active [State-Level UAS Compliance Burden Index methodology](methodologies/state-uas-compliance-burden-index.md). This is a state-level downstream assessment, not a fifth per-record interpretation, and it does not change the 33-field source-register schema.

A national comparison may be published only when every included state passes the methodology evidence gate and uses the same methodology version. Provisional method testing and incomplete comparisons must remain clearly labeled and must not be presented as national rankings.

## 7. Evidence governance

- Prefer current official primary authority and canonical government URLs.
- A reputable normalized legal publisher is acceptable when an official site is inaccessible or impractical to parse. Label it accurately, verify currency and citation when possible, and do not assume it links to the primary source.
- Secondary compilations, news, trade press, and search results may discover leads or support clearly labeled Non-Regulatory Context; they do not control material legal conclusions.
- Review the underlying text. Do not rely on snippets or AI summaries.
- Distinguish binding law, executive orders, decisions, opinions, official policy, permit/property requirements, guidance, proposed authority, and repealed/superseded material.
- Do not describe guidance as law or low-confidence material as settled.
- Use `Unknown` or `Unresolved` rather than guessing.
- Do not infer that no authority exists merely because a search failed.

Confidence means:

- **High:** current primary authority directly supports the conclusion;
- **Moderate:** official or primary material supports it but interpretation or a source limitation remains; and
- **Low:** evidence is incomplete, conflicting, inaccessible, outdated, or not independently verified.

## 8. Change control and revision history

Git history provides repository-level revision history; record metadata and notes provide record-level explanation. Both are required for material updates.

### 8.1 Objective record changes

- Preserve `record_id` when updating the same authority.
- Recheck the controlling evidence and update every affected field.
- Update `revision_date`, `date_accessed`, `verification_status`, `confidence_level`, citation, URL, status, and notes as applicable.
- Explain a material amendment, supersession, conflict, reclassification, or removal in `notes` and/or the checklist.
- Do not erase a superseded authority merely to make the register appear current; classify it and connect the successor when it remains materially useful.

### 8.2 Interpretation changes

- Each role changes only its governed field and matching printable-summary bullet.
- Identify the affected record ID and role version in the handoff.
- Do not claim that a newly created role document governed historical work. Provenance records the instructions actually used.
- An objective change that alters meaning triggers reconsideration of all four interpretation fields.

### 8.3 Document provenance

Every printable state summary includes, directly below its title:

- intended audience;
- research date;
- document version and phase;
- model/checkpoint, using `not recorded` rather than guessing;
- interpretation scope or role-scope version actually used; and
- scope note.

For new or materially revised work under the separate role documents, record the applicable role IDs and versions in the process note or handoff. Do not retroactively rewrite historical provenance.

### 8.4 Commits and concurrent work

- Fetch and compare with the current remote branch before committing assigned state work.
- Normally use one state per research commit. A shared governance, schema, build, validation, or UI change may span states when its purpose is repository-wide.
- Keep unrelated user changes intact.
- Rebuild generated data after source changes and include the matching generated artifacts.
- Commit and push only when authorized by the assignment.

## 9. Interpretation governance

Practical interpretations must be useful, conservative, and grounded in the verified packet.

- Do not invent an exception, consent process, approval mechanism, defense, burden, retention requirement, or contract flow-down.
- Do not state that permission cures a prohibition unless the authority says so.
- Use `must` for actual requirements; use `consider`, `confirm`, `coordinate`, or `escalate` for prudent recommendations.
- Distinguish private operators, public agencies, public purchasers, property owners, and institutional programs.
- Do not name or recommend a product, declare equipment compliant, or infer origin/security from brand reputation.
- Treat lists, country-of-origin determinations, components, cybersecurity approvals, phased dates, and grandfathering as time-sensitive.
- Do not turn confidence into a legal-to-fly result.

The specialized role documents contain the full operating rules for their fields.

## 10. Printable summary and non-regulatory context

The printable Markdown is a concise human-readable briefing derived from the source register. It contains:

1. State UAS Regulatory Overview
2. Statewide UAS Laws and Regulations
3. State Agency UAS Requirements
4. Non-Regulatory Context, when material
5. Unresolved Operational Questions, when material

Each authority contains an objective summary followed by the four labeled AI perspectives. Do not create full authority sections for `no source found` results.

Non-Regulatory Context is clearly disclaimed, dated, linked, state-specific, and normally limited to three to six useful items. It does not create source-register records or legal conclusions.

## 11. Website and link governance

The public website is a presentation of the research, not an independent research source. The web role may improve structure, navigation, hyperlinks, accessibility, filtering, and printing but may not change objective or subjective meaning.

Internal anchors and source links should be useful and restrained. Link to cited URLs already present in the data; do not infer or research substitute URLs through the presentation layer. Preserve source classification and avoid implying that every linked publisher is an official source.

See [`agents/roles/web-ux-ui-editor.md`](agents/roles/web-ux-ui-editor.md) and [`docs/DESIGN_SYSTEM.md`](docs/DESIGN_SYSTEM.md).

## 12. Required quality gates

Before completing assigned work, run the applicable checks and confirm:

- scope and role ownership were respected;
- material objective claims have traceable evidence;
- status, applicability, dates, citations, confidence, and source type are accurate;
- state-agency rules are not presented as private requirements;
- interpretations are substantive, role-specific, and source-grounded;
- exact N/A values are used only when appropriate;
- record IDs and the 33-field schema remain valid;
- summary, register, generated JSON, and downloadable mirrors agree;
- role/model provenance is recorded without guessing;
- no company-specific language, human-review workflow, or flight-clearance claim was introduced;
- `python build_data.py` was run after source changes;
- `python scripts/validate_phase2.py` and `python scripts/validate_site.py` pass when applicable; and
- remaining warnings or unresolved issues are reported rather than hidden.

## 13. Revision history

- **6.2.0 — August 2, 2026:** Added the State UAS Regulatory Burden Analyst and a gated Phase 4 for comparative state-level assessment under a separate versioned methodology; preserved the 33-field authority schema and prohibited partial provisional work from being presented as a national ranking.
- **6.1.0 — August 2, 2026:** Converted the former mixed governance/role document into high-level governance; established individual versioned role documents and common role metadata; formalized field ownership, role-version provenance, and record-change documentation; retained the state/state-agency scope and AI-only product boundary; and clarified acceptable use of normalized legal publishers.
- **6.0 — August 2, 2026:** Added the procurement role, 33-field schema, Phase 2 authorization, one-to-three-sentence norm with justified exceptions, model provenance, and substantive QA applicability checks; consolidated prior amendments.
