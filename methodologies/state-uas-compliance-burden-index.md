---
methodology_id: state-uas-compliance-burden-index
name: State-Level UAS Compliance Burden Index
version: 1.0.0
status: active
last_updated: 2026-08-02
governance: ../Agent_Instructions.v6.md
intended_owner_role: state-uas-regulatory-burden-analyst
unit_of_analysis: state-by-reference-mission
source_data: verified objective fields in the 50 state source registers
---

# State-Level UAS Compliance Burden Index Methodology

## 1. Purpose

The State-Level UAS Compliance Burden Index (SCBI) is a comparative assessment of the incremental state and state-agency compliance effort affecting commercial small-UAS work conducted under the federal Part 107 baseline. It is designed for architecture, engineering, environmental, surveying, GIS, construction, infrastructure-inspection, and aerial-mapping users.

The index answers a bounded question:

> Relative to the same federally compliant reference mission in other states, how much additional state-level compliance effort, coordination, constraint, and exposure does this state create?

The index is not legal advice, flight clearance, a measure of FAA or live-airspace difficulty, or a judgment that a state is good or bad for UAS operations.

## 2. Scope boundary

### Included

- Enacted state statutes, current state regulations, controlling state cases, executive actions, attorney-general materials, and current state-agency policies retained in the verified source register.
- State requirements that apply directly to commercial operators.
- State requirements that become relevant because work is performed for, on behalf of, or on property controlled by a public agency.
- State-specific privacy, property, infrastructure, wildlife, public-land, registration, licensing, procurement, data, and enforcement implications within repository scope.
- State allocation or preemption of local authority, but only as established by state-level evidence.

### Excluded

- The common federal Part 107 baseline, except where a state authority expressly incorporates it in a way that changes state consequences or workflow.
- Federal land-manager, tribal, county, municipal, site-specific property, client-specific, and live-airspace requirements.
- Terrain, weather, travel logistics, technical mission difficulty, or ordinary business cost unrelated to a state requirement.
- Proposed, failed, repealed, superseded, or merely discoverable material as a current burden driver.

The absence of local-jurisdiction research must never be described as an absence of local requirements.

## 3. Unit of analysis and reference missions

The primary unit is a **state-by-reference-mission assessment**, not an individual source record. Records expressing the same practical obligation are consolidated into one requirement cluster before scoring.

Each state is evaluated under three reference missions:

1. **Routine commercial AEC mission** — privately controlled, non-sensitive site; ordinary mapping, inspection, documentation, or environmental data collection; no state-agency client and no regulated professional deliverable assumption.
2. **Public-agency project** — technically ordinary work performed for or on ordinary property controlled by a state or public agency; no critical-infrastructure or other sensitive-site condition.
3. **Infrastructure or sensitive-site mission** — privately operated or owner-authorized corridor, utility, transportation, critical-infrastructure, emergency-facility, correctional, or similarly regulated-site work; no public-agency procurement condition unless the authority expressly reaches the commercial contractor.

The scenarios hold federal compliance, ordinary competent program practices, client authorization, and necessary property access constant so the score isolates state-level differences. A state-specific form, proof, notice, lead time, or approval path beyond ordinary authorization remains scoreable.

The three profiles are comparison constructs, not claims about the actual distribution of commercial work. Their fixed weights define a **reference portfolio** for the headline index.

## 4. Scoring dimensions and weights

Each reference mission receives a 0–5 rating on six burden dimensions. The weights sum to 100.

| Dimension | Weight | Measurement question |
|---|---:|---|
| Operator prerequisites | 20 | Does the state add registration, licensing, fees, training, certification, or recurring operator filings? |
| Mission authorization and coordination | 20 | Does a mission require state permission, notice, consent, special-use authorization, or material advance coordination? |
| Operational restrictions | 25 | How broadly do state rules constrain otherwise legitimate flight, launch/landing, imaging, payload, location, timing, or use? |
| Privacy, data, and documentation | 15 | What additional collection, purpose, retention, disclosure, documentation, or evidentiary controls affect the mission? |
| Public-project and acquisition conditions | 10 | Do agency policy, contracting, cybersecurity, sourcing, procurement, or equipment conditions add project burden? |
| Regulatory complexity | 10 | How fragmented, conditional, exception-dependent, or difficult to administer is the applicable state framework? |

### Dimension-specific anchors

