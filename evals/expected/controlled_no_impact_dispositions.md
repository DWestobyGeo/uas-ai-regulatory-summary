# Controlled No-Material-Impact Dispositions

Authoritative source: `Agent_Instructions.v6.md` §6 ("Only these exact N/A dispositions are
governed"). This file exists so evals and validators have one place to check the exact strings
against, rather than each script hard-coding its own copy silently.

## Currently authorized (governance §6)

| Role | Exact governed value |
|---|---|
| Agency Practitioner | `N/A — no agency process involved` |
| UAS Procurement Expert | `N/A — no procurement or equipment-selection implication identified` |

The AEC Industry UAS Expert and AEC Industry Legal Counsel roles provide a substantive
disposition for every retained record — governance §6 is explicit that these two roles do not
currently have a governed N/A.

## Proposed, not yet authorized (Workstream 5)

`planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md` Workstream 5 proposes two
additional controlled values for the AEC and legal roles:

- `No material AEC operational implication identified beyond the objective requirement.`
- `No separate legal-risk implication identified beyond compliance with the stated authority.`

**These are not active.** Workstream 5 is Phase C work and is out of scope for this Phase B
pass. Nothing in this repository — including `evals/pilot_states/*_role_applicability.yaml`,
which treats `aec_relevant` and `legal_analysis_relevant` as always `true` — should apply them
until governance §6 is amended to authorize them and `scripts/validate_phase2.py` is updated to
recognize them the same way it already recognizes the agency/procurement N/A values.

## Why this matters for evals

`scripts/validate_phase2.py` already fails any AEC or legal field that starts with `N/A`
(`unsupported N/A in AEC/legal role`). If Workstream 5 is implemented in a later phase, that
check and this table must be updated together, and `evals/pilot_states/*_role_applicability.yaml`
must be regenerated to allow `aec_relevant: false` / `legal_analysis_relevant: false` outcomes.
Until then, a fixture or generated file that shows either of the proposed values in active use
is a bug, not a preview.
