#!/usr/bin/env python3
"""Validate active comparative methodologies and their ownership contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METHOD = ROOT / "methodologies" / "state-uas-compliance-burden-index.md"
PREFLIGHT = ROOT / "methodologies" / "preflight" / "scbi-v0.1-preflight.md"
ROLE = ROOT / "agents" / "roles" / "state-uas-regulatory-burden-analyst.md"
GOVERNANCE = ROOT / "Agent_Instructions.v6.md"
REQUIRED_KEYS = {
    "methodology_id",
    "name",
    "version",
    "status",
    "last_updated",
    "governance",
    "intended_owner_role",
    "unit_of_analysis",
    "source_data",
}
EXPECTED_DIMENSIONS = {
    "Operator prerequisites": 20,
    "Mission authorization and coordination": 20,
    "Operational restrictions": 25,
    "Privacy, data, and documentation": 15,
    "Public-project and acquisition conditions": 10,
    "Regulatory complexity": 10,
}


def parse_front_matter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"{path.relative_to(ROOT)} has no valid YAML front matter block.")
        return {}, text
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key_match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if key_match:
            metadata[key_match.group(1)] = key_match.group(2).strip()
    return metadata, text[match.end() :]


def validate_local_links(path: Path, text: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)", text):
        clean = target.split("#", 1)[0]
        if re.match(r"^[a-z]+://", clean, flags=re.I):
            continue
        if not (path.parent / clean).resolve().is_file():
            errors.append(f"Broken Markdown link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []
    for path in (METHOD, PREFLIGHT, ROLE, GOVERNANCE):
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    metadata, body = parse_front_matter(METHOD, errors)
    missing = REQUIRED_KEYS - metadata.keys()
    if missing:
        errors.append(f"Methodology metadata is missing: {', '.join(sorted(missing))}")
    if metadata.get("methodology_id") != "state-uas-compliance-burden-index":
        errors.append("Unexpected SCBI methodology_id.")
    if metadata.get("version") != "1.0.0" or metadata.get("status") != "active":
        errors.append("SCBI must remain active v1.0.0 until a documented versioned revision is adopted.")
    if metadata.get("governance") != "../Agent_Instructions.v6.md":
        errors.append("SCBI governance path is incorrect.")
    if metadata.get("intended_owner_role") != "state-uas-regulatory-burden-analyst":
        errors.append("SCBI owner role is incorrect.")

    found_weights: dict[str, int] = {}
    for name in EXPECTED_DIMENSIONS:
        match = re.search(rf"^\| {re.escape(name)} \| (\d+) \|", body, flags=re.M)
        if match:
            found_weights[name] = int(match.group(1))
        else:
            errors.append(f"Missing weighted dimension row: {name}")
    if found_weights != EXPECTED_DIMENSIONS:
        errors.append(f"SCBI dimension weights changed: {found_weights}")
    if sum(found_weights.values()) != 100:
        errors.append(f"SCBI weights total {sum(found_weights.values())}, not 100.")

    for required in (
        "Routine commercial AEC mission",
        "Public-agency project",
        "Infrastructure or sensitive-site mission",
        "Companion consequence indicator",
        "Not rateable — objective evidence incomplete",
        "reference-portfolio composite",
        "scbi-assessments.csv",
    ):
        if required not in body:
            errors.append(f"SCBI methodology is missing required contract text: {required}")

    role_text = ROLE.read_text(encoding="utf-8")
    governance_text = GOVERNANCE.read_text(encoding="utf-8")
    preflight_text = PREFLIGHT.read_text(encoding="utf-8")
    if "methodologies/state-uas-compliance-burden-index.md" not in role_text:
        errors.append("Owner role does not link to the SCBI methodology.")
    if "methodologies/state-uas-compliance-burden-index.md" not in governance_text:
        errors.append("Governance does not link to the SCBI methodology.")
    if "no publishable state scores produced" not in preflight_text:
        errors.append("Preflight report does not clearly disclaim publishable sample scores.")

    for path in (METHOD, PREFLIGHT, ROLE, GOVERNANCE, ROOT / "methodologies" / "README.md"):
        validate_local_links(path, path.read_text(encoding="utf-8"), errors)

    if errors:
        print("Methodology validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Methodology validation passed: SCBI v1.0.0 is frozen, owned, linked, and internally consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