| Dimension | 0 | 1 | 3 | 5 |
|---|---|---|---|---|
| Operator prerequisites | No incremental state prerequisite. | Narrow, one-time, or rarely applicable administrative check. | One material recurring statewide prerequisite, or multiple conditional prerequisites, affecting the scenario. | Multiple recurring statewide prerequisites, renewals, or fees that materially gate ordinary scenario operations. |
| Mission authorization and coordination | No incremental state mission authorization. | Rare or narrowly site-specific contact with negligible lead time. | Approval, notice, or coordination applies to a meaningful mission class and can affect mobilization. | Broad recurring approval or multi-party coordination materially gates most missions in the scenario. |
| Operational restrictions | No material incremental restriction. | Narrow intent-based misconduct or uncommon-location restriction with little legitimate-project effect. | A restriction affects common sites, activities, sensors, or methods and requires meaningful replanning. | Broad restrictions prevent or fundamentally reconfigure most otherwise legitimate missions in the scenario. |
| Privacy, data, and documentation | No UAS-specific incremental control identified. | Narrow intent-based or uncommon-use control satisfied by ordinary legitimate-purpose practice. | Purpose, consent, collection, retention, disclosure, or documentation controls affect a meaningful share of scenario missions. | Broad recurring controls materially change collection design, data handling, documentation, or deliverables for most scenario missions. |
| Public-project and acquisition conditions | No applicable state condition. | Internal agency condition not normally reaching a commercial contractor, or a narrow product concern. | Contractor, equipment, cybersecurity, sourcing, or project conditions materially affect a meaningful share of scenario work. | Broad vendor or fleet eligibility, equipment replacement, or contract-flow-down requirements materially gate most scenario work. |
| Regulatory complexity | Applicable state framework is explicit, concentrated, and has no material state-created branching. | Few clear authorities or exceptions; applicability is readily resolved. | Multiple agencies, conditional exceptions, site regimes, or state-created decision branches require material analysis. | Pervasive fragmentation or interdependent state processes make ordinary applicability and sequencing difficult even with complete evidence. |

Ratings 2 and 4 are used only when the evidence falls demonstrably between the adjacent anchors; the rationale must state why neither neighboring anchor fits. The analyst must apply the anchor to the scenario and cite the requirement clusters supporting the rating. Record count is not a scoring input. One broad statewide requirement may outweigh numerous narrow prohibitions.

### Companion consequence indicator

Each scenario also receives a 0–5 **consequence exposure** indicator. It is published beside the burden score but is not included in the 0–100 index:

- **0:** no material state-specific consequence identified for plausible scenario conduct;
- **1:** narrow or low-level administrative, contractual, or civil consequence;
- **3:** meaningful civil, misdemeanor, contract, or operational consequence for a plausible compliance error; and
- **5:** severe criminal, civil, disqualification, or operational consequence for a plausible mission-relevant error.

Use 2 or 4 only with an explanation between adjacent anchors. Severe consequences for rare intentional misconduct do not increase level-of-effort ratings unless they create an actual preventive action, documentation step, or operating constraint for the legitimate reference mission.

## 5. Calculation

For each reference mission:

```text
scenario_score = sum(dimension_rating / 5 * dimension_weight)
```

The headline **reference-portfolio composite** uses fixed mission weights:

```text
composite_score =
    0.50 * routine_commercial_score
  + 0.30 * public_agency_score
  + 0.20 * infrastructure_sensitive_score
```

These normative weights are part of the index definition, not an estimate of any user's actual project mix. Scores are calculated by script from recorded integer ratings and published to one decimal place. The AI analyst supplies ratings, citations, and rationale; it does not manually calculate totals, percentiles, or rank.

### Fixed descriptive bands

| Composite score | Band |
|---:|---|
| 0.0–19.9 | Minimal |
| 20.0–39.9 | Low |
| 40.0–59.9 | Moderate |
| 60.0–79.9 | Elevated |
| 80.0–100.0 | High |

These are absolute rubric bands, not quotas. Do not alter thresholds to create a preferred distribution.

National percentile and rank are secondary comparative statistics calculated only from states assessed under the same methodology version and common research cutoff. Tied composite scores receive the same rank.

## 6. Requirement clustering and applicability

Before rating a state, the analyst creates an internal requirement-cluster table containing:

- cluster ID and concise obligation;
- supporting `record_id` values;
- current legal or policy status;
- affected parties and activities;
- applicable reference missions;
- direct requirement, conditional requirement, prohibition, exception, guidance, or consequence;
- burden mechanism, such as time, fee, documentation, equipment, coordination, constraint, or uncertainty; and
- confidence and unresolved evidence.

Rules for clustering and applicability:

- Consolidate duplicate, overlapping, and implementation records that express one practical obligation.
- Preserve separate clusters when obligations create independently required actions.
- Do not sum mutually exclusive property or institution policies as though one mission must satisfy all of them. Rate the breadth and representative applicable burden of the scenario, and identify exceptional sites separately.
- Do not count an exception as a separate burden; apply it to narrow the relevant cluster.
- Do not score public-agency-only controls against the routine private-site mission.
- Do not score voluntary guidance as a mandatory action. It may support a complexity observation only when its relationship to binding authority is accurately described.
- Do not score proposed or inactive authorities as current burden. Identify a material pending change separately.
- Do not score acquisition-method-neutral professional licensing, competency, or deliverable obligations unless state evidence creates an incremental UAS-specific action or restriction.
- When a state authority incorporates a federal requirement, score only the incremental state action or state consequence; do not count the common federal step again.
- Hold ordinary client authorization and property access constant. Score additional state-specified proof, form, notice, timing, decision maker, or restriction.
- Affirmative state preemption may reduce state-created complexity when supported by current authority. Absence of preemption, or failure to locate it, does not prove and must not proxy for unresearched local burden.
- Do not assume property permission, client authorization, or FAA approval cures a state prohibition unless the source says so.

