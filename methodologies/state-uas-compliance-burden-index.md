---
methodology_id: state-uas-compliance-burden-index
name: State-Level UAS Compliance Burden Index
version: 0.1.0
status: provisional
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

1. **Routine commercial AEC mission** — privately controlled site; ordinary mapping, survey support, inspection, documentation, or environmental data collection; no state-agency client or specially regulated facility.
2. **Public-agency project** — the same technically ordinary work performed for, contracted by, incorporated into, or conducted on property controlled by a state or public agency.
3. **Infrastructure or sensitive-site mission** — corridor, utility, transportation, critical-infrastructure, emergency-facility, correctional, or similarly regulated-site work for which the operator has an otherwise legitimate project purpose.

The scenarios hold federal compliance and ordinary competent program practices constant so the score isolates state-level differences.

## 4. Scoring dimensions and weights

Each reference mission receives a 0–5 rating on seven dimensions. The weights sum to 100.

| Dimension | Weight | Measurement question |
|---|---:|---|
| Operator prerequisites | 15 | Does the state add registration, licensing, fees, training, certification, or recurring operator filings? |
| Mission authorization and coordination | 15 | Does a mission require state permission, notice, consent, special-use authorization, or material advance coordination? |
| Operational restrictions | 20 | How broadly do state rules constrain otherwise legitimate flight, launch/landing, imaging, payload, location, timing, or use? |
| Privacy, data, and documentation | 15 | What additional collection, purpose, retention, disclosure, documentation, or evidentiary controls affect the mission? |
| Public-project and acquisition conditions | 10 | Do agency policy, contracting, cybersecurity, sourcing, procurement, or equipment conditions add project burden? |
| Regulatory complexity | 15 | How fragmented, conditional, ambiguous, exception-dependent, or difficult to administer is the applicable state framework? |
| Consequence exposure | 10 | For requirements materially applicable to the scenario, how significant are the state enforcement, civil, contractual, or operational consequences of error? |

### Common 0–5 anchor scale

| Rating | Anchor |
|---:|---|
| 0 | No material incremental state driver identified for the scenario. |
| 1 | Narrow, uncommon, or low-effort consideration with little effect on the ordinary workflow. |
| 2 | Limited recurring check or modest one-time action; manageable without material schedule or operating change. |
| 3 | Material planning, documentation, coordination, or constraint affecting a meaningful share of missions in the scenario. |
| 4 | Multiple common-mission controls, recurring administration, meaningful lead time, or substantial operating constraint. |
| 5 | Broad or pervasive state controls that create a recurring approval barrier, major workflow change, or severe restriction for the reference mission. |

The analyst must apply the anchor to the scenario and cite the requirement clusters supporting the rating. Record count is not a scoring input. One broad statewide requirement may outweigh numerous narrow prohibitions.

## 5. Calculation

For each reference mission:

```text
scenario_score = sum(dimension_rating / 5 * dimension_weight)
```

The headline composite uses fixed mission weights:

```text
composite_score =
    0.50 * routine_commercial_score
  + 0.30 * public_agency_score
  + 0.20 * infrastructure_sensitive_score
```

Scores are calculated by script from recorded integer ratings and published to one decimal place. The AI analyst supplies ratings, citations, and rationale; it does not manually calculate totals, percentiles, or rank.

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
- Do not count an exception as a separate burden; apply it to narrow the relevant cluster.
- Do not score public-agency-only controls against the routine private-site mission.
- Do not score voluntary guidance as a mandatory action. It may support a complexity observation only when its relationship to binding authority is accurately described.
- Do not score proposed or inactive authorities as current burden. Identify a material pending change separately.
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

The comparative source of truth will be `comparisons/state-compliance-burden.csv`. Generated JSON and website views are derivatives.

Each state result must preserve at least:

```text
state, state_abbr, research_cutoff_date, assessed_date,
methodology_version, role_id, role_version, model_checkpoint,
evidence_confidence, evidence_limitations,
routine_commercial_score, public_agency_score,
infrastructure_sensitive_score, composite_score, burden_band,
national_rank, national_percentile,
operator_prerequisites_rating, mission_authorization_rating,
operational_restrictions_rating, privacy_data_rating,
public_project_acquisition_rating, regulatory_complexity_rating,
consequence_exposure_rating,
summary, primary_record_ids, calibration_notes
```

The detailed assessment packet must also retain scenario-specific dimension ratings and requirement clusters, even if the public view presents a compact subset.

## 10. Presentation standard

Every published state result shows:

- composite score and descriptive band;
- all three reference-mission scores;
- component ratings;
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

## 12. Initial preflight requirement

This provisional methodology must not be used for the national assessment until the designated analyst role:

1. tests it against a deliberately varied sample of state records;
2. identifies ambiguous anchors, double-counting risks, missing fields, and scenario distortions;
3. documents proposed changes in a preflight report;
4. revises this document; and
5. freezes a version 1.0.0 methodology before nationwide scoring begins.

## 13. Revision history

- **0.1.0 — August 2, 2026:** Initial provisional specification defining scope, scenarios, dimensions, calculation, evidence gates, calibration, output, and change control. Requires analyst preflight before use.
