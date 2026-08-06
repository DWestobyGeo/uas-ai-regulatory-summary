"""Validate nationwide Phase 2 completion and report legacy evidence warnings."""

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER_FILES = sorted((ROOT / "States").glob("**/*_UAS_Source_Register.csv"))
EXPECTED = [
    "record_id", "state", "state_abbr", "state_fips", "jurisdiction_name",
    "jurisdiction_type", "geographic_scope", "issuing_authority", "source_title",
    "citation", "source_type", "effective_date", "revision_date", "status",
    "binding_level", "uas_topic", "regulated_party", "regulated_activity",
    "requirement_type", "permit_or_approval_required", "public_agency_only",
    "commercial_operator_relevance", "aec_relevance", "summary",
    "practical_interpretation_aec_expert",
    "practical_interpretation_agency_practitioner",
    "practical_interpretation_uas_procurement_expert",
    "practical_interpretation_legal_counsel", "source_url", "date_accessed",
    "confidence_level", "verification_status", "notes",
]
ROLE_FIELDS = EXPECTED[24:28]
AGENCY_NA = "N/A — no agency process involved"
PROCUREMENT_NA = "N/A — no procurement or equipment-selection implication identified"
# Governed as of Agent_Instructions.v6.md 6.4.0 (Workstream 5) -- usable only when a documented
# routing determination supports them (scripts/route_interpretation_roles.py). Expected to be
# rare; see the AEC/legal role docs.
AEC_NO_IMPACT = "No material AEC operational implication identified beyond the objective requirement."
LEGAL_NO_IMPACT = "No separate legal-risk implication identified beyond compliance with the stated authority."
PENDING_VALUES = {"PENDING — Phase 2", "Pending Phase 2 interpretation pass"}
errors: list[str] = []
warnings: list[str] = []
ids: list[str] = []
states: list[str] = []
records = 0

if len(REGISTER_FILES) != 50:
    errors.append(f"Expected 50 registers, found {len(REGISTER_FILES)}")

for path in REGISTER_FILES:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED:
            errors.append(f"{path.relative_to(ROOT)}: schema mismatch ({len(reader.fieldnames or [])} fields)")
        rows = list(reader)
    if not rows:
        errors.append(f"{path.relative_to(ROOT)}: no records")
        continue
    states.append(rows[0].get("state_abbr", ""))
    for row in rows:
        records += 1
        rid = row.get("record_id", "")
        ids.append(rid)
        if None in row:
            errors.append(f"{rid}: extra CSV columns")
        for field in EXPECTED:
            if row.get(field) is None:
                errors.append(f"{rid}: missing field {field}")
        for field in ROLE_FIELDS:
            value = (row.get(field) or "").strip()
            if not value:
                errors.append(f"{rid}: empty {field}")
            if value in PENDING_VALUES:
                errors.append(f"{rid}: pending {field}")
        agency = (row.get(ROLE_FIELDS[1]) or "").strip()
        procurement = (row.get(ROLE_FIELDS[2]) or "").strip()
        aec = (row.get(ROLE_FIELDS[0]) or "").strip()
        legal = (row.get(ROLE_FIELDS[3]) or "").strip()
        if agency.startswith("N/A") and agency != AGENCY_NA:
            errors.append(f"{rid}: nonstandard agency N/A: {agency}")
        if procurement.startswith("N/A") and procurement != PROCUREMENT_NA:
            errors.append(f"{rid}: nonstandard procurement N/A: {procurement}")
        if aec.startswith("N/A"):
            errors.append(f"{rid}: unsupported N/A in AEC role (governed value is {AEC_NO_IMPACT!r}, not a bare N/A)")
        elif aec.lower().startswith("no material") and aec != AEC_NO_IMPACT:
            errors.append(f"{rid}: nonstandard AEC no-impact value: {aec}")
        if legal.startswith("N/A"):
            errors.append(f"{rid}: unsupported N/A in legal role (governed value is {LEGAL_NO_IMPACT!r}, not a bare N/A)")
        elif legal.lower().startswith("no separate legal-risk") and legal != LEGAL_NO_IMPACT:
            errors.append(f"{rid}: nonstandard legal no-impact value: {legal}")
        source_type = row.get("source_type", "")
        if re.search(r"Discovery lead|not found|^N/A$", source_type, re.I):
            warnings.append(f"legacy non-authority row {rid}: {row.get('source_title', '')}")
        url = (row.get("source_url") or "").strip()
        if url and not re.search(r"https?://", url):
            warnings.append(f"legacy source URL for {rid}: {url}")

dupes = [rid for rid, count in Counter(ids).items() if count > 1]
if dupes:
    errors.append(f"Duplicate record ids: {', '.join(dupes)}")
if len(set(states)) != 50:
    errors.append(f"Expected 50 unique state abbreviations, found {len(set(states))}")

for summary in sorted((ROOT / "States").glob("**/*_UAS_Regulatory_Summary.md")):
    text = summary.read_text(encoding="utf-8-sig")
    for label in (
        "**Prepared for:**", "**Research date:**", "**Version:**",
        "**Model / checkpoint:**", "**Interpretation scope:**", "**Scope note:**",
    ):
        if label not in text:
            errors.append(f"{summary.relative_to(ROOT)}: missing {label}")
    if any(value in text for value in PENDING_VALUES):
        errors.append(f"{summary.relative_to(ROOT)}: pending Phase 2 text")

print(f"registers={len(REGISTER_FILES)} states={len(set(states))} records={records} unique_ids={len(set(ids))}")
print(f"errors={len(errors)} warnings={len(warnings)}")
for item in errors:
    print(f"ERROR: {item}")
for item in warnings:
    print(f"WARNING: {item}")
raise SystemExit(1 if errors else 0)
