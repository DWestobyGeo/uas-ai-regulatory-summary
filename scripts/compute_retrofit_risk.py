#!/usr/bin/env python3
"""Workstream 9, tasks 1-2: compute a retrofit-risk score and publish a transparent, risk-ordered
national retrofit queue for the 45 non-pilot states.

Scope note: this script scores and orders retrofit work; it does not perform it. Actually
re-verifying a state's law against current primary sources (Workstream 9 task 3, "process one
state per substantive research commit") is real legal research requiring live web access and
careful, record-by-record judgment -- deliberately out of scope for a deterministic script, and
not something this repository's tooling should attempt to automate wholesale. See
planning/national_retrofit_queue.md's own preamble for how the queue is meant to be worked.

## Tier assignment (mirrors planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md,
## "Workstream 9" verbatim)

Tier 1 (Immediate) if ANY of:
  - the state has no research manifest and no narrative research checklist at all, OR its
    checklist contains an explicit unresolved/TBD marker ("legacy states" / "states with
    unresolved checklist categories")
  - any record has confidence_level Low ("low-confidence records")
  - any record's status reads as proposed/pending/failed/died/stalled/superseded/uncertain
    ("proposed/pending/failed/superseded records")
  - any record's requirement_type/summary/title mentions felony or misdemeanor ("criminal/felony
    restrictions")
  - any record involves registration, licensing, permitting, or procurement ("registration,
    licensing, permit, and procurement restrictions")
  - any record's source_type reads as secondary/non-primary ("secondary-source controlling
    records")

Tier 2 (High complexity) if not Tier 1 and ANY of:
  - record_count is large (>= HIGH_RECORD_COUNT) ("states with many authorities")
  - no record's text mentions preemption at all ("states lacking broad preemption")
  - more than one distinct issuing_authority among permit-required records ("states with
    multiple agency permit systems")
  - more than PROCUREMENT_OR_PUBLIC_AGENCY_THRESHOLD public-agency-only or procurement-flavored
    records ("states with significant public-agency or procurement restrictions")

Tier 3 (Recent clean states): everything else.

A state satisfying multiple triggers is still just Tier 1/2/3 (the tier rules aren't scored),
but WITHIN each tier, states are ordered by a numeric risk_score (a documented, unweighted sum
of the underlying signal counts) so the queue is a total order, not just three buckets -- highest
score first.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"
PILOT_STATES_DOC = ROOT / "evals" / "pilot_states.md"

PROGRESS_SECTION_PLACEHOLDER = "\x00PROGRESS_SECTION\x00"

HIGH_RECORD_COUNT = 10
PROCUREMENT_OR_PUBLIC_AGENCY_THRESHOLD = 2

UNSTABLE_STATUS_MARKERS = (
    "pending", "not yet effective", "not enacted", "died in", "stalled",
    "not law", "uncertain", "failed", "superseded", "repealed", "expired",
)
SECONDARY_SOURCE_MARKERS = (
    "secondary", "normalized legal publisher", "compilation", "discovery lead", "advisory",
)
REG_LICENSE_PERMIT_PROCUREMENT_MARKERS = (
    "registration", "licens", "permit", "procurement", "manufacturer", "cybersecurity", "vendor",
)
CRIMINAL_MARKERS = ("felony", "misdemeanor")
UNRESOLVED_CHECKLIST_MARKERS = ("unresolved", "tbd", "to be determined", "needs verification")


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


def score_state(state_dir: Path) -> dict:
    rows = load_register(state_dir)
    abbr = rows[0].get("state_abbr", state_dir.name.split("_", 1)[0]) if rows else state_dir.name.split("_", 1)[0]
    name = rows[0].get("state", state_dir.name.split("_", 1)[-1]) if rows else state_dir.name.split("_", 1)[-1]

    has_manifest = any(state_dir.glob("*_UAS_Research_Manifest.yaml"))
    checklist_files = list(state_dir.glob("*_UAS_Research_Checklist.md"))
    has_checklist = bool(checklist_files)
    checklist_unresolved = False
    if checklist_files:
        text = checklist_files[0].read_text(encoding="utf-8", errors="replace").lower()
        checklist_unresolved = any(marker in text for marker in UNRESOLVED_CHECKLIST_MARKERS)

    low_confidence_count = 0
    unstable_status_count = 0
    criminal_count = 0
    reg_permit_count = 0
    secondary_source_count = 0
    preemption_mentioned = False
    permit_authorities: set[str] = set()
    public_agency_or_procurement_count = 0

    for r in rows:
        confidence = (r.get("confidence_level") or "").strip().lower()
        status = (r.get("status") or "").lower()
        source_type = (r.get("source_type") or "").lower()
        blob = " ".join([
            r.get("requirement_type", ""), r.get("summary", ""), r.get("source_title", ""),
        ]).lower()

        if confidence == "low":
            low_confidence_count += 1
        if any(m in status for m in UNSTABLE_STATUS_MARKERS):
            unstable_status_count += 1
        if any(m in blob for m in CRIMINAL_MARKERS):
            criminal_count += 1
        if any(m in blob for m in REG_LICENSE_PERMIT_PROCUREMENT_MARKERS):
            reg_permit_count += 1
        if any(m in source_type for m in SECONDARY_SOURCE_MARKERS):
            secondary_source_count += 1
        if "preempt" in blob:
            preemption_mentioned = True
        if (r.get("permit_or_approval_required") or "").strip().lower() == "yes":
            permit_authorities.add((r.get("issuing_authority") or "").strip())
        if (r.get("public_agency_only") or "").strip().lower() == "yes" or "procurement" in blob:
            public_agency_or_procurement_count += 1

    record_count = len(rows)
    legacy_signal = (not has_manifest) and (not has_checklist or checklist_unresolved)

    tier1_triggers = []
    if legacy_signal:
        tier1_triggers.append(
            "legacy state (no manifest" + (", no checklist" if not has_checklist else ", checklist has an unresolved/TBD marker") + ")"
        )
    if low_confidence_count:
        tier1_triggers.append(f"{low_confidence_count} low-confidence record(s)")
    if unstable_status_count:
        tier1_triggers.append(f"{unstable_status_count} proposed/pending/failed/superseded record(s)")
    if criminal_count:
        tier1_triggers.append(f"{criminal_count} criminal/felony-restriction record(s)")
    if reg_permit_count:
        tier1_triggers.append(f"{reg_permit_count} registration/licensing/permit/procurement record(s)")
    if secondary_source_count:
        tier1_triggers.append(f"{secondary_source_count} secondary-source-controlling record(s)")

    tier2_triggers = []
    if record_count >= HIGH_RECORD_COUNT:
        tier2_triggers.append(f"{record_count} authorities (>= {HIGH_RECORD_COUNT})")
    if not preemption_mentioned:
        tier2_triggers.append("no record mentions state preemption of local ordinances")
    if len(permit_authorities) > 1:
        tier2_triggers.append(f"{len(permit_authorities)} distinct permit-issuing authorities")
    if public_agency_or_procurement_count > PROCUREMENT_OR_PUBLIC_AGENCY_THRESHOLD:
        tier2_triggers.append(f"{public_agency_or_procurement_count} public-agency/procurement record(s)")

    if tier1_triggers:
        tier = 1
    elif tier2_triggers:
        tier = 2
    else:
        tier = 3

    risk_score = (
        (3 if legacy_signal else 0)
        + low_confidence_count
        + unstable_status_count
        + criminal_count
        + reg_permit_count
        + secondary_source_count
        + (1 if record_count >= HIGH_RECORD_COUNT else 0)
        + (1 if not preemption_mentioned else 0)
        + (1 if len(permit_authorities) > 1 else 0)
        + (1 if public_agency_or_procurement_count > PROCUREMENT_OR_PUBLIC_AGENCY_THRESHOLD else 0)
    )

    return {
        "state_abbr": abbr,
        "state": name,
        "tier": tier,
        "risk_score": risk_score,
        "record_count": record_count,
        "has_manifest": has_manifest,
        "has_checklist": has_checklist,
        "checklist_unresolved": checklist_unresolved,
        "tier1_triggers": tier1_triggers,
        "tier2_triggers": tier2_triggers,
    }


def compute_all() -> list[dict]:
    pilot_abbrs = get_pilot_state_abbrs()
    state_dirs = sorted(d for d in STATES_DIR.glob("*") if d.is_dir())
    results = []
    for state_dir in state_dirs:
        abbr_guess = state_dir.name.split("_", 1)[0]
        if abbr_guess in pilot_abbrs:
            continue  # already current_method_complete via Phase B; not part of the retrofit queue
        result = score_state(state_dir)
        if result["record_count"] == 0:
            continue
        results.append(result)
    results.sort(key=lambda r: (r["tier"], -r["risk_score"], r["state_abbr"]))
    return results


def load_progress(pilot_abbrs: set[str]) -> list[dict]:
    """States (pilot or not) that have a research manifest at all -- i.e., have been touched by
    the current-method process, whether via Phase B piloting or a Workstream 9 retrofit. This is
    the authoritative, mechanically-derived answer to "which states are done / in progress" for a
    fresh session picking up this repo cold: don't rely on prose handoff notes alone (SESSIONS.md
    entries can get buried once multiple sessions have logged since), read this instead, or just
    `ls States/*/*_UAS_Research_Manifest.yaml`.
    """
    if yaml is None:
        return []
    progress = []
    for manifest_path in sorted(STATES_DIR.glob("*/*_UAS_Research_Manifest.yaml")):
        try:
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        abbr = str(manifest.get("state_abbr", manifest_path.parent.name.split("_", 1)[0]))
        progress.append({
            "state_abbr": abbr,
            "state": manifest.get("state", manifest_path.parent.name.split("_", 1)[-1]),
            "is_pilot": abbr in pilot_abbrs,
            "research_status": manifest.get("research_status", "unknown"),
            "legacy_retrofit_status": manifest.get("legacy_retrofit_status", "unknown"),
            "last_currency_check": manifest.get("last_currency_check", "unknown"),
            "unresolved_count": manifest.get("unresolved_count", "?"),
        })
    progress.sort(key=lambda p: (str(p["last_currency_check"]), p["state_abbr"]))
    return progress


def render_progress_section(progress: list[dict]) -> str:
    lines = [
        "## Retrofit progress so far",
        "",
        "**Read this section first if you are a new session picking this up.** Generated from",
        "every `States/*/*_UAS_Research_Manifest.yaml` that currently exists -- not a hand-kept",
        "list, so it cannot drift out of sync the way a prose note can. A state appears here once",
        "it has a manifest at all (`current_method_in_progress` or better); it does not mean every",
        "open question in that state is resolved -- check `research_status` and",
        "`unresolved_count` per row, and that state's own checklist for specifics.",
        "",
        "| State | Pilot (Phase B) or Workstream 9 retrofit | research_status | unresolved_count | last_currency_check |",
        "|---|---|---|---|---|",
    ]
    for p in progress:
        origin = "Phase B pilot" if p["is_pilot"] else "Workstream 9 retrofit"
        lines.append(
            f"| {p['state_abbr']} ({p['state']}) | {origin} | {p['research_status']} | "
            f"{p['unresolved_count']} | {p['last_currency_check']} |"
        )
    lines += [
        "",
        f"**{len(progress)} of 50 states** have a manifest as of this generation. Everything else",
        "below is the queue for states that do not yet.",
        "",
    ]
    return "\n".join(lines)


def render_markdown(results: list[dict], pilot_abbrs: set[str]) -> str:
    lines = [
        "# National retrofit queue (Workstream 9)",
        "",
        "Generated by `scripts/compute_retrofit_risk.py` from the 45 non-pilot states' source",
        "registers and (where present) research checklists -- not hand-ranked. Re-run the script",
        "after any state's register/checklist changes to keep this current; do not hand-edit the",
        "table below.",
        "",
        "**This is a queue, not a completed retrofit.** Actually re-verifying a state against",
        "current primary sources (plan Workstream 9, task 3 -- \"process one state per substantive",
        "research commit\") is real legal research: it needs live access to official state sources,",
        "record-by-record judgment, and the same evidence-governance discipline",
        "(`Agent_Instructions.v6.md` Sec 7) already applied to the five pilot states. This script",
        "does not perform that research -- it only scores and orders it so the highest-risk work",
        "happens first and the order is auditable, per the plan's own acceptance criteria",
        "(\"Retrofit order is risk-based and documented\").",
        "",
        f"Pilot states ({', '.join(sorted(pilot_abbrs))}) are excluded from the queue below -- see",
        "the progress ledger immediately below for their status instead.",
        "",
        PROGRESS_SECTION_PLACEHOLDER,
        "## Tier definitions",
        "",
        "| Tier | Meaning |",
        "|---|---|",
        "| 1 -- Immediate | Legacy/no-manifest state, or any record that is low-confidence,",
        "  proposed/pending/failed/superseded, a criminal/felony restriction,",
        "  registration/licensing/permit/procurement, or secondary-source-controlled. |",
        "| 2 -- High complexity | Not Tier 1, but many authorities, no preemption record found,",
        "  multiple permit-issuing agencies, or significant public-agency/procurement content. |",
        "| 3 -- Recent clean | Neither of the above. |",
        "",
        "Within a tier, states are ordered by `risk_score` (highest first) -- an unweighted sum of",
        "the underlying signal counts; see the script's module docstring for the exact formula.",
        "This ordering is a prioritization aid, not a precise severity measurement -- two states in",
        "the same tier with close scores are, for practical purposes, equally urgent.",
        "",
        "## Queue",
        "",
        "| Rank | State | Tier | Risk score | Records | Manifest? | Checklist? | Why |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(results, start=1):
        why = "; ".join(r["tier1_triggers"] + r["tier2_triggers"]) or "no trigger fired"
        manifest = "yes" if r["has_manifest"] else "no"
        checklist = ("yes, unresolved" if r["checklist_unresolved"] else "yes") if r["has_checklist"] else "no"
        lines.append(
            f"| {i} | {r['state_abbr']} ({r['state']}) | {r['tier']} | {r['risk_score']} | "
            f"{r['record_count']} | {manifest} | {checklist} | {why} |"
        )

    tier_counts = {1: 0, 2: 0, 3: 0}
    for r in results:
        tier_counts[r["tier"]] += 1
    lines += [
        "",
        f"**Totals:** {len(results)} states queued -- Tier 1: {tier_counts[1]}, "
        f"Tier 2: {tier_counts[2]}, Tier 3: {tier_counts[3]}.",
        "",
    ]
    if tier_counts[1] == len(results) and results:
        lines += [
            "**Note on the Tier 1 sweep:** every non-pilot state currently lands in Tier 1. This",
            "is expected, not a scoring bug -- the plan's own 'legacy states' trigger fires for any",
            "state without a research manifest, and manifests have so far only been piloted for the",
            "five Phase B states (`evals/pilot_states.md`). Until more states adopt the manifest",
            "convention, the tier label itself won't discriminate; `risk_score` is doing the real",
            "ordering work within Tier 1 for now.",
            "",
        ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-md", type=Path, default=ROOT / "planning" / "national_retrofit_queue.md")
    parser.add_argument("--out-json", type=Path, default=ROOT / "planning" / "national_retrofit_queue.json")
    parser.add_argument("--print", action="store_true", dest="print_only", help="print to stdout, don't write files")
    args = parser.parse_args()

    pilot_abbrs = get_pilot_state_abbrs()
    results = compute_all()
    progress = load_progress(pilot_abbrs)
    md = render_markdown(results, pilot_abbrs).replace(PROGRESS_SECTION_PLACEHOLDER, render_progress_section(progress))

    if args.print_only:
        print(md)
        return 0

    args.out_md.write_text(md, encoding="utf-8")
    args.out_json.write_text(json.dumps({"pilot_states_excluded": sorted(pilot_abbrs), "progress": progress, "queue": results}, indent=2), encoding="utf-8")
    print(f"wrote {args.out_md.relative_to(ROOT)} and {args.out_json.relative_to(ROOT)} ({len(results)} states)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
