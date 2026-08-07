# Hawaii UAS Research Checklist

- **State:** Hawaii (HI)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. County ordinances are outside this pass but flagged as a materially higher-than-usual priority for Hawaii (see Section 4's scope note in the narrative).

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found; interpretation error corrected | HI-001 (§ 711-1114 trespass/harassment) re-confirmed directly against Justia; its `practical_interpretation_aec_expert` field previously contained mismatched wildlife-harassment content (apparently copy-pasted from a different topic) and has been rewritten to address the actual property-line/dwelling-proximity trespass conduct this statute targets. |
| 2 | Graduated felony framework | Applicable source found; re-corroborated | HI-002 (§§ 711-1121–1123, Act 161 misuse-of-uncrewed-aircraft tiers) re-corroborated via multiple independent secondary legal-summary sources. A direct full-text fetch was attempted again against both capitol.hawaii.gov and Justia and again returned no retrievable content — the same result as the original pass. Confidence held at Moderate. |
| 3 | Privacy statutes | Applicable source found; upgraded | HI-003 (§§ 711-1111, 711-1110.9) — § 711-1111's full current text fetched and read directly against Justia's codification in this pass, confirming the register's description including the law-enforcement-recording exception (added 2016) and the cross-reference to § 711-1110.9 for the felony tier. |
| 4 | Administrative rules and regulations | Applicable source found | HI-004 (Haw. Admin. R. § 13-146-9, state park aircraft restriction) — unchanged, already High confidence and directly verified against DLNR's own published rule compilation in the original pass; corrects a widespread secondary-source citation error (§ 13-146-35). Not independently re-fetched in this pass given no flag or currency concern was identified. |
| 5 | Executive orders | Reviewed — no applicable source located | No Hawaii gubernatorial executive order specifically and solely addressing UAS regulation was located. Not independently re-searched in this retrofit pass beyond the original finding. |
| 6 | Court decisions and attorney-general materials | Reviewed — no applicable source located | No Hawaii Attorney General opinion or appellate court decision directly construing a Hawaii UAS statute was located. Not independently re-searched in this retrofit pass beyond the original finding. |
| 7 | Aviation and transportation agencies | Not separately tracked | No standalone state DOT/aviation-agency UAS record exists for HI; not identified as a gap in this pass. |
| 8 | Parks, public lands, and natural resources | Applicable source found — see rows 4 and 9 | HI-004 (state parks) and the rewritten HI-007 (DOCARE conservation-enforcement UAS program). |
| 9 | State-agency UAS programs and procurement | Applicable source found; MAJOR finding | **HI-007 substantially rewritten and upgraded from a discovery lead to an affirmative register record.** Haw. Rev. Stat. § 199-9 requires DLNR to operate a DOCARE unmanned aircraft systems program (established by June 30, 2025) for conservation/cultural-resource enforcement, with annual legislative reporting, AND separately prohibits DLNR from purchasing, operating, or funding UAS manufactured or assembled by a "covered foreign entity" absent a narrow chairperson waiver. This is a real state-agency UAS procurement/foreign-hardware restriction — a category that has been absent (`not_applicable`) in most other states retrofitted to date. Corroborated via multiple independent search-mediated readings of Justia's codification; a direct full-page fetch was attempted against both Justia and capitol.hawaii.gov and returned no retrievable content in this pass, so confidence is held at Moderate rather than High. |
| 10 | Privacy, surveillance, trespass, and interference | Applicable source found — see rows 1 and 3 | HI-001 and HI-003. |
| 11 | Professional licensing-board materials | Reviewed — no applicable UAS-specific source located; upgraded confidence | HI-006 (Board of Registration for Professional Engineers, Architects, Surveyors and Landscape Architects, general Ch. 464 competency framework) — general framework citation corroborated against DCCA's own published chapter text (replacing a citation based on general knowledge). A fresh, independent search (including current EASLA FAQs and HAR Title 16, Ch. 115) again found no Hawaii-specific UAS/photogrammetry board guidance — confidence Low → Moderate, consistent with the IL-009/LA-007/CO-010 pattern from prior Workstream 9 retrofits. |
| 12 | State preemption / state-local boundary | Reviewed — no applicable UAS-specific source located; relocated | The negative-finding record for a comprehensive statewide UAS-preemption statute (previously register record HI-005, whose own `source_type` field said "not included in the final source register") was moved to this checklist per `Agent_Instructions.v6.md` §5.2. No such statute was located; Hawaii's four counties (Honolulu, Maui, Hawaii, Kauai) each remain free to regulate UAS on county-owned property. The underlying finding remains as general contextual discussion in the narrative, which is not itself a register record. This remains one of relatively few states researched so far without any statewide UAS preemption at all — flagged as a materially higher-than-usual local-ordinance research priority. |

## Open verification items

1. A direct, full-text fetch of Haw. Rev. Stat. §§ 711-1121 through 711-1123 (Act 161 misuse framework) has now failed against both capitol.hawaii.gov and Justia in two independent research passes. Recommend trying a Hawaii Legislative Reference Bureau session-law PDF for Act 161, or a manual retrieval, before a client-facing opinion turns on the precise statutory elements.
2. A direct, full-text fetch of Haw. Rev. Stat. § 199-9 (DOCARE UAS program) was also unsuccessful in this pass via the same two source pages, despite consistent search-mediated corroboration of its substance. Recommend a follow-up direct read before relying on exact statutory wording for a client-facing opinion.
3. Haw. Admin. R. § 13-146-9's verified text dates to a 1999/2002 compilation cycle; confirm the current version and DLNR's current special-use-permit process directly with the Division of State Parks.
4. County ordinances (Honolulu, Maui, Hawaii, and Kauai counties, each separately) remain out of scope for this phase and are a materially higher-than-usual priority for Hawaii given the absence of any statewide preemption.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/news-aggregator.md`, as the closing step of this retrofit. Searched: HI-001
(trespass/harassment enforcement), HI-004 (state park drone enforcement), HI-007 (DOCARE/DLNR UAS program
activity), professional licensing board (HI-006).

One genuine match found: Hawaii News Now's July 31, 2026 report on the first felony arrest under "Duke's Law"
(Act 235, 2025) for illegal hunting on private ranch land, which disclosed that the Hawaii Department of Law
Enforcement (DLE) — a separate state agency from DLNR/DOCARE, though it responded jointly with DLNR to this
incident — has expanded its enforcement fleet with drones equipped with cameras, thermal imaging, and
loudspeakers to locate illegal hunters. Directly relevant context for HI-007 (state-agency conservation/
natural-resource UAS enforcement), even though the specific incident involved DLE rather than DOCARE itself.
Added to `HI_UAS_News.yaml` and anchored inline under the rewritten HI-007 section, with the agency distinction
made explicit in the relevance note to avoid overstating the connection to § 199-9's DOCARE-specific program.

Other candidates considered and rejected: a separate August 7, 2026 Hawaii News Now story on HPD releasing new
drone video from an Oahu Community Correctional Center inmate-escape timeline is a genuine current event
involving state drone use, but does not map to any existing Hawaii register record (Hawaii has no
correctional-facility-specific UAS restriction comparable to North Carolina's § 15A-300.3), so it was not added
as a news item in this pass — flagged instead as a possible future research lead if Hawaii enacts a
correctional-facility UAS provision.
