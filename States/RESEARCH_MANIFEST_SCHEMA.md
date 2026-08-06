# State Research Manifest Schema

**Status:** Piloted for the five Workstream 1 pilot states only (see `evals/pilot_states.md`). Not yet
required for the other 45 states — this is Workstream 2 of
`planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`, scoped to Phase B pilot states.
Nationwide rollout is downstream Workstream 9 work and is explicitly out of scope for this pass.

**Owner:** Research Expert (`agents/roles/research-expert.md`), per the plan's recommendation that
research completeness be owned by the same role that owns the checklist it supersedes for
machine-readability purposes. The manifest supplements, and does not replace, the narrative
`XX_UAS_Research_Checklist.md` where one exists.

**File:** One `States/XX_State/XX_UAS_Research_Manifest.yaml` per state that has one. Validated by
`scripts/validate_research_manifests.py`.

## Purpose

Make state research completeness machine-readable and distinguish legacy packets (produced before
current-method provenance and semantic-validation conventions existed) from current-method packets,
without expanding the 33-field source-register schema.

## Controlled values

### `research_status` (state-level)

| Value | Meaning |
|---|---|
| `current_method_complete` | All required coverage categories resolved; provenance, dates, and role N/A routing follow the current governance and validator conventions; no known unresolved semantic issue. |
| `current_method_in_progress` | Phase 1/2 work using current conventions is underway but not yet complete. |
| `legacy_needs_retrofit` | Predates current-method provenance/semantic conventions (e.g., no recorded model/checkpoint, negative findings stored as register records instead of checklist entries) and has not yet been re-verified under them. Workstream 9 retrofit target. |
| `legacy_retrofit_in_progress` | A legacy state currently being re-verified against current-method conventions. |
| `legacy_retrofit_complete` | A former legacy state that has been fully re-verified against current-method conventions. |

A state manifest may not declare `current_method_complete` unless every required coverage category
below is `applicable_source_found`, `reviewed_no_applicable_source`, or `not_applicable` — i.e., none
are `unresolved_verification_required` — per the plan's Workstream 2 acceptance criteria.

### `legacy_retrofit_status`

`not_applicable` (never a legacy packet) | `retrofit_not_started` | `retrofit_in_progress` | `retrofit_complete`

### Coverage category `status` (one entry per required category below)

Mirrors the four controlled checklist results already defined in `Agent_Instructions.v6.md` §5.2,
in machine-readable form:

| Manifest value | Governance §5.2 equivalent |
|---|---|
| `applicable_source_found` | Applicable source found |
| `reviewed_no_applicable_source` | Reviewed — no applicable UAS-specific source located |
| `unresolved_verification_required` | Unresolved — additional verification required |
| `not_applicable` | Not applicable |

### Required coverage categories

These eleven keys mirror `Agent_Instructions.v6.md` §3.1 in-scope research areas and the category
rows already used in narrative checklists (e.g. `States/OK_Oklahoma/OK_UAS_Research_Checklist.md`):

```text
state_statutes_and_amendments
administrative_rules
executive_orders
court_decisions_and_ag_opinions
aviation_and_transportation_agencies
parks_public_lands_and_natural_resources
corrections_public_safety_and_critical_infrastructure
privacy_surveillance_trespass_and_interference
procurement_equipment_and_cybersecurity
professional_licensing_board_material
state_preemption
```

## Suggested fields

See `States/OK_Oklahoma/OK_UAS_Research_Manifest.yaml` for a fully worked example. Summary:

```yaml
state: Oklahoma
state_abbr: OK
method_version: 1.0.0
research_status: current_method_complete
legacy_retrofit_status: not_applicable
last_full_research_date: 2026-08-02
last_currency_check: 2026-08-02
source_cutoff_date: 2026-08-02
coverage:
  state_statutes_and_amendments:
    status: applicable_source_found
    sources_searched: [...]
    unresolved: false
    note: optional free-text note
  # ... one entry per required category
record_count: 3
unresolved_count: 0
low_confidence_record_count: 0
primary_source_percentage: 100
known_issues: []          # optional; short pointers to eval fixtures / notes.md items
```

`unresolved_count` and `low_confidence_record_count` must match what `validate_research_manifests.py`
computes directly from the state's `XX_UAS_Source_Register.csv` (a `confidence_level` of `Low`, or an
`unresolved: true` coverage entry) — this is the manifest/register agreement check from Workstream 3's
rule list. `primary_source_percentage` is the share of register rows whose `source_type` denotes a
primary/official source (statute, regulation, or official agency policy) rather than a secondary,
proposed, repealed, or discovery-lead source type.

## Non-goals

This schema does not expand the 33-field source-register CSV schema, does not create a human
publication-approval workflow, and does not itself trigger a national retrofit — it only makes
existing (or newly assessed) completeness state machine-readable for the five pilot states.
