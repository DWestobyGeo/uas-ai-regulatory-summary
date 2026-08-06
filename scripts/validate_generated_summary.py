#!/usr/bin/env python3
"""Workstream 7 CI gate: fail if any state's authored/generated split has drifted.

For every state that has adopted the authored/generated split (i.e. has an
XX_UAS_Summary_Authored.md), regenerates XX_UAS_Regulatory_Summary.md from the template +
CSV register via scripts/generate_summary.generate() and compares it against the committed
file. This catches two failure modes:

  1. Someone hand-edits a generated authority section directly in
     XX_UAS_Regulatory_Summary.md (the GENERATED_WARNING banner tells them not to, but
     nothing previously enforced it).
  2. Someone edits XX_UAS_Source_Register.csv and forgets to re-run
     `python3 scripts/generate_summary.py --state XX --write`, so the published summary and
     the register (the actual source of truth per governance Sec 5.1) silently disagree.

States that have not yet adopted the split (no authored template -- e.g. WA as of this
writing) are skipped, not flagged; conversion is opt-in per Workstream 7's phased rollout.

Exit code 0 if every converted state's generated output matches the committed file, 1 if any
state has drifted.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_summary as gs  # noqa: E402


def main() -> int:
    state_dirs = sorted(
        d for d in gs.STATES_DIR.iterdir()
        if d.is_dir() and list(d.glob("*_UAS_Summary_Authored.md"))
    )
    if not state_dirs:
        print("no states have adopted the authored/generated split yet -- nothing to check")
        return 0

    failures = []
    for state_dir in state_dirs:
        abbr = state_dir.name.split("_", 1)[0]
        try:
            generated = gs.generate(state_dir)
        except (FileNotFoundError, KeyError, ValueError) as exc:
            failures.append(f"{abbr}: generation error: {exc}")
            continue
        out_path = next(state_dir.glob("*_UAS_Regulatory_Summary.md"), None)
        if out_path is None or not out_path.is_file():
            failures.append(f"{abbr}: has an authored template but no {abbr}_UAS_Regulatory_Summary.md to check against")
            continue
        current = out_path.read_text(encoding="utf-8-sig")
        if current.rstrip() + "\n" != generated:
            failures.append(
                f"{abbr}: {out_path.relative_to(gs.ROOT)} does not match generate_summary.py output "
                f"-- run `python3 scripts/generate_summary.py --state {abbr} --write` and commit the result"
            )

    print(f"checked {len(state_dirs)} converted state(s): {', '.join(d.name.split('_', 1)[0] for d in state_dirs)}")
    if failures:
        print(f"errors={len(failures)}")
        for f in failures:
            print(f"ERROR: {f}")
        return 1
    print("errors=0 -- all converted states' generated summaries match their register + authored template")
    return 0


if __name__ == "__main__":
    sys.exit(main())
