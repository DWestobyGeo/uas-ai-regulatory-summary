# Missouri — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 1, 2026; retrofitted August 6, 2026 (Workstream 9) | **Version:** 2.2 (Phase 2 — subjective-scope audit complete August 2, 2026; Workstream 9 retrofit August 6, 2026)
**Model / checkpoint:** Original objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet (not retroactively guessed at, per governance §8.3). The August 6, 2026 Workstream 9 retrofit pass used claude-sonnet-5.
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent_Instructions.md v3), this summary covers Missouri **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase and are not included here. Full citations and metadata are in `MO_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Missouri regulates UAS through two enacted criminal statutes targeting specific location types — open-air facilities/critical infrastructure (§577.800) and correctional centers (§217.850) — rather than a comprehensive UAS code. A 2026 merged enactment (H.B. 2637 & 3155, merged with S.B. 1421), signed June 12, 2026 ahead of Kansas City's FIFA World Cup 2026 matches, significantly expanded §577.800's reach: it lowered the open-air-facility capacity threshold from 5,000 to 500, added a flat prohibition on UAS use anywhere within a critical infrastructure facility's boundary (cross-referencing RSMo 569.086's extensive facility list), added a railroad-employee exemption, and added a mandatory warning-sign requirement. Multiple 2026 press sources also report the same act authorizes certified peace officers to take mitigation measures against a drone posing an imminent public-safety threat or involved in criminal activity; the specific codified section for that authority was not independently located in this pass and is flagged as an open item. Missouri does not currently have an enacted general drone-privacy/surveillance-consent statute, despite a bill with that goal being introduced repeatedly since 2013 (most recently HB 209 in 2025) without passing — a gap worth flagging rather than assuming exists. State agencies (MoDOT, DNR State Parks, MDC) each maintain their own UAS-relevant programs or permit requirements.

## 2. Statewide UAS Laws and Regulations

### RSMo 577.800 — Unlawful use of unmanned aircraft over open-air facility or critical infrastructure facility (as amended by 2026 H.B. 2637 & 3155 merged with S.B. 1421)
*Binding law | Current, current codified text effective June 12, 2026 (S.B. 1421 provisions effective July 9, 2026)*

**Objective Summary:** As consolidated by the 2026 merged enactment (current codified text independently re-verified directly against the Revisor of Statutes on 2026-08-06), it is an offense to purposely: (1) operate a UAS within 400 ft AGL and within the property line of an "open-air facility" — now defined as capacity 500 or more (lowered from 5,000), not fully enclosed by a roof; (2) use a UAS to deliver a weapon/explosive device (Class B felony) or controlled substance (Class D felony) to a person there; (3) use a UAS at all within the boundary of a "critical infrastructure facility" — no altitude threshold applies; or (4) operate within 400 ft AGL and within the property line of a critical infrastructure facility in furtherance of any other criminal violation. "Critical infrastructure facility" takes the definition in RSMo 569.086 — an extensive list including electric power generation/substations/transmission, water and wastewater treatment, chemical/petroleum/gas facilities and pipelines, telecommunications infrastructure (including cell towers), ports/railroads, dams, broadband infrastructure, and CFATS-regulated sites, among others; note that 569.086's own amended, fuller list does not take effect until Aug. 28, 2026, so the cross-referenced definition is narrower between June 12 and Aug. 28, 2026. Exemptions cover facility employees/owners/operators; a person with written consent from the facility's president/CEO; law enforcement/fire/EMS and government employees on official duty; a public utility or rural electric cooperative conducting inspection/repair/maintenance (with advance facility notice and no unescorted entry); a railroad employee on railroad-owned/operated land; and, separately, a commercial operator lawfully authorized by the FAA to operate in that airspace. Each covered facility must post an 11x14-inch warning sign. Multiple 2026 press sources also report the same act authorizes certified peace officers to take mitigation measures against a drone posing an imminent public-safety threat or involved in criminal activity; the specific codified section for that authority was not independently located in this pass (see Section 1 and the Confidence Summary).

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat any event venue with 500+ capacity, and any facility on the RSMo 569.086 critical-infrastructure list (power generation/substations, water/wastewater, chemical/petroleum, telecom and cell towers, pipelines, ports/rail, dams, broadband infrastructure, and CFATS-regulated sites, among others), as a no-fly zone by default for Missouri work — as of the June 12, 2026 amendment, mere presence within a critical-infrastructure facility's boundary is itself prohibited, with no altitude threshold. For utility inspection work, give the facility advance notice as required by the utility exemption rather than assuming it is self-executing, and confirm the facility has posted the now-required 11x14-inch warning sign before treating a site as clearly marked.
- **Agency Practitioner:** Contact the protected facility's owner, operator, administrator, commander, or other official identified by the authority before mobilization and ask whether the proposed AEC mission qualifies for written approval or an employment/contractor exception. Provide the site, purpose, dates, flight area, crew and aircraft details the facility requests, and retain the signed authorization and security conditions; do not assume ordinary site access or a client work order is sufficient.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** The 2026 merged-bill amendment is now confirmed reflected in the current codified text via a direct re-pull — a prior research pass's concern about a site-update lag is resolved. Document the specific exemption relied upon (utility inspection, government duty, facility consent, or now also railroad-employee duty) for any flight near a covered venue or facility given the felony-level exposure for prohibited deliveries. Note the cross-referenced "critical infrastructure facility" definition (RSMo 569.086) does not reach its full expanded list until Aug. 28, 2026, so the scope of covered facilities is narrower between June 12 and Aug. 28, 2026 than after.
### RSMo 217.850 — Correctional center, unlawful use of unmanned aircraft over
*Binding law | Current, unamended since original 2020 enactment (confirmed via direct 2026 pull)*

**Objective Summary:** Makes it an offense to purposely operate a UAS within 400 ft vertical distance over a correctional center's secure perimeter fence, or to allow a UAS to make contact with the facility (including any person or object on the premises). "Correctional center" is defined broadly to include state correctional centers, private jails, and county or municipal jails. Exemptions include facility-authorized operators, written consent from the chief administrative officer, law enforcement/fire/EMS and government employees on official duty, qualifying utility infrastructure work, a railroad employee on railroad-owned/operated land, and a person operating under and complying with an FAA waiver issued under 14 C.F.R. § 107.200. Punishable as an infraction generally, escalating to a class B felony for weapon delivery, a class C felony for facilitating an escape under §575.210, or a class D felony for controlled-substance delivery. Each correctional center must post an 11x14-inch warning sign.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Identify any state, private, county, or municipal correctional/jail facility near a project site during pre-flight planning and maintain the 400 ft vertical standoff by default unless the project specifically requires facility work, in which case get the chief administrative officer's written consent first.
- **Agency Practitioner:** Contact the protected facility's owner, operator, administrator, commander, or other official identified by the authority before mobilization and ask whether the proposed AEC mission qualifies for written approval or an employment/contractor exception. Provide the site, purpose, dates, flight area, crew and aircraft details the facility requests, and retain the signed authorization and security conditions; do not assume ordinary site access or a client work order is sufficient.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain written consent documentation for any flight authorized near a correctional facility; the broad definition of "correctional center" — reaching county and municipal jails, not just state prisons — means this statute applies more often than a quick check for "state prison" alone would suggest. The offense escalates to a class C felony if the UAS is used to facilitate an escape (RSMo 575.210) and a class B felony for weapon delivery — treat any flight activity a facility could plausibly read as escape-related as an acute risk requiring prior written coordination, not just routine site consent.
### "Preserving Freedom from Unwarranted Surveillance Act" — not current law
*Repealed, expired, or superseded authority (never enacted)*

**Objective Summary:** A bill by this title would prohibit any person, entity, or state agency from using a drone to conduct surveillance or observation of an individual, their property, a farm, or agricultural industry without consent, absent a warrant. It has been introduced repeatedly (HB 46 in 2013, later as HB 1204, and HB 209 in 2025) and has never passed; the proposed section numbers (RSMo 305.635–305.641) do not exist in current Missouri statutes.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not build a general Missouri drone-surveillance-consent or farm/agricultural-consent step into standard operating procedure based on this bill — it is not currently required by Missouri statute. Rely on the actual enacted statutes (open-air facility, correctional center) and ordinary privacy/trespass considerations instead.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Correct this specific point if it appears in any internal compliance document or client-facing guidance sourced from a drone-law aggregator. Missouri currently has no comprehensive UAS privacy/surveillance-consent statute — that gap is itself worth flagging to a client rather than asserting a consent requirement that isn't there.
### Unmanned Aerial Systems Security Act of 2025 — did not pass
*Proposed or pending authority (died in committee)*

**Objective Summary:** HB 210 (2025) would have prohibited Missouri government agencies from purchasing or using a UAS (or related services/equipment) from a manufacturer domiciled in a designated "country of concern" (China, Russia, Iran, North Korea, Cuba, Venezuela's Maduro regime, or Syria), required federally compliant encryption for drone communications, established a three-tier drone classification system, and included a Department of Public Safety replacement-grant program for affected agencies. The bill drew opposition from law enforcement and died in committee on May 16, 2025.

**Practical Interpretation**

- **AEC Industry UAS Expert:** No Missouri state procurement restriction currently limits fleet/manufacturer choice for private commercial work or for public-agency contract work, but track whether this bill (or a successor) is reintroduced in a future session.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** No current state equipment restriction is established by this research result. Do not treat that absence as permanent; check current solicitation terms, client policies, and independently applicable federal restrictions before committing a fleet to the work.
- **AEC Industry Legal Counsel:** Do not represent to a client that Missouri has, or is about to have, a manufacturer-restriction law based on this bill — it failed. Separately confirm the federal American Security Drone Act / OMB M-26-02 restrictions for any federally funded engagement (see MoDOT entry below), since those apply regardless of state law.
## 3. State Agency UAS Requirements

### Department of Transportation — Missouri Department of Transportation (MoDOT)
*Official agency policy*

**Objective Summary:** MoDOT operates a centralized UAV program with its own operation manual, safety program, and training program, used for real-time aerial data collection, structural inspections, and incident-site monitoring, emphasizing centralized standards, responsible procurement, and federal-regulation compliance.

**Practical Interpretation**

- **AEC Industry UAS Expert:** For any consultant contract involving MoDOT-adjacent UAS work (bridge/structure inspection, corridor mapping, incident documentation), request MoDOT's current UAV operations manual and align field procedures with it.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Treat MoDOT's centralized standards as an early contract-discovery item, not as proof that a particular firm-owned platform is approved. Before pricing equipment or support, request the current operating manual and project requirements, then compare required aircraft, payload, data, safety, training, insurance, and lifecycle-support capabilities with the proposed fleet.
- **AEC Industry Legal Counsel:** Confirm in the scope of work whether MoDOT's internal UAV standards (equipment, data handling, pilot qualifications) are being incorporated as contract requirements, and get any such incorporation in writing.
### Department of Transportation — Federal Foreign-Drone Procurement Restriction (MoDOT notice)
*Official agency policy — state notice of a federal requirement*

**Objective Summary:** Effective December 22, 2025, the federal American Security Drone Act of 2023 and OMB Memorandum M-26-02 prohibit the use of federal funds for UAS manufactured by "covered foreign entities," including any aircraft, flight controller, camera, or ground control station from a manufacturer based in or controlled by the People's Republic of China (or other designated foreign adversary countries). MoDOT published a notice informing its programs and contractors of this obligation as it flows down through federally funded transportation work. This is a federal requirement administered through a Missouri state agency, not a Missouri statute.

**Practical Interpretation**

- **AEC Industry UAS Expert:** If your firm does UAS work on any federally funded MoDOT (or other Missouri agency) transportation project, audit your fleet against covered-foreign-entity status before mobilizing — this applies at the component level (flight controller, camera, ground station), not just the airframe brand.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Require current vendor documentation for aircraft, critical components, installed software, ownership, origin, and support lifecycle before purchase. Compare the proposed configuration with the controlling authority and preserve the evidence supporting the acquisition decision.
- **AEC Industry Legal Counsel:** Confirm whether a specific MoDOT task order is federally funded (versus 100% state-funded) before assuming this restriction applies, since it is tied to the federal-funds nexus rather than being a general Missouri state law; document equipment-compliance representations in the proposal for any federally funded scope.
### Parks and Public Lands — Missouri Department of Natural Resources, Division of State Parks
*Official agency policy / permit requirement*

**Objective Summary:** Missouri State Parks does not impose a blanket drone ban; recreational pilots are asked to stay within main, open day-use areas and avoid disturbing other visitors. Professional or commercial UAS use requires prior approval through the Division of State Parks before flying.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Start the Division of State Parks commercial-use approval process as early as possible for any project involving a Missouri state park — don't assume day-use-area recreational tolerance extends to commercial operations.
- **Agency Practitioner:** Start with the site manager or permitting office for Missouri Department of Natural Resources, Division of State Parks before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Get the Division of State Parks' commercial-use approval in writing and keep it in the project file; confirm current approval requirements directly with DNR.
### Fish and Wildlife / Natural Resources — Missouri Department of Conservation (MDC)
*Binding administrative regulation + official agency policy*

**Objective Summary:** MDC requires a special use permit to launch, land, or operate a UAS on any of its 1,000+ conservation areas statewide. The Wildlife Code of Missouri (3 CSR 10-7.410 and related rules) forbids using a UAS to pursue, take, drive, or molest wildlife, or to operate it in a way that harasses wildlife or other visitors, with a narrow exception allowing drone-assisted recovery of wounded deer, turkey, elk, or black bear during the applicable season, with landowner permission, prior conservation-agent authorization, and no weapon on the operator.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat any MDC conservation area the same as a state park for launch/landing purposes — apply for the special use permit before staging a crew there for environmental monitoring, habitat mapping, or resource-inventory work, and build the permit lead time into project scheduling.
- **Agency Practitioner:** Start with the site manager or permitting office for Missouri Department of Conservation (MDC) before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain the MDC special use permit in the project file for any conservation-area launch/land activity; document flight altitude and purpose for work near wildlife concentrations given the judgment-based harassment standard.
### Professional Licensing — Missouri Board for Architects, Professional Engineers, Professional Land Surveyors and Professional Landscape Architects (APELSLA)
*Binding general regulation | No UAS-specific board guidance located*

**Objective Summary:** APELSLA's Mapping Survey Standards (20 CSR 2030-20.010 to .030) govern survey/mapping practice generally; a licensee must practice only in fields in which they are fully competent by education/experience — noted by secondary sources as especially applicable to UAS-derived mapping. No standalone UAS-specific board guidance document was located.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Route drone-derived photogrammetry/LiDAR mapping products through a Missouri-licensed PE or PLS for review under the existing Mapping Survey Standards before delivery on any official survey/engineering deliverable.
- **Agency Practitioner:** Before relying on an unlicensed or exempt delivery path, give Missouri Board for Architects, Professional Engineers, Professional Land Surveyors and Professional Landscape Architects (APELSLA) a written description of the proposed UAS-derived product, its stated accuracy, and whether it will establish or certify boundaries, elevations, or authoritative locations. Ask the board to confirm the applicable license, responsible-charge, certification, or exemption path and retain the response with the project quality plan; the research packet does not establish a UAS-specific turnaround time.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Absent UAS-specific board guidance, rely on the general 20 CSR 2030-20 framework and document licensed-professional review in the QA/QC record; consider a direct inquiry to APELSLA for novel UAS-derived-product certification questions.
### Executive Orders, Court Decisions, and Attorney General Opinions
*Categories reviewed — none located*

**Objective Summary:** No Missouri governor's executive order specifically addressing UAS, no state court decision directly interpreting a UAS statute, and no Attorney General opinion directly involving UAS were located in this research pass. Missouri police drone use is reported to be governed largely by ordinary Fourth Amendment doctrine and individual agency policy rather than a body of state UAS case law.

**Practical Interpretation**

- **AEC Industry UAS Expert:** No executive-order- or case-law-driven requirement to track separately from the statutes already covered.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** The absence of interpretive case law is a source of residual uncertainty around how broadly Missouri courts might read terms like "property line" or "contact" in the enacted statutes — this favors a conservative operational buffer around covered facilities until case law develops.
## 4. Confidence Summary

| Finding | Confidence |
|---|---|
| RSMo 577.800, current merged text (2026-08-06 retrofit) | High — full current text independently re-pulled directly from the Revisor of Statutes, resolving a prior site-update-lag concern |
| RSMo 569.086 critical-infrastructure-facility definition | High — pulled directly; note its own amended list is not effective until Aug. 28, 2026 |
| Peace-officer counter-UAS mitigation authority (reported in the same 2026 act) | Unresolved — reported by multiple press sources; specific codified section not independently located in this pass |
| RSMo 217.850 correctional-center restriction (2026-08-06 retrofit) | High — full current text independently re-pulled; unamended since 2020, escape-facilitation felony tier and FAA-waiver exemption added to the record |
| "Preserving Freedom from Unwarranted Surveillance Act" is not enacted law | Moderate — bill history re-confirmed 2026-08-06 via house.mo.gov-sourced tracking; no 2026 reintroduction found |
| HB 210 (2025) died, not enacted | Moderate — status re-confirmed 2026-08-06 via house.mo.gov-sourced tracking; no 2026 reintroduction found |
| MoDOT UAV Program | High — re-confirmed 2026-08-06 directly from MoDOT's own webpage |
| MoDOT federal foreign-drone notice | High — re-confirmed 2026-08-06 directly from MoDOT's published notice; narrowed to the FHWA-specific funding it addresses |
| DNR State Parks commercial-use approval process | High — re-confirmed 2026-08-06 directly from the primary agency page |
| MDC conservation-area permit and Wildlife Code drone rules | High — re-confirmed 2026-08-06 via MDC's own page; full 3 CSR 10-7.410 regulatory text itself still not independently re-parsed |
| APELSLA UAS-specific guidance | Low — re-confirmed 2026-08-06; still none located beyond general licensing regulation |
| Executive orders / court decisions / AG opinions | Low — re-confirmed 2026-08-06; none located; absence is not confirmation none exists |

*This document is objective legal/regulatory summary plus labeled practical interpretation. It is not legal advice; consult Missouri counsel for project-specific compliance determinations. Local and tribal UAS considerations are out of scope for this phase per current research instructions. Retrofitted 2026-08-06 under Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md` — see `MO_UAS_Research_Manifest.yaml` and `MO_UAS_Research_Checklist.md` for the full retrofit record.*
