# Workstream 6 baseline: prompt size vs. naive assembly

Date: 2026-08-06. Scope: the five Phase B pilot states (`evals/pilot_states.md`).

## What this measures, and what it doesn't

This is a **structural character-count proxy**, produced by
`scripts/assemble_prompt.py --measure`, comparing two ways of assembling an interpretation-role
prompt for a given record:

- **Naive baseline:** the full 33-field CSV row (JSON-encoded) plus the full text of *all four*
  interpretation role documents plus the full governance document, repeated in full for every
  single record with no prefix reuse credited. This approximates how a prompt would look without
  Workstream 5 (role routing) or 6 (compact packets, prefix reuse) applied.
- **Stable-prefix / dynamic-suffix (this workstream):** `Agent_Instructions.v6.md` + *one* role's
  operating instructions + that role's task-frame file, assembled once per role and reused
  (`agents/prompt_templates/`), plus one compact evidence packet
  (`scripts/build_evidence_packet.py`) per record.

It is **not** live-metered token count or dollar cost — no `runs/` telemetry exists yet
(Workstream 0 is schema-only so far; see `runs/README.md`), so there is no real API-billed
baseline to compare against. Character count is a reasonable proxy for token count (roughly
4 characters per token for English prose) but is not equivalent, and it says nothing about
provider-side prompt-cache discount rates, which vary and are not modeled here. Per the plan's
own Workstream 6 non-goal, this report does **not** claim a token-reduction percentage as
a production metric — it demonstrates that the structural approach is directionally sound and
gives a first, honestly-labeled number.

## Results, role = AEC Industry UAS Expert (representative; all four roles are within ~2% of each other — see per-record detail below)

| State | Records | Stable prefix (chars) | Dynamic suffix, all records (chars) | New total | Naive total | Reduction |
|---|---|---|---|---|---|---|
| WA | 9 | 31,084 | 18,198 | 49,282 | 447,937 | 89% |
| OK | 3 | 31,084 | 7,480 | 38,564 | 152,602 | 75% |
| CA | 14 | 31,084 | 33,227 | 64,311 | 703,618 | 91% |
| MN | 7 | 31,084 | 24,094 | 55,178 | 365,594 | 85% |
| FL | 8 | 31,084 | 18,079 | 49,163 | 400,426 | 88% |

The stable prefix is identical across every record and state for a given role (it only changes
on a governance/role/task-frame version bump), so "new total" here counts it exactly once per
state even though it would in practice be cached at the provider level across states too. The
reduction percentage grows with record count (OK's 3 records amortize the prefix less than CA's
14), which is expected and is itself evidence the prefix-reuse mechanism is doing real work.

## Per-record example (OK-002, all four roles)

| Role | Stable prefix (chars) | Dynamic suffix (chars) |
|---|---|---|
| AEC Industry UAS Expert | 31,084 | 2,526 |
| Agency Practitioner | 28,915 | 2,526 |
| UAS Procurement Expert | 29,349 | 2,526 |
| AEC Industry Legal Counsel | 30,023 | 2,526 |

The dynamic suffix (the evidence packet) is identical across roles for the same record, since all
four roles receive the same objective evidence — only the stable prefix differs, by role
document length.

## Skip-regeneration check

`runs/objective_packet_hashes/{WA,OK,CA,MN,FL}.json` were snapshotted from the register as it
stood at this commit, then `--check-regeneration` was re-run immediately with no source changes:

```
WA: unchanged=9 changed=0 new=0
OK: unchanged=3 changed=0 new=0
CA: unchanged=14 changed=0 new=0
MN: unchanged=7 changed=0 new=0
FL: unchanged=8 changed=0 new=0
```

All 41 pilot-state records correctly report as unchanged, confirming the hash convention itself
is stable and reproducible (same objective fields in → same hash out). This has not yet been
exercised against a *real* content change (e.g. a currency-update research pass), which would be
the actual test of "an unchanged record is not regenerated, a changed one is" — that is deferred
to whenever a real Workstream 8 currency-update pass runs against a pilot state.

## Honest limitations

- No real interpretation drafting or API call happened to produce these numbers; this measures
  prompt *assembly*, not drafting quality or actual token/cost telemetry.
- The naive baseline is a reasonable but constructed comparison point, not a literal record of
  how any past session actually assembled its prompts.
- Character-to-token ratio varies by content (JSON is denser than prose); treat the percentages
  as directional, not exact.
