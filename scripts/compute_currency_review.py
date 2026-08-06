#!/usr/bin/env python3
"""Workstream 8: compute currency-review due dates from the register + manifest (per-state,
pilot states only), instead of leaving `next_currency_review` unset or hand-guessed.

Classifies every record in a state's CSV register into a review cadence bucket using the
"Suggested review frequency" table from
planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md (Workstream 8), derived from
fields the register already has (status, requirement_type, confidence_level) -- no new CSV
columns, per the manifest schema's own non-goals.

  Pending / not-yet-effective / stalled / died-in-committee -> event-triggered + monthly (30d)
  Low confidence_level                                      -> until resolved (30d, same as above)
  Negative finding (reviewed/category-reviewed/no source)   -> annual, and after next legislative
                                                                 session (modeled as 365d)
  Procurement / manufacturer / cybersecurity                -> quarterly (90d)
  Registration / licensing / permit                         -> semiannual (180d)
  Everything else (stable codified statute)                 -> annual (365d)

A record can match more than one bucket (e.g. a low-confidence procurement record); the
shortest cadence wins, since that's the more conservative (more frequently rechecked) choice.

State-level `next_currency_review` = last_currency_check + the shortest cadence across all of
that state's records. `recheck_triggers` lists every record that is pending, not-yet-effective,
or otherwise event-triggered -- these need a recheck on the relevant external event (bill
enacted/failed, amendment's effective date arrives), not just a calendar date, so they are
called out by record_id/reason rather than folded silently into the date math.

This does NOT check whether source URLs are still reachable -- see
scripts/check_source_urls.py for that (a separate, non-blocking concern; URL availability is
not proof of current legal status, and unavailability of an external site is not proof a law
changed).
"""

from __future__ import annotations

import argparse
import csv
import datetime
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"

CADENCE_DAYS = {
    "event_triggered_or_pending": 30,
    "low_confidence": 30,
    "negative_finding": 365,
    "procurement": 90,
    "registration_licensing_permit": 180,
    "stable_statute": 365,
}

PENDING_STATUS_MARKERS = (
    "pending", "not yet effective", "not enacted", "died in", "stalled",
    "not law", "uncertain",
)
NEGATIVE_FINDING_MARKERS = (
    "reviewed", "category reviewed", "no applicable", "no source located",
    "unconfirmed",
)
PROCUREMENT_MARKERS = ("procurement", "manufacturer", "cybersecurity", "vendor")
REG_LICENSE_PERMIT_MARKERS = ("registration", "licens", "permit", "license")


def classify_record(row: dict) -> tuple[str, str]:
    """Return (bucket_key, reason) -- the SHORTEST-cadence bucket the record matches."""
    status = (row.get("status") or "").lower()
    requirement_type = (row.get("requirement_type") or "").lower()
    confidence = (row.get("confidence_level") or "").lower()

    candidates: list[tuple[int, str, str]] = []  # (days, bucket_key, reason)

    if any(m in status for m in PENDING_STATUS_MARKERS):
        candidates.append((
            CADENCE_DAYS["event_triggered_or_pending"], "event_triggered_or_pending",
            f"status is event-triggered/pending ({row.get('status', '')!r})",
        ))
    if confidence == "low":
        candidates.append((
            CADENCE_DAYS["low_confidence"], "low_confidence",
            "confidence_level is Low",
        ))
    if any(m in status for m in NEGATIVE_FINDING_MARKERS):
        candidates.append((
            CADENCE_DAYS["negative_finding"], "negative_finding",
            "status reads as a negative finding (reviewed, no applicable source located)",
        ))
    if any(m in requirement_type for m in PROCUREMENT_MARKERS):
        candidates.append((
            CADENCE_DAYS["procurement"], "procurement",
            "requirement_type involves procurement/manufacturer/cybersecurity",
        ))
    if any(m in requirement_type for m in REG_LICENSE_PERMIT_MARKERS):
        candidates.append((
            CADENCE_DAYS["registration_licensing_permit"], "registration_licensing_permit",
            "requirement_type involves registration/licensing/permitting",
        ))
    if not candidates:
        candidates.append((
            CADENCE_DAYS["stable_statute"], "stable_statute",
            "stable codified statute/rule, no shorter-cadence trigger matched",
        ))

    candidates.sort(key=lambda c: c[0])
    _, bucket, reason = candidates[0]
    return bucket, reason


