# North Carolina UAS Research Checklist

- **State:** North Carolina (NC)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. Local ordinances and tribal rules are outside this pass (see Section 4 of the narrative for the general state/local boundary discussion).

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found | G.S. 15A-300.1 (privacy/surveillance, NC-001) and G.S. 15A-300.4 (forest fire, NC-004) re-fetched directly against ncleg.gov and confirmed to match the register exactly, including NC-001's emergency-management exception (c1) and NC-004's felony-tier penalty structure. |
| 2 | Administrative rules and regulations | Applicable source found | 07 NCAC 13B .1204 (state park UAS prohibition, NC-010) — confidence unchanged from prior High rating; not independently re-fetched in this pass given no flag or currency concern was identified. |
| 3 | Executive orders | Not separately tracked | No standalone executive-order register record exists for NC; not re-searched as a distinct category in this pass (no prior finding to re-verify). |
| 4 | Court decisions and attorney-general materials | Applicable source found; MAJOR finding | **NC-012 materially expanded.** *360 Virtual Drone Services LLC v. Ritter*, 102 F.4th 263 (4th Cir. 2024), cert. denied Apr. 20, 2026 — a binding federal appellate decision upholding NCBELS's authority to require a PE/PLS license for drone-derived orthomosaic maps, 3D models, and metadata-tagged aerial photography. This is a real, currently enforced risk (NCBELS has issued cease-and-desist letters to at least a half-dozen drone companies since 2018), not merely an absence of guidance as the prior version of this record stated. Verified directly via the Institute for Justice's case page (counsel of record) and Justia's reproduction of the published opinion. |
| 5 | Aviation and transportation agencies | Applicable source found | NCDOT Division of Aviation's official laws-and-regulations crosswalk page re-confirmed directly against ncdot.gov, corroborating the citation numbering for NC-002, NC-003, NC-005, NC-006, NC-007, NC-008. |
| 6 | Parks, public lands, forestry, fish, wildlife, and natural resources | Applicable source found | NC-004 (forest fire) re-confirmed directly; NC-010 (state parks) and NC-008 (wildlife harassment) unchanged from prior High-confidence findings. |
| 7 | Corrections, public safety, emergency management, and critical infrastructure | Applicable source found | NC-003 (confinement/correctional-facility UAS prohibition) unchanged; see also the news-aggregator pass below for a directly on-point, currently active enforcement gap (drone-borne prison contraband). |
| 8 | Privacy, surveillance, harassment, trespass, and interference | Applicable source found | See row 1 (NC-001). |
| 9 | Procurement, equipment, cybersecurity, and manufacturer restrictions | Not separately tracked | No register record exists for this category; not identified as a gap requiring a new record in this pass. |
| 10 | Professional licensing-board materials | Applicable source found; MAJOR finding — see row 4 | NC-012 was substantially rewritten. The prior framing ("no standalone Board guidance was located") significantly understated the real, currently binding risk documented by the *360 Virtual Drone Services v. Ritter* litigation. Confidence upgraded Low -> High. |
| 11 | State preemption / state-local boundary | Applicable source found; one record relocated | The narrow-local-authority research finding (previously register record NC-011) was moved to this checklist row. **NC-011 removed from the register** per `Agent_Instructions.v6.md` §5.2 (its own `source_type` field said "not included in the final source register," a self-contradiction as a register row) and the negative-finding-in-register governance principle already applied elsewhere in this project. The underlying research finding remains intact in the narrative's Section 4 ("State/Local Regulatory Boundary"), which is general contextual discussion, not a register record. |

## Open verification items

1. Confirm NCBELS's exact current published enforcement/guidance position (21 NCAC 56) for specific deliverable characteristics — the *Ritter* litigation record describes the Board's asserted scope, but the Board's own current rule text was not independently re-verified section-by-section in this pass.
2. § 15A-300.3(b)(3)(d)'s commercial correctional-facility exception references "Chapter 63, Article 10," which was substantially repealed effective Dec. 1, 2024 (NC-009) — confirm with NCDOT's Division of Aviation how this cross-reference now operates.
3. Jockey's Ridge State Park's historically separate operator-permit arrangement was not independently verified in this or the prior pass.
4. No statewide inventory of municipal park-specific UAS ordinances (e.g., Raleigh's, Wake Forest's) was compiled; confirm directly with the relevant local government for a site-specific engagement.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/research-expert.md` Section 4.7, as the closing step of this
retrofit. Searched: NC-003 (correctional-facility drone incidents), NC-001 (privacy/surveillance
lawsuits), NC-010 (state park enforcement), NC-012 (licensing-board enforcement).

One genuine match found: WECT News's Aug. 3, 2026 report on rising drone-borne contraband
deliveries into North Carolina prisons, including a June 2026 Columbus County arrest tied to a
drone drug-delivery plot, directly on point for NC-003. Added to `NC_UAS_News.yaml` and anchored
inline under NC-003.

Other candidates considered and rejected: additional syndicated re-runs of the same Columbus
County/NCDAC story across several radio-station websites (same underlying event as the WECT
item — not a second genuine story); the UNC School of Government Criminal Law Blog's November
2025 "update on law enforcement use of drones" (legal-analysis commentary, not primary event
reporting, so not "news" under the role's Section 4.3 standard); the *360 Virtual Drone Services
v. Ritter* litigation and its April 2026 cert-denial coverage (this is the underlying legal
authority itself, already folded directly into NC-012's objective content per the role's Section
5 — not layered on top as a separate news item, to avoid redundancy).
