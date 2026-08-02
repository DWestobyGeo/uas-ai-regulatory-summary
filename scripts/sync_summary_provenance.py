"""Normalize Phase 2 provenance metadata without rewriting research or opinions."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE = "Agent Instructions v6 (August 2, 2026)"
UNKNOWN_MODEL = "Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet."
CODEX_MODEL = "Objective research model retained from Phase 1; Phase 2 interpretations drafted with OpenAI GPT-5 (Codex; exact checkpoint unavailable)."


def state_name_from_title(text: str, fallback: str) -> str:
    first = text.splitlines()[0] if text.splitlines() else ""
    match = re.match(r"#\s+(.+?)(?:\s+[—-]\s+|\s+UAS\b)", first)
    return match.group(1).strip() if match else fallback


def sync(path: Path, model: str | None, scope: str, role_scopes: str | None) -> bool:
    original = path.read_text(encoding="utf-8-sig")
    text = original
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Expected H1 title in {path}")

    state = state_name_from_title(text, path.parent.name.split("_", 1)[-1].replace("_", " "))
    if "**Prepared for:**" not in text:
        block = (
            "\n\n**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management\n"
            "**Research date:** August 2, 2026\n"
            "**Version:** 2.0 (Phase 2 — practical interpretation complete)\n"
            f"**Model / checkpoint:** {model or UNKNOWN_MODEL}\n"
            f"**Interpretation scope:** {scope}\n"
            f"**Scope note:** This summary covers {state} state and state-agency-level UAS authority only. FAA Part 107 remains the nationwide operating baseline; local, tribal, and live-airspace layers are deferred under the current research scope.\n"
            "\n> **Process note:** Objective research is retained from the Phase 1 source packet. The four practical-interpretation roles were completed in Phase 2 on 2026-08-02; model provenance is recorded above."
        )
        text = lines[0] + block + "\n" + "\n".join(lines[1:]).lstrip("\n")
    else:
        if "**Model / checkpoint:**" not in text:
            model_line = f"**Model / checkpoint:** {model or UNKNOWN_MODEL}\n"
            scope_match = re.search(r"(?m)^\*\*Scope note:\*\*", text)
            if scope_match:
                text = text[: scope_match.start()] + model_line + text[scope_match.start() :]
            else:
                text = text.replace("\n", "\n\n" + model_line, 1)
        if "**Interpretation scope:**" not in text:
            model_match = re.search(r"(?m)^\*\*Model / checkpoint:\*\*.*$", text)
            if not model_match:
                raise ValueError(f"Could not place interpretation scope in {path}")
            text = text[: model_match.end()] + f"\n**Interpretation scope:** {scope}" + text[model_match.end() :]
    if role_scopes:
        role_line = f"**Role scopes:** {role_scopes}"
        if "**Role scopes:**" in text:
            text = re.sub(r"(?m)^\*\*Role scopes:\*\*.*$", role_line, text)
        else:
            scope_match = re.search(r"(?m)^\*\*Interpretation scope:\*\*.*$", text)
            if not scope_match:
                raise ValueError(f"Could not place role scopes in {path}")
            text = text[: scope_match.end()] + "\n" + role_line + text[scope_match.end() :]

    text = re.sub(
        r"\*This document is objective legal/regulatory summary; Practical Interpretation content is pending Phase 2 \(see process note above\) and, once added, is not legal advice\.",
        "*This document combines objective legal/regulatory summaries with Phase 2 Practical Interpretation content, which is AI-generated operational opinion and not legal advice.",
        text,
    )
    normalized = text.rstrip() + "\n"
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--state", help="two-letter state abbreviation")
    target.add_argument("--all", action="store_true", help="all state summaries")
    parser.add_argument("--model", help="model/checkpoint provenance for missing metadata")
    parser.add_argument("--scope", default=DEFAULT_SCOPE)
    parser.add_argument("--role-scopes", help="semicolon-separated role IDs and versions actually used")
    args = parser.parse_args()

    if args.all:
        paths = sorted((ROOT / "States").glob("**/*_UAS_Regulatory_Summary.md"))
    else:
        abbr = args.state.upper()
        paths = list((ROOT / "States").glob(f"{abbr}_*/{abbr}_UAS_Regulatory_Summary.md"))
    if not paths:
        raise SystemExit("No matching summary files")

    changed = sum(sync(path, args.model, args.scope, args.role_scopes) for path in paths)
    print(f"Checked {len(paths)} summaries; updated {changed}.")


if __name__ == "__main__":
    main()
