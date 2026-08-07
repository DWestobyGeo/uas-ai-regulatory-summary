# Indiana UAS Research Checklist

- **State:** Indiana (IN)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources.
- **Scope:** Statewide and state-agency UAS authorities only. Local ordinances are outside this pass (Fort Wayne and Carmel each maintain their own drone ordinances, consistent with the absence of a statewide preemption statute).

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found; interpretation errors corrected | IN-001 through IN-006, IN-008 re-confirmed/re-verified. IN-002 and IN-003's `practical_interpretation_aec_expert` fields previously contained mismatched wildlife-harassment content (apparently copy-pasted from a different topic) and have been rewritten to address the actual conduct each statute targets. IN-004's field similarly said "Build Indiana General Assembly approval into pre-mobilization planning" — corrected to reference the facility head's authorization, the statute's actual mechanism. |
| 2 | Administrative rules and regulations | Applicable source found; MAJOR finding | IN-007 (312 IAC 8-2-8(i), DNR property landing/launch prohibition) — the citation/discrepancy flag left open in the original pass is now resolved: DNR's own official State Form 56490 guidance (fetched directly) confirms four specific drone exception categories (professional journalists, university researchers, documentary filmmakers, tourism agencies), each requiring advance permit review — more precise and complete than the three-category description on secondary aggregator sites. Confidence Moderate → High. |
| 3 | Executive orders | Applicable source found; repurposed | IN-010 (Executive Order 25-73, Indiana Initiative for Drone Dominance Task Force) — retained as an affirmative record. A search for the task force's July 31, 2026 statutory-deadline strategic plan did not locate a published version as of this retrofit's research date (one week after the deadline). |
| 4 | Court decisions and attorney-general materials | Reviewed — no applicable source located | No Indiana Attorney General opinion or appellate/Supreme Court decision directly construing an Indiana UAS-specific statute was located. Previously combined into IN-010's negative-finding portion; not independently re-searched in this retrofit pass beyond the original finding. |
| 5 | Aviation and transportation agencies | Not separately tracked | INDOT's Division of Aeronautics/Land and Aerial Survey Office maintains an active internal UAS program (public webtool, FAQ page) but its public-facing material imposes no located operator-facing permit or manufacturer restriction; not identified as a gap requiring a standalone record. |
| 6 | Parks, public lands, and natural resources | Applicable source found — see rows 1 and 2 | IN-006 (hunting) and IN-007 (DNR property). |
| 7 | Corrections, public safety, and critical infrastructure | Applicable source found; operative-status update | IN-004 (contraband trafficking), IN-005 (public-safety interference), and IN-008 (counter-UAS authority). IN-008's federal-law trigger condition (a qualifying federal law authorizing SLTT counter-UAS activity) has been satisfied since the original pass — DOJ/DHS published the SAFER SKIES Act interim final rule in the Federal Register July 6, 2026, effective July 1, 2026. Direct confirmation of the Governor's required Indiana Register notice publication (the state-law trigger's second half) was not located in this pass. |
| 8 | Privacy, surveillance, trespass, and interference | Applicable source found — see row 1 | IN-001, IN-002, IN-003. |
| 9 | Procurement, equipment, and cybersecurity | Applicable source found | IN-008's requirement that counter-UAS systems appear on the federal C-UAS Technology List is Indiana's state-agency UAS procurement restriction in this category; unchanged from the original pass. |
| 10 | Professional licensing-board materials | Applicable source found; MAJOR finding | **IN-009 substantially expanded.** The original pass cited only the general "practice of surveying" framework via a secondary aggregator (LawServer), without reading subsections (d) or (e). This retrofit pass fetched and read the full current text directly against Justia, locating subsection (e)'s previously unflagged requirement that photogrammetric/remote-sensing survey work be performed "only under the direct control and supervision of a professional surveyor or professional photogrammetrist" holding a current "Certified Photogrammetrist" title — a specific, previously understated requirement directly applicable to UAS-derived photogrammetric products. Confidence Low → High. |
| 11 | State preemption / state-local boundary | Reviewed — no applicable UAS-specific source located; relocated | The negative-finding categories previously combined into IN-010 (no AG opinion, no court decision, no general state-agency procurement restriction beyond IN-008, no local-ordinance preemption statute) were moved to this checklist per `Agent_Instructions.v6.md` §5.2, since the prior combined record's own `source_type` field said "not included in the final source register." No statewide preemption statute was located; Fort Wayne and Carmel each maintain their own drone ordinances, reconfirmed as inconsistent with a preemption regime being in force. |

## Open verification items

1. IC 35-45-10-6's July 1, 2026 livestock/crops/farm-operations amendment (H.E.A. 1249/P.L.158-2026) still does not appear in Justia's or FindLaw's Indiana Code mirrors as of August 7, 2026 — more than five weeks post-effective-date, across two independent research passes. Confirm the current codified text directly with the Indiana General Assembly (iga.in.gov) before relying on it for agricultural or rural-corridor flight planning.
2. IC 10-22's gubernatorial Indiana Register notice publication (the second half of the counter-UAS operative trigger) was not independently located in this pass, even though the federal-law half of the trigger has been satisfied. Confirm current operational status directly with the Indiana State Police.
3. Indiana's general critical-infrastructure-facility trespass statute (IC 35-46-10-2) does not on its face reference UAS or airspace; its application to drone overflight versus physical entry is unresolved and was excluded from the register on that basis.
4. Whether a specific UAS-derived deliverable satisfies IC 25-21.5-1-7(e)'s certified-photogrammetrist/professional-surveyor supervision requirement is fact-specific and was not resolved for any particular deliverable type against current Board guidance.
5. The Indiana Initiative for Drone Dominance Task Force's strategic plan (statutory deadline July 31, 2026) had not been located as a published document as of this retrofit's research date (August 7, 2026); check for publication in a future pass.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/news-aggregator.md`, as the closing step of this retrofit. This state's prior research
packet already included an inline "Non-Regulatory Context" news list from its original pass; this retrofit
standardized that list onto the project's now-established `*_UAS_News.yaml` + inline-anchor workflow rather than
re-running the search from scratch, since the original items were themselves genuine, dated, primary-source news
(not aggregator content) and remain current.

One item retained as a standalone news entry: the Indiana Capital Chronicle's April 27, 2026 feature "Rural
Hoosiers lean on the law to fight drones," anchored to IN-003. It contains specific incidents and testimony
(the Adams County drone-swarm/poultry-farm episode, a Shelbyville resident's account) that materially enrich
IN-003's objective content beyond a bare description of the legal change.

Two items previously listed separately were folded directly into their respective records' own objective content
instead of being retained as separate news items, consistent with this project's redundancy-avoidance rule:
- The WBIW "Indiana DNR files first prosecution in illegal drone scouting case" item and the sentencing details
  in the Capital Chronicle feature — both describe the same Pettit-case prosecution already referenced in IN-006's
  objective content ("current enforcement corroborated by Indiana DNR's first prosecution under this statute").
- The Indiana Capital Chronicle's October 31, 2025 "New Indiana task force" brief — describes the same EO 25-73
  announcement already fully covered in the rewritten IN-010's own objective content.

The WFIU "Indiana law targets unauthorized drones amid farm safety concerns" item (March 12, 2026) was reviewed
and judged substantially redundant with the more detailed Capital Chronicle feature already retained; not
separately added to avoid duplicating the same underlying story.
