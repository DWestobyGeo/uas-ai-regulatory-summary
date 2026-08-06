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

### 2026-08-06 — Agency Practitioner role prompt improved (1.0.0 -> 1.1.0)

**Status:** Complete and pushed (`234f11d`). User-requested, outside the Workstream 7/8 task
list, done before Workstream 9 per explicit instruction ("go ahead with 36 first, then 9").

**What landed:** `agents/roles/agency-practitioner.md` gets a new Section 4a ("Sourcing real
process detail"). The role previously defaulted to generic "confirm requirements with the
agency" language whenever the base evidence packet didn't spell out a process's mechanics. Now,
before falling back to that: (1) prefer agency-published operational guidance beyond the bare
statute/rule citation, attributed explicitly as official with a named URL; (2) if none exists,
first-hand practitioner accounts from an appropriate venue (a UAS/industry/agency-specific
subreddit, forum, professional group, podcast, video, trade/local news) are acceptable,
attributed explicitly and kept visually distinct from official guidance -- never blended into
one unattributed sentence; (3) if neither is found, say so briefly rather than silently defaulting
to generic advice as if it were a complete answer -- but the role is never forced to fabricate a
source or account to avoid saying so. None of this lets community-sourced detail override an
objective field or convert a governed `N/A` disposition into a process where none exists in law.
`agents/prompt_templates/agency-practitioner.task.md` carries the same instructions into the
assembled prompt. **No already-published `practical_interpretation_agency_practitioner` text was
rewritten** -- this is a prompt-design change only, same boundary applied to every other
retroactive-interpretation-change question in this project. No governance-document version bump
(role-scoped, Agent_Instructions.v6.md §9 already delegates full operating rules to role docs).

**Next task:** Workstream 9 (national retrofit), authorized by the user immediately after this.
See the plan doc's own Tier 1/2/3 risk-based sequencing (`planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`,
"Workstream 9") before starting -- this is the largest-scope work authorized so far in this
project (45 non-pilot states vs. 5 pilot states for everything up to this point) and needs its
own scoping/plan before touching any state, consistent with how every other phase in this
project started with an explicit scoping step.

---

### 2026-08-06 — Phase D, Workstream 8 (currency metadata) complete; Phase D closed out

**Status:** Complete and pushed as `b35d3dc`. Same fresh-clone/PAT caveats as prior entries apply.
This closes out Phase D (Workstreams 7-8) in full -- everything the "Please continue with phase
d" authorization covered is now landed and pushed.

**What landed:**

- **`build_data.py` no longer uses filesystem mtime for `last_updated`.** A fresh checkout resets
  every file's mtime regardless of whether content changed, so every rebuild was touching every
  state's `last_updated` -- confirmed reproducible since Phase B, previously worked around by
  discarding the resulting diff (`git checkout -- docs/data/v1/`) after every sanity-check build.
  Now prefers a pilot state's manifest `last_currency_check` (an explicit, verified date), then
  the date of the most recent git commit that actually changed the source register CSV (stable
  across checkouts), and only falls back to mtime if this isn't a git checkout at all. Verified:
  two consecutive `build_data.py` runs with zero content changes now produce zero diff.
- **`scripts/compute_currency_review.py` (new).** Classifies every pilot-state register record
  into a review-cadence bucket (event-triggered/pending, low-confidence, negative finding,
  procurement, registration/licensing/permit, stable statute) per the plan's Workstream 8
  cadence table, using fields the register already has -- no CSV schema expansion, per the
  manifest schema's own non-goals. Computes a state-level `next_currency_review` (soonest due
  date) and `recheck_triggers` (records needing an event-triggered recheck rather than a purely
  calendar one). Run `--write` for all five pilot states; found real, correct triggers: OK-001's
  not-yet-effective penalty amendment, WA-004's uncertain codification, WA-010's stalled bill,
  CA-012's pending bill, CA-014's died-in-committee bill.
- **`validate_research_manifests.py`** now requires both fields: `next_currency_review` must be
  on/after `last_currency_check` (error if not) and warns (non-blocking) if it's already in the
  past; `recheck_triggers` entries are validated against the register.
