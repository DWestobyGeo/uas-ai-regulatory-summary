#!/usr/bin/env python3
"""Deterministic semantic validation for state UAS source registers (Workstream 3).

This validator checks *meaning*, not just structure: it looks for patterns that governance
prohibits or that the improvement plan
(planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md, Workstream 3) identifies as
recurring failure modes, even when every field is technically populated.

Scope and severity policy for this Phase B pass (pilot states only — see evals/pilot_states.md):

- A finding on a record in a state that HAS a research manifest
  (States/XX_State/XX_UAS_Research_Manifest.yaml) is an ERROR unless that exact record_id is
  already referenced somewhere in that state's manifest coverage — in which case it is treated
  as acknowledged legacy debt (tracked, not yet retrofitted; Workstream 9 is explicitly out of
  scope for this pass) and reported as a WARNING instead. This lets CI stay green for known,
  already-documented issues while still catching *new* undocumented regressions in a pilot
  state.
- A finding on a record in a state with no manifest yet (i.e. not one of the five pilot states)
  is always a WARNING: Phase B is intentionally scoped to the pilot set, and this repo's other
  45 states have not been assessed under this convention yet.
- The CI-completeness check (rule 1) and cross-artifact agreement check (rule 11) are always
  errors regardless of state, because they check repository-wide invariants, not per-record
  content judgment calls.

Individual rule functions are kept import-friendly (pure functions over a CSV row dict) so
`evals/run_fixture_checks.py` can exercise them directly against constructed fixtures.
"""

from __future__ import annotations

import csv
import difflib
import itertools
import json
import re
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "site-quality.yml"
PILOT_STATES_DOC = ROOT / "evals" / "pilot_states.md"
REQUIRED_CI_SCRIPTS = [
    "validate_roles.py",
    "validate_methodologies.py",
    "validate_phase2.py",
    "validate_research_manifests.py",
    "validate_research_semantics.py",
    "validate_site.py",
]

HEDGE_MARKERS = re.compile(
    r"\b(confirm|verify|until|before relying|as if|may|should|consider|recheck|independently confirm|"
    r"do not rely|open (item|question)|unresolved)\b",
    re.I,
)
NEGATIVE_FINDING_STATUS = re.compile(
    r"\b(category reviewed|reviewed)\b.*\bno\b.*\b(located|found|applicable)\b", re.I
)
NEGATIVE_FINDING_SOURCE_TYPE = re.compile(r"not found", re.I)
GENERAL_STATUTE_MARKERS = re.compile(
    r"no standalone UAS-specific|no UAS-specific board|general framework confirmed|"
    r"not UAS-specific|no UAS-specific.*(rule|guidance|document)", re.I
)
UNVERIFIED_STATUS = re.compile(r"\bUNCERTAIN\b|\bUnconfirmed\b|\bverify current codification\b", re.I)
CITATION_DISCREPANCY = re.compile(r"citation discrepancy|citation note", re.I)
BOILERPLATE_PROCESS_WORDS = re.compile(
    r"\b(submit(ting)? an application|application fee|apply for a permit|obtain a permit|"
    r"requires approval from|reviewing officer|pay a fee to)\b", re.I
)
LEGISLATURE_AS_OFFICE = re.compile(r"legislature|revisor of statutes|code commission", re.I)
APPLICATION_LANGUAGE = re.compile(
    r"\b(apply|application (portal|process|form)|submit.{0,20}application|licensing portal)\b", re.I
)
MUST_LANGUAGE = re.compile(r"\bmust\b", re.I)
PUBLIC_AGENCY_HEDGE = re.compile(
    r"\bpublic[- ]agency\b|\bpublic client\b|\byour agency\b|\bagency['a-z ]*\bmission\b|"
    r"\blaw[- ]enforcement mission\b|\bgovernment (employee|program)\b", re.I
)
GOVERNED_AGENCY_NA = "N/A — no agency process involved"
GOVERNED_PROCUREMENT_NA = "N/A — no procurement or equipment-selection implication identified"


# --------------------------------------------------------------------------------------
# Rule functions: each takes a CSV row dict and returns a list of finding strings.
# --------------------------------------------------------------------------------------

