# Agent Role Directory

This directory is the authoritative home for individual agent operating instructions. [`../../Agent_Instructions.v6.md`](../../Agent_Instructions.v6.md) provides repository-wide governance; it does not replace the specialized role files listed below.

## Active roles

| Role | Primary responsibility | Governs |
|---|---|---|
| [Research Expert](research-expert.md) | Source discovery, verification, objective analysis, and source-register metadata | Objective fields, research checklist, objective summary, Non-Regulatory Context |
| [AEC Industry UAS Expert](aec-industry-uas-expert.md) | Commercial AEC flight-program and field interpretation | `practical_interpretation_aec_expert` |
| [Agency Practitioner](agency-practitioner.md) | Agency application, permit, registration, and approval-process interpretation | `practical_interpretation_agency_practitioner` |
| [UAS Procurement Expert](uas-procurement-expert.md) | Aircraft, payload, software, cybersecurity, sourcing, and fleet interpretation | `practical_interpretation_uas_procurement_expert` |
| [AEC Industry Legal Counsel](aec-industry-legal-counsel.md) | Legal-risk, contract, documentation, liability, and escalation interpretation | `practical_interpretation_legal_counsel` |
| [Editorial and QA Reviewer](editorial-qa-reviewer.md) | Independent consistency, fact-drift, schema, and publication-artifact QA | Review only; corrections must be attributed to the owning role |
| [Web UX/UI and Editorial Agent](web-ux-ui-editor.md) | Static-site presentation, navigation, accessibility, links, and print behavior | `docs/` presentation layer and UI provenance |

## Required role-document template

Every role document uses the same YAML metadata keys so ownership and change authority can be read by a person or parsed by tooling:

```yaml
---
role_id: stable-kebab-case-id
name: Human-readable role name
version: semantic role-instruction version
status: active | draft | retired
last_updated: YYYY-MM-DD
governance: ../../Agent_Instructions.v6.md
role_type: research | interpretation | quality | presentation
phases:
  - phase name
governs_sections:
  - named document or workflow section
governs_fields:
  - source-register field name, or none
may_edit:
  - authorized file or content class
must_not_edit:
  - prohibited file or content class
record_change_authority: concise statement of record authority
record_change_documentation:
  - required evidence or revision notation
required_handoff:
  - required completion information
---
```

The body normally uses these sections, but a complex role may add or reorganize sections when that makes the operating instructions easier to use:

1. Role and mission
2. Background and expertise
3. Required inputs
4. Operating instructions
5. Record-change protocol
6. Boundaries and escalation
7. Quality checklist
8. Required handoff

Every active role must still include a clear role/mission section and required handoff, while the common YAML metadata remains mandatory and structurally identical.

## Versioning a role

- Increment the role document's `version` when its operating instructions or authority changes.
- Update `last_updated` in the same change.
- Do not rewrite past state provenance to claim a newer role version was used. New or revised state work records the role version actually used.
- If a role is replaced, mark it `retired` and link to the successor rather than deleting the historical instructions.
- Changes to repository-wide scope, source standards, schema, phase gates, or product boundaries belong in the governance document, not in only one role file.