- **`scripts/check_source_urls.py` (new).** Checks register `source_url` reachability, with an
  explicit module-docstring disclaimer that reachability is not proof of legal currency and
  unreachability is not proof of change -- a narrow, low-cost "worth a human glance" signal only.
  **Not wired into the required `site-quality.yml` gate** -- a flaky or allowlist-blocked
  external government site must never fail a PR. Could not be exercised against real government
  URLs from this sandbox (confirmed 403/blocked-by-allowlist against oklegislature.gov); instead
  verified against a local mock server (`evals/fixtures/url_health/mock_server.py`) covering all
  four response cases the checker needs to classify correctly (200, 404, HEAD-unsupported-falls-
  back-to-GET, connection-refused), wrapped in `evals/run_url_health_fixture_check.py` --
  localhost-only, so this fixture check IS wired into the required CI gate (it needs no real
  internet access, unlike the checker it's testing).
  `.github/workflows/url-health-check.yml` runs the real checker weekly plus on manual dispatch,
  uploads a JSON artifact, `continue-on-error`, never blocks a merge.

**Also landed this session, outside the original Workstream 7/8 task list (both user-reported
mid-session):**
- The "Generated content notice" banner (Workstream 7's authored/generated split) was a visible
  Markdown blockquote on the live site, addressed to a general reader but referencing internal
  script/file names -- changed to an HTML comment (invisible on the live site via marked.js,
  still visible in the raw `.md` source).
- `check_duplicate_interpretations` now also scans `practical_interpretation_legal_counsel`
  (previously only the AEC-expert field), surfacing that Oklahoma's legal-counsel interpretation
  is an identical boilerplate template across all 3 OK records including one with no
  application/approval process at all -- documented in OK's manifest `known_issues`, not
  rewritten (out of scope for a detection change; see that entry below for detail).

**Next task:** Nothing further authorized yet. Two things are queued but explicitly deferred by
the user rather than started:
- A prompt-engineering pass on the Agency Practitioner role (`agents/roles/`,
  `agents/prompt_templates/agency-practitioner.task.md`): stop giving generic "get agency
  permission" advice: when specific agency-sourced guidance related to the law/regulation is
  found, include it and attribute it as direct-from-source with the URL. First-hand community
  sources (relevant subreddits, Facebook groups, podcasts, YouTube) are also acceptable if
  reported as such and appropriately filtered -- don't compile the actual source list now, just
  make the option available in the prompt. The role must not be forced to fabricate this
  information if no appropriate source exists; it should report that none was found. Do not
  start this without the user's go-ahead.
- Do **not** start Workstream 9 (national retrofit) or touch the Compliance Burden Index without
  explicit authorization -- both remain gated on Phase B/D landing first per the plan's own
  Definition of Done, and Phase D just landed; that doesn't imply authorization to proceed to
  Workstream 9 on its own.

**Access/environment notes, reconfirmed this session:** same as prior entries (bash-only repo
file access from this sandbox's `/tmp/...` clone; PAT redaction discipline; `git fetch` +
`git rebase origin/main` before every push, every time; sandbox network egress is an allowlist
that blocks arbitrary external domains, confirmed again this session against
oklegislature.gov -- assume any script that needs real internet access cannot be tested live
here and must be verified against a local mock instead, as done for
`scripts/check_source_urls.py`).

---

### 2026-08-06 — Phase D, Workstream 7 (register-as-publication-source) complete and pushed

**Status:** Complete and pushed in three commits (`8868b05` authored/generated split for OK/MN/CA/FL,
`2afe00c` rebuild of docs/data/v1 for those four states, `a4b7de0` drift-detection CI gate + banner
fix + legal-counsel boilerplate finding). Same fresh-clone/PAT caveats as prior entries apply.
Authorized by the user via "Please continue with phase d" after Phase C landed; user also confirmed
mid-workstream that they wanted milestone pushes to continue, and separately asked to see the effect
live on the site, which is what `2afe00c` was for.

**What landed:**

- **The authored/generated split.** `scripts/generate_summary.py` regenerates the authority
  sections of a state's printable `XX_UAS_Regulatory_Summary.md` (headings, type/status line,
  Objective Summary, and the four Practical Interpretation bullets) verbatim from
  `XX_UAS_Source_Register.csv`, so the CSV register is now the actual publication source of truth
  instead of a hand-maintained parallel copy that can silently drift from it. Each converted state
  gets a new `XX_UAS_Summary_Authored.md` holding the narrative/authored sections (header block,
  Overview, Non-Regulatory Context, Unresolved Operational Questions, Confidence Summary) plus
  `<!-- GENERATED_SECTION heading="..." records="ID1,ID2,..." heading_style="..." -->` markers.
  `--write` regenerates; `--check` diffs without writing (drift = exit 1).
- **Scope of conversion, deliberately uneven across the five pilot states:**
  - **OK:** fully converted (proof of concept first, before touching the other four). Diffing the
    generator's first output against the previously published file surfaced exactly one real
    content difference — OK-002's summary wording — confirming the register was already
    authoritative and the old Markdown had drifted.
  - **MN:** fully converted, one generated section (7 records).
  - **CA, FL:** only "Statewide UAS Laws and Regulations" converted. Each state's "State Agency UAS
    Requirements" section uses non-derivable custom heading labels (e.g. FL's
    "### Procurement — Florida Department of Management Services") with no field that reconstructs
    them, so those sections are left authored/untouched rather than forcing a scheme onto them.
  - **WA: not converted.** Its headers are inconsistent/custom throughout both sections with no
    salvageable pattern — left as legacy hand-maintained content for a future cleanup pass.
  - Regenerating MN/CA/FL surfaced substantially more register-vs-published drift than OK did
    (reworded Objective Summary/interpretation text, updated type/status formatting, one added
    record detail on a CA immunity statute). All of it traces to fields already present in the
    committed CSV register — the generator performs template substitution only and introduces no
    new interpretive content, so publishing it brings the printed files in line with data that was
    already authoritative per governance Sec 5.1, rather than rewriting interpretive judgments.
  - `docs/data/v1/{OK,MN,CA,FL}.json` were rebuilt and committed (not reverted like the routine
    mtime-only `build_data.py` diff — these four had real `summary_markdown` content changes) so
    the live printable view actually reflects the fix. The structured "compare four perspectives"
    view was already sourced live from the CSV register and unaffected by this workstream.