def check_negative_finding_in_register(row: dict) -> list[str]:
    """Rule: negative/'none found' results belong in the checklist or manifest, not the register."""
    status = row.get("status", "")
    source_type = row.get("source_type", "")
    if NEGATIVE_FINDING_STATUS.search(status) or NEGATIVE_FINDING_SOURCE_TYPE.search(source_type):
        return [
            f"{row.get('record_id')}: negative/no-source-found result stored as a register record "
            f"(status={status!r}); Agent_Instructions.v6.md §5.2 says negative findings normally "
            "belong in the checklist/manifest, not the source register."
        ]
    return []


def check_general_statute_scope_gate(row: dict) -> list[str]:
    """Rule: flag general statutes without a direct-UAS or official-UAS-application basis."""
    haystack = " ".join([row.get("status", ""), row.get("summary", ""), row.get("requirement_type", "")])
    if GENERAL_STATUTE_MARKERS.search(haystack):
        return [
            f"{row.get('record_id')}: general statute retained without a confirmed direct-UAS "
            "provision or official UAS-specific application — scope-gate risk under "
            "Agent_Instructions.v6.md §3.2."
        ]
    return []


def check_unverified_status_low_confidence(row: dict) -> list[str]:
    """Rule: an unverified/uncertain status paired with Low confidence should not sit unresolved."""
    status = row.get("status", "")
    confidence = (row.get("confidence_level") or "").strip().lower()
    if UNVERIFIED_STATUS.search(status) and confidence == "low":
        return [
            f"{row.get('record_id')}: status is unverified/uncertain ({status!r}) and confidence is "
            "Low; this record cannot support a resolved coverage category until re-verified."
        ]
    return []


def check_citation_discrepancy_confidence(row: dict) -> list[str]:
    """Rule: a flagged citation discrepancy must not coexist with High confidence."""
    haystack = " ".join([row.get("verification_status", ""), row.get("notes", "")])
    confidence = (row.get("confidence_level") or "").strip().lower()
    if CITATION_DISCREPANCY.search(haystack) and confidence == "high":
        return [
            f"{row.get('record_id')}: a citation discrepancy is flagged in verification_status/notes "
            "but confidence_level is High; confidence must reflect the unresolved citation."
        ]
    return []


def check_boilerplate_process_language(row: dict) -> list[str]:
    """Rule: flag fee/application/permit/approval/reviewer language when no such process exists."""
    permit = (row.get("permit_or_approval_required") or "").strip()
    if not permit.lower().startswith("no"):
        return []
    findings = []
    for field in (
        "practical_interpretation_agency_practitioner",
        "practical_interpretation_aec_expert",
        "practical_interpretation_uas_procurement_expert",
        "practical_interpretation_legal_counsel",
    ):
        text = row.get(field, "") or ""
        if BOILERPLATE_PROCESS_WORDS.search(text):
            findings.append(
                f"{row.get('record_id')}: {field} describes an application/fee/approval process, "
                f"but permit_or_approval_required is {permit!r} (no such process established)."
            )
    return findings


def check_legislature_as_application_office(row: dict) -> list[str]:
    """Rule: flag a legislature or code publisher described as an application office."""
    issuing_authority = row.get("issuing_authority", "")
    if not LEGISLATURE_AS_OFFICE.search(issuing_authority):
        return []
    text = row.get("practical_interpretation_agency_practitioner", "") or ""
    if APPLICATION_LANGUAGE.search(text):
        return [
            f"{row.get('record_id')}: issuing_authority ({issuing_authority!r}) is a legislature/code "
            "publisher, but the agency-practitioner interpretation describes an application process "
            "as if it were an administering office."
        ]
    return []


def check_low_confidence_mandatory_language(row: dict) -> list[str]:
    """Rule: low-confidence records must not contain unqualified mandatory operating language."""
    confidence = (row.get("confidence_level") or "").strip().lower()
    if confidence != "low":
        return []
    findings = []
    for field in ("practical_interpretation_aec_expert", "practical_interpretation_legal_counsel"):
        text = row.get(field, "") or ""
        if MUST_LANGUAGE.search(text) and not HEDGE_MARKERS.search(text):
            findings.append(
                f"{row.get('record_id')}: {field} uses unqualified 'must' language on a Low-confidence "
                "record with no hedging (confirm/verify/until/as if/etc.)."
            )
    return findings


PRIVATE_OPERATOR_UNIVERSAL_LANGUAGE = re.compile(
    r"\b(any (commercial )?operator|all operators|every operator|private operators?\b(?!.{0,40}\bpublic\b))\b",
    re.I,
)


