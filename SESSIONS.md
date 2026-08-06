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

### 2026-08-06 — Phase B (Workstreams 2-4, pilot states) complete; awaiting push authorization

**Status:** Completed the Phase B work described in the entry directly below, on a fresh clone
(the mounted States folder some sessions see is a stale leftover, not this repo). Committed
locally; **not yet pushed** — waiting on the user to paste a GitHub PAT before pushing, per this
session's explicit instruction. If you are picking this up because that push never happened,
check `git log` for a commit around this message before redoing any of this work.

**What landed:**

- **Workstream 2:** `States/RESEARCH_MANIFEST_SCHEMA.md` (controlled values for `research_status`,
  `legacy_retrofit_status`, and eleven coverage-category statuses) and one
  `XX_UAS_Research_Manifest.yaml` per pilot state (WA, OK, CA, MN, FL). Content is grounded in
  what's actually in each state's register/summary today, not aspirational: OK is
  `current_method_complete`; MN is `current_method_in_progress` (one never-swept category —
  professional-licensing-board material — blocks it from `_complete` under this schema's own
  rule); WA, CA, and FL are `legacy_needs_retrofit` (each has 3-4 genuinely unresolved coverage
  categories, consistent with their "legacy state packet" provenance line). Did **not** touch the
  33-field CSV schema.
- **Workstream 3:** `scripts/validate_research_manifests.py` (manifest schema/controlled-value
  gate, cross-checked against each register) and `scripts/validate_research_semantics.py`
  (9 per-record deterministic rules + a duplicate-interpretation similarity check + a
  cross-artifact manifest/register/generated-JSON agreement check + a CI-completeness check).
  Both, plus the already-written-but-unwired `validate_phase2.py`, are now wired into
  `.github/workflows/site-quality.yml` (also added a `pip install pyyaml` step — the new
  manifest validator needs it and the stock runner doesn't have it preinstalled).
  **Severity policy** (see the module docstring): a finding in a pilot state is an ERROR unless
  the exact record_id is already referenced in that state's manifest (acknowledged legacy debt,
  since Workstream 9 retrofit is explicitly out of scope this pass); a finding in a non-pilot
  state (no manifest yet) is always a WARNING, so this doesn't turn CI red across the other 45
  states before they've been assessed. All validators plus `python3 build_data.py` currently
  pass clean (0 errors) on this branch.
- **Workstream 4:** `evals/` now has `pilot_states/{ABBR}_role_applicability.yaml` (deterministic,
  regenerable from the live register — not hand-maintained trivia), `fixtures/known_bad/` (11
  cases) and `fixtures/known_good/` (5 cases) — most are pulled from real pilot-state records
  (WA-008/CA-013 negative-findings-in-register, WA-007/CA-010/CA-011/FL-008 general-licensing
  scope-gate risk, WA-004 uncertain/low-confidence, MN-004 citation-discrepancy-vs-confidence,
  MN-001 and WA-004 as *correct*-handling contrast cases); a few (legislature-as-application-office,
  boilerplate-process-language) are marked `synthetic` in the fixture file because no current
  pilot-state record actually violates that specific rule yet. `evals/run_fixture_checks.py` runs
  both fixture and role-applicability checks (57/57 passing) and is now in CI too.
  `evals/expected/controlled_no_impact_dispositions.md` and `evals/rubrics/layer_{b,c}_*.md`
  round out the rest of the Workstream 4 deliverable list. Fixture count (11 known-bad) is short
  of the plan's "at least twenty" figure, but that figure explicitly gates Workstream 9
  (nationwide retrofit), which this pass does not start — noted as a running total in
  `evals/README.md`, not silently ignored.
- **Governance housekeeping (repo-wide, so it's one commit spanning states per §8.4):** bumped
  `Agent_Instructions.v6.md` to 6.3.0 with a revision-history entry, added the manifest to §5.1
  and a manifest-agreement bullet to §12; bumped `research-expert.md` to 1.1.0 as the manifest's
  owner (added it to `may_edit`/`governs_sections`, a §4.4 cross-reference, and a quality-checklist
  bullet); updated `README.md`'s repository-structure listing to mention the new scripts/dirs.

**Deliberately not done (in scope for a later phase, not this one):** Workstream 9 (national
retrofit) — untouched, per this session's instruction. Workstream 5/6 (routing, compact evidence
packets) — Phase C, not started. Website display of research status
(`docs/data/v1/index.json` / `docs/app.js`) — the plan's Workstream 2 task list mentions this, but
it requires a web-role UI-version bump (`docs/DESIGN_SYSTEM.md`, `docs/ui-release.json`) that
this session's instruction (Workstreams 2-4 only) didn't ask for; flagging it as a clean follow-up
rather than doing it silently. `runs/` telemetry is still schema-only (Workstream 0, unchanged).

**New real findings surfaced by this pass** (beyond the three already listed below) that a
future retrofit/QA session should know about, all now tracked in the relevant state's manifest
`known_issues` and referenced from an eval fixture:
- WA-008 and CA-013 store a negative ("no source found") finding as a register record instead of
  in the checklist/manifest — the same defect in two different legacy states, so it's systemic,
  not a one-off. `validate_phase2.py` already half-detects this as a "legacy non-authority row"
  warning across ~35 states; `validate_research_semantics.py`'s `check_negative_finding_in_register`
  makes it an explicit, named rule.
- WA-007, CA-010, CA-011, and FL-008 are general professional-licensing statutes retained without
  a confirmed direct-UAS provision or an official source expressly applying them to UAS — a
  scope-gate risk under Agent_Instructions.v6.md §3.2, reproduced across three of the five pilot
  states.
- MN-005 and MN-008's `practical_interpretation_aec_expert` text is ~72% identical (same sentence
  template, only the property name swapped) — a real, mild instance of the templated-boilerplate
  pattern Workstream 3 asks the duplicate-interpretation rule to catch. The same rule found many
  more (mostly 80-100% similarity) non-pilot-state pairs when run repo-wide as a warning; worth a
  look before Workstream 9 starts in earnest.

**Next task:** Push once the user supplies a PAT (see "Access/environment notes" below — nothing
else should block this). After that, Phase C (Workstreams 5-6: route interpretation roles by
material relevance, compact evidence packets) is the next planned phase per the plan's own
`Proposed implementation phases` section, but confirm with the user before starting new
substantive work rather than assuming Phase C is authorized.

---

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
