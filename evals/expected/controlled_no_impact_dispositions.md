# Controlled No-Material-Impact Dispositions

Authoritative source: `Agent_Instructions.v6.md` §6 ("Only these exact no-material-impact
dispositions are governed"). This file exists so evals and validators have one place to check
the exact strings against, rather than each script hard-coding its own copy silently.

## Currently authorized (governance §6, as of 6.4.0 / Workstream 5)

| Role | Exact governed value | Requires a documented routing determination? |
|---|---|---|
| Agency Practitioner | `N/A — no agency process involved` | No — this was already governed pre-Workstream-5. |
| UAS Procurement Expert | `N/A — no procurement or equipment-selection implication identified` | No — same. |
| AEC Industry UAS Expert | `No material AEC operational implication identified beyond the objective requirement.` | Yes. |
| AEC Industry Legal Counsel | `No separate legal-risk implication identified beyond compliance with the stated authority.` | Yes. |

The AEC and legal values are new as of governance 6.4.0 and are expected to be rare: this
product exists specifically to give AEC operators field-relevant and legal-risk interpretation,
so most retained records will have a substantive AEC and legal disposition even when the agency
or procurement disposition is governed N/A. A role may use its governed no-impact value only
when `scripts/route_interpretation_roles.py` (or equivalent reasoning recorded in the record's
`notes` field or the drafting handoff) supports it. `scripts/validate_research_semantics.py`'s
`check_aec_legal_no_impact_undocumented` rule cross-checks any use of these two values against
the router's output and fails when the router still thinks the record is relevant.

## Deliberately not applied retroactively

Implementing Workstream 5 did **not** rewrite any already-published `practical_interpretation_*`
field in any pilot state's source register. `scripts/route_interpretation_roles.py` and
`evals/pilot_states/*_role_applicability.yaml` describe what routing *recommends* going forward;
none of the five pilot states currently has a record using either new governed value, and that's
expected — re-judging already-published interpretive text is Phase 2 drafting work, not a
tooling/process change, and doing it without the actual record-level analysis that a real
interpretation pass requires would risk introducing incorrect content into a published research
dataset.

## Calibration

`scripts/route_interpretation_roles.py --calibrate` compares the router's
`agency_process_relevant` / `procurement_relevant` output against the real governed-N/A decisions
already made in the five pilot states (the only ground truth available, since AEC/legal never had
a governed N/A before 6.4.0): 98% and 100% agreement respectively as of this version, with one
documented, expected disagreement (WA-004 — see the script's module docstring). There is no
equivalent ground truth for `aec_relevant` / `legal_analysis_relevant` yet; the router defaults
both to `true` and only returns `false` for informational, debunked/never-enacted, or negative
("no source found") records with no operative requirement.
