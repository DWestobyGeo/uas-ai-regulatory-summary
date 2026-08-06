#!/usr/bin/env python3
"""Deterministic interpretation-role routing (Workstream 5).

For each record, decide whether each of the four interpretation roles is materially relevant
BEFORE that role drafts anything, using only the objective fields (record_id through
date_accessed/confidence_level/notes) -- never the interpretation fields themselves, since the
whole point of routing is to decide relevance ahead of drafting. Output matches the routing
schema in planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md Workstream 5:

    {
      "record_id": "OK-002",
      "aec_relevant": true,
      "agency_process_relevant": false,
      "procurement_relevant": false,
      "legal_analysis_relevant": true,
      "reasons": {"agency_process_relevant": "..."}
    }

Honesty about limits: this is a deterministic heuristic, not a model. It is calibrated against
the agency/procurement governed-N/A decisions already made by the real Phase 2 interpretation
passes in the five pilot states (the only ground truth that currently exists — AEC/legal have no
prior governed N/A to compare against, since Agent_Instructions.v6.md only authorized it at
6.4.0). Run with --calibrate to print the agreement rate and every disagreement.

As of this version: 40/41 (98%) agreement on agency_process_relevant, 41/41 (100%) on
procurement_relevant across the five pilot states. The one remaining disagreement is WA-004,
where the record's own status is 'UNCERTAIN - verify current codification' -- a keyword rule
has no way to know a mentioned process (DOC authorization) shouldn't be routed as relevant when
the record itself hasn't been verified; a human/model reviewer correctly withheld a governed
agency disposition here pending verification, which this script cannot replicate without reading
status/confidence semantics more deeply than a keyword pass. New routing decisions should be
spot-checked, not trusted blindly, exactly per the plan's Workstream 5 acceptance criterion that
every substantive output document its reason.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
AGENCY_NA = "N/A — no agency process involved"
PROCUREMENT_NA = "N/A — no procurement or equipment-selection implication identified"

AGENCY_PROCESS_KEYWORDS = re.compile(
    r"\b(permi(t|ts|ssion)|regist(er|ration)\w*|licens\w*|warrant\w*|authoriz\w*|"
    r"director-issued|program plan|application|approv(e|ed|al)|consent)\b", re.I
)
NEGATED_PROCESS_PATTERN = re.compile(
    r"\bnot a (separate )?(state )?(permit|process)\b|\bno permit\b", re.I
)
PRIVATE_CONSENT_CARVEOUT = re.compile(
    r"owner or lessee|landowner|property owner|private[- ]property.{0,20}consent", re.I
)
APPROVED_EQUIPMENT_LIST_PATTERN = re.compile(
    r"approved?\s+(manufacturer|equipment|vendor)(\s*list)?", re.I
)
MANUFACTURER_TEST_DEMO_CARVEOUT = re.compile(r"manufactur\w*\s+(test|demo)", re.I)
PROCUREMENT_KEYWORDS = re.compile(
    r"\b(procur\w*|manufactur\w*|cybersecurity|security (requirement|standard)|component\w*|"
    r"country of origin|approved?.{0,20}(list|manufacturer|vendor)|fleet\w*|"
    r"registration (certificate|requirement)\w*)\b", re.I
)
INERT_RECORD_MARKERS = re.compile(
    r"myth-busting|widely repeated misinformation|informational|no.{0,10}(source|authority) "
    r"(found|located)|negative finding|not law", re.I
)


def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def route_record(row: dict) -> dict:
    record_id = row.get("record_id", "")
    permit = row.get("permit_or_approval_required", "") or ""
    req_type = row.get("requirement_type", "") or ""
    topic = row.get("uas_topic", "") or ""
    summary = row.get("summary", "") or ""
    status = row.get("status", "") or ""

    haystack_agency = " ".join([permit, req_type])
    haystack_procurement = " ".join([topic, req_type, summary, permit])

    agency_has_keyword = bool(AGENCY_PROCESS_KEYWORDS.search(haystack_agency))
    agency_is_private_consent_only = bool(PRIVATE_CONSENT_CARVEOUT.search(haystack_agency)) and not re.search(
        r"\bstate park|\bdirector|\bagency\b|\bdepartment\b", haystack_agency, re.I
    )
    agency_is_negated = bool(NEGATED_PROCESS_PATTERN.search(haystack_agency))
    agency_is_equipment_approval_only = bool(APPROVED_EQUIPMENT_LIST_PATTERN.search(haystack_agency)) and not bool(
        re.sub(APPROVED_EQUIPMENT_LIST_PATTERN, "", haystack_agency).strip() and
        AGENCY_PROCESS_KEYWORDS.search(re.sub(APPROVED_EQUIPMENT_LIST_PATTERN, "", haystack_agency))
    )
    agency_relevant = (
        agency_has_keyword
        and not agency_is_private_consent_only
        and not agency_is_negated
        and not agency_is_equipment_approval_only
    )

    procurement_text_for_matching = MANUFACTURER_TEST_DEMO_CARVEOUT.sub(" ", haystack_procurement)
    procurement_relevant = bool(PROCUREMENT_KEYWORDS.search(procurement_text_for_matching))

    is_inert = bool(INERT_RECORD_MARKERS.search(" ".join([status, req_type, topic])))
    aec_relevant = not is_inert
    legal_relevant = not is_inert

    reasons = {}
    if not agency_relevant:
        if agency_is_private_consent_only:
            reasons["agency_process_relevant"] = (
                "The only consent/authorization language found is a private-party (owner/lessee) "
                "consent, not a government-administered application, registration, permit, waiver, "
                "or approval process."
            )
        else:
            reasons["agency_process_relevant"] = (
                "No government-administered application, registration, permit, waiver, or approval "
                "process found in permit_or_approval_required or requirement_type."
            )
    if not procurement_relevant:
        reasons["procurement_relevant"] = (
            "No equipment, manufacturer, component, cybersecurity, registration/fleet, or "
            "procurement-program language found in the objective fields."
        )
    if not aec_relevant:
        reasons["aec_relevant"] = (
            "Record is informational, a debunked/non-enacted claim, or a negative ('no source "
            "found') result with no operative requirement for AEC field operations."
        )
    if not legal_relevant:
        reasons["legal_analysis_relevant"] = (
            "Record is informational, a debunked/non-enacted claim, or a negative ('no source "
            "found') result with no separate legal-risk implication beyond that finding itself."
        )

    result = {
        "record_id": record_id,
        "aec_relevant": aec_relevant,
        "agency_process_relevant": agency_relevant,
        "procurement_relevant": procurement_relevant,
        "legal_analysis_relevant": legal_relevant,
    }
    if reasons:
        result["reasons"] = reasons
    return result


def route_state(state_dir: Path) -> list[dict]:
    return [route_record(row) for row in load_register(state_dir)]


def calibrate() -> int:
    """Compare agency_process_relevant / procurement_relevant against the real governed-N/A
    decisions already made in the five pilot states -- the only ground truth available."""
    pilot_doc = ROOT / "evals" / "pilot_states.md"
    pilot_abbrs = set(re.findall(r"States/([A-Z]{2})_", pilot_doc.read_text(encoding="utf-8")))
    total = 0
    agree_agency = 0
    agree_procurement = 0
    disagreements = []
    for state_dir in sorted(STATES_DIR.glob("*")):
        rows = load_register(state_dir)
        if not rows:
            continue
        abbr = rows[0].get("state_abbr", "")
        if abbr not in pilot_abbrs:
            continue
        for row in rows:
            routed = route_record(row)
            actual_agency = row["practical_interpretation_agency_practitioner"].strip() != AGENCY_NA
            actual_procurement = row["practical_interpretation_uas_procurement_expert"].strip() != PROCUREMENT_NA
            total += 1
            if routed["agency_process_relevant"] == actual_agency:
                agree_agency += 1
            else:
                disagreements.append(
                    f"{row['record_id']}: agency_process_relevant routed={routed['agency_process_relevant']} "
                    f"actual={actual_agency}"
                )
            if routed["procurement_relevant"] == actual_procurement:
                agree_procurement += 1
            else:
                disagreements.append(
                    f"{row['record_id']}: procurement_relevant routed={routed['procurement_relevant']} "
                    f"actual={actual_procurement}"
                )
    print(f"calibration records={total}")
    print(f"agency_process_relevant agreement: {agree_agency}/{total} ({agree_agency/total:.0%})")
    print(f"procurement_relevant agreement: {agree_procurement}/{total} ({agree_procurement/total:.0%})")
    for item in disagreements:
        print(f"DISAGREEMENT: {item}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", help="state abbreviation, e.g. OK (default: all pilot states)")
    parser.add_argument("--calibrate", action="store_true", help="print agreement rate vs. real pilot-state data")
    parser.add_argument("--out-dir", default=None, help="write one {ABBR}_routing.json per state here")
    args = parser.parse_args()

    if args.calibrate:
        return calibrate()

    pilot_doc = ROOT / "evals" / "pilot_states.md"
    pilot_abbrs = sorted(set(re.findall(r"States/([A-Z]{2})_", pilot_doc.read_text(encoding="utf-8"))))
    targets = [args.state.upper()] if args.state else pilot_abbrs

    out_dir = Path(args.out_dir) if args.out_dir else None
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)

    for abbr in targets:
        matches = list(STATES_DIR.glob(f"{abbr}_*"))
        if not matches:
            print(f"no States/{abbr}_* directory found", file=sys.stderr)
            continue
        routing = route_state(matches[0])
        doc = {"state_abbr": abbr, "records": routing}
        if out_dir:
            out_path = out_dir / f"{abbr}_routing.json"
            out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"wrote {out_path}")
        else:
            print(json.dumps(doc, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    sys.exit(main())
