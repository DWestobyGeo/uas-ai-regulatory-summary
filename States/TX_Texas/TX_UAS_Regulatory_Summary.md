# Texas — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 1, 2026; Workstream 9 retrofit August 6, 2026 | **Version:** 2.2 (Workstream 9 retrofit — corrected TX-007, TX-010, TX-013 citations; re-confirmed all other records)
**Model / checkpoint:** Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet.
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent Instructions v6), this summary covers Texas **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase and are not included here. Texas Government Code § 423.009 (covered below) broadly preempts local UAS ordinances, which narrows the practical significance of that deferral. Full citations and metadata are in `TX_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Texas regulates UAS primarily through the "Texas Privacy Act" (Government Code Chapter 423, enacted 2013) and a set of Penal Code facility-protection offenses. Chapter 423 combines a criminal surveillance-image restriction (§ 423.003) with 21 statutory exceptions (§ 423.002) — including dedicated exceptions for licensed land surveyors and professional engineers — plus no-fly restrictions over critical infrastructure (§ 423.0045) and large sports venues (§ 423.0046). The Fifth Circuit upheld Chapter 423's core provisions against a facial First Amendment challenge in 2023. Separate Penal Code sections added in 2023 and 2025 protect correctional/detention facilities (§ 38.115) and airports, military installations, and spaceports (§ 42.15) — the spaceport provision (added by S.B. 1197, eff. Sept. 1, 2025) carries a Class B misdemeanor penalty (Class A on repeat conviction), independently confirmed against the official Senate Research Center bill analysis. Texas broadly preempts local UAS ordinances (§ 423.009), so this state-level picture is largely the whole picture for most Texas AEC work. State agencies (TPWD, TxDOT) maintain their own UAS-relevant permit and program requirements, and a gubernatorial executive directive restricts specified foreign-manufactured UAS hardware (including DJI and Autel) on state-owned devices and networks.

## 2. Statewide UAS Laws and Regulations

### Tex. Gov't Code § 423.002 — Nonapplicability (lawful image-capture exceptions)
*Binding law | Current*

**Objective Summary:** Lists 21 circumstances in which capturing an image by UAS is lawful notwithstanding § 423.003, including images captured with the property owner's/occupant's consent (¶6); by a registered professional land surveyor in connection with professional surveying, provided no individual is identifiable (¶19); by a licensed professional engineer in connection with the practice of engineering, provided no individual is identifiable (¶20); by or for a utility or telecommunications provider for operations, maintenance, inspection, vegetation management, or routing/siting (¶5); of public real property or a person on it (¶15); and from 8 ft or less above ground level in a public place without image-amplifying equipment (¶14). Does not apply to UAS manufacture, assembly, distribution, or sale.

**Practical Interpretation**

- **AEC Industry UAS Expert:** The PLS exception (¶19) and PE exception (¶20) are the most directly relevant carve-outs for AEC survey/engineering work, but both require that no individual be identifiable in the captured image — plan flight paths and processing workflows accordingly on any project with people present in frame.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** These exceptions are narrower than general Part 107 commercial authority — they require the activity be "in connection with the practice of" surveying or engineering as statutorily defined. For work that doesn't cleanly fit a licensed-practice exception, document reliance on property-owner consent or another applicable exception instead.
### Tex. Gov't Code § 423.003 — Offense: Illegal Use of Unmanned Aircraft to Capture Image
*Binding law | Current — upheld against facial constitutional challenge*

**Objective Summary:** A person commits a Class C misdemeanor by using a UAS to capture an image of an individual or privately owned real property with intent to conduct surveillance on the individual or property. It is a defense that the person destroyed the image as soon as they knew it was captured in violation of the section, without disclosing, displaying, or distributing it. Upheld against a facial First Amendment challenge in *National Press Photographers Ass'n v. McCraw* (5th Cir. 2023) (see Section 3 below).

**Practical Interpretation**

- **AEC Industry UAS Expert:** The offense turns on intent to surveil, not merely capturing an image that happens to include private property — routine AEC aerial mapping is not the targeted conduct, but avoid deliberately orbiting on or lingering over neighboring private property or individuals outside the survey scope without an applicable exception or the owner's consent.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** This is a criminal, intent-based statute — keep flight logs and mission-purpose documentation that establish a flight's professional purpose. The Fifth Circuit rejected only a facial challenge and expressly left as-applied First Amendment defenses open, so this is not fully settled as to every fact pattern.
### Tex. Gov't Code § 423.0045 — Offense: Operation of Unmanned Aircraft Over Critical Infrastructure Facility
*Binding law | Current, last amended 2023*

**Objective Summary:** Prohibits intentionally/knowingly operating a UAS at or below 400 ft AGL over a defined "critical infrastructure facility" (refineries; power generation/switching facilities; chemical/polymer/rubber plants; water/wastewater facilities; gas compressor stations; LNG terminals; telecom switching offices; ports/rail yards/freight terminals; gas processing plants; broadcast transmission facilities; electric-arc steelmaking facilities; TCEQ high-hazard dams; concentrated animal feeding operations; and, if fenced, pipelines, drill sites, tank batteries, production facilities, wellheads, and active-flare oil/gas facilities), or allowing contact with or interference/disturbance of the facility. Facilities generally must be fenced/barricaded or clearly posted. Exemptions include a broad commercial-operator exemption (§(c)(5)) for UAS operated for a commercial purpose in compliance with applicable FAA rules and authorizations, the facility owner/operator and its contractors, and persons with the facility's prior written consent. Class B misdemeanor, enhanced to Class A on a prior conviction under this section or § 423.0046.

**Practical Interpretation**

- **AEC Industry UAS Expert:** The commercial-operator exemption is broad — Part 107 compliance plus required FAA authorizations generally suffices to fly a covered facility for legitimate commercial work without separate facility consent, but the facility itself still controls site access and safety, so coordinate directly with the owner/operator regardless.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document FAA Part 107 compliance and any required FAA authorization for flights over an enumerated facility, since the commercial exemption is what most AEC operators will rely on; retain this documentation given the misdemeanor exposure.
### Tex. Gov't Code § 423.0046 — Offense: Operation of Unmanned Aircraft Over Sports Venue
*Binding law | Current*

**Objective Summary:** Prohibits intentionally/knowingly operating a UAS at or below 400 ft AGL over a sports venue (arena, racetrack, coliseum, stadium, or similar) with a seating capacity of 30,000 or more used primarily for sports/athletics events. Exemptions mirror § 423.0045, including the FAA-compliant commercial-operator exemption. Class B misdemeanor, enhanced to Class A on a prior conviction under this section or § 423.0045.

**Practical Interpretation**

- **AEC Industry UAS Expert:** The 30,000-seat threshold excludes most mid-size and small venues — confirm actual capacity before treating a project site as covered, but coordinate with venue management regardless given event-day TFRs and independent safety considerations.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Apply the same FAA-compliance documentation practice used for critical-infrastructure work, and obtain the venue's written consent where practical even though not strictly required by the exemption.
### Tex. Gov't Code § 423.009 — Regulation of Unmanned Aircraft by Political Subdivision (state preemption)
*Binding law | Current*

**Objective Summary:** A political subdivision (county, joint transportation board, or municipality) may not adopt or enforce any ordinance, order, or similar measure regulating UAS operation, except: (1) regulation of UAS use during a defined "special event"; (2) the subdivision's own UAS use; or (3) regulation of UAS near the subdivision's own facility or infrastructure, and only with FAA authorization and a public hearing after reasonable notice. A measure violating the general prohibition is void and unenforceable.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Texas's broad state preemption means AEC operators generally should not expect a patchwork of municipal/county drone rules on top of state law — but confirm whether a project site falls within a subdivision's own facility/infrastructure or a properly authorized special-event zone.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** A local ordinance purporting to independently regulate UAS operation outside the three statutory exceptions is void by operation of state law, but confirm this on a project-specific basis and don't assume it displaces facility-level access, trespass, or generally applicable safety rules.
### Tex. Penal Code § 38.115 — Operation of Unmanned Aircraft over Correctional Facility or Detention Facility
<span class="news-anchor" data-record-id="TX-006" hidden></span>
*Binding law | Current, enacted 2023*

**Objective Summary:** Prohibits intentionally/knowingly operating a UAS at or below 400 ft AGL over a "correctional facility" (TDCJ facilities, municipal/county jails, federal BOP facilities, or secure juvenile facilities) or "detention facility" (an ICE-contracted immigration detention facility), allowing contact, or interfering with/disturbing operations. Exemptions include government entities and contractors, persons with the facility's prior written consent, and law enforcement and contractors — there is **no** general commercial-operator/FAA-compliance exemption comparable to §§ 423.0045–.0046. Class B misdemeanor, enhanced to Class A on a prior conviction, or a state jail felony if used to introduce contraband.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Identify any correctional or immigration-detention facility near a project site during pre-flight planning; because there is no standalone commercial exemption here, obtain the facility owner/operator's prior written consent before flying at or below 400 ft over or near such a facility.
- **Agency Practitioner:** Contact the protected facility's owner, operator, administrator, commander, or other official identified by the authority before mobilization and ask whether the proposed AEC mission qualifies for written approval or an employment/contractor exception. Provide the site, purpose, dates, flight area, crew and aircraft details the facility requests, and retain the signed authorization and security conditions; do not assume ordinary site access or a client work order is sufficient.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain written consent documentation given the absence of a general commercial exemption and the state-jail-felony exposure if contraband introduction is alleged; confirm facility classification before relying on any exemption.
### Tex. Penal Code § 42.15 — Operation of Unmanned Aircraft over Airport, Military Installation, or Spaceport
*Binding law | Current, amended effective September 1, 2025 to add spaceports — fully re-verified 2026-08-06*

**Objective Summary:** Prohibits intentionally/knowingly operating a UAS over an airport (as defined by Transportation Code § 22.001) or military installation, allowing contact, or interfering with/disturbing operations. Defenses include government entities and contractors, law enforcement and contractors, the facility owner/operator and contractors, a person with prior written or electronic authorization from the owner/operator **or the FAA**, and the property owner/occupant or a person with their consent. Class B misdemeanor, enhanced to Class A on a prior conviction. S.B. 1197 (89th Legislature), signed June 20, 2025 and effective September 1, 2025, amended this section to add "spaceport" (defined by reference to Local Government Code § 507.001) as a third protected facility type; the penalty tier for a spaceport violation remains Class B misdemeanor (Class A on a prior conviction) — independently confirmed via the official Texas Senate Research Center bill analysis, which resolves a conflict in secondary sources where one had mischaracterized the spaceport provision as a state-jail felony.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Directly relevant to any AEC project near a Texas airport — the FAA-authorization defense means a standard Part 107 airspace authorization for controlled airspace near an airport can double as a state-law defense, but confirm the authorization is documented before relying on it.
- **Agency Practitioner:** Contact the protected facility's owner, operator, administrator, commander, or other official identified by the authority before mobilization and ask whether the proposed AEC mission qualifies for written approval or an employment/contractor exception. Provide the site, purpose, dates, flight area, crew and aircraft details the facility requests, and retain the signed authorization and security conditions; do not assume ordinary site access or a client work order is sufficient.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Both the pre-2025 text and the 2025 spaceport amendment are now independently verified against official sources. The penalty for any violation, including the spaceport provision, is a Class B misdemeanor (Class A on a prior conviction) — not a felony; do not rely on secondary sources characterizing the spaceport provision as a state-jail felony.
### *National Press Photographers Ass'n v. McCraw*, 90 F.4th 770 (5th Cir. 2023)
<span class="news-anchor" data-record-id="TX-008" hidden></span>
*Court decision | Current — facial challenge rejected*

**Objective Summary:** The Fifth Circuit reversed a district-court ruling that had enjoined several Chapter 423 provisions, holding that plaintiffs' facial First Amendment challenge to the surveillance-image, critical-infrastructure, sports-venue, and correctional-facility provisions failed, and remanded with instructions to enter judgment for the state defendants. The court also affirmed dismissal of a related federal field-preemption claim. The panel did not foreclose future as-applied First Amendment challenges.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Chapter 423's core AEC-relevant provisions are currently enforceable statewide and were not struck down — plan operations accordingly rather than assuming litigation has suspended the statute.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** The ruling addressed only a facial challenge and left as-applied challenges open; this doesn't change the practical compliance posture for routine commercial operations, but track any future as-applied litigation affecting the AEC-relevant provisions.
## 3. State Agency UAS Requirements

### Parks and Wildlife — Texas Parks and Wildlife Department (Aerial Management Permit / wildlife-related UAS use)
*Binding administrative regulation*

**Objective Summary:** Except under a TPWD-issued Aerial Management Permit (AMP) with an approved Land Owner Authorization (LOA), 31 TAC § 65.152 makes it unlawful to use a UAS to count, photograph, relocate, capture, hunt, or take wildlife or exotic animals, implementing the state framework under the federal Airborne Hunting Act. Recreational/sport-hunting aircraft-assisted pursuit is not permitted; a hunter may act as an AMP sub-agent for feral hog and coyote take. Violation may be a Class A misdemeanor and/or a federal Airborne Hunting Act violation. *(Codified text of § 65.152, including its UAV-specific feral-hog-locating carve-out, independently re-verified 2026-08-06 against Cornell Law School's Legal Information Institute mirror of the Texas Administrative Code.)*

**Practical Interpretation**

- **AEC Industry UAS Expert:** Plan environmental-monitoring or habitat-mapping flights to avoid counting, identifying, or photographing wildlife within the rule's meaning; obtain an AMP and LOA first if a project specifically requires wildlife documentation.
- **Agency Practitioner:** Contact Texas Parks and Wildlife Department before fixing the mobilization date and ask for the current application or approval route, supporting-document checklist, fees, and processing estimate. Describe the proposed site, dates, purpose, aircraft, operator, and requested exception clearly, and retain the issued approval and all conditions; the captured requirement is: Yes — Aerial Management Permit (AMP) plus an approved Land Owner Authorization (LOA).
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the AMP/LOA permit chain for any UAS work with a wildlife-survey purpose; the rule's breadth warrants a conservative read for any project scope including wildlife documentation.
### Parks and Wildlife — Texas Parks and Wildlife Department (State Park launch/land/operate authorization)
*Official agency policy under general administrative-rule authority — citation corrected 2026-08-06*

**Objective Summary:** TPWD's own current Park Rules page states that drones are allowed in Texas state parks only in two circumstances: (1) a designated area at Martin Dies, Jr. State Park, or (2) with a filming permit obtained from the specific park. Outside those two circumstances, UAS launch/land/operate is not permitted. This is TPWD agency policy exercised under the director's general authority (31 TAC § 59.132(a)) to restrict activity in a state park; a violation of §§ 59.132–59.134 is a Class C misdemeanor per § 59.136 — **not** the Class A misdemeanor/$4,000 fine claimed by a previously-cited secondary source. **Correction:** the previously-cited § 59.134 was independently re-pulled in full and contains no UAS/drone provision whatsoever; no dedicated numbered TAC rule for drones was located. Prior public reporting naming San Angelo and Lake Whitney State Parks as additional designated RC-aircraft zones was not corroborated by TPWD's current Park Rules page (which names only Martin Dies, Jr. State Park) and should be treated as unconfirmed pending direct TPWD confirmation.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Build superintendent-authorization lead time into scheduling for any state-park-adjacent work; FAA Part 107 authority alone does not permit launch or landing within park boundaries. Confirm with the specific park whether a filming permit — TPWD's own stated mechanism — is the correct route, rather than relying on a specific TAC section number, since none currently codifies the restriction.
- **Agency Practitioner:** Start with the site manager or permitting office for Texas Parks and Wildlife Department before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Do not cite "31 TAC § 59.134" as the source of the drone restriction — the current text of that section contains no UAS/drone provision at all. Cite TPWD's own Park Rules page as the operative source, exercised under the director's general § 59.132(a) authority, and note that the penalty for violating §§ 59.132–59.134 is a Class C misdemeanor (§ 59.136), not a Class A misdemeanor/$4,000 fine as a prior secondary source claimed.
### Transportation — Texas Department of Transportation (UAS Flight Operations and User's Manual)
*Official agency policy (contractually mandatory for TxDOT-scoped work)*

**Objective Summary:** TxDOT operates a centralized UAS program requiring a flight plan, a completed Project Risk Assessment (PRA), appropriate liability insurance, and (project-dependent) pre-approval from the TxDOT UAS Coordinator. All UAS operations performed for TxDOT must comply with the current Manual (dated April 1, 2023) and the applicable Traffic Control Plan for survey operations; a current FAA Part 107 certificated Remote Pilot in Command is required. TxDOT's separate aerial-mapping specification calls for a minimum 5 cm ground sampling distance for 2D planimetric mapping. TxDOT's current UAS Services page (re-confirmed 2026-08-06) additionally requires FAA Remote ID-compliant aircraft registration and confirmation that equipment does not appear on the DIR/Texas Cyber Command Prohibited Technologies List (see below).

**Practical Interpretation**

- **AEC Industry UAS Expert:** Obtain and follow the current Manual and relevant Traffic Control Plan before mobilizing on any TxDOT-scoped task order, and confirm whether PRA and UAS Coordinator pre-approval are required.
- **Agency Practitioner:** For work subject to this policy, contact the agency project manager and Texas Department of Transportation before fixing the mobilization date. Submit the proposed aircraft and payload configuration, operator credentials, flight purpose and location, insurance evidence, and any federal authorization the agency requests; retain the agency's confirmation and project-specific conditions.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Confirm in the scope of work whether the Manual's standards are incorporated as binding contract requirements, and retain the completed PRA and insurance documentation in the project file.
### Procurement / Cybersecurity — Prohibited Technologies List (Office of the Governor / Texas Cyber Command)
<span class="news-anchor" data-record-id="TX-012" hidden></span>
*Official agency policy (executive-branch directive) — state-agency and state-device scope*

**Objective Summary:** Pursuant to gubernatorial directives (originating December 2022, updated January 26, 2026, now administered by the Texas Cyber Command), the Department of Information Resources publishes a Prohibited Technologies list barring specified hardware/manufacturers from state-owned devices and networks. As of the February 4, 2026 published update (independently re-confirmed 2026-08-06 directly from DIR's website), the hardware list explicitly includes SZ DJI Technology Company, Autel Robotics, RoboSense Technology Co. Ltd. (LiDAR), and Wuhan Geosun Navigation Technology Co. Ltd. (LiDAR) — all UAS or UAS-payload manufacturers. An agency head may approve narrow exceptions for law-enforcement or legitimate-use purposes, with notice to the Governor's office and DIR. This is separate from Government Code Chapter 620 (which addresses social-media "Covered Applications," not UAS hardware).

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not assume this restriction reaches firm-owned equipment on non-state-funded work — confirm with the contracting state agency whether a specific task order treats consultant-owned UAS equipment as subject to the agency's own device policy.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Require current vendor documentation for aircraft, critical components, installed software, ownership, origin, and support lifecycle before purchase. Compare the proposed configuration with the controlling authority and preserve the evidence supporting the acquisition decision.
- **AEC Industry Legal Counsel:** Do not represent to a client that Texas law bars private firms from using DJI, Autel, or other listed-manufacturer equipment generally — the restriction is directed at state-owned devices and networks; confirm specific contract language where a state task order may incorporate the agency's policy by reference.
### Professional Licensing — Texas Board of Professional Engineers and Land Surveyors (TBPELS)
*Binding general regulation | No UAS-specific board guidance located | citation corrected 2026-08-06*

**Objective Summary:** TBPELS's rules require a licensed professional engineer (22 TAC § 137.59) or land surveyor (22 TAC § 138.59, the parallel provision following TBPELS's 2019 board merger) to practice only in fields in which they are, by education and/or experience, competent and proficient. **Correction:** the previously-cited "Chapter 663 (Surveyors)" citation is stale — TBPELS's 2019 merger of the former engineering and land-surveying boards (H.B. 1523, 86th Leg.) consolidated the surveyors' standards-of-conduct rules from old Chapter 663 into new Chapter 138. No standalone TBPELS guidance document, advisory, or rule specifically addressing UAS-derived photogrammetry, LiDAR, or mapping products was located during this research pass.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Route UAS-derived photogrammetry/LiDAR mapping products through a Texas-licensed PE or PLS for review under the existing general competency framework before delivery on any official deliverable.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document licensed-professional review and QA/QC of UAS-derived deliverables; consider a direct inquiry to TBPELS for novel UAS-derived-product certification questions.
### Executive Orders, Attorney General Opinions
*Categories reviewed — none UAS-specific located*

**Objective Summary:** No Texas gubernatorial executive order specifically and solely addressing UAS regulation was located (the Prohibited Technologies directive, covered above, addresses UAS hardware only incidentally within a broader foreign-technology security framework). No Texas Attorney General opinion directly involving UAS was located; the Attorney General's office instead defended Chapter 423 as a litigant in *McCraw*, which is reported above as a court decision.

**Practical Interpretation**

- **AEC Industry UAS Expert:** No separate executive-order- or AG-opinion-driven requirement to track beyond the statutes and agency policies already covered.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** No current state equipment restriction is established by this research result. Do not treat that absence as permanent; check current solicitation terms, client policies, and independently applicable federal restrictions before committing a fleet to the work.
- **AEC Industry Legal Counsel:** Absence of a located AG opinion is not confirmation none exists; if a specific interpretive question arises, consider whether an AG opinion has addressed it before relying solely on the statutory text.
## 4. Unresolved Operational Questions

- **§ 42.15 spaceport amendment:** The exact current text of the September 1, 2025 spaceport amendment (S.B. 1197) was not independently re-verified against the codified statute; confirm before relying on specific spaceport-related language for Boca Chica/Starbase-area or other spaceport-adjacent work.
- **31 TAC § 59.134 (state park UAS authorization):** Citation sourced from a secondary legal-summary site rather than independently verified against the Texas Administrative Code; confirm directly with TPWD or the Secretary of State's TAC database before citing the specific section number to a client.
- **TBPELS UAS-specific guidance:** No board-issued UAS-specific guidance was located; this may reflect a genuine regulatory gap rather than a search limitation — a direct inquiry to TBPELS is recommended for novel certification questions involving UAS-derived deliverables.

## 5. Confidence Summary

| Finding | Confidence |
|---|---|
| Gov't Code § 423.002 (nonapplicability/exceptions) | High — verified directly against Justia's codification; re-confirmed 2026-08-06 |
| Gov't Code § 423.003 (surveillance-image offense) | High — verified directly; re-confirmed 2026-08-06 |
| Gov't Code § 423.0045 (critical infrastructure) | High — verified directly, full facility enumeration confirmed; re-confirmed 2026-08-06 |
| Gov't Code § 423.0046 (sports venue) | High — verified directly; re-confirmed 2026-08-06 |
| Gov't Code § 423.009 (local preemption) | High — verified directly; re-confirmed 2026-08-06 |
| Penal Code § 38.115 (correctional/detention facility) | High — verified via Texas.Public.Law republication; re-confirmed 2026-08-06 |
| Penal Code § 42.15 (airport/military/spaceport) | High — pre-2025 text and the 2025 spaceport amendment both independently verified 2026-08-06, including via the official Senate Research Center bill analysis |
| *NPPA v. McCraw* holding | High — confirmed via multiple concurring secondary legal summaries; re-confirmed 2026-08-06 |
| TPWD Aerial Management Permit / wildlife UAS rule | High — confirmed via TPWD's own FAQ page and, as of 2026-08-06, independently re-pulled codified text (31 TAC § 65.152) |
| TPWD state park UAS authorization | Moderate — citation corrected 2026-08-06 (prior "31 TAC § 59.134" citation was verified to contain no drone provision); now grounded in TPWD's own current Park Rules page |
| TxDOT UAS Manual | Moderate — confirmed via TxDOT's own webpage, re-confirmed 2026-08-06; full manual text not independently read |
| Prohibited Technologies List (DIR/Texas Cyber Command) | High — verified directly against DIR's official webpage, re-confirmed 2026-08-06 |
| TBPELS competency rule (22 TAC §§ 137.59, 138.59) | Moderate — citation corrected 2026-08-06 from a stale, superseded Chapter 663 reference; no UAS-specific guidance located |

*This document is objective legal/regulatory summary plus labeled practical interpretation. It is not legal advice; consult Texas counsel for project-specific compliance determinations. Local and tribal UAS considerations are out of scope for this phase per current research instructions.*
