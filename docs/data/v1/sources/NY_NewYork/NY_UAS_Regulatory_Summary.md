# New York — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 1, 2026 | **Version:** 2.2 (Workstream 9 retrofit — August 7, 2026)
**Model / checkpoint:** Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet. Retrofit pass performed with claude-sonnet-5.
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent Instructions v6), this summary covers New York **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase and are not included here. Unlike Texas or Florida, New York has **not** enacted a state preemption statute for local UAS ordinances (see Section 4), and New York City in particular maintains an extensive independent permit regime — a project-specific municipal check will be necessary before this state-level picture can be treated as complete for any specific New York site. Full citations and metadata are in `NY_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

New York's UAS regulatory landscape changed materially on May 28, 2026, with the enactment of new Penal Law Article 280 and companion Executive Law § 236 (Part D of the FY2027 Public Protection Budget, S.9005-B). Article 280 creates a tiered set of drone offenses keyed to a broadly defined 500-ft "prohibited space" around airports, military installations, correctional facilities, police/fire stations, emergency dispatch centers, large public gatherings, critical infrastructure, and schools — notably **without** a general FAA-authorization or commercial-operator exemption comparable to Texas's or Florida's critical-infrastructure carve-outs; only a narrow governmental-employee exemption applies. Executive Law § 236 separately authorizes police counter-drone measures and establishes the "New York State Blue List," a State Police vendor registry that will restrict state-agency and political-subdivision drone procurement once published. Both provisions were enacted but are **not yet effective** as of this research date (effective date is the 90th day after enactment, approximately August 26, 2026). Outside this new statute, New York regulates UAS through state-park permit rules (OPRHP), DEC land-classification and wildlife-harassment rules, and general professional-licensing competency requirements — but has **not** enacted a state preemption statute, so local ordinances (most notably New York City's) remain independently significant and are not addressed in this state-level pass.

## 2. Statewide UAS Laws and Regulations

### N.Y. Penal Law Article 280 (§§ 280.00–280.15) — Offenses Relating to Unlawful Use of a Drone
*Binding law | Enacted May 28, 2026; effective ~August 26, 2026 (90 days after enactment) — not yet effective as of this research date*

**Objective Summary:** New Article 280 defines "drone," "nefarious manner" (conduct that violates or facilitates violation of the Penal Law, constitutes intentional unauthorized surveillance of a prohibited space, interferes with emergency operations, facilitates criminal activity, or creates significant risk of physical injury or property damage), and "prohibited space" (any area within 500 ft of an airport; a state/federal military installation; a state, local, or federal correctional facility; a police station; a fire department station; an emergency services dispatch station; a large public gathering such as a concert, festival, or sporting event; "critical infrastructure" as defined in Public Officers Law § 86(5); or a school as defined in Education Law § 1125(10)). § 280.05 (Unlawful Use of a Drone in the Second Degree, Class A misdemeanor) is committed by operating a drone in a nefarious manner, or over a prohibited space without express prior approval from someone the operator reasonably believes has authority to grant it; a governmental employee acting within official duties is exempted. § 280.10 (First Degree, Class E felony) applies to a repeat violation or one committed in furtherance of another crime. § 280.15 (Aggravated, Class D felony) applies to a repeat First Degree violation.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This is a materially different compliance posture than Texas or Florida — treat any project within 500 ft of an airport, jail/prison, police/fire station, school, or critical-infrastructure facility as requiring documented prior authorization from someone with actual or apparent authority over that site before flying, once the law takes effect (~Aug. 26, 2026). Do not assume FAA Part 107 certification alone is a defense here.
- **Agency Practitioner:** Contact the official or office designated by the cited authority before fixing mobilization dates. Request the current form, documentation checklist, fees, submission route, and processing estimate; retain the issued approval and all site-specific conditions with the flight record.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Build a written-authorization-collection step into standard operating procedure for any New York project near a listed facility type ahead of the effective date, and monitor for implementing guidance or a companion bill adding a commercial exemption. This record is based on the passed bill text (S.9005-B); confirm the final chapter-law number and that no amendment altered the exemption structure before the effective date.
### N.Y. Executive Law § 236(5) — Drone Procurement Restriction ("New York State Blue List")
*Binding law | Enacted May 28, 2026; effective ~August 26, 2026 — not yet effective as of this research date*

**Objective Summary:** Directs the Superintendent of State Police to establish a vendor registry — the "New York State Blue List" — of vetted, federally-compliant drone and drone-mitigation-technology vendors. Once published, the state, its agencies, and political subdivisions may purchase or lease drones and drone-mitigation technology only from Blue List vendors. § 236 separately authorizes trained police/peace officers to detect, track, and (as a last resort) disable a drone posing a credible threat to a prohibited space, subject to a 48-hour reporting requirement.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This restricts state-agency and political-subdivision procurement, not a private AEC firm's own equipment purchases — but confirm Blue List compliance if bidding on a New York public-sector task order that specifies government-purchased or -leased UAS equipment, once the registry is published.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Require current vendor documentation for aircraft, critical components, installed software, ownership, origin, and support lifecycle before purchase. Compare the proposed configuration with the controlling authority and preserve the evidence supporting the acquisition decision.
- **AEC Industry Legal Counsel:** Do not represent to a client that this restricts a private firm's choice of UAS manufacturer generally; check whether a specific public-agency contract independently incorporates Blue List compliance as a contract term once the registry exists (it did not yet exist as of this research date).
## 3. State Agency and Land-Management UAS Requirements

### Parks — NYS Office of Parks, Recreation and Historic Preservation (OPRHP)
*Binding administrative regulation | Current*

**Objective Summary:** 9 NYCRR §§ 372.7(b)–(j) (statewide) and § 409.1(c),(j) (Palisades region), together with PRHPL § 3.09(2), prohibit unauthorized launching, landing, or operation of a UAS on OPRHP-administered land or water. Recreational UAS use requires a Special UAS Permit specifying time, place, and manner; commercial UAS use generally requires a permit for commercial activity within OPRHP facilities.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Apply for the applicable commercial-activity/UAS permit before staging any AEC UAS work (inspection, environmental documentation, corridor mapping) on state park, historic site, or parkway property, and build permit lead time into scheduling.
- **Agency Practitioner:** Start with the site manager or permitting office for NYS Office of Parks, Recreation and Historic Preservation (OPRHP) before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain the OPRHP permit in the project file for any launch, landing, or operation on OPRHP land; confirm current procedure directly with the relevant OPRHP region, since region-specific rules (e.g., Palisades) may vary from the statewide rule.
### Land Management — NYS Department of Environmental Conservation (DEC) UAS Policy
*Official agency policy / binding administrative regulation | Current*

**Objective Summary:** DEC prohibits launching, landing, or operating a UAS on DEC land classified as Wilderness, Primitive, or Canoe area (consistent with the general prohibition on motorized equipment in those classifications). On other DEC lands, written permission from the relevant regional director is generally required before UAS takeoff, landing, or operation.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Check the land classification of any DEC parcel near a project site before planning a launch — Wilderness/Primitive/Canoe classifications are a hard no-fly for launch/landing, while other DEC lands require advance regional-director permission.
- **Agency Practitioner:** Start with the site manager or permitting office for NYS Department of Environmental Conservation (DEC) before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain written regional-director permission in the project file for any DEC-land launch/land/operate activity outside a classified no-fly area; confirm current classification and procedure directly with the relevant DEC region.
### Wildlife — DEC Prohibition on Aircraft Use to Hunt, Locate, Drive, or Take Wildlife
*Binding administrative regulation | Current*

**Objective Summary:** 6 NYCRR § 180.3 and ECL § 11-0923 prohibit using an aircraft — a category DEC treats as including drones — to hunt, locate, drive, or take wildlife. New York's broad statutory definition of "taking" includes disturbing, harrying, or worrying wildlife. A narrow allowance exists for recovering already-harvested game.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Plan environmental-monitoring, habitat-mapping, or resource-inventory flights to avoid disturbing, harrying, or worrying wildlife, and avoid any use that could be read as locating or driving game during an active hunting season.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the survey/mapping purpose of any UAS flight over wildlife habitat to distinguish it from a hunting-assistance or harassment use; the "disturbing/harrying/worrying" standard is broad and judgment-based, so build a conservative standoff buffer near known wildlife concentrations.
### Professional Licensing — NYS Board of Regents / Office of the Professions
*Binding general regulation | No UAS-specific board guidance located*

**Objective Summary:** New York's professional-conduct rules for licensed engineers and land surveyors require practicing only in fields in which the licensee is, by education and/or experience, fully competent and proficient (8 NYCRR Part 29, general unprofessional-conduct framework). No standalone State Education Department or licensing-board guidance document specifically addressing UAS-derived photogrammetry, LiDAR, or mapping products was located during this research pass.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Route UAS-derived photogrammetry/LiDAR mapping products through a New York-licensed PE or PLS for review under the existing general competency framework before delivery on any official deliverable, since no UAS-specific board standard currently exists.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document licensed-professional review and QA/QC of UAS-derived deliverables given the absence of UAS-specific board guidance; consider a direct inquiry to the Office of the Professions for novel UAS-derived-product certification questions.
## 4. State Preemption of Local Ordinances

*This section reflects a research result (no statute located), not an affirmative source record; per this project's negative-finding governance principle (`Agent_Instructions.v6.md` §5.2), it is retained here as narrative context rather than as a `NY_UAS_Source_Register.csv` row.*

**Objective Summary:** No New York statute broadly preempting local UAS regulation was located during this research pass, in contrast to Texas (Gov't Code § 423.009) and similar to California. New York City independently regulates UAS takeoff/landing through NYC Administrative Code § 10-126(c) and a permit system (38 RCNY § 24) administered jointly by the NYPD and NYC DOT, and other municipalities (e.g., the Village of Cooperstown) have adopted their own local drone ordinances.

**Practical Interpretation**
- **AEC Industry UAS Expert:** Do not assume New York state law displaces local drone ordinances — New York City alone has an extensive permit-based UAS regime layered on top of the new state Penal Law Article 280, and other municipalities have their own rules. A project-specific municipal ordinance check will be necessary in a later research phase before finalizing site-specific flight plans anywhere in New York.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Flag for the client that New York's local-ordinance landscape is at least as significant as the state-level rules summarized here, particularly in New York City; advise local counsel or a jurisdiction-specific ordinance check before relying on this state-level summary alone for a specific New York project site.

## 5. Superseded / Non-Enacted Proposals

### Standalone Correctional-Facility Drone Bills (S.2125/S.1380/S.2660/S.694-A and successors)
*Proposed or pending authority | Repeatedly introduced 2017–2025; not independently enacted*

**Objective Summary:** A standalone bill prohibiting drone operation within a set distance (1,000 ft in earlier Senate versions; the Governor's FY2026-27 executive budget proposal used 500 ft) of a state or local correctional facility has been introduced in most legislative sessions since at least 2017 without independently passing. This subject matter was ultimately addressed through the broader, independently-enacted Penal Law Article 280 (Section 2 above), which includes correctional facilities within its 500-ft "prohibited space" definition.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not track this bill series as a separate compliance requirement — the operative correctional-facility protection for AEC purposes going forward is the enacted Penal Law Article 280 500-ft prohibited-space rule, not this superseded bill lineage.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Do not represent to a client that a standalone New York correctional-facility drone statute with a 1,000-ft or 500-ft buffer exists independent of Penal Law Article 280; rely on Article 280 for current and forthcoming correctional-facility UAS restrictions in New York.
## 6. Unresolved Operational Questions

- **Retrofit-pass tool limitation (added August 7, 2026):** A planned direct re-fetch of the NY Senate bill page, the NY Department of State eRules database, and a news-aggregator search were not completed in this retrofit pass due to a web-fetch tool-availability interruption. All items below are therefore carried forward from the original pass rather than newly re-confirmed; a follow-up currency and news-aggregator pass is recommended.
- **Article 280 / Executive Law § 236 final chapter number:** This summary is based on the passed bill text (S.9005-B, Part D); the final signed chapter-law number was not independently cross-checked against the NY Session Laws, and no amendment activity between passage and the ~Aug. 26, 2026 effective date was confirmed absent.
- **New York State Blue List content:** The Executive Law § 236(5) vendor registry had not yet been published as of the research date; its actual vendor/equipment content should be re-checked once the law takes effect.
- **Statewide DOT/aviation-office UAS program:** Research located NYC-specific DOT/NYPD UAS material but did not confirm whether NYSDOT maintains a separate statewide UAS operations program comparable to TxDOT's UAS Manual; this remains an open question for a future research pass.
- **Court decisions / AG opinions:** No New York court decision or Attorney General opinion directly addressing UAS regulation was located during this research pass; this may reflect a genuine gap rather than a search limitation.
- **New York City and other local ordinances:** Out of scope for this phase, but flagged as materially significant — see Section 4.

## 7. Confidence Summary

| Finding | Confidence |
|---|---|
| Penal Law Article 280 (§§ 280.00–280.15) | High — verified directly against the enacted S.9005-B bill text |
| Executive Law § 236(5) / Blue List | High — verified directly against the enacted S.9005-B bill text |
| OPRHP state park UAS permit rules | Moderate — citations and substance from a secondary industry-compliance source; underlying NYCRR text not independently re-pulled |
| DEC Wilderness/Primitive/Canoe UAS policy | Moderate — confirmed via DEC's own Environmental Notice Bulletin posting; full current policy text not independently re-pulled |
| DEC wildlife-harassment rule (6 NYCRR § 180.3) | Moderate — citations and substance from a secondary industry-compliance source; DEC's own regulations page could not be re-fetched |
| General professional-licensing competency rule | Low — secondary source using a generic "Rule 415" label seen across multiple states; exact NYCRR citation not independently verified |
| No state preemption of local ordinances | Low — reports a research result (absence of a located statute), not a comprehensive negative search of the full Consolidated Laws |
| Standalone correctional-facility bills (superseded) | Moderate — bill history confirmed via nysenate.gov bill listings and a secondary news source |

*This document is objective legal/regulatory summary plus labeled practical interpretation. It is not legal advice; consult New York counsel for project-specific compliance determinations. Local ordinances — particularly New York City's independent UAS permit regime — and tribal UAS considerations are out of scope for this phase per current research instructions.*
