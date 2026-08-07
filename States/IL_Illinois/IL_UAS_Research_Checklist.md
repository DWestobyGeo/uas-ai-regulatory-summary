# Illinois UAS Research Checklist

- **State:** Illinois (IL)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. Chicago's own ordinance, other local ordinances, and tribal rules are outside this pass.

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found | 725 ILCS 167 (Freedom from Drone Surveillance Act, IL-001), 620 ILCS 5/42.1 (state preemption, IL-002), and 520 ILCS 5/2.33(i) (Wildlife Code, IL-003) each re-fetched and re-confirmed directly against the Illinois General Assembly's own codification (2026-08-06/07) — all three matched the register's existing text exactly, no substantive change. Corrected IL-001's and IL-002's `practical_interpretation` fields in the register, which had generic/templated content (IL-002's `practical_interpretation_aec_expert` had wildlife-harassment text copy-pasted from IL-003 — wrong for a preemption record). |
| 2 | Administrative rules and regulations | Applicable source found | 71 Ill. Adm. Code 2005.65 (Capitol Complex, IL-004) and 17 Ill. Adm. Code 110.160(i) (IDNR land, IL-005) re-confirmed directly against Cornell LII's and Justia's current codification mirrors — both matched exactly. Corrected templated interpretation fields for both records. |
| 3 | Executive orders | Reviewed — no applicable UAS-specific source located | Re-searched 2026-08-06; no Illinois gubernatorial executive order specific to UAS located. **Previously stored as part of register record IL-010 (a combined negative-finding record); moved to this checklist row** per `Agent_Instructions.v6.md` §5.2 (negative findings belong in the checklist, not the source register) and the matching `scripts/validate_research_semantics.py` finding (`check_negative_finding_in_register`). |
| 4 | Court decisions and attorney-general materials | Reviewed — no applicable UAS-specific source located | Re-searched 2026-08-06; no Illinois appellate court decision directly construing 725 ILCS 167, 620 ILCS 5/42.1, or 520 ILCS 5/2.33(i) located, and no formal Illinois Attorney General opinion construing a UAS-specific statute located (the AG's office has published non-regulatory guidance to law enforcement on drone usage under 725 ILCS 167, but this is agency guidance, not a formal opinion, and not separately regulatory of private AEC operators). **Also previously part of register record IL-010; moved to this checklist row** for the same reason as row 3. |
| 5 | Aviation and transportation agencies | Applicable source found | IDOT Division of Aeronautics UAS program page and its March 18, 2026 FASC-prohibited-manufacturer memo (IL-006) re-confirmed directly against idot.illinois.gov — matched the register exactly. Corrected the record's templated interpretation fields (the prior text was a landing-permit template; IL-006 is an equipment/compliance restriction, not a property-boundary permit). |
| 6 | Parks, public lands, forestry, fish, wildlife, and natural resources | Applicable source found | See rows 1 and 2 (520 ILCS 5/2.33(i), 17 Ill. Adm. Code 110.160(i)). |
| 7 | Corrections, public safety, emergency management, and critical infrastructure | Reviewed — no current enacted source; pending legislation tracked | No current Illinois statute specifically restricting UAS near correctional facilities or critical infrastructure was located. SB 3930 / HB 5275 (Drone Safety and Interference Prevention Act, IL-008) would create such offenses but has not passed; re-confirmed directly against ILGA's own bill-status pages 2026-08-06 — HB 5275 last action 4/17/2026 (re-referred to Rules), SB 3930 last action 3/27/2026 (re-referred to Assignments). The Illinois General Assembly's 2026 spring session adjourned sine die June 1, 2026 without further action on either bill; a fall veto session is scheduled Oct. 14–16 and Oct. 28–30, 2026. |
| 8 | Privacy, surveillance, harassment, trespass, and interference | Applicable source found | See row 1 (725 ILCS 167, law-enforcement-only). No general private-party UAS privacy/surveillance statute was located beyond this. |
| 9 | Procurement, equipment, cybersecurity, and manufacturer restrictions | Applicable source found (agency policy); pending legislation tracked | See row 5 (IDOT/IL-006, federal-nexus only). SB 2364 (Unmanned Aerial Systems Security Act, IL-007) would create a general government-agency procurement/country-of-origin restriction but has not passed; re-confirmed directly against ILGA's bill-status page 2026-08-06 — last action still 2/7/2025 (referred to Assignments), no further movement in over a year. |
| 10 | Professional licensing-board materials | Applicable source found (general statute); no board-specific UAS guidance | 225 ILCS 330/5 (Illinois Professional Land Surveyor Act definitions, IL-009) re-fetched directly from ILGA 2026-08-06 and confirmed to match the register's existing summary exactly, including the photogrammetric-methods certification exception. A fresh targeted search again found no standalone IDFPR or Illinois Land Surveyors Licensing Board UAS-specific guidance document. Confidence upgraded Low → Moderate (statute now directly re-verified; absence of board guidance remains a negative search result). |
| 11 | State preemption | Applicable source found | See row 1 (620 ILCS 5/42.1, IL-002). |

## Open verification items

1. If Illinois' Board of Registration ever publishes standalone UAS-specific guidance for land surveyors, add it to the register as a new record — the general 225 ILCS 330/5 licensing/photogrammetry-exception framework itself remains real and worth mentioning to clients, it simply does not currently meet this register's scope-gate bar on its own.
2. Monitor SB 2364 and SB 3930/HB 5275 for movement in the 104th General Assembly's fall veto session (Oct. 2026) or a future General Assembly; none has passed as of this retrofit.
3. No statewide inventory of local 620 ILCS 5/42.1(b-5) "reasonable rules" (park/recreation-land UAS rules) was compiled — confirm directly with the relevant local land-managing agency for a site-specific engagement.
4. 17 Ill. Adm. Code 110.160(i) uses the general term "aircraft," not "drone" — its application to UAS rests on IDNR site practice, not rule text; confirm directly with IDNR's Office of Land Management if a dispute over scope arises.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/research-expert.md` Section 4.7, as the closing step of this
retrofit. Searched: IL-001 (law-enforcement drone use / PSAP-dispatch practice), IL-004
(Capitol Complex incidents), IL-006 (IDOT FASC-ban contractor impact), IL-002 (Chicago
ordinance enforcement), IL-007 (SB 2364 coverage), IL-008 (SB 3930/HB 5275 coverage).

One genuine match found: Oak Brook Police Department's Flock Safety drone-as-first-responder
program (ABC7 Chicago, Aug. 15, 2025) directly illustrates the PSAP-dispatch exception in
725 ILCS 167 Section 15(9) and the Act's retention/oversight provisions in current practice.
Added to `IL_UAS_News.yaml` and anchored inline in the narrative under IL-001.

Other candidates considered and rejected: the FAA's October 2025 Chicago-area drone TFR
(genuine news, but a federal FAA action, not tied to any state-authority record's regulated
activity -- remains in Section 4 "Non-Regulatory Context" as general situational awareness,
not attached via news-anchor); the University of Illinois football-stadium drone arrest
(general security enforcement, not matched to a specific state UAS authority); HB 4332
(sex-offender drone-ownership disclosure bill, not enacted and no corresponding register
record to anchor to); SB 2364 and SB 3930/HB 5275 bill-tracker coverage (not event/incident
reporting, so not "news" under the role's Section 4.3 standard).