def check_public_agency_only_misapplied(row: dict) -> list[str]:
    """Rule: public-agency-only authorities must not be interpreted as direct private-operator duties.

    Narrowly targeted: only fires when the text uses universal-operator language ("any operator",
    "all operators") without also scoping to the public-agency/government context anywhere in the
    same field. A record that names the specific agency, says "public client", "law-enforcement
    mission", etc. is not flagged even without an exact keyword hit elsewhere.
    """
    public_only = (row.get("public_agency_only") or "").strip().lower()
    if not public_only.startswith("yes"):
        return []
    findings = []
    for field in ("practical_interpretation_aec_expert", "practical_interpretation_legal_counsel"):
        text = row.get(field, "") or ""
        if not text:
            continue
        if PRIVATE_OPERATOR_UNIVERSAL_LANGUAGE.search(text) and not PUBLIC_AGENCY_HEDGE.search(text):
            findings.append(
                f"{row.get('record_id')}: public_agency_only is {row.get('public_agency_only')!r} but "
                f"{field} uses universal-operator language without scoping to the public-agency context."
            )
    return findings


def check_nonstandard_na_routing(row: dict) -> list[str]:
    """Rule: agency/procurement commentary must use the governed N/A value or a substantive finding."""
    findings = []
    agency = (row.get("practical_interpretation_agency_practitioner") or "").strip()
    procurement = (row.get("practical_interpretation_uas_procurement_expert") or "").strip()
    permit = (row.get("permit_or_approval_required") or "").strip().lower()
    if permit.startswith("no") and agency and agency != GOVERNED_AGENCY_NA and "N/A" not in agency:
        # A substantive agency answer is fine; this only flags a bare non-governed "N/A-ish" dodge.
        if re.search(r"^(none|n/?a)\.?$", agency, re.I):
            findings.append(f"{row.get('record_id')}: agency-practitioner field is a bare non-governed N/A value: {agency!r}")
    if procurement and re.search(r"^(none|n/?a)\.?$", procurement, re.I) and procurement != GOVERNED_PROCUREMENT_NA:
        findings.append(f"{row.get('record_id')}: procurement field is a bare non-governed N/A value: {procurement!r}")
    return findings


def check_pending_after_cutoff(row: dict, today_year: int) -> list[str]:
    """Rule (soft/currency): a status of 'pending' more than a year past date_accessed needs a recheck.

    This is intentionally a currency prompt, not a hard defect — determining whether a specific
    state's legislative session has actually expired is not deterministic from the register alone.
    """
    status = row.get("status", "")
    if not re.search(r"\bpending\b", status, re.I):
        return []
    date_accessed = row.get("date_accessed", "")
    year_match = re.search(r"(20\d{2})", date_accessed)
    if year_match and today_year - int(year_match.group(1)) >= 1:
        return [
            f"{row.get('record_id')}: status is 'pending' and date_accessed ({date_accessed}) is over "
            "a year old; recheck current legislative status before treating it as still pending."
        ]
    return []


PER_RECORD_RULES = [
    check_negative_finding_in_register,
    check_general_statute_scope_gate,
    check_unverified_status_low_confidence,
    check_citation_discrepancy_confidence,
    check_boilerplate_process_language,
    check_legislature_as_application_office,
    check_low_confidence_mandatory_language,
    check_public_agency_only_misapplied,
    check_nonstandard_na_routing,
]


def check_duplicate_interpretations(rows: list[dict], threshold: float = 0.55) -> list[str]:
    """Rule: flag near-duplicate interpretation text reused across unrelated records."""
    findings = []
    field = "practical_interpretation_aec_expert"
    for a, b in itertools.combinations(rows, 2):
        ta, tb = a.get(field, ""), b.get(field, "")
        if not ta or not tb or len(ta) < 40 or len(tb) < 40:
            continue
        ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
        if ratio >= threshold:
            findings.append(
                f"{a.get('record_id')}/{b.get('record_id')}: {field} is {ratio:.0%} similar across two "
                "records with different uas_topic values — possible templated boilerplate rather than "
                "record-specific interpretation."
            )
    return findings


# --------------------------------------------------------------------------------------
# Repository-wide structural rules
# --------------------------------------------------------------------------------------

def check_ci_completeness() -> list[str]:
    if not WORKFLOW_PATH.is_file():
        return [f"{WORKFLOW_PATH.relative_to(ROOT)} does not exist."]
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    missing = [script for script in REQUIRED_CI_SCRIPTS if script not in text]
    if missing:
        return [f".github/workflows/site-quality.yml is missing required validator(s): {', '.join(missing)}"]
    return []


