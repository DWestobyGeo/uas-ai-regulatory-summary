# Layer C — Adversarial Challenge Pass

Per Workstream 4 Layer C of the improvement plan. Require a separate context/model pass — one
that did not draft the record — to actively try to break each record in the categories below,
rather than passively reviewing it. This is a process checklist, not automatable code.

For each pilot state, the challenge reviewer should specifically pull every record matching a
category below and attempt to falsify it against the primary source.

## Challenge categories and current pilot-state instances to start from

| Category | Pilot-state records already in scope for this pass |
|---|---|
| Proposed or failed bills | WA-010 (stalled, never enacted); CA-012 (pending as of Aug 1, 2026 cutoff); CA-014 (died in committee) |
| Old unresolved records | WA-004 (uncertain codification); FL-005 (unconfirmed park policy) |
| Secondary-source authorities | WA-007, CA-010, CA-011, FL-008 (general licensing statutes without a confirmed direct-UAS source) |
| General laws with questionable UAS scope | Same four records as above — this is the scope-gate risk pattern (`Agent_Instructions.v6.md` §3.2) |
| Criminal or felony restrictions | WA-004 (as-drafted felony), OK-001/OK-002, FL-007 |
| Registration and permit rules | WA-001/WA-002, MN-003/MN-004, OK-003 |
| Procurement/manufacturer restrictions | FL-003, WA-008 (negative finding), CA-014 (failed proposal) |
| "No law found" conclusions | WA-008, CA-013 (both stored as register records rather than checklist/manifest entries — see `scripts/validate_research_semantics.py`'s `check_negative_finding_in_register`) |

## For each challenged record, confirm

1. The cited section actually says what the objective summary claims — open the primary source,
   do not trust the summary or a secondary description of it.
2. The `status` value is still accurate as of today, not just as of `date_accessed`.
3. A proposed or pending record has not since been enacted, amended, or definitively killed.
4. A "no source found" conclusion was not caused by a failed search rather than a confirmed
   absence (`Agent_Instructions.v6.md` §7: "Do not infer that no authority exists merely because
   a search failed").
5. A felony/criminal provision's exact elements, thresholds, and exceptions match the summary —
   these carry the highest consequence for an operator who relies on this repository.
6. A registration/permit/procurement record's current fee, form, and submission channel are
   still the ones actually in effect, not stale from `date_accessed`.

## Recording results

Drop a dated `{utc_timestamp}_{state_abbr}_layer_c.json` (or `.md`) summary of confirmed and
unconfirmed challenges under `evals/results/` when a Layer C pass is run, per
`evals/results/README.md`.
