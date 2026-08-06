#!/usr/bin/env python3
"""Assemble a stable-prefix / dynamic-suffix interpretation prompt (Workstream 6).

    prompt = Agent_Instructions.v6.md + role doc + task-frame file + one evidence packet

The first three pieces are the stable, cacheable prefix (unchanged across every record in a
state, and across states, until a governance/role/task-frame version bump); the evidence packet
is the only part that changes per call. See agents/prompt_templates/README.md.

Also supports --measure, which reports assembled-prompt size against a naive baseline (the full
33-field CSV row instead of a compact evidence packet, with no prefix reuse credited) so
Workstream 6's "prompt size is measured against the baseline" acceptance criterion has an actual
number behind it. This is a character-count proxy for token/cost, not live-metered API usage --
said plainly, since no runs/ telemetry exists yet to measure the latter.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
TEMPLATES_DIR = ROOT / "agents" / "prompt_templates"
GOVERNANCE = ROOT / "Agent_Instructions.v6.md"

ROLE_FILES = {
    "aec-expert": ("aec-industry-uas-expert.md", "aec-industry-uas-expert.task.md", "practical_interpretation_aec_expert"),
    "agency-practitioner": ("agency-practitioner.md", "agency-practitioner.task.md", "practical_interpretation_agency_practitioner"),
    "procurement-expert": ("uas-procurement-expert.md", "uas-procurement-expert.task.md", "practical_interpretation_uas_procurement_expert"),
    "legal-counsel": ("aec-industry-legal-counsel.md", "aec-industry-legal-counsel.task.md", "practical_interpretation_legal_counsel"),
}

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_evidence_packet as bep  # noqa: E402
import route_interpretation_roles as rir  # noqa: E402


def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def assemble(role_key: str, row: dict, routing: dict | None) -> tuple[str, str]:
    """Returns (stable_prefix, dynamic_suffix)."""
    role_filename, task_filename, _ = ROLE_FILES[role_key]
    stable_prefix = "\n\n".join([
        GOVERNANCE.read_text(encoding="utf-8"),
        (ROOT / "agents" / "roles" / role_filename).read_text(encoding="utf-8"),
        (TEMPLATES_DIR / task_filename).read_text(encoding="utf-8"),
    ])
    packet = bep.build_packet(row)
    packet["objective_packet_hash"] = bep.packet_hash(packet)
    payload = {"evidence_packet": packet}
    if routing is not None:
        payload["routing"] = routing
    dynamic_suffix = json.dumps(payload, indent=2, ensure_ascii=False)
    return stable_prefix, dynamic_suffix


def naive_baseline_size(role_key: str, row: dict, state_dir: Path) -> int:
    """A prompt built the pre-Workstream-6 way: full CSV row, all four role docs, full
    governance, repeated in full for every single record (no prefix reuse credited)."""
    all_role_text = "\n\n".join(
        (ROOT / "agents" / "roles" / fname).read_text(encoding="utf-8") for fname, _, _ in ROLE_FILES.values()
    )
    full_row_json = json.dumps(row, indent=2, ensure_ascii=False)
    return len(GOVERNANCE.read_text(encoding="utf-8")) + len(all_role_text) + len(full_row_json)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--record-id", required=True)
    parser.add_argument("--role", required=True, choices=list(ROLE_FILES))
    parser.add_argument("--measure", action="store_true")
    args = parser.parse_args()

    matches = list(STATES_DIR.glob(f"{args.state.upper()}_*"))
    if not matches:
        print(f"no States/{args.state.upper()}_* directory found", file=sys.stderr)
        return 1
    state_dir = matches[0]
    rows = {r["record_id"]: r for r in load_register(state_dir)}
    row = rows.get(args.record_id)
    if row is None:
        print(f"record {args.record_id} not found", file=sys.stderr)
        return 1

    routing = rir.route_record(row)
    stable_prefix, dynamic_suffix = assemble(args.role, row, routing)

    if args.measure:
        naive = naive_baseline_size(args.role, row, state_dir)
        assembled = len(stable_prefix) + len(dynamic_suffix)
        print(f"record={args.record_id} role={args.role}")
        print(f"stable_prefix_chars={len(stable_prefix)} (cacheable across every record/state until a version bump)")
        print(f"dynamic_suffix_chars={len(dynamic_suffix)} (unique per call)")
        print(f"assembled_total_chars={assembled}")
        print(f"naive_baseline_chars={naive} (full CSV row + all four role docs + governance, no reuse)")
        print(f"dynamic-suffix-only vs naive baseline: {dynamic_suffix and (1 - len(dynamic_suffix)/naive):.0%} smaller"
              if naive else "n/a")
    else:
        print(stable_prefix)
        print("\n---\n")
        print(dynamic_suffix)
    return 0


if __name__ == "__main__":
    sys.exit(main())
