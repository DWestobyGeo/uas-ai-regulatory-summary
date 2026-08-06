# Evals

Layered agent-evaluation artifacts for Workstream 4 of
`planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`, scoped to the five
Phase B pilot states (`pilot_states.md`). This directory does not evaluate all fifty states —
that is Workstream 9 (national retrofit) and is explicitly out of scope for this pass.

## Status

Pilot set finalized 2026-08-05 (see `pilot_states.md`). Phase B benchmark packet — expected
role-applicability results, controlled no-impact dispositions, known-bad fixtures, and scoring
rubrics — added 2026-08-06 under this same directory. This is Layer A (deterministic grading)
plus rubric documents for Layers B-D; automated Layer A checks run in CI via
`python evals/run_fixture_checks.py`.

## Directory guide

- **`pilot_states.md`** — the finalized five-state pilot set and selection rationale (Workstream 1).
- **`pilot_states/`** — one `{ABBR}_role_applicability.yaml` per pilot state: a deterministic
  restatement of which records currently carry a governed agency/procurement N/A, generated
  from the live source register. `run_fixture_checks.py` re-derives this from the register on
  every run and fails if it drifts, so a role silently gaining or losing its N/A is caught
  automatically. AEC and legal-analysis relevance is always `true` under current governance —
  Workstream 5's proposed AEC/legal no-material-impact values are not yet authorized (see
  `expected/controlled_no_impact_dispositions.md`), so this file does not apply them.
- **`fixtures/known_bad/`** and **`fixtures/known_good/`** — one JSON file per test case: a
  constructed or real-derived CSV-row dict, the `validate_research_semantics.py` rule function
  it exercises, and the expected outcome (`flag` or `clean`). Where a case is pulled directly
  from an actual repository record (e.g. `wa-008_negative_finding_in_register.json`, sourced
  from `States/WA_Washington/WA_UAS_Source_Register.csv` record WA-008), the fixture's `source`
  field says so; where no current pilot-state record violates a rule, the fixture is marked
  `synthetic` and constructed instead — this is stated plainly in each file rather than implied.
  Currently 11 known-bad and 5 known-good fixtures. The plan's Workstream 4 acceptance criterion
  of "at least twenty known failure-mode fixtures" is a precondition for starting Workstream 9
  (national retrofit), not for Phase B; this set will grow as retrofit work begins.
- **`expected/`** — `controlled_no_impact_dispositions.md`: the exact governed N/A strings
  currently authorized by `Agent_Instructions.v6.md` §6, and an explicit note on which
  Workstream-5-proposed values are *not yet* authorized.
- **`rubrics/`** — scoring rubrics for the plan's Layer B (rubric-based model grading) and
  Layer C (adversarial challenge pass). These are human/model-graded process documents, not
  Python — see each rubric file for how to apply it.
- **`results/`** — see `results/README.md`. Reserved for dated output from a Layer B/C/D
  scoring pass; Layer A's own CI output is not persisted here (git/CI logs already capture it).

## Running the deterministic checks

```sh
pip install pyyaml
python evals/run_fixture_checks.py
```

This is also run in CI (`.github/workflows/site-quality.yml`) alongside
`scripts/validate_research_manifests.py` and `scripts/validate_research_semantics.py`.
