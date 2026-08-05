# Maintainer Notes on the Research Quality & Efficiency Improvement Plan

**Added:** 2026-08-05
**Status:** Accepted; implementation underway (Phase A in progress)
**Companion file:** `AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md` (this directory)

This note records maintainer decisions needed to start implementing the plan, since the
plan itself intentionally leaves several choices open.

## Decisions

1. **Fifth pilot state (Workstream 1).** Selected **Florida**, not Texas. Florida is
   already a completed (legacy, pre-Amendment-2) state, so including it in the pilot set
   does double duty: it exercises the plan's legacy-retrofit path (alongside Washington)
   *and* its own distinctive regulatory pattern — a statewide local-preemption statute
   (Fla. Stat. § 330.41) plus public-agency UAS procurement/data-use restrictions distinct
   from the private commercial-operator baseline. Texas has an equally strong preemption
   and government/critical-infrastructure UAS statute but no incremental legacy-retrofit
   value, since it would need to be researched fresh either way. If a second procurement-
   heavy state is wanted later, Texas is the natural next candidate — see Workstream 9
   Tier 2 queue.

2. **Issue filing.** This session could not authenticate to GitHub (no working `gh` CLI in
   the sandbox, direct REST API calls to `api.github.com` are blocked by sandbox network
   egress rules, and the connected browser session is unauthenticated). Rather than block
   on that, the plan is committed here as a tracked repository document — which is durable
   and diffable — and a pre-filled "create issue" link is provided in the PR/commit
   description and the chat response for a maintainer to submit with one click.

3. **Scope of this initial commit (Phase A).** This commit implements the acceptance
   criteria of Workstream 0 (telemetry schema + convention, not yet wired into every
   historical run) and Workstream 1 (pilot state set finalized and documented). It does
   **not** yet implement Workstreams 2-9; those remain queued per the plan's phased
   rollout (Phase B onward) and are tracked as follow-up work under the same issue.

## Cross-reference to existing repo state

- The State UAS Regulatory Burden Analyst / Compliance Burden Index work
  (`methodologies/state-uas-compliance-burden-index.md`, preflighted in
  `methodologies/preflight/scbi-v0.1-preflight.md`) is exactly the kind of publication
  this plan's Definition of Done gates on a common evidence standard (see plan
  Non-goals and Definition of Done, last bullet). That preflight already reaches the same
  conclusion independently ("blocked pending evidence-gate and common-cutoff
  verification"); this plan gives that conclusion a concrete, machine-checkable path
  (Workstreams 2-3 manifests/validators) rather than leaving it as a documented caveat.
- The AEC Industry UAS Expert role was broadened this same day (see the preceding commit)
  to cover the multidisciplinary AEC/environmental-consulting scope reflected in Apex
  Companies' actual service lines, rather than adding a fifth interpretation role/schema
  field — consistent with this plan's Workstream 5 principle of routing interpretation by
  material relevance rather than expanding role count.
