#!/usr/bin/env python3
"""Validate the shared GitHub Pages shell and state-data contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_text(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        fail(errors, f"Missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path, errors: list[str]) -> object:
    text = read_text(path, errors)
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        fail(errors, f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def validate_shared_shell(errors: list[str]) -> None:
    html = read_text(DOCS / "index.html", errors)
    css = read_text(DOCS / "style.css", errors)
    js = read_text(DOCS / "app.js", errors)
    design = read_text(DOCS / "DESIGN_SYSTEM.md", errors)
    release = load_json(DOCS / "ui-release.json", errors)

    required_html = {
        'href="style.css"': "shared stylesheet reference",
        'src="app.js"': "shared JavaScript reference",
        'id="main-content"': "main-content landmark",
        'id="state-select"': "state selector",
        'id="state-content"': "state content container",
        'id="summary-panel"': "summary renderer target",
        'id="toc-nav"': "table-of-contents target",
        'id="source-register"': "source register anchor",
        'id="register-list"': "source register list",
        'id="page-status"': "accessible status region",
    }
    for needle, label in required_html.items():
        if needle not in html:
            fail(errors, f"docs/index.html is missing the {label}.")

    required_css = [
        "--content-width:",
        ".reading-layout",
        ".page-toc",
        ".summary-section",
        ".authority-card",
        ".register-section",
        "@media print",
        "prefers-reduced-motion",
    ]
    for selector in required_css:
        if selector not in css:
            fail(errors, f"docs/style.css is missing required design-system rule: {selector}")

    required_js = [
        "function enhanceSummary()",
        "function buildTableOfContents()",
        "function buildCard(record, index)",
        "function renderRegisterList()",
        "UI_VERSION",
    ]
    for contract in required_js:
        if contract not in js:
            fail(errors, f"docs/app.js is missing required shared-renderer contract: {contract}")

    if "How every state inherits the design" not in design:
        fail(errors, "docs/DESIGN_SYSTEM.md does not document state style inheritance.")

    html_match = re.search(r'data-ui-version="([^"]+)"', html)
    js_match = re.search(r'var UI_VERSION = "([^"]+)"', js)
    css_match = re.search(r'UI version:\s*([^\s*]+)', css)
    release_version = release.get("ui_version") if isinstance(release, dict) else None
    versions = {
        "HTML": html_match.group(1) if html_match else None,
        "JavaScript": js_match.group(1) if js_match else None,
        "CSS": css_match.group(1) if css_match else None,
        "release manifest": release_version,
    }
    if None in versions.values():
        fail(errors, f"Missing UI version identifier: {versions}")
    elif len(set(versions.values())) != 1:
        fail(errors, f"UI version identifiers disagree: {versions}")


def validate_state_data(errors: list[str]) -> None:
    index_path = DOCS / "data" / "v1" / "index.json"
    index = load_json(index_path, errors)
    states = index.get("states", []) if isinstance(index, dict) else []
    if not states:
        fail(errors, "docs/data/v1/index.json contains no states.")
        return

    seen: set[str] = set()
    for entry in states:
        if not isinstance(entry, dict):
            fail(errors, "State index contains a non-object entry.")
            continue
        abbr = str(entry.get("state_abbr", "")).upper()
        if not re.fullmatch(r"[A-Z]{2}", abbr):
            fail(errors, f"Invalid state abbreviation in index: {abbr!r}")
            continue
        if abbr in seen:
            fail(errors, f"Duplicate state abbreviation in index: {abbr}")
            continue
        seen.add(abbr)

        state_path = DOCS / "data" / "v1" / f"{abbr}.json"
        data = load_json(state_path, errors)
        if not isinstance(data, dict):
            fail(errors, f"{abbr}.json must contain an object.")
            continue
        if data.get("state_abbr") != abbr:
            fail(errors, f"{abbr}.json state_abbr does not match its filename.")
        if not str(data.get("summary_markdown", "")).strip():
            fail(errors, f"{abbr}.json has no summary_markdown.")
        records = data.get("records")
        if not isinstance(records, list):
            fail(errors, f"{abbr}.json records must be a list.")
            continue
        if data.get("record_count") != len(records):
            fail(errors, f"{abbr}.json record_count does not equal records length.")
        record_ids = [str(record.get("record_id", "")) for record in records if isinstance(record, dict)]
        if len(record_ids) != len(set(record_ids)):
            fail(errors, f"{abbr}.json contains duplicate record IDs.")


def validate_neutral_naming(errors: list[str]) -> None:
    scan_roots = [ROOT / "README.md", ROOT / "agents", DOCS / "index.html", DOCS / "app.js", DOCS / "style.css", DOCS / "DESIGN_SYSTEM.md"]
    paths: list[Path] = []
    for candidate in scan_roots:
        if candidate.is_dir():
            paths.extend(path for path in candidate.rglob("*") if path.is_file() and path.suffix.lower() in {".md", ".html", ".js", ".css", ".json"})
        elif candidate.is_file():
            paths.append(candidate)

    prohibited_name = "ape" + "x"
    prohibited_domain = prohibited_name + "cos.com"
    company_pattern = re.compile(rf"\b{prohibited_name}\b|{re.escape(prohibited_domain)}", re.IGNORECASE)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if company_pattern.search(text):
            fail(errors, f"Company-specific naming found in {path.relative_to(ROOT)}.")


def main() -> int:
    errors: list[str] = []
    validate_shared_shell(errors)
    validate_state_data(errors)
    validate_neutral_naming(errors)

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site validation passed: shared UI contract and state data are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