## 7. Evidence readiness and confidence

A state is eligible for a published score only when:

- its Phase 1 objective packet is complete under the repository governance;
- retained records have stable IDs and the required objective fields;
- material current authorities have usable citations and URLs;
- applicability can be resolved for all three reference missions; and
- material unresolved issues would not plausibly change a dimension by more than one rating point.

If a material gap fails this gate, publish **Not rateable — objective evidence incomplete** and list the missing evidence. Do not convert missing evidence to a zero.

For rateable states, confidence describes evidence support rather than the analyst's personal certainty:

- **High:** current evidence is substantially complete, material drivers are directly supported, and no unresolved issue is likely to change a dimension rating.
- **Moderate:** the score is supportable, but source access, currency, ambiguity, or a bounded coverage issue could change one or more ratings by one point.
- **Low:** reserved for a provisional internal result; a low-confidence score is not published as a national comparison.

Do not present statistical confidence intervals. The index is an anchored ordinal assessment, not an empirical estimate from a probability sample.

## 8. Cross-state calibration and statistical checks

The first national run uses two passes:

1. **Independent state pass:** Apply the fixed rubric without using a desired rank or distribution.
2. **Calibration pass:** Compare dimension neighbors and outliers, then correct only demonstrable inconsistency, double-counting, or applicability error. Record every changed rating and reason.

Required diagnostics include:

- dimension and composite distributions;
- median and interquartile range;
- states outside 1.5 interquartile ranges, reviewed as possible—not presumed—errors;
- tied scores and compressed dimensions;
- rank sensitivity to equal mission weights and to a one-point change in any single dimension; and
- correlation between record count and score, investigated for count-driven bias.

An unexpected result is not grounds for changing a rating. Evidence and the fixed anchors control.

## 9. Published result and data contract

The scoring source of truth will be the long-form `comparisons/scbi-assessments.csv`, with one row per state, reference mission, and dimension. It must retain:

```text
state, state_abbr, scenario_id, dimension_id, included_in_score,
rating, rationale, primary_record_ids, requirement_cluster_ids,
evidence_confidence, evidence_limitations,
research_cutoff_date, assessed_date,
methodology_version, role_id, role_version, model_checkpoint,
calibration_status, prior_rating, calibration_notes
```

The six burden dimensions use `included_in_score=true`. The companion consequence indicator uses `included_in_score=false`.

`comparisons/state-compliance-burden.csv`, generated JSON, website views, ranks, percentiles, and bands are calculated derivatives. The generated state result must include all three scenario scores, the reference-portfolio composite, band, rank, percentile, confidence, concise summary, and provenance.

The detailed state assessment packet additionally retains the requirement clusters and any future-change note. A compact public view may omit internal clustering detail but may not omit the three scenario scores, evidence confidence, scope qualification, or provenance.

## 10. Presentation standard

Every published state result shows:

- reference-portfolio composite score and descriptive band;
- all three reference-mission scores;
- component ratings;
- the separate consequence-exposure indicator;
- national percentile or rank only when nationally comparable;
- evidence confidence and material limitation;
- a concise explanation of the principal burden drivers and counterweights;
- links to cited state records and their existing sources; and
- methodology, role, model, assessment-date, and research-cutoff provenance.

Do not label a score as the difficulty of flying in the state without the qualifier **state-level compliance burden**.

## 11. Change control

- A changed state authority triggers reassessment of the affected state, then recalculation of national rank and percentile.
- A changed rating must cite the affected cluster and record IDs and state why the prior rating no longer fits the anchor.
- A methodology clarification that cannot change a score increments the patch version.
- A scoring-anchor, weight, scenario, scope, calculation, or eligibility change increments at least the minor version and requires an impact assessment.
- A materially redefined index increments the major version.
- States compared in one published ranking must use the same methodology version. If a methodology change can affect results, rescore every state before publishing the new national comparison.
- Never rewrite historical provenance to imply that a newer method or role produced an older result.

## 12. Initial preflight disposition

The designated analyst tested provisional v0.1.0 against eight deliberately varied state packets. The [preflight report](preflight/scbi-v0.1-preflight.md) documents ambiguous anchors, double-counting risks, scenario distortions, data-contract corrections, and the changes adopted here.

Version 1.0.0 is frozen for the initial national assessment. Freezing the method does not authorize scoring or publication until the evidence-readiness and common-research-cutoff gates are verified.

## 13. Revision history

- **1.0.0 — August 2, 2026:** Completed the required analyst preflight; added dimension-specific anchors; separated consequence exposure from compliance effort; clarified mutually exclusive reference missions and the reference-portfolio composite; added authorization, alternative-site, professional-practice, federal-incorporation, preemption, and inactive-authority rules; and corrected the data contract to preserve scenario-specific ratings. Frozen for the initial national assessment, subject to its readiness gates.
- **0.1.0 — August 2, 2026:** Initial provisional specification defining scope, scenarios, dimensions, calculation, evidence gates, calibration, output, and change control. Requires analyst preflight before use.
