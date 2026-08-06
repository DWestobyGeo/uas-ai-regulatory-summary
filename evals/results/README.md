# Eval results

Reserved for dated output from a Layer B (rubric-based model grading), Layer C (adversarial
challenge), or Layer D (sampled primary-source verification) pass — see `../rubrics/`.

## Convention

One file per pass: `{utc_timestamp}_{state_abbr}_{layer}.json` or `.md`, e.g.
`20260806T000000Z_WA_layer_c.json`. This directory is additive and append-only, mirroring the
convention already established in `../../runs/README.md` — do not edit or delete a past result.

Layer A (deterministic fixture and role-applicability checks, `../run_fixture_checks.py`) is not
persisted here; it runs in CI on every relevant push/PR and its pass/fail output is already
captured in CI logs. This directory is for the layers that require a human or a separate model
pass and produce a result worth keeping independent of any one CI run.

This directory also holds one-off dated measurement reports that don't fit `runs/` (per-run
telemetry) or a fixture (pass/fail check) -- e.g. the Workstream 6 prompt-size baseline.

## Status

- `20260806_workstream6_prompt_size_baseline.md` — Workstream 6 (Phase C) prompt-size structural
  comparison and skip-regeneration check across the five pilot states.
- No Layer B/C/D pass has been run yet under this convention.
