#!/usr/bin/env python3
"""Validate role metadata, standard sections, and governance links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROLE_DIR = ROOT / "agents" / "roles"
GOVERNANCE = ROOT / "Agent_Instructions.v6.md"
ACTIVE_ROLE_FILES = {
    "research-expert.md",
    "aec-industry-uas-expert.md",
    "agency-practitioner.md",
    "uas-procurement-expert.md",
    "aec-industry-legal-counsel.md",
    "state-uas-regulatory-burden-analyst.md",
    "editorial-qa-reviewer.md",
    "web-ux-ui-editor.md",
    "news-aggregator.md",
}
REQUIRED_KEYS = [
    "role_id",
    "name",
    "version",
    "status",
    "last_updated",
    "governance",
    "role_type",
    "phases",
    "governs_sections",
    "governs_fields",
    "may_edit",
    "must_not_edit",
    "record_change_authority",
    "record_change_documentation",
    "required_handoff",
]
REQUIRED_BODY_PHRASES = ["Role and mission", "Required handoff"]


def parse_front_matter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"{path.relative_to(ROOT)} has no valid YAML front matter block.")
        return {}, text
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key_match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if key_match:
            metadata[key_match.group(1)] = (key_match.group(2) or "").strip()
    return metadata, text[match.end() :]


def validate_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)", text):
        clean = target.split("#", 1)[0]
        if re.match(r"^[a-z]+://", clean, flags=re.I):
            continue
        resolved = (path.parent / clean).resolve()
        if not resolved.is_file():
            errors.append(f"Broken Markdown link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if not GOVERNANCE.is_file():
        errors.append("Missing Agent_Instructions.v6.md governance document.")
        governance_text = ""
    else:
        governance_text = GOVERNANCE.read_text(encoding="utf-8")

    actual = {path.name for path in ROLE_DIR.glob("*.md") if path.name not in {"README.md", "ROLE_TEMPLATE.md"}}
    missing = ACTIVE_ROLE_FILES - actual
    extra = actual - ACTIVE_ROLE_FILES
    if missing:
        errors.append(f"Missing active role files: {', '.join(sorted(missing))}")
    if extra:
        warnings.append(f"Unlisted role documents: {', '.join(sorted(extra))}")

    role_ids: set[str] = set()
    role_versions: dict[str, str] = {}
    for filename in sorted(ACTIVE_ROLE_FILES):
        path = ROLE_DIR / filename
        if not path.is_file():
            continue
        metadata, body = parse_front_matter(path, errors)
        for key in REQUIRED_KEYS:
            if key not in metadata:
                errors.append(f"{path.relative_to(ROOT)} is missing metadata key: {key}")
        role_id = metadata.get("role_id", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", role_id):
            errors.append(f"{path.relative_to(ROOT)} has invalid role_id: {role_id!r}")
        elif role_id in role_ids:
            errors.append(f"Duplicate role_id: {role_id}")
        role_ids.add(role_id)
        role_versions[role_id] = metadata.get("version", "")
        for key in ("role_id", "name", "version", "status", "last_updated", "governance", "role_type", "record_change_authority"):
            if not metadata.get(key):
                errors.append(f"{path.relative_to(ROOT)} has an empty scalar metadata value: {key}")
        if metadata.get("status") != "active":
            errors.append(f"{path.relative_to(ROOT)} is listed active but status is {metadata.get('status')!r}.")
        if not re.fullmatch(r"\d+\.\d+\.\d+", metadata.get("version", "")):
            errors.append(f"{path.relative_to(ROOT)} has a non-semantic version.")
        if metadata.get("governance") != "../../Agent_Instructions.v6.md":
            errors.append(f"{path.relative_to(ROOT)} has the wrong governance path.")
        for phrase in REQUIRED_BODY_PHRASES:
            if phrase not in body:
                errors.append(f"{path.relative_to(ROOT)} is missing required body section: {phrase}")
        if f"agents/roles/{filename}" not in governance_text:
            errors.append(f"Governance does not link to agents/roles/{filename}.")
        validate_markdown_links(path, body, errors)

    directory_readme = ROLE_DIR / "README.md"
    template = ROLE_DIR / "ROLE_TEMPLATE.md"
    for path in (directory_readme, template, GOVERNANCE, ROOT / "README.md"):
        if path.is_file():
            validate_markdown_links(path, path.read_text(encoding="utf-8"), errors)

    web_version = role_versions.get("web-ux-ui-editor")
    design_path = ROOT / "docs" / "DESIGN_SYSTEM.md"
    release_path = ROOT / "docs" / "ui-release.json"
    if design_path.is_file() and web_version:
        design = design_path.read_text(encoding="utf-8")
        design_match = re.search(r"\*\*Agent scope:\*\* `web-ux-ui-editor` v([^\s]+)", design)
        if not design_match or design_match.group(1) != web_version:
            errors.append("docs/DESIGN_SYSTEM.md agent-scope version does not match the web role.")
    if release_path.is_file() and web_version:
        try:
            release = json.loads(release_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid docs/ui-release.json: {exc}")
        else:
            if release.get("agent_scope_version") != web_version:
                errors.append("docs/ui-release.json agent_scope_version does not match the web role.")

    if errors:
        print("Role validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Role validation passed: {len(role_ids)} active roles use the shared metadata and section contract.")
    for warning in warnings:
        print(f"Warning: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
