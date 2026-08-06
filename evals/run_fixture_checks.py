#!/usr/bin/env python3
"""Layer A (deterministic) eval runner for Workstream 4.

Loads every fixture in evals/fixtures/{known_bad,known_good}/*.json, runs the named rule
function from scripts/validate_research_semantics.py against its row, and asserts the
fixture's expected outcome ("flag" or "clean"). Also cross-checks each
evals/pilot_states/{ABBR}_role_applicability.yaml expected file against the live source
register, so a role-applicability regression (a record silently gaining or losing a governed
N/A) is caught the same way a fixture regression would be.

This intentionally only covers Layer A (deterministic grading) from the plan's four
evaluation layers (planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md,
Workstream 4). Layers B-D (rubric-based model grading, adversarial challenge, sampled
primary-source verification) are process rubrics under evals/rubrics/ for a human or a
separate model-graded pass to apply; they are not automatable with plain Python.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_research_semantics as vrs  # noqa: E402

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


def run_role_applicability_checks() -> tuple[int, int, list[str]]:
    passed = 0
    failed = 0
    failures: list[str] = []
    AGENCY_NA = "N/A — no agency process involved"
    PROCUREMENT_NA = "N/A — no procurement or equipment-selection implication identified"

    for path in sorted(PILOT_STATES_DIR.glob("*_role_applicability.yaml")):
        expected_doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        abbr = expected_doc["state_abbr"]
        state_dirs = list((ROOT / "States").glob(f"{abbr}_*"))
        if not state_dirs:
            failures.append(f"{path.name}: no States/{abbr}_* directory found")
            failed += 1
            continue
        csv_path = next(state_dirs[0].glob("*_UAS_Source_Register.csv"))
        with csv_path.open(encoding="utf-8-sig") as f:
            live_rows = {row["record_id"]: row for row in csv.DictReader(f)}

        for expected in expected_doc["records"]:
            rid = expected["record_id"]
            live = live_rows.get(rid)
            if live is None:
                failures.append(f"{path.name}: expected record {rid} no longer exists in the live register")
                failed += 1
                continue
            live_agency_relevant = live["practical_interpretation_agency_practitioner"].strip() != AGENCY_NA
            live_proc_relevant = live["practical_interpretation_uas_procurement_expert"].strip() != PROCUREMENT_NA
            ok = (
                live_agency_relevant == expected["agency_process_relevant"]
                and live_proc_relevant == expected["procurement_relevant"]
            )
            if ok:
                passed += 1
            else:
                failed += 1
                failures.append(
                    f"{path.name}: {rid} role applicability drifted from the expected packet "
                    f"(expected agency={expected['agency_process_relevant']}, procurement={expected['procurement_relevant']}; "
                    f"live agency={live_agency_relevant}, procurement={live_proc_relevant})"
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