def load_register(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No source register found in {state_dir}")
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_manifest(state_dir: Path) -> tuple[Path, dict]:
    manifest_files = list(state_dir.glob("*_UAS_Research_Manifest.yaml"))
    if not manifest_files:
        raise FileNotFoundError(f"No research manifest found in {state_dir}")
    if yaml is None:
        raise RuntimeError("pyyaml is required")
    manifest_path = manifest_files[0]
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    return manifest_path, manifest


def compute(state_dir: Path) -> dict:
    rows = load_register(state_dir)
    manifest_path, manifest = load_manifest(state_dir)
    last_check_str = manifest.get("last_currency_check")
    if not last_check_str:
        raise ValueError(f"{manifest_path.relative_to(ROOT)} has no last_currency_check to compute from")
    last_check = datetime.date.fromisoformat(str(last_check_str))

    per_record = []
    triggers = []
    min_days = None
    for row in rows:
        bucket, reason = classify_record(row)
        days = CADENCE_DAYS[bucket]
        due = last_check + datetime.timedelta(days=days)
        per_record.append({
            "record_id": row.get("record_id", ""),
            "bucket": bucket,
            "cadence_days": days,
            "due": due.isoformat(),
            "reason": reason,
        })
        min_days = days if min_days is None else min(min_days, days)
        if bucket == "event_triggered_or_pending":
            triggers.append({"record_id": row.get("record_id", ""), "reason": reason})

    next_review = (last_check + datetime.timedelta(days=min_days)).isoformat() if per_record else None

    return {
        "manifest_path": manifest_path,
        "manifest": manifest,
        "last_currency_check": last_check.isoformat(),
        "next_currency_review": next_review,
        "recheck_triggers": triggers,
        "per_record": per_record,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True, help="state abbreviation, e.g. OK")
    parser.add_argument("--write", action="store_true", help="write next_currency_review and recheck_triggers into the manifest")
    args = parser.parse_args()

    matches = list(STATES_DIR.glob(f"{args.state.upper()}_*"))
    if not matches:
        print(f"no States/{args.state.upper()}_* directory found", file=sys.stderr)
        return 1
    state_dir = matches[0]

    try:
        result = compute(state_dir)
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"state={args.state.upper()} last_currency_check={result['last_currency_check']} "
          f"next_currency_review={result['next_currency_review']}")
    for rec in result["per_record"]:
        print(f"  {rec['record_id']}: bucket={rec['bucket']} due={rec['due']} ({rec['reason']})")
    if result["recheck_triggers"]:
        print("recheck_triggers:")
        for t in result["recheck_triggers"]:
            print(f"  {t['record_id']}: {t['reason']}")

    if args.write:
        manifest = result["manifest"]
        manifest["next_currency_review"] = result["next_currency_review"]
        manifest["recheck_triggers"] = result["recheck_triggers"] or []
        manifest_path = result["manifest_path"]
        # Preserve key order / formatting by only touching the two keys via a light text patch
        # rather than a full yaml.safe_dump (which would reformat comments/ordering away).
        text = manifest_path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        out_lines = []
        skip_until_dedent = False
        wrote_next_review = False
        wrote_triggers = False
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("next_currency_review:"):
                out_lines.append(f"next_currency_review: '{result['next_currency_review']}'\n")
                wrote_next_review = True
                i += 1
                continue
            if line.startswith("recheck_triggers:"):
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                    i += 1
                continue
            out_lines.append(line)
            i += 1
        text = "".join(out_lines)
        if not wrote_next_review:
            text = text.rstrip("\n") + f"\nnext_currency_review: '{result['next_currency_review']}'\n"
        if result["recheck_triggers"]:
            trigger_block = "recheck_triggers:\n"
            for t in result["recheck_triggers"]:
                trigger_block += f"  - record_id: {t['record_id']}\n    reason: {t['reason']!r}\n"
        else:
            trigger_block = "recheck_triggers: []\n"
        text = text.rstrip("\n") + "\n" + trigger_block
        manifest_path.write_text(text, encoding="utf-8")
        print(f"wrote {manifest_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
