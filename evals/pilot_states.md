# Gold-Standard Pilot State Set

Per Workstream 1 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`.
This is the finalized pilot set used to build the initial benchmark packets, expected
role-applicability results, and known-bad fixtures for Workstreams 2-4.

| State | Directory | Purpose |
|---|---|---|
| Washington | `States/WA_Washington` | Legacy retrofit target: obsolete/failed-authority detection, scope-gate cleanup, pre-Amendment-2 schema |
| Oklahoma | `States/OK_Oklahoma` | Current-method sparse state; tests permission/consent/agency-process distinctions and boilerplate risk |
| California | `States/CA_California` | High-complexity state: dense statutes, multiple agencies, permits, and active pending legislation |
| Minnesota | `States/MN_Minnesota` | State registration/licensing regime, mixed public/private rules, citation ambiguity (see MN-004 citation note) |
| Florida | `States/FL_Florida` | Procurement/preemption pattern; statewide local-preemption statute + public-agency procurement/data-use restrictions; also a legacy state, giving it double duty as a second retrofit case alongside Washington |

## Selection rationale for the fifth state

The plan proposed "Florida or Texas" for the procurement/preemption slot. Florida was
selected because it is already a completed legacy state, so adding it to the pilot set
exercises both the legacy-retrofit path and the procurement/preemption pattern in one
state, rather than requiring a sixth state to cover retrofit work twice. Texas remains a
strong candidate for the Workstream 9 Tier 2 (high-complexity) retrofit queue given its
own preemption and critical-infrastructure UAS statute.

## Status

Pilot set finalized 2026-08-05. Benchmark packet construction (expected
role-applicability results, controlled no-impact dispositions, known-bad examples,
scoring rubrics — remaining Workstream 1 tasks) is follow-up work under the same
improvement-plan issue; it has not started as of this commit.
