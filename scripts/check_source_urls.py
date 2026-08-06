#!/usr/bin/env python3
"""Workstream 8: check whether register source_url values are still reachable.

**What this checks, and what it deliberately does not claim:** URL reachability is not proof a
cited law/rule/policy is still current, and URL unreachability is not proof it changed --
government sites reorganize URLs, have maintenance windows, block non-browser user agents, or
sit behind CDNs that occasionally hiccup, all without the underlying legal status changing at
all. This script exists to surface a specific, narrow, low-cost signal (a source_url that has
started 404ing, or whose domain no longer resolves, is worth a human glance) -- nothing more. It
is intentionally NOT wired into the required `site-quality.yml` CI gate: a flaky or temporarily
blocked external government site should never fail this repository's build. Run it manually, or
via a separate, non-blocking scheduled workflow (see .github/workflows/url-health-check.yml).

**Sandbox note:** this script cannot be exercised against real government URLs from within the
agent sandbox used to develop it -- that sandbox's network egress is an allowlist that returns
403/blocked-by-allowlist for arbitrary external domains (confirmed against
https://www.oklegislature.gov during development). It has been tested against a local HTTP
server standing in for a mix of 200/404/timeout/connection-refused cases (see
evals/fixtures/url_health/), which exercises the same code paths a real run would. A GitHub
Actions runner has normal internet access and should run this without modification.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES_DIR = ROOT / "States"

DEFAULT_TIMEOUT = 15
DEFAULT_USER_AGENT = (
    "uas-ai-regulatory-summary-url-health-check/1.0 "
    "(+https://github.com/DWestobyGeo/uas-ai-regulatory-summary; informational link check, "
    "not a scraper; low request volume, one pass per URL)"
)


def load_records(state_dir: Path) -> list[dict]:
    csv_files = list(state_dir.glob("*_UAS_Source_Register.csv"))
    if not csv_files:
        return []
    with csv_files[0].open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def check_url(url: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """Return {'url', 'ok', 'status', 'error', 'elapsed_s'}. Tries HEAD first (cheaper, politer),
    falls back to GET since some government servers reject HEAD outright."""
    req_headers = {"User-Agent": DEFAULT_USER_AGENT}
    start = time.monotonic()
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=req_headers, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                elapsed = round(time.monotonic() - start, 2)
                status = getattr(resp, "status", None) or resp.getcode()
                return {"url": url, "ok": 200 <= status < 400, "status": status, "error": None, "elapsed_s": elapsed}
        except urllib.error.HTTPError as exc:
            elapsed = round(time.monotonic() - start, 2)
            if method == "HEAD" and exc.code in (405, 501):
                continue  # server doesn't like HEAD -- fall through to GET
            return {"url": url, "ok": False, "status": exc.code, "error": str(exc), "elapsed_s": elapsed}
        except urllib.error.URLError as exc:
            elapsed = round(time.monotonic() - start, 2)
            return {"url": url, "ok": False, "status": None, "error": str(exc.reason), "elapsed_s": elapsed}
        except (TimeoutError, OSError) as exc:
            elapsed = round(time.monotonic() - start, 2)
            return {"url": url, "ok": False, "status": None, "error": str(exc), "elapsed_s": elapsed}
    return {"url": url, "ok": False, "status": None, "error": "all methods failed", "elapsed_s": round(time.monotonic() - start, 2)}


def collect_urls(state_abbr: str | None) -> dict[str, list[str]]:
    """Return {url: [record_id, ...]} -- one entry per unique URL, since several records
    sometimes cite the same page."""
    url_to_records: dict[str, list[str]] = {}
    state_dirs = sorted(d for d in STATES_DIR.glob("*") if d.is_dir())
    if state_abbr:
        state_dirs = [d for d in state_dirs if d.name.upper().startswith(state_abbr.upper() + "_")]
    for state_dir in state_dirs:
        for row in load_records(state_dir):
            url = (row.get("source_url") or "").strip()
            if not url or not url.lower().startswith(("http://", "https://")):
                continue
            url_to_records.setdefault(url, []).append(row.get("record_id", ""))
    return url_to_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", help="limit to one state abbreviation, e.g. OK (default: all states)")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--delay", type=float, default=0.5, help="seconds to sleep between requests (politeness)")
    parser.add_argument("--out", type=Path, help="write full JSON report to this path")
    parser.add_argument("--fail-on-broken", action="store_true",
                         help="exit 1 if any URL is unreachable (off by default -- see module docstring on why this should stay off in required CI)")
    args = parser.parse_args()

    url_to_records = collect_urls(args.state)
    print(f"checking {len(url_to_records)} unique source_url value(s)"
          + (f" for state {args.state.upper()}" if args.state else " across all states"))

    results = []
    broken = []
    for i, (url, record_ids) in enumerate(sorted(url_to_records.items())):
        result = check_url(url, timeout=args.timeout)
        result["record_ids"] = record_ids
        results.append(result)
        tag = "OK" if result["ok"] else "BROKEN"
        print(f"[{i+1}/{len(url_to_records)}] {tag} status={result['status']} {url} "
              f"(records: {', '.join(record_ids)})")
        if not result["ok"]:
            broken.append(result)
        if args.delay and i < len(url_to_records) - 1:
            time.sleep(args.delay)

    print(f"checked={len(results)} ok={len(results) - len(broken)} broken={len(broken)}")
    if broken:
        print("Broken URLs are worth a human glance, not an automatic finding of legal change "
              "(see module docstring). None of this blocks CI.")
        for r in broken:
            print(f"  BROKEN: {r['url']} status={r['status']} error={r['error']} records={', '.join(r['record_ids'])}")

    if args.out:
        args.out.write_text(json.dumps({
            "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "state_filter": args.state,
            "results": results,
        }, indent=2), encoding="utf-8")
        print(f"wrote {args.out}")

    return 1 if (broken and args.fail_on_broken) else 0


if __name__ == "__main__":
    sys.exit(main())
