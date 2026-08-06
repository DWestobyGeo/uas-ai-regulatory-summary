#!/usr/bin/env python3
"""CI-safe sanity check for scripts/check_source_urls.py's request logic.

Spins up a local HTTP server (evals/fixtures/url_health/mock_server.py) covering the four cases
the checker needs to handle correctly -- reachable (200), broken (404), a server that rejects
HEAD and must fall back to GET, and connection-refused (nothing listening) -- and asserts
check_url()'s classification of each. This does NOT touch the real internet, so unlike
scripts/check_source_urls.py itself (which checks real government source_url values and is
deliberately excluded from the required CI gate, see that script's module docstring), this
fixture check is safe to run on every push/PR.
"""

from __future__ import annotations

import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "evals" / "fixtures" / "url_health"))

import check_source_urls as checker  # noqa: E402
import mock_server  # noqa: E402

PORT = 18917  # arbitrary high port, unlikely to collide in a CI runner


def main() -> int:
    httpd = mock_server.serve(PORT)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    time.sleep(0.2)

    cases = [
        (f"http://127.0.0.1:{PORT}/good.html", True, 200),
        (f"http://127.0.0.1:{PORT}/notfound.html", False, 404),
        (f"http://127.0.0.1:{PORT}/no-head.html", True, 200),  # HEAD->405, must fall back to GET->200
        ("http://127.0.0.1:18999/nothing", False, None),  # nothing listening
    ]

    failures = []
    try:
        for url, expected_ok, expected_status in cases:
            result = checker.check_url(url, timeout=3)
            if result["ok"] != expected_ok or result["status"] != expected_status:
                failures.append(
                    f"{url}: expected ok={expected_ok} status={expected_status}, got "
                    f"ok={result['ok']} status={result['status']} error={result['error']}"
                )
    finally:
        httpd.shutdown()
        httpd.server_close()

    print(f"url_health_fixture_checks: passed={len(cases) - len(failures)} failed={len(failures)}")
    for f in failures:
        print(f"FAIL: {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