- **`scripts/validate_generated_summary.py` (new, wired into `site-quality.yml`).** Regenerates
  every state with an authored template and fails CI if the committed
  `XX_UAS_Regulatory_Summary.md` disagrees with the generator's output against the current
  register + template — catches both hand-edits to a generated section and CSV edits that forgot
  a regenerate. States without an authored template (WA) are skipped, not flagged.
- **Banner fix (user-reported mid-session):** the "Generated content notice" was originally a
  visible Markdown blockquote injected into the published summary — it showed up on the live site
  addressed to a general reader, referencing internal script/file names, redundant with and
  tonally inconsistent against the site's existing AI-research disclaimer banner/footer. Changed
  to an HTML comment (marked.js passes raw HTML through; browsers don't display comments), so it's
  invisible on the live site but still visible to anyone reading the raw `.md` source or editing
  the file.
- **`check_duplicate_interpretations` (in `validate_research_semantics.py`) now also scans
  `practical_interpretation_legal_counsel`**, not just the AEC-expert field. This surfaces a real
  finding: **Oklahoma's `practical_interpretation_legal_counsel` is an identical boilerplate
  template across OK-001, OK-002, and OK-003**, differing only in the substituted citation —
  including OK-002, a pure privacy/consent statute with no application/approval process at all,
  where the template still instructs retaining "the current application, all attachments, written
  approval, conditions, amendments, and closeout records" and to escalate if "the approving
  official ... is unclear." This is exactly the boilerplate-risk failure mode OK was selected to
  pilot (`evals/pilot_states.md`). **Not corrected here** — rewriting OK's already-published
  interpretive text would be retroactive interpretation authorship, out of scope for a
  tooling/detection change (same boundary established for the AEC/legal no-impact work in Phase
  C). Documented in `States/OK_Oklahoma/OK_UAS_Research_Manifest.yaml`'s `known_issues`, and
  surfaces as `ACKNOWLEDGED` (visible, non-blocking) rather than `ERROR` in validator output,
  since OK's records are already covered in its manifest. Left for a future dedicated
  legal-counsel-role research pass on OK.

**Next task — start here:** Workstream 8 (currency/URL-health), not yet started:
- Extend the research manifest schema with currency fields (next-review date, cadence, recheck
  triggers).
- Stop using filesystem mtime for `docs/data/v1/*.json`'s `last_updated` — it's populated from
  the build script's run time, not actual research currency, and gets rewritten on every
  `build_data.py` run regardless of content change (confirmed reproducible; this is why every
  build-sanity-check in this project's history ends with `git checkout -- docs/data/v1/` unless
  content genuinely changed, as it did this workstream for OK/MN/CA/FL).
- A URL-health checker script — **cannot be tested live from this sandbox**: its shell has an
  egress allowlist that returns `403`/`blocked-by-allowlist` for arbitrary government source
  domains (confirmed against `www.oklegislature.gov`). Build it to run correctly in an
  environment with real network access (e.g., a GitHub Actions job), but do **not** wire it into
  the required `site-quality.yml` gate — external-site flakiness shouldn't fail the whole build.
  Make it a separate, optional/manual script or a non-blocking scheduled workflow.
- Test, commit, push as milestone 3 of Phase D, following the same per-workstream push
  discipline used throughout Phase C/D.

Also outstanding, lower priority: consider whether `check_duplicate_interpretations`'s
manifest-acknowledgment mechanism (any record_id appearing anywhere in a pilot state's
`coverage.*.record_ids` counts as "acknowledged," regardless of finding type) is too coarse —
it means a fully-researched pilot state effectively pre-acknowledges any future finding on its
records. Not changed in this workstream since it's pre-existing, established behavior from
Workstream 3, but worth a second look before leaning on it for a genuinely new finding category.

---

### 2026-08-06 — Phase C (Workstreams 5-6) complete and pushed

**Status:** Complete and pushed in two commits (`2db3547` Workstream 5, `20aba12` Workstream 6),
both confirmed green in CI (`Site quality` #51 and #52, "Status Success"). Same fresh-clone
caveat as the entry below applies. This was authorized explicitly by the user after the Phase B
push landed, with an explicit instruction to push at logical milestones rather than holding
everything for one final push (session-continuity risk) — that's why this landed as two commits
instead of one.

**What landed:**

- **Workstream 5 (routing):** `Agent_Instructions.v6.md` → 6.4.0, authorizing two new governed
  no-material-impact values for the AEC Industry UAS Expert and AEC Industry Legal Counsel roles
  (previously only agency/procurement had one), gated on "a documented routing determination"
  (§6, §12). `scripts/route_interpretation_roles.py` is that determination: a deterministic
  router that decides `aec_relevant` / `agency_process_relevant` / `procurement_relevant` /
  `legal_analysis_relevant` from objective fields only, with a reason for every `false`. Run
  `--calibrate` to see it graded against the real governed-N/A decisions already in the five
  pilot states (the only ground truth that exists): 98% agreement on
  `agency_process_relevant`, 100% on `procurement_relevant`, one documented and expected
  disagreement (WA-004 — its own status is unverified, which a keyword rule can't detect; see the
  script's module docstring, which is worth reading before trusting its output on a new state).
  `validate_phase2.py` and a new `validate_research_semantics.py` rule
  (`check_aec_legal_no_impact_undocumented`) enforce that the two new values are only used when
  the router agrees. **Important:** none of the five pilot states' already-published
  `practical_interpretation_*` fields were rewritten — the router describes what it recommends
  going forward, not a retroactive edit. Re-judging already-published interpretive text is Phase 2
  drafting work, not a tooling change, and doing it without real record-level analysis would risk
  bad content.
- **Workstream 6 (compact packets/prompts):** `scripts/build_evidence_packet.py` builds a
  17-field evidence packet per record (vs. the 33-field row), each with an
  `objective_packet_hash`. `agents/prompt_templates/` documents stable-prefix (governance + role
  doc + task-frame) / dynamic-suffix (one packet) assembly; `scripts/assemble_prompt.py --measure`
  reports the size difference — 75-91% smaller than a naive full-row/all-roles/no-reuse baseline
  across the five pilot states, growing with record count as expected from prefix amortization.
  **Read the honesty section in
  `evals/results/20260806_workstream6_prompt_size_baseline.md` before citing that number** — it's
  a character-count structural proxy, not live-metered tokens or dollar cost, since no real API
  calls happened and `runs/` telemetry is still schema-only (Workstream 0). Also new:
  `runs/objective_packet_hashes/{WA,OK,CA,MN,FL}.json`, a skip-regeneration snapshot;
  `--check-regeneration` was verified to correctly report all 41 pilot-state records unchanged
  immediately after snapshotting, but that only proves the hash mechanism is stable — it hasn't
  yet been exercised against a real content change.

**Deliberately not done:** Phase D (Workstreams 7-8: register as the single publication source
of truth for generated Markdown; currency metadata correction) — not started, was not in scope
for this session's authorization. Workstream 9 (national retrofit) — still untouched. The
`aec_relevant` / `legal_analysis_relevant` router output has no ground truth to calibrate against
yet (unlike agency/procurement) since no real record has used the new governed values; treat its
"defaults true, false only for informational/debunked/negative-finding records" heuristic as a
reasonable starting point, not a validated one, until it's actually used and checked.

**Next task:** Ask the user before starting Phase D or anything else substantive — this session's
authorization was specifically "Phase C, proceed," not a blanket authorization for the rest of
the plan. If picking this up cold, the plan's own `Proposed implementation phases` section still
shows Phase D (Workstreams 7-8) as the next step in sequence.

---

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
