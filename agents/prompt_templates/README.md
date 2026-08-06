# Prompt Templates (Workstream 6)

Per Workstream 6 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`: assemble
each interpretation-role prompt as **stable prefix + dynamic suffix**, so a provider's prompt
cache can reuse the (large, unchanging) prefix across every record in a state pass and every
state, and only the (small, per-record) suffix changes.

## Assembly order

1. **`Agent_Instructions.v6.md`**, verbatim — repository-wide governance. Stable until the next
   governance version bump.
2. **The role's own file** under `agents/roles/`, verbatim — e.g. `aec-industry-uas-expert.md`.
   Stable until the next role-version bump.
3. **This directory's task-frame file** for that role (e.g. `aec-industry-uas-expert.task.md`) —
   a short, mostly-stable wrapper stating the output contract (produce exactly one field, exact
   format, no extra prose). Changes only when the output contract itself changes.
4. **One evidence packet** (`scripts/build_evidence_packet.py`) for the specific record, as JSON
   — the only part that changes on every call. Comes last, per the plan's "keep dynamic record
   content at the end" rule, so steps 1-3 form one stable, cacheable prefix.

`scripts/assemble_prompt.py` builds the concatenated prompt from these four pieces and reports
size versus a naive baseline (full 33-field CSV row instead of a compact evidence packet, no
prompt-prefix reuse) — see `evals/results/20260806_workstream6_prompt_size_baseline.md` for the
measured comparison. This is a structural/character-count proxy, not live-metered token or cost
data; no `runs/` telemetry exists yet to measure the latter (Workstream 0 is schema-only so far).

## What is NOT included

Per the plan: no website files, no unrelated states, no unrelated role documents. A given
assembled prompt contains exactly one role's governance-relevant text and exactly one record's
evidence -- never another role's operating instructions, another state's data, or `docs/`.

## Skip-regeneration convention

Each evidence packet carries an `objective_packet_hash`. `runs/objective_packet_hashes/{ABBR}.json`
snapshots the hash last used to generate each record's interpretation. A future run should skip
re-drafting a record whose current packet hash matches the stored one -- see
`runs/objective_packet_hashes/README.md`.
