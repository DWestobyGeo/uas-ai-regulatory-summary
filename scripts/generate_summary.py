#!/usr/bin/env python3
"""Generate a state's printable Markdown summary from its authored template + source register
(Workstream 7).

Per the plan: "Generate authority headings, metadata, objective summaries, and four role
bullets from the register. Keep state overview, cross-record synthesis, unresolved questions,
and limited context as authored sections." This script implements that split.

Inputs, per state:
  States/XX_State/XX_UAS_Summary_Authored.md   -- the authored template (see format below)
  States/XX_State/XX_UAS_Source_Register.csv   -- the 33-field register (unchanged, source of truth)

Output:
  States/XX_State/XX_UAS_Regulatory_Summary.md -- regenerated in full, every run

Authored template format: ordinary Markdown for the header block and authored sections
(overview, non-regulatory context, unresolved questions, confidence summary, etc.), with one
HTML-comment marker per generated section, in place of that section's body:

    <!-- GENERATED_SECTION heading="2. Statewide UAS Laws and Regulations"
         records="OK-001,OK-002" heading_style="record_id_and_title" -->

`records` is an explicit, authored ordered list of record_ids -- which section an authority
belongs in (statewide law vs. state-agency requirement) is an editorial/organizational
judgment, not a fact derivable from any single register field (jurisdiction_type does not
reliably distinguish this across the five pilot states; see the Workstream 7 note in
SESSIONS.md). `heading_style` controls per-record header formatting, since the five pilot
states did not converge on one convention before this workstream:

  record_id_and_title -> ### {record_id} — {source_title}      (Oklahoma's existing style)
  citation_and_title  -> ### {citation} — {source_title}       (Minnesota/California/Florida's existing style)

This script picks whichever style each state's authored template specifies, so a first
regeneration reproduces that state's EXISTING headings exactly -- Workstream 7 deduplicates
authorship, it does not silently change a state's presentation.

Every authority's `### ... *type | status*` block, Objective Summary, and four Practical
Interpretation bullets are generated from the register every time; hand-editing them in
XX_UAS_Regulatory_Summary.md is pointless (they are overwritten on the next `python3
build_data.py`/generate run) and is exactly what scripts/validate_generated_summary.py checks
for and fails on.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"

MARKER_PATTERN = re.compile(
    r'<!--\s*GENERATED_SECTION\s+heading="([^"]+)"\s+records="([^"]*)"\s+heading_style="([^"]+)"\s*-->'
)

GENERATED_WARNING = (
    "> **Generated content notice:** The authority sections below (headings, type/status line, "
    "Objective Summary, and the four Practical Interpretation bullets for each record) are "
    "generated verbatim from `{csv_name}` by `scripts/generate_summary.py`. Do not hand-edit "
    "them here -- edit the register and regenerate. The overview, unresolved-questions, and any "
    "other narrative sections are authored directly in `{authored_name}`."
)

ROLE_LABELS = [
    ("practical_interpretation_aec_expert", "AEC Industry UAS Expert"),
    ("practical_interpretation_agency_practitioner", "Agency Practitioner"),
    ("practical_interpretation_uas_procurement_expert", "UAS Procurement Expert"),
    ("practical_interpretation_legal_counsel", "AEC Industry Legal Counsel"),
]


def load_register(state_dir: Path) -> dict[str, dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No source register found in {state_dir}")
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["record_id"]: row for row in csv.DictReader(handle)}, csv_files[0].name


def format_record_heading(row: dict, heading_style: str) -> str:
    if heading_style == "record_id_and_title":
        return f"### {row['record_id']} — {row['source_title']}"
    if heading_style == "citation_and_title":
        return f"### {row['citation']} — {row['source_title']}"
    raise ValueError(f"Unknown heading_style: {heading_style!r}")


def render_record(row: dict, heading_style: str) -> str:
    lines = [
        format_record_heading(row, heading_style),
        f"*{row['source_type']} | {row['status']}*",
        "",
        f"**Objective Summary:** {row['summary']}",
        "",
        "**Practical Interpretation**",
        "",
    ]
    for field, label in ROLE_LABELS:
        lines.append(f"- **{label}:** {row[field]}")
    return "\n".join(lines)


def render_section(heading: str, record_ids: list[str], heading_style: str, records: dict[str, dict]) -> str:
    parts = [f"## {heading}", ""]
    missing = [rid for rid in record_ids if rid not in records]
    if missing:
        raise KeyError(f"records referenced in template but not in register: {missing}")
    for rid in record_ids:
        parts.append(render_record(records[rid], heading_style))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def generate(state_dir: Path) -> str:
    templates = list(state_dir.glob("*_UAS_Summary_Authored.md"))
    if not templates:
        raise FileNotFoundError(f"No authored template found in {state_dir}")
    template_path = templates[0]
    template = template_path.read_text(encoding="utf-8-sig")
    records, csv_name = load_register(state_dir)

    def replace(match: re.Match) -> str:
        heading, records_csv, heading_style = match.groups()
        record_ids = [r.strip() for r in records_csv.split(",") if r.strip()]
        return render_section(heading, record_ids, heading_style, records).rstrip()

    body = MARKER_PATTERN.sub(replace, template)

    # Insert the generated-content notice right after the header block (before the first "## ").
    warning = GENERATED_WARNING.format(csv_name=csv_name, authored_name=template_path.name)
    first_heading = re.search(r"(?m)^## ", body)
    if first_heading and warning not in body:
        insertion_point = first_heading.start()
        body = body[:insertion_point] + warning + "\n\n" + body[insertion_point:]

    return body.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True, help="state abbreviation, e.g. OK")
    parser.add_argument("--write", action="store_true", help="write the result to XX_UAS_Regulatory_Summary.md (default: print to stdout)")
    parser.add_argument("--check", action="store_true", help="exit 1 if the generated output differs from the committed file (does not write)")
    args = parser.parse_args()

    matches = list(STATES_DIR.glob(f"{args.state.upper()}_*"))
    if not matches:
        print(f"no States/{args.state.upper()}_* directory found", file=sys.stderr)
        return 1
    state_dir = matches[0]

    try:
        generated = generate(state_dir)
    except (FileNotFoundError, KeyError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    out_path = next(state_dir.glob("*_UAS_Regulatory_Summary.md"), None)

    if args.check:
        if out_path is None or not out_path.is_file():
            print(f"no existing {args.state.upper()}_UAS_Regulatory_Summary.md to check against", file=sys.stderr)
            return 1
        current = out_path.read_text(encoding="utf-8-sig")
        if current.rstrip() + "\n" != generated:
            print(f"DRIFT: {out_path.relative_to(ROOT)} does not match what generate_summary.py would produce.")
            return 1
        print(f"OK: {out_path.relative_to(ROOT)} matches the generator output.")
        return 0

    if args.write:
        if out_path is None:
            out_path = state_dir / f"{args.state.upper()}_UAS_Regulatory_Summary.md"
        out_path.write_text(generated, encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(generated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