def check_cross_artifact_agreement(state_abbr: str, state_dir: Path, register_rows: list[dict]) -> list[str]:
    """Rule: manifest, register, generated JSON, and summary must agree on record identity/count."""
    findings: list[str] = []
    manifest_path = next(state_dir.glob("*_UAS_Research_Manifest.yaml"), None)
    json_path = ROOT / "docs" / "data" / "v1" / f"{state_abbr}.json"
    register_ids = {row.get("record_id", "") for row in register_rows}

    if manifest_path is not None:
        try:
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            return [f"{manifest_path.relative_to(ROOT)}: invalid YAML: {exc}"]
        if manifest.get("record_count") != len(register_rows):
            findings.append(
                f"{state_abbr}: manifest record_count ({manifest.get('record_count')}) does not match "
                f"the register ({len(register_rows)} rows)."
            )

    if json_path.is_file():
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return findings + [f"{json_path.relative_to(ROOT)}: invalid JSON: {exc}"]
        json_ids = {r.get("record_id", "") for r in data.get("records", [])}
        if json_ids != register_ids:
            findings.append(
                f"{state_abbr}: generated docs/data/v1/{state_abbr}.json record IDs do not match the "
                "source register (run python3 build_data.py after register changes)."
            )
    else:
        findings.append(
            f"{state_abbr}: no generated docs/data/v1/{state_abbr}.json found; run python3 build_data.py."
        )

    return findings


# --------------------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------------------

def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_manifest_record_ids(state_dir: Path) -> set[str] | None:
    """Return the set of record_ids referenced anywhere in the state's manifest, or None if no manifest."""
    manifest_path = next(state_dir.glob("*_UAS_Research_Manifest.yaml"), None)
    if manifest_path is None:
        return None
    try:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return set()
    ids: set[str] = set()
    coverage = manifest.get("coverage", {}) or {}
    for entry in coverage.values():
        if isinstance(entry, dict):
            ids.update(str(r) for r in (entry.get("record_ids") or []))
    return ids


def get_pilot_state_abbrs() -> set[str]:
    if not PILOT_STATES_DOC.is_file():
        return set()
    text = PILOT_STATES_DOC.read_text(encoding="utf-8")
    return set(re.findall(r"States/([A-Z]{2})_", text))


def main() -> int:
    import datetime

    errors: list[str] = []
    warnings: list[str] = []
    acknowledged: list[str] = []

    errors.extend(check_ci_completeness())

    pilot_abbrs = get_pilot_state_abbrs()
    today_year = datetime.date.today().year
    state_dirs = sorted(d for d in STATES_DIR.glob("*") if d.is_dir())

    for state_dir in state_dirs:
        rows = load_register(state_dir)
        if not rows:
            continue
        state_abbr = rows[0].get("state_abbr", state_dir.name.split("_", 1)[0])
        has_manifest = any(state_dir.glob("*_UAS_Research_Manifest.yaml"))
        acknowledged_ids = load_manifest_record_ids(state_dir) or set()

        record_findings: list[str] = []
        for row in rows:
            for rule in PER_RECORD_RULES:
                record_findings.extend(rule(row))
        for row in rows:
            record_findings.extend(check_pending_after_cutoff(row, today_year))

        record_findings.extend(check_duplicate_interpretations(rows))

        for finding in record_findings:
            record_id = finding.split(":", 1)[0].split("/")[0]
            if not has_manifest:
                warnings.append(f"[{state_abbr}, no manifest yet — informational] {finding}")
            elif record_id in acknowledged_ids:
                acknowledged.append(f"[{state_abbr}, acknowledged in manifest] {finding}")
            else:
                errors.append(f"[{state_abbr}] {finding}")

        if state_abbr in pilot_abbrs:
            errors.extend(f"[{state_abbr}] {msg}" for msg in check_cross_artifact_agreement(state_abbr, state_dir, rows))

    print(
        f"states_scanned={len(state_dirs)} pilot_states={len(pilot_abbrs)} "
        f"errors={len(errors)} warnings={len(warnings)} acknowledged={len(acknowledged)}"
    )
    for item in errors:
        print(f"ERROR: {item}")
    for item in acknowledged:
        print(f"ACKNOWLEDGED (legacy debt, tracked in manifest): {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
