#!/usr/bin/env python3
"""Compact per-record evidence packets for interpretation roles (Workstream 6).

Per the improvement plan, each interpretation role should receive only the record-level input
it actually needs to draft its disposition -- not the full 33-field register row (which repeats
state/jurisdiction identity on every record within the same batched state pass, carries raw
source_url/date_accessed citation-verification metadata a drafting role doesn't need, and
duplicates the interpretation fields the role is about to fill in) and not the whole website or
unrelated states/roles.

Packet fields (superset of the plan's Workstream 6 example, extended with the few additional
objective fields an interpretation role plainly needs to draft correctly -- issuing_authority,
source_type, binding_level, effective_date, uas_topic, requirement_type -- while still dropping
everything else):

    record_id, citation, issuing_authority, source_type, binding_level, effective_date,
    status, uas_topic, regulated_party, regulated_activity, requirement_type,
    permit_or_approval_required, public_agency_only, objective_summary, evidence_locator,
    confidence_level, unresolved_questions

`evidence_locator` is synthesized from source_title + source_url, since the 33-field schema has
no dedicated locator field and this does not expand it. `unresolved_questions` is a short list
derived from notes/verification_status when they signal an open issue (citation discrepancy,
unconfirmed status, "recheck", etc.); otherwise empty.

Each packet also gets an `objective_packet_hash` (sha256 of the canonical packet JSON), the same
field name already defined in runs/schema.json (Workstream 0) -- this is what lets a future run
skip regenerating an interpretation whose underlying evidence hasn't changed. See
scripts/route_interpretation_roles.py for the companion role-relevance decision, which normally
runs before this and decides which roles even need a packet for a given record.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
HASH_SNAPSHOT_DIR = ROOT / "runs" / "objective_packet_hashes"

PACKET_FIELDS = [
    "record_id", "citation", "issuing_authority", "source_type", "binding_level",
    "effective_date", "status", "uas_topic", "regulated_party", "regulated_activity",
    "requirement_type", "permit_or_approval_required", "public_agency_only",
    "objective_summary", "evidence_locator", "confidence_level", "unresolved_questions",
]

UNRESOLVED_MARKERS = re.compile(
    r"citation discrepancy|unresolved|not independently confirmed|recheck|verify current|"
    r"UNCERTAIN|unconfirmed|open (item|question)|flagged", re.I
)


def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def build_evidence_locator(row: dict) -> str:
    title = (row.get("source_title") or "").strip()
    url = (row.get("source_url") or "").strip()
    if title and url:
        return f"{title} ({url})"
    return title or url or "Unknown"


def extract_unresolved_questions(row: dict) -> list[str]:
    questions = []
    for field in ("verification_status", "notes"):
        text = (row.get(field) or "").strip()
        if text and UNRESOLVED_MARKERS.search(text):
            # Keep the whole sentence/field rather than a truncated snippet -- an interpreter
            # needs the actual caveat (e.g. the MN-004 citation-discrepancy explanation), not
            # just a flag that one exists.
            questions.append(text)
    return questions


def build_packet(row: dict) -> dict:
    return {
        "record_id": row.get("record_id", ""),
        "citation": row.get("citation", ""),
        "issuing_authority": row.get("issuing_authority", ""),
        "source_type": row.get("source_type", ""),
        "binding_level": row.get("binding_level", ""),
        "effective_date": row.get("effective_date", ""),
        "status": row.get("status", ""),
        "uas_topic": row.get("uas_topic", ""),
        "regulated_party": row.get("regulated_party", ""),
        "regulated_activity": row.get("regulated_activity", ""),
        "requirement_type": row.get("requirement_type", ""),
        "permit_or_approval_required": row.get("permit_or_approval_required", ""),
        "public_agency_only": row.get("public_agency_only", ""),
        "objective_summary": row.get("summary", ""),
        "evidence_locator": build_evidence_locator(row),
        "confidence_level": row.get("confidence_level", ""),
        "unresolved_questions": extract_unresolved_questions(row),
    }


def packet_hash(packet: dict) -> str:
    canonical = json.dumps(packet, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_state_packets(state_dir: Path) -> list[dict]:
    packets = []
    for row in load_register(state_dir):
        packet = build_packet(row)
        packet["objective_packet_hash"] = packet_hash(packet)
        packets.append(packet)
    return packets


def load_hash_snapshot(abbr: str) -> dict[str, str]:
    path = HASH_SNAPSHOT_DIR / f"{abbr}.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("hashes", {})


def write_hash_snapshot(abbr: str, packets: list[dict]) -> Path:
    HASH_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    doc = {
        "state_abbr": abbr,
        "hashes": {p["record_id"]: p["objective_packet_hash"] for p in packets},
    }
    path = HASH_SNAPSHOT_DIR / f"{abbr}.json"
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def check_regeneration(abbr: str, packets: list[dict]) -> tuple[list[str], list[str], list[str]]:
    """Returns (unchanged, changed, new) record_id lists vs. the stored hash snapshot."""
    stored = load_hash_snapshot(abbr)
    current = {p["record_id"]: p["objective_packet_hash"] for p in packets}
    unchanged, changed, new = [], [], []
    for rid, current_hash in current.items():
        if rid not in stored:
            new.append(rid)
        elif stored[rid] == current_hash:
            unchanged.append(rid)
        else:
            changed.append(rid)
    return unchanged, changed, new


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True, help="state abbreviation, e.g. OK")
    parser.add_argument("--record-id", help="build a single record's packet instead of the whole state")
    parser.add_argument("--out-dir", default=None, help="write {ABBR}_evidence_packets.json here instead of stdout")
    parser.add_argument("--snapshot-hashes", action="store_true", help="write runs/objective_packet_hashes/{ABBR}.json from the current register")
    parser.add_argument("--check-regeneration", action="store_true", help="compare current packet hashes against the stored snapshot; skip drafting for unchanged records")
    args = parser.parse_args()

    matches = list(STATES_DIR.glob(f"{args.state.upper()}_*"))
    if not matches:
        print(f"no States/{args.state.upper()}_* directory found", file=sys.stderr)
        return 1
    abbr = args.state.upper()

    packets = build_state_packets(matches[0])

    if args.check_regeneration:
        unchanged, changed, new = check_regeneration(abbr, packets)
        print(f"unchanged={len(unchanged)} changed={len(changed)} new={len(new)}")
        if unchanged:
            print(f"SKIP (objective packet unchanged since last snapshot): {', '.join(unchanged)}")
        if changed:
            print(f"REGENERATE (objective packet changed): {', '.join(changed)}")
        if new:
            print(f"REGENERATE (no prior snapshot): {', '.join(new)}")
        return 0

    if args.snapshot_hashes:
        path = write_hash_snapshot(abbr, packets)
        print(f"wrote {path} ({len(packets)} record hashes)")
        return 0

    if args.record_id:
        packets = [p for p in packets if p["record_id"] == args.record_id]
        if not packets:
            print(f"record {args.record_id} not found", file=sys.stderr)
            return 1

    doc = {"state_abbr": abbr, "packets": packets}
    if args.out_dir:
        out_dir = Path(args.out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{abbr}_evidence_packets.json"
        out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(json.dumps(doc, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
