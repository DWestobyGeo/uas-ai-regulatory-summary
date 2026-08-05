# Run Telemetry

This directory holds machine-readable telemetry records for research, interpretation, and
QA agent runs, per Workstream 0 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`.

## Convention

Each substantive agent run (a research pass, a Phase 2 interpretation batch, a QA/retrofit
pass) should write one JSON file to this directory named `{run_id}.json`, where `run_id` is
a sortable identifier: `{utc_timestamp}_{state_abbr}_{phase}_{role_or_stage}`, e.g.
`20260805T142230Z_FL_phase1_research.json`.

This directory is additive and append-only — do not edit or delete a past run's record.
Rebuilding derived reports (cost/quality summaries by state, phase, role) should read all
files here rather than mutate them.

## Schema

See `schema.json` in this directory for the authoritative field list. Summary:

- **Identity:** `run_id`, `state`, `state_abbr`, `phase` (`phase1_research` | `phase2_interpretation` | `phase3_qa` | `retrofit`), `role` (nullable — research/QA runs may not be role-scoped), `record_ids` (array, nullable).
- **Model/version provenance:** `model_provider`, `model_id`, `agent_instructions_version`, `role_version` (nullable), `prompt_template_version`.
- **Token/cost accounting:** `input_tokens`, `cached_input_tokens`, `output_tokens`, `reasoning_tokens` (nullable, provider-dependent), `cost_usd` (nullable, if computable), `retries`, `latency_ms`, `tool_calls`, `sources_opened`.
- **Change tracking:** `objective_packet_hash` (hash of the input evidence packet for interpretation runs), `interpretation_input_hash`.
- **Timestamps:** `started_at`, `completed_at` (ISO 8601 UTC).

## Status

This is the Workstream 0 schema/convention definition (Phase A of the improvement plan).
Historical runs prior to 2026-08-05 predate this convention and have no telemetry records;
they are not backfilled. Wiring this into the live agent workflow (so every future run
actually emits a record here) is follow-up work tracked under the same improvement-plan
issue.
