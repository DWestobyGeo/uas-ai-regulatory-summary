# Methodology Directory

This directory contains versioned measurement specifications. A methodology defines what is measured, how it is calculated, when a result is publishable, and how revisions affect prior results. Agent expertise and operating behavior belong separately in [`agents/roles/`](../agents/roles/).

## Active methodologies

| Methodology | Owner role | Status | Current version |
|---|---|---|---:|
| [State-Level UAS Compliance Burden Index](state-uas-compliance-burden-index.md) | [State UAS Regulatory Burden Analyst](../agents/roles/state-uas-regulatory-burden-analyst.md) | Active; national scoring still subject to evidence-readiness gates | 1.0.0 |

## Change rules

- Methodology rules control the measurement; the role document controls how the agent performs the work.
- A provisional method may be tested and revised only through a documented preflight.
- Freeze one method version before a comparison run.
- Never alter the method silently in response to an unexpected state result.
- A score-affecting methodology change requires a version increment, impact assessment, and consistent rescoring before a new comparison is published.
- Preserve prior versions and preflight reports through Git history and revision notes.

Run `python scripts/validate_methodologies.py` after editing a methodology, its owner role, governance, or preflight documentation.
