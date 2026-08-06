# Session Ledger

This file tracks work sessions on this repository by any AI agent (any model/checkpoint,
any chat client). The repo is actively edited by more than one independent AI session
under the same GitHub identity, so this ledger exists to reduce collision risk and give
each new session a fast, accurate starting point instead of re-deriving repo state from
scratch.

**If you are starting a new session on this repo:**
1. Read the most recent entry below before doing anything else.
2. Run `git fetch origin && git log --oneline origin/main -5` to confirm you're not
   picking up stale state (another session may have pushed since the last entry here).
3. `git fetch` + `git rebase origin/main` before every push, every time — not just at
   session start. This repo has had 6+ concurrent-push collisions resolved this way with
   zero manual conflict resolution needed so far, but only because this discipline was
   followed every time.
4. Add a new entry at the top of the log when you start, and update it (or add a follow-up
   entry) when you stop, even mid-task. Note what's in flight so the next session — human
   or AI — doesn't duplicate or clobber it.

---

## Log (newest first)

### 2026-08-06 — Handoff for Phase B of the research-quality improvement plan

**Status at handoff:** All 50 states complete and published. Issue #1 ("Improve research
quality, completeness assurance, and token efficiency") is open and tracks
`planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`. Phase A of that plan is
done (commit `848ff55`): run-telemetry schema (`runs/schema.json`, `runs/README.md`) and
the finalized pilot state set (`evals/pilot_states.md`). The AEC Industry UAS Expert role
was broadened the same day (commit `8ba09b6`) to cover Apex-style multidisciplinary
AEC/environmental-consulting scope, in lieu of adding a new interpretation role.

**Next task — start here:** Phase B of the plan = Workstreams 2-4, scoped to the five
pilot states only (Washington, Oklahoma, California, Minnesota, Florida — see
`evals/pilot_states.md` for why these five and why Florida over Texas). Concretely:

- Workstream 2: one `States/XX_State/XX_UAS_Research_Manifest.yaml` per pilot state (schema
  and suggested fields are in the plan doc). Do not expand the 33-column CSV schema for
  this.
- Workstream 3: new `scripts/validate_research_semantics.py` deterministic validator, with
  the rule list from the plan doc. Add it (and `validate_phase2.py`, currently written but
  NOT wired into CI) to `.github/workflows/site-quality.yml`.
- Workstream 4: `evals/` benchmark packets for the five pilot states — expected
  role-applicability results, controlled no-impact dispositions, known-bad fixtures pulled
  from real failure modes already observed in this repo (see "Known issues" below),
  scoring rubrics.

Do **not** start Workstream 9 (national retrofit) or touch the Compliance Burden Index
(`methodologies/state-uas-compliance-burden-index.md`) — both are explicitly gated on
Phase B/D landing first per the plan's Definition of Done and the SCBI's own preflight doc
(`methodologies/preflight/scbi-v0.1-preflight.md`).

**Known issues / technical debt to fold into the eval fixtures:**
- `docs/data/v1/*.json`'s `last_updated` field is populated from the build script's run
  time, not actual research currency — confirmed reproducible: re-running
  `python3 build_data.py` with zero content changes still rewrites `last_updated` on 20+
  states. This is exactly what Workstream 8 exists to fix; don't commit the resulting
  diffs as if they were real updates (`git checkout -- docs/data/v1/` after any build-only
  rerun).
- `States/` directory naming is inconsistent between sessions: no-underscore style
  (`NC_NorthCarolina`, `NY_NewYork`, `WV_WestVirginia`) vs. underscored style
  (`ND_North_Dakota`, `NH_New_Hampshire`, `RI_Rhode_Island`, `SC_South_Carolina`,
  `SD_South_Dakota`). Harmless today; worth a lint rule before something depends on it.
- Minnesota MN-004's citation (MnDOT's own page cites Minn. Stat. § 360.075 for its
  Commercial Operations License, but that section is actually a criminal-penalties
  provision) is a good known-bad fixture for citation-drift detection — see
  `States/MN_Minnesota/MN_UAS_Regulatory_Summary.md`, "Citation note."

**Access/environment notes for a fresh session:**
- Git operations only work from a local clone (e.g. `/tmp/...` in a sandboxed shell), never
  from a mounted/synced filesystem — lock-file semantics break otherwise.
- The git remote URL has a PAT embedded. Never print it unredacted; pipe any git output
  shown to the user through a `ghp_[A-Za-z0-9]*` → `[REDACTED]` substitution.
- `gh` CLI is not available in a typical sandbox for this repo, and `api.github.com` is
  commonly blocked by sandbox network egress rules — this affects issue/PR creation via
  API, not `git push`/`fetch`, which use the PAT fine over the git protocol. Don't assume
  API access without checking; fall back to committing planning docs + a pre-filled
  `github.com/.../issues/new?title=...&body=...&labels=...` URL for the user to submit
  themselves if API access isn't available.
- The governing spec is `Agent_Instructions.v6.md` (Amendments 1-5 currently applied).
  Read it before making any schema or role change.

---
