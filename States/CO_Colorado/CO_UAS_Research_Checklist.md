# Colorado UAS Research Checklist

- **State:** Colorado (CO)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. Local ordinances and tribal rules are outside this pass (see Section 4 of the narrative for the state/local boundary discussion).

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found | CRS § 18-8-104 (drone obstruction of public-safety operations, CO-001) and CRS § 18-7-801 (criminal invasion of privacy, CO-002) — both re-confirmed directly against Justia's codification, unchanged from the prior pass. |
| 2 | Civil liability statutes | Applicable source found; upgraded | CRS § 41-1-107 (landowner airspace rights / civil trespass, CO-003) — full current text fetched and read directly against Justia in this pass (previously secondary-source only). Confidence Moderate → High; `source_url` corrected away from the dronelaws.us aggregator. |
| 3 | Administrative rules and regulations | Applicable source found; major citation finding | CO-004 (CPW state-park manned-aircraft prohibition, 2 CCR 405-1 #100.b.15) — full Chapter P-1 text fetched and read directly from cpw.state.co.us. The widely-recirculated "Regulation #100-c.24" UAS-specific citation, repeated across at least six secondary drone-law compilation sites, could not be traced to any primary CPW document and does not match the regulation's actual subsection-lettering scheme. Treated as an unverifiable/likely-erroneous citation rather than a confirmed rule; record rewritten accordingly with a continued conservative practical recommendation. |
| 4 | Wildlife-related administrative rules | Applicable source found; upgraded | CO-005 (CPW drone-hunting/scouting prohibition) — full current text of 2 CCR 406-0, Article IV, #004(C) fetched and read directly from the Colorado Secretary of State's CCR database, confirming the exact operative text and the drone/UAV/UAVS definition. Confidence Moderate → High; `source_url` corrected away from dronelaws.us. |
| 5 | Executive orders | Not separately tracked | No standalone executive-order register record exists for CO; not re-searched as a distinct category in this pass. |
| 6 | Court decisions and attorney-general materials | Reviewed — no applicable source located | No Colorado court decision or AG opinion addressing UAS operation was located in this pass (not separately re-searched beyond the original pass's negative result). |
| 7 | Aviation and transportation agencies | Not separately tracked | No standalone state DOT/aviation-agency UAS record exists for CO beyond the public-safety program (row 9 below); not identified as a gap in this pass. |
| 8 | Parks, public lands, forestry, fish, and wildlife | Applicable source found — see rows 3–4 | CO-004 and CO-005. |
| 9 | Corrections, public safety, and critical infrastructure | Reviewed — no applicable UAS-specific source located; relocated | **CO-006 removed from the register in this pass.** Its own `source_type` field read "Discovery lead — not final authority and not included in the final source register," a self-contradiction as a register row, matching the negative-finding-in-register governance principle already applied to IL-010, LA-008, and NC-011 in prior WS9 retrofits. No enacted Colorado statute prohibiting UAS operation over/near critical infrastructure, correctional facilities, airports, or sports venues (comparable to Texas or New York) was located; three prior bills (HB 15-1555, HB 15-059, HB 16-1026) died in committee. Corroborated via the Colorado Legislative Council Staff's October 2024 issue brief and bill-history searches — not independently re-searched for new 2025–2026 legislative activity in this pass beyond the news-aggregator pass below. |
| 10 | Privacy, surveillance, and trespass | Applicable source found — see rows 1–2 | CO-002 (privacy) and CO-003 (civil trespass). |
| 11 | Procurement, equipment, and cybersecurity | Not applicable | No Colorado-specific state-agency UAS procurement restriction or foreign-hardware ban (comparable to Texas's Prohibited Technologies List) was located in the original pass; not re-searched in this pass. |
| 12 | Professional licensing-board materials | Reviewed — no applicable UAS-specific source located; upgraded confidence | CO-010 (DORA/State Board of Licensure general competency framework) — general Title 12, Article 120 framework re-confirmed directly against Justia; a fresh, independent search (including the 3 CCR 720 rule series) again found no Colorado-specific UAS/photogrammetry guidance. Confidence Low → Moderate given the negative finding is now corroborated across two independent research passes, consistent with the IL-009/LA-007 pattern. `source_url` corrected away from FindLaw to Justia. |
| 13 | State preemption / state-local boundary | Reviewed — no applicable UAS-specific source located; relocated | **CO-007 removed from the register in this pass.** Its own `source_type` field read the same self-contradictory "Discovery lead... not included in the final source register" language as CO-006. No Colorado statute broadly preempting local UAS regulation was located; SB26-024 (the one 2026 bill that would have limited local authority) was postponed indefinitely February 25, 2026 (confirmed directly against leg.colorado.gov in this pass — see row 14). Colorado's municipal/county ordinance patchwork remains dense and out of scope for this phase. |
| 14 | State-agency public-safety UAS programs | Applicable source found | CO-009 (Center of Excellence for Advanced Technology Aerial Firefighting, § 24-33.5-1228) — unchanged, already High confidence and directly verified against the Legislative Council Staff issue brief. |
| 15 | Non-enacted proposals | Applicable source found | CO-008 (SB26-024) — bill status re-confirmed directly against the Colorado General Assembly's official bill-tracking page (leg.colorado.gov) in this pass: "Postponed Indefinitely" by the Senate Local Government & Housing Committee, February 25, 2026, status "Lost." No correction needed. |

## Open verification items

1. Direct written confirmation from CPW's Office of the Regulations Manager on whether any UAS-specific state-park/outdoor-recreation-lands prohibition currently exists in Colorado's Code of Regulations — CO-004's citation discrepancy could not be fully resolved from public sources alone in this pass, only more precisely characterized.
2. No Colorado-specific state-agency UAS procurement policy or foreign-hardware restriction was located; not independently re-searched in this retrofit pass.
3. No comprehensive negative-search confirmation was performed against the full Colorado Revised Statutes for either the critical-infrastructure/correctional-facility category (CO-006) or the state-preemption category (CO-007); both remain research results, not exhaustive negative findings.
4. Local municipal/county UAS ordinances (Denver, Boulder, Colorado Springs, mountain resort communities, etc.) remain out of scope for this phase; a project-specific ordinance check is required before relying on this state-level summary for a specific Colorado site.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/news-aggregator.md`, as the closing step of this retrofit. Searched: CO-001
(drone interference with public-safety/emergency operations), CO-004/CO-005 (CPW state-park and wildlife-scouting
enforcement), CO-008 (SB26-024 and any successor legislation).

One genuine match found: KRDO News (Colorado Springs) and corroborating regional coverage (DroneXL,
Unofficial Networks) reporting that a drone pilot in southern Colorado is facing federal charges for allegedly
flying inside the temporary flight restriction (TFR) over the "Aspen Acres" wildfire near Pueblo County in
July 2026, forcing firefighting aircraft to ground until the airspace was cleared. Directly on point for CO-001's
prohibition on using a UAS to obstruct, impair, or hinder emergency/public-safety operations (here, wildfire
suppression). Added to `CO_UAS_News.yaml` and anchored inline under CO-001.

Other candidates considered and rejected: continued syndicated repetition of the "CPW Regulation #100-c.24"
citation across dronelaws.us, flyusi.org, pilotinstitute.com, uavcoach.com, dronesgator.com, and propelrc.com —
these are the same secondary drone-law compilation content already distrusted as "news" sources under this
role's standing guidance, and in this case were also affirmatively shown (see row 3 above) to repeat an
unverifiable citation rather than report any actual current event; the CBS News Colorado piece on drone-assisted
hunting prohibitions ("You Aren't Giving The Animals A Chance") is general explanatory coverage of the
already-registered CO-005 rule rather than a new, dated event, so it was not added as a separate news item.
