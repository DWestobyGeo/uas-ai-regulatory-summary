#!/usr/bin/env python3
"""Layer A (deterministic) eval runner for Workstream 4.

Loads every fixture in evals/fixtures/{known_bad,known_good}/*.json, runs the named rule
function from scripts/validate_research_semantics.py against its row, and asserts the
fixture's expected outcome ("flag" or "clean"). Also cross-checks each
evals/pilot_states/{ABBR}_role_applicability.yaml expected file against a fresh run of
scripts/route_interpretation_roles.py over the live source register, so a role-applicability
regression -- from either the routing heuristic changing or the register changing -- is caught
the same way a fixture regression would be.

This intentionally only covers Layer A (deterministic grading) from the plan's four
evaluation layers (planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md,
Workstream 4). Layers B-D (rubric-based model grading, adversarial challenge, sampled
primary-source verification) are process rubrics under evals/rubrics/ for a human or a
separate model-graded pass to apply; they are not automatable with plain Python.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_research_semantics as vrs  # noqa: E402
import route_interpretation_roles as rir  # noqa: E402

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PILOT_STATES_DIR = Path(__file__).resolve().parent / "pilot_states"

RULES_BY_NAME = {fn.__name__: fn for fn in vrs.PER_RECORD_RULES}


def run_fixtures() -> tuple[int, int, list[str]]:
    passed = 0
    failed = 0
    failures: list[str] = []
    for subdir, expect in (("known_bad", "flag"), ("known_good", "clean")):
        for path in sorted((FIXTURES_DIR / subdir).glob("*.json")):
            fixture = json.loads(path.read_text(encoding="utf-8"))
            if fixture.get("expect") != expect:
                failures.append(f"{path.name}: fixture is in {subdir}/ but declares expect={fixture.get('expect')!r}")
                failed += 1
                continue
            rule_name = fixture["rule"]
            rule_fn = RULES_BY_NAME.get(rule_name)
            if rule_fn is None:
                failures.append(f"{path.name}: unknown rule {rule_name!r} (not in validate_research_semantics.PER_RECORD_RULES)")
                failed += 1
                continue
            findings = rule_fn(fixture["row"])
            flagged = bool(findings)
            expected_flag = fixture["expect"] == "flag"
            if flagged == expected_flag:
                passed += 1
            else:
                failed += 1
                failures.append(
                    f"{path.name}: expected {fixture['expect']!r} from {rule_name}, got "
                    f"{'flag' if flagged else 'clean'} (findings={findings})"
                )
    return passed, failed, failures


ROUTING_FIELDS = ("aec_relevant", "agency_process_relevant", "procurement_relevant", "legal_analysis_relevant")


def run_role_applicability_checks() -> tuple[int, int, list[str]]:
    passed = 0
    failed = 0
    failures: list[str] = []

    for path in sorted(PILOT_STATES_DIR.glob("*_role_applicability.yaml")):
        expected_doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        abbr = expected_doc["state_abbr"]
        state_dirs = list((ROOT / "States").glob(f"{abbr}_*"))
        if not state_dirs:
            failures.append(f"{path.name}: no States/{abbr}_* directory found")
            failed += 1
            continue
        routed_by_id = {r["record_id"]: r for r in rir.route_state(state_dirs[0])}

        for expected in expected_doc["records"]:
            rid = expected["record_id"]
            routed = routed_by_id.get(rid)
            if routed is None:
                failures.append(f"{path.name}: expected record {rid} no longer exists in the live register")
                failed += 1
                continue
            ok = all(routed[field] == expected[field] for field in ROUTING_FIELDS)
            if ok:
                passed += 1
            else:
                failed += 1
                failures.append(
                    f"{path.name}: {rid} role applicability drifted from the expected packet "
                    f"(expected={ {f: expected[f] for f in ROUTING_FIELDS} }; routed={ {f: routed[f] for f in ROUTING_FIELDS} })"
                )
    return passed, failed, failures


def main() -> int:
    fx_passed, fx_failed, fx_failures = run_fixtures()
    ra_passed, ra_failed, ra_failures = run_role_applicability_checks()

    total_passed = fx_passed + ra_passed
    total_failed = fx_failed + ra_failed

    print(f"fixture_checks: passed={fx_passed} failed={fx_failed}")
    print(f"role_applicability_checks: passed={ra_passed} failed={ra_failed}")
    for item in fx_failures + ra_failures:
        print(f"FAIL: {item}")
    print(f"TOTAL: passed={total_passed} failed={total_failed}")
    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main())
