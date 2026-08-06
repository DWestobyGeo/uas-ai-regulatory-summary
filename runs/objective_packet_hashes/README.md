# Objective Packet Hash Snapshots (Workstream 6)

One `{ABBR}.json` per state that has been snapshotted, mapping `record_id` to the
`objective_packet_hash` (`scripts/build_evidence_packet.py`) computed from that record's
objective fields the last time interpretation was run against it.

## Convention

- `python scripts/build_evidence_packet.py --state XX --snapshot-hashes` writes/overwrites
  `{ABBR}.json` from the current register.
- `python scripts/build_evidence_packet.py --state XX --check-regeneration` compares the
  current register's packet hashes against the stored snapshot and reports which records are
  unchanged (skip re-drafting), changed (regenerate), or new (no prior snapshot, regenerate).
- Unlike `runs/*.json` (append-only run telemetry) or `evals/results/` (append-only dated
  results), this directory is **overwritten in place per state** — it holds current state, not
  history. Git history is the audit trail for how it changed.
- A snapshot should be updated only after the interpretation roles that consumed it have
  actually run (real or simulated) against the current register — snapshotting before drafting
  would cause a real subsequent change to be silently skipped.

## Status

Snapshotted for the five pilot states on 2026-08-06, immediately after Workstream 5/6 landed and
confirmed against the register as it stood at that commit. Re-running
`--check-regeneration` right after `--snapshot-hashes` with no source changes correctly reports
100% unchanged for all five states — see
`evals/results/20260806_workstream6_prompt_size_baseline.md` for the full check.
