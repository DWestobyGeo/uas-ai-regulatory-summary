# SCBI v0.1 Methodology Preflight

**Assessment type:** Methodology preflight; no publishable state scores produced

**Draft tested:** State-Level UAS Compliance Burden Index v0.1.0

**Role used:** `state-uas-regulatory-burden-analyst` v1.0.0

**Model / checkpoint:** GPT-5 Codex

**Date:** August 2, 2026

**Result:** Revise and freeze methodology v1.0.0 before national assessment

## 1. Purpose

This preflight tested whether the provisional methodology could be applied consistently to materially different state packets without counting records, unresearched local rules, general professional practice, or penalty severity as compliance effort. It was a rubric and data-contract test, not an attempt to rank the sample states.

## 2. Deliberately varied sample

| State | Reason selected | Illustrative records tested |
|---|---|---|
| California | Site-specific permits, professional-practice material, pending items, and mixed confidence | `CA-006`, `CA-008`–`CA-014` |
| Minnesota | Stacked statewide registration and commercial-operator licensing plus property approvals | `MN-003`–`MN-005`, `MN-008` |
| North Carolina | Repealed operator licensing, privacy, consent, and retained local-boundary context | `NC-001`, `NC-002`, `NC-009`–`NC-012` |
| Ohio | Many mutually exclusive public-land and university approval processes | `OH-004`–`OH-017` |
| Oklahoma | Few records but broad infrastructure and property rules | `OK-001`–`OK-003` |
| Rhode Island | State registration with unresolved application mechanics and state-land permission | `RI-001`–`RI-004` |
| Utah | Registration, state preemption, contractor procurement, infrastructure authorization, and park permitting | `UT-001`, `UT-002`, `UT-008`–`UT-014` |
| Virginia | Strong preemption counterweights, registration exemption, public-only controls, and severe infrastructure consequences | `VA-003`, `VA-004`, `VA-007`–`VA-014` |

## 3. Findings and required revisions

| Draft issue | Evidence from the sample | Resolution adopted for v1.0.0 |
|---|---|---|
| One generic 0–5 anchor was not sufficient for reproducible dimension ratings. | State registration (`MN-003`, `RI-003`, `UT-001`) and site permission (`CA-008`, `OH-004`) impose different burden mechanisms even when both appear as approvals. | Add dimension-specific 0, 1, 3, and 5 anchors, with documented interpolation for 2 and 4. |
| Consequence severity was mixed into level of effort. | Authorized infrastructure work can face severe unauthorized-operation consequences (`OK-001`, `VA-003`, `VA-004`) without necessarily requiring a high recurring administrative effort. | Remove consequence exposure from the weighted burden score and publish it as a separate 0–5 companion indicator. |
| The three reference missions could overlap. | A public-agency infrastructure project could fit both the public and sensitive-site scenarios. | Make scenario assumptions mutually exclusive and label the composite a fixed reference-portfolio index, not an estimate of actual work mix. |
| Ordinary client/property authorization could be counted as a new state burden. | Infrastructure exceptions commonly rely on facility authorization or consent (`UT-008`, `VA-003`), while ordinary legitimate consulting already requires client and property coordination. | Hold ordinary client/property authorization constant; score only state-specific form, proof, notice, approval path, lead time, or constraint beyond that baseline. |
| Multiple site policies could be incorrectly stacked. | Ohio university and land-manager approvals (`OH-004`–`OH-017`) are usually alternatives tied to different properties, not cumulative actions for one flight. | Cluster mutually exclusive site regimes separately but rate scenario breadth and representative applicable burden rather than summing alternative approvals. |
| General professional-practice law could distort UAS burden. | `CA-010`, `CA-011`, and `NC-012` concern professional practice or competency that can apply regardless of collection platform. | Exclude acquisition-method-neutral professional obligations unless the state evidence creates a UAS-specific incremental action or restriction. |
| Federal incorporation could be mistaken for added state effort. | `RI-001`, `RI-002`, and `UT-007` reference federal compliance. | Score only the incremental state action or state consequence; do not rescore the common FAA step itself. |
| Lack of broad state preemption could be used as a proxy for unknown local burden. | `CA-013` reports no applicable UAS-specific state source; the repository intentionally does not survey local ordinances. | Permit a complexity counterweight for affirmative state preemption, but do not increase burden merely because preemption was not found. |
| The proposed output had one set of component fields despite scenario-specific ratings. | The draft calculation required 21 ratings but the data contract exposed only seven component fields. | Use long-form state/scenario/dimension assessment rows as the scoring source of truth and generate state-level results from them. |
| Inactive and incomplete material required clearer handling. | `CA-012`, `CA-014`, and `NC-009` are pending, failed, or repealed; `RI-003` has unresolved application mechanics. | Exclude inactive authorities from current scores, retain a future-change note, and use the evidence gate/confidence rules for unresolved current mechanics. |

## 4. Decisions retained

- Use a fixed 0–100 anchored index rather than min-max normalization or a forced distribution.
- Show three scenario scores alongside the composite.
- Preserve fixed descriptive bands and test sensitivity rather than changing thresholds to make results look balanced.
- Prevent record-count bias through requirement clustering and a record-count correlation diagnostic.
- Withhold a score rather than treating materially missing evidence as no burden.
- Calculate totals, bands, percentiles, rank, and diagnostics by script.

## 5. Readiness conclusion

The sample exposed correctable methodology and data-contract issues but did not show that the concept itself was unworkable. The adopted revisions make the index more faithful to compliance level of effort, more resistant to site-policy and record-count inflation, and clearer about legitimate authorized AEC work.

Methodology v1.0.0 may be frozen as the specification for the first national assessment. This preflight does **not** establish that all 50 current state packets pass the evidence-readiness gate or share a suitable research cutoff. Those gates must be checked before scoring or publication.

## 6. Change log produced by this preflight

- Weighted dimensions: seven to six; consequence exposure moved outside the composite.
- Weights: revised to 20/20/25/15/10/10.
- Reference scenarios: made mutually exclusive and composite relabeled as a reference-portfolio construct.
- Anchors: dimension-specific anchors added.
- Applicability: authorization baseline, alternative-site, professional-practice, federal-incorporation, preemption, and inactive-authority rules added.
- Data contract: detailed long-form ratings made authoritative; summary comparison made generated.
- Nationwide scoring status: remains blocked pending evidence-gate and common-cutoff verification.
