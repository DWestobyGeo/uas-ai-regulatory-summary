#!/usr/bin/env python3
"""Validate state research manifests (Workstream 2, Phase B pilot).

Schema and controlled values: States/RESEARCH_MANIFEST_SCHEMA.md
Scope: piloted for the five states in evals/pilot_states.md only. A manifest found for any
other state is not an error (states may adopt the convention early), but every manifest that
does exist, pilot or not, must pass this validator.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
PILOT_STATES_DOC = ROOT / "evals" / "pilot_states.md"

REQUIRED_TOP_KEYS = [
    "state", "state_abbr", "method_version", "research_status", "legacy_retrofit_status",
    "last_full_research_date", "last_currency_check", "source_cutoff_date", "coverage",
    "record_count", "unresolved_count", "low_confidence_record_count",
    "primary_source_percentage", "known_issues",
]

RESEARCH_STATUS_VALUES = {
    "current_method_complete", "current_method_in_progress",
    "legacy_needs_retrofit", "legacy_retrofit_in_progress", "legacy_retrofit_complete",
}
LEGACY_RETROFIT_STATUS_VALUES = {
    "not_applicable", "retrofit_not_started", "retrofit_in_progress", "retrofit_complete",
}
CATEGORY_STATUS_VALUES = {
    "applicable_source_found", "reviewed_no_applicable_source",
    "unresolved_verification_required", "not_applicable",
}
REQUIRED_CATEGORIES = [
    "state_statutes_and_amendments",
    "administrative_rules",
    "executive_orders",
    "court_decisions_and_ag_opinions",
    "aviation_and_transportation_agencies",
    "parks_public_lands_and_natural_resources",
    "corrections_public_safety_and_critical_infrastructure",
    "privacy_surveillance_trespass_and_interference",
    "procurement_equipment_and_cybersecurity",
    "professional_licensing_board_material",
    "state_preemption",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SECONDARY_MARKERS = [
    "discovery lead", "proposed", "pending", "repealed", "expired", "superseded",
    "secondary", "advisory", "not found", "failed to pass", "died",
]


def get_pilot_state_abbrs() -> set[str]:
    if not PILOT_STATES_DOC.is_file():
        return set()
    text = PILOT_STATES_DOC.read_text(encoding="utf-8")
    return set(re.findall(r"States/([A-Z]{2})_", text))


def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def compute_expected(rows: list[dict]) -> dict:
    total = len(rows)
    low_conf = sum(1 for r in rows if (r.get("confidence_level") or "").strip().lower() == "low")
    primary = 0
    for r in rows:
        source_type = (r.get("source_type") or "").lower()
        if any(marker in source_type for marker in SECONDARY_MARKERS):
            continue
        if "binding" in source_type or "official agency policy" in source_type or "permit or property-use" in source_type:
            primary += 1
    pct = round(100 * primary / total) if total else 0
    return {"record_count": total, "low_confidence_record_count": low_conf, "primary_source_percentage": pct}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    pilot_abbrs = get_pilot_state_abbrs()
    manifest_paths = sorted(STATES_DIR.glob("*/*_UAS_Research_Manifest.yaml"))
    found_abbrs: set[str] = set()

    for path in manifest_paths:
        rel = path.relative_to(ROOT)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: top level must be a mapping")
            continue

        missing = [k for k in REQUIRED_TOP_KEYS if k not in data]
        if missing:
            errors.append(f"{rel}: missing required keys: {', '.join(missing)}")

        abbr = str(data.get("state_abbr", ""))
        found_abbrs.add(abbr)
        state_dir_abbr = path.parent.name.split("_", 1)[0]
        if abbr != state_dir_abbr:
            errors.append(f"{rel}: state_abbr {abbr!r} does not match directory prefix {state_dir_abbr!r}")
        if path.name != f"{abbr}_UAS_Research_Manifest.yaml":
            errors.append(f"{rel}: filename does not match state_abbr {abbr!r}")

        research_status = data.get("research_status")
        if research_status not in RESEARCH_STATUS_VALUES:
            errors.append(f"{rel}: invalid research_status {research_status!r}")

        legacy_status = data.get("legacy_retrofit_status")
        if legacy_status not in LEGACY_RETROFIT_STATUS_VALUES:
            errors.append(f"{rel}: invalid legacy_retrofit_status {legacy_status!r}")
        if isinstance(research_status, str) and research_status.startswith("legacy_") and legacy_status == "not_applicable":
            errors.append(f"{rel}: research_status {research_status!r} is inconsistent with legacy_retrofit_status 'not_applicable'")
        if research_status == "current_method_complete" and legacy_status != "not_applicable":
            errors.append(f"{rel}: research_status 'current_method_complete' requires legacy_retrofit_status 'not_applicable'")

        for date_field in ("last_full_research_date", "last_currency_check", "source_cutoff_date"):
            value = data.get(date_field)
            if not isinstance(value, str) or not DATE_RE.match(value):
                errors.append(f"{rel}: {date_field} must be an explicit YYYY-MM-DD date, got {value!r}")

        coverage = data.get("coverage")
        computed_unresolved = 0
        referenced_ids: set[str] = set()
        if not isinstance(coverage, dict):
            errors.append(f"{rel}: coverage must be a mapping")
        else:
            missing_categories = [c for c in REQUIRED_CATEGORIES if c not in coverage]
            if missing_categories:
                errors.append(f"{rel}: coverage is missing required categories: {', '.join(missing_categories)}")
            extra_categories = [c for c in coverage if c not in REQUIRED_CATEGORIES]
            if extra_categories:
                warnings.append(f"{rel}: coverage has unrecognized categories (not in the controlled list): {', '.join(extra_categories)}")
            for cat_name, entry in coverage.items():
                if not isinstance(entry, dict):
                    errors.append(f"{rel}: coverage.{cat_name} must be a mapping")
                    continue
                status = entry.get("status")
                if status not in CATEGORY_STATUS_VALUES:
                    errors.append(f"{rel}: coverage.{cat_name}.status invalid value {status!r}")
                unresolved_flag = entry.get("unresolved")
                if not isinstance(unresolved_flag, bool):
                    errors.append(f"{rel}: coverage.{cat_name}.unresolved must be true/false")
                elif unresolved_flag != (status == "unresolved_verification_required"):
                    errors.append(
                        f"{rel}: coverage.{cat_name}.unresolved ({unresolved_flag}) disagrees with status ({status!r})"
                    )
                if status == "unresolved_verification_required":
                    computed_unresolved += 1
                for rid in entry.get("record_ids", []) or []:
                    referenced_ids.add(str(rid))

        if research_status == "current_method_complete" and computed_unresolved:
            errors.append(
                f"{rel}: research_status is 'current_method_complete' but {computed_unresolved} coverage "
                "categories are unresolved_verification_required"
            )

        declared_unresolved = data.get("unresolved_count")
        if declared_unresolved != computed_unresolved:
            errors.append(
                f"{rel}: unresolved_count={declared_unresolved!r} does not match "
                f"{computed_unresolved} unresolved_verification_required categories"
            )

        state_dir = path.parent
        rows = load_register(state_dir)
        if not rows:
            errors.append(f"{rel}: could not load a source register to cross-check computed fields")
        else:
            expected = compute_expected(rows)
            for field in ("record_count", "low_confidence_record_count", "primary_source_percentage"):
                if data.get(field) != expected[field]:
                    errors.append(
                        f"{rel}: {field}={data.get(field)!r} does not match computed value "
                        f"{expected[field]!r} from the source register"
                    )
            actual_ids = {row.get("record_id", "") for row in rows}
            unknown_refs = referenced_ids - actual_ids
            if unknown_refs:
                errors.append(f"{rel}: coverage references record_ids not present in the register: {', '.join(sorted(unknown_refs))}")

        if not isinstance(data.get("known_issues"), list):
            errors.append(f"{rel}: known_issues must be a list (may be empty)")

    if pilot_abbrs:
        missing_pilot_manifests = pilot_abbrs - found_abbrs
        if missing_pilot_manifests:
            errors.append(f"Pilot states missing a research manifest: {', '.join(sorted(missing_pilot_manifests))}")

    print(f"manifests_found={len(manifest_paths)} pilot_states={len(pilot_abbrs)} errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
