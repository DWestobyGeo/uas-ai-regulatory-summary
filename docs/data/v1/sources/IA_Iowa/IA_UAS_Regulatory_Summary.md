# Iowa — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 2, 2026 | **Version:** 2.1 (Phase 2 — subjective-scope audit complete August 2, 2026)
**Model / checkpoint:** Claude Sonnet 5 (research and drafting)
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent Instructions v6, Amendment 2), this summary covers Iowa **state and state-agency** UAS authorities only — municipal and county ordinances are deferred. **No statewide statute preempting local UAS ordinances was located for Iowa.** In practice, Iowa cities appear to have declined to adopt standalone drone ordinances, and the Iowa League of Cities (a non-authoritative municipal advisory association) advises member cities to consult the FAA before doing so — but this is custom and advisory guidance, not a preemption statute. Full citations and metadata are in `IA_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Iowa's actual enacted UAS-specific statutory scheme is materially narrower than most secondary drone-law sources describe, and one of this pass's principal findings is a citation correction on that point (see Section 3). Iowa's earliest UAS law, 2014's House File 2289, was substantially stripped by the Senate before passage: only two operative sections survived — §321.492B, barring the state or a political subdivision from using a UAV for traffic law enforcement, and §808.15, making UAV-derived information inadmissible as evidence absent a search warrant or other lawful basis. The bill's proposed Chapter 708C — a UAV weaponization ban, a state-agency image-capture/search-warrant regime, and a companion amendment to the stalking statute — was never enacted and does not exist in current Iowa law, notwithstanding its frequent appearance in secondary drone-law aggregator sites. Iowa's most substantively important current UAS statute is Chapter 715E ("Remotely Piloted Aircraft"), enacted in 2024 (H.F. 572) and expanded in 2025 (S.F. 491): it makes it a misdemeanor to fly a drone over another's "homestead" or "farmstead" (now defined as 40+ contiguous acres generating at least $15,000 annually in farm-commodity sales) without consent, with enhanced penalties where the drone carries a "surveillance device." Critically for AEC work, §715E.6 expressly exempts commercial or agricultural UAS use conducted in compliance with FAA regulations, authorizations, or exemptions, as well as any flight above 400 feet AGL — an exemption broader than comparable statutes in some other states reviewed in this program. Separately, §719.9 (2018) bars UAV operation in, on, or above a correctional or detention facility, again with an express commercial-use-in-FAA-compliance exemption. Iowa's DNR construes its long-standing "hunting from aircraft" statute (§481A.120) to include drones via its own hunting-regulations guidance, though the statute's text does not itself say so. No UAS-specific DNR state-park/land administrative rule, no Iowa DOT UAS-specific policy beyond a page of FAA resource links, no Attorney General opinion, no court decision, no state-agency UAS procurement/manufacturer restriction, and no UAS-specific professional-licensing-board guidance were located.

## 2. Statewide UAS Laws and Regulations

### Unmanned Aerial Vehicle — Information — Admissibility — Iowa Code §808.15
*Binding law | Current, 2014 Acts, ch. 1111, §2*

**Objective Summary:** Provides that information obtained through the use of an unmanned aerial vehicle is not admissible as evidence in a criminal or civil proceeding unless obtained pursuant to the authority of a search warrant, or otherwise obtained in a manner consistent with state and federal law. This is an evidentiary rule; it does not itself authorize, restrict, or license UAV operation by any person or agency, and does not directly regulate private/commercial UAS operators.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Add this restriction to the state preflight screen, brief the field crew on the prohibited conduct, and identify a stop-work or escalation point. Document any exception relied upon rather than assuming Part 107 authority resolves the state requirement.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat the cited authority as a documented compliance gate where applicable. Preserve the facts supporting any exception or consent theory, allocate client and operator responsibilities clearly, and seek state counsel when project facts approach ambiguous or penal language.
### Use of Unmanned Aerial Vehicle for Traffic Law Enforcement Prohibited — Iowa Code §321.492B
*Binding law | Current, 2014 Acts, ch. 1111, §1*

**Objective Summary:** Prohibits the state or a political subdivision of the state from using an unmanned aerial vehicle for traffic law enforcement. The section is narrow — it contains no definitions, exceptions, or independent penalty provision — and governs only this one specific government use case.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Use the statewide rule as the regulatory baseline, while separately screening site-control rules and any local authority preserved by the preemption provision. Record that jurisdictional check in the project flight-planning package.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the applicability analysis and any exception relied upon in the project file. Align the scope, client representations, and operator procedures with the verified authority, and seek state counsel if material facts fall outside its clear terms.
### Remotely Piloted Aircraft — Intrusion, Surveillance, Injunctive Relief, and Exceptions — Iowa Code ch. 715E (§§715E.1–.6)
*Binding law | Current, originally 2024 Acts ch. 1131 (H.F. 572); expanded by 2025 Acts ch. 56 (S.F. 491)*

**Objective Summary:** Makes it an offense to knowingly fly a remotely piloted aircraft over another's "homestead" (a principal residence outside city limits, plus up to 400 feet of surrounding land) or over a "farmstead" (at least 40 contiguous acres used for farming, generating at least $15,000 annually in farm-commodity sales) within 400 feet of a farm animal, farm equipment, or farm structure, without the owner's or lessee's consent (§§715E.3–.4). Flying without a surveillance device is a simple misdemeanor ("intrusion"); flying equipped with a device capturing an identifiable image, sound, or data is a serious misdemeanor ("surveillance"); both are enhanced on repeat conviction. The property owner or lessee may petition for a temporary injunction (up to two years, renewable) plus costs and attorney fees, and a court generally must order destruction of unlawfully obtained recordings, subject to defined ownership-interest exceptions (§715E.5). Section 715E.6 exempts, among others: a person with the owner's/lessee's consent; **a person operating "for a commercial or agricultural use in compliance with Federal Aviation Administration regulations, authorizations, or exemptions"**; a person flying more than 400 feet above the earth's surface; government agencies at any level; public utilities; and railroad companies. Originally enacted in 2024 protecting only a narrower "secured farmstead" (an animal feeding operation plus 400 feet); broadened in 2025 to the current 40-acre/$15,000 "farmstead" definition.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Design acquisition and data-handling workflows to minimize unnecessary capture of people and private activity. Confirm the source-supported consent or project-purpose basis before flight and carry that limitation through processing, access control, retention, and delivery.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** This authority governs a public entity rather than private operators directly. Review the solicitation and contract for incorporation or flow-down before treating it as binding on the consultant, and document the basis for that conclusion.
## 3. State Agency and Facility-Specific UAS Requirements

### Use of Unmanned Aerial Vehicle — Prohibitions (Correctional and Detention Facilities) — Iowa Code §719.9
*Binding law | Current, 2018 Acts, ch. 1168, §20*

**Objective Summary:** Makes it a class "D" felony to knowingly operate a UAV in, on, or above a county jail, municipal holding facility, secure juvenile detention facility, community-based correctional facility, or Iowa Department of Corrections institution — or its contiguous surrounding grounds — unless the UAV is operated by a law enforcement agency or the operator has permission from the authority in charge of the facility. Subsection 3 expressly exempts a UAV "operating for commercial use in compliance with federal aviation administration regulations, authorizations, or exemptions."

**Practical Interpretation**

- **AEC Industry UAS Expert:** Screen the project map for protected facilities and active emergency operations before dispatch. Establish conservative stand-off and escalation points, brief the crew on the applicable restriction, and document any source-supported authorization before entering the affected area.
- **Agency Practitioner:** Contact the facility authority identified by Iowa General Assembly before mobilization; do not treat client access or a general work order as the required UAS approval. Ask for the current written-authorization route, security review, notice period, required crew and aircraft information, and on-site coordination conditions, and retain the issued authorization.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat the cited authority as a documented compliance gate where applicable. Preserve the facts supporting any exception or consent theory, allocate client and operator responsibilities clearly, and seek state counsel when project facts approach ambiguous or penal language.
### Hunting from Aircraft Prohibited — DNR Construction Applying the Statute to Drones — Iowa Code §481A.120
*Binding law (statute) with supplemental agency guidance | Current, statute most recently amended 2022; DNR guidance reflects the 2025-26 hunting season*

**Objective Summary:** Iowa Code §481A.120 prohibits intentionally killing, wounding, attempting to kill or wound, or pursuing an animal, fowl, or fish from or with an "aircraft in flight" or a snowmobile. The statutory text does not itself define "aircraft" to include a drone. The Iowa DNR's own "2025-26 Iowa Hunting, Trapping & Migratory Game Bird Regulations" booklet states, under a "DRONES" heading, that "drones are considered aircraft by the U.S. Federal Government" and that "the use of drones while hunting is not allowed," and separately restates the prohibition as reaching hunting "from or with an aircraft or drone in flight." The booklet itself discloses that it is "not a complete list of all hunting regulations or laws, nor is it a legal document."

**Practical Interpretation**

- **AEC Industry UAS Expert:** Plan environmental and mapping flights to avoid conduct that could be characterized as locating, pursuing, disturbing, or harassing wildlife. Coordinate mission timing and stand-off distances with the land manager when project work overlaps sensitive habitat or hunting activity.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat the cited authority as a documented compliance gate where applicable. Preserve the facts supporting any exception or consent theory, allocate client and operator responsibilities clearly, and seek state counsel when project facts approach ambiguous or penal language.
### Professional Licensing — Iowa Land Surveyors Statute (Iowa Code §542B.2(10))
*Binding general regulation | No UAS-specific board guidance located*

**Objective Summary:** Defines the "practice of land surveying" to include consultation, investigation, evaluation, planning, mapping, and interpreting reliable scientific measurements relative to property boundaries — including geodetic surveying and the creation or modification of GIS/LIS electronic data relative to those activities — performed under licensure. The definition is method-neutral and does not reference photogrammetry, LiDAR, or UAS by name. No standalone rule, advisory opinion, or FAQ from the Iowa Engineering and Land Surveying Examining Board specifically addressing UAS-derived mapping products was located.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Classify the intended UAS-derived deliverable before mobilization and place licensed-professional review where the verified authority requires it. Keep flight acquisition, analysis, and final professional deliverable responsibilities explicit in the project workflow.
- **Agency Practitioner:** Before relying on an unlicensed or exempt delivery path, give Iowa Engineering and Land Surveying Examining Board / Iowa Department of Inspections, Appeals, and Licensing a written description of the proposed UAS-derived product, its stated accuracy, and whether it will establish or certify boundaries, elevations, or authoritative locations. Ask the board to confirm the applicable license, responsible-charge, certification, or exemption path and retain the response with the project quality plan; the research packet does not establish a UAS-specific turnaround time.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Describe this source as guidance or policy, not a generally binding statute. Check whether the client or property owner incorporates it contractually, preserve the version relied upon, and escalate conflicts with controlling authority.
### Executive Orders, AG Opinions, Court Decisions, Procurement, Preemption, and Related Negative/Discrepancy Findings
*Categories reviewed — no dispositive UAS-specific authority located; one material historical citation discrepancy documented*

**Objective Summary:** No Iowa Governor executive order, Iowa Attorney General opinion, or Iowa appellate/Supreme Court decision directly addressing UAS was located. No Iowa-specific state-agency UAS procurement, approved-manufacturer, or country-of-origin restriction beyond the federal American Security Drone Act framework was located. No statewide statute preempting local UAS ordinances was located. Iowa DNR's state-park/recreation-area public-use administrative rule (571 IAC 61.10) was reviewed directly in full and contains no aircraft- or UAV-specific provision. The Iowa DOT's "Uncrewed Aircraft Systems" webpage links to FAA resources (Part 107 certification, B4UFLY, a controlled-airspace map, a waiver webinar series) but imposes no independent state requirement. Iowa's critical-infrastructure sabotage statute (Iowa Code §§716.11–.12) contains no UAS-specific text and reaches a UAV only where it is the instrument of an actual, overt sabotage act; it is excluded from the source register under this project's non-UAS scope gate. **Citation-discrepancy finding:** numerous secondary drone-law sites describe a current Iowa Code §708C.1 imposing a UAV weaponization ban and a state-agency image-capture/search-warrant regime. Direct review of the enrolled/chaptered text of the 2014 enacting act (House File 2289, 2014 Acts ch. 1111, approved May 23, 2014) confirms the Senate struck the bill's proposed Chapter 708C — including the weaponization ban and a companion stalking-statute amendment — before passage; only §321.492B, §808.15, and an uncodified Department of Public Safety study directive were actually enacted. A direct query of the Iowa Legislature's current (2026) Code section listing for chapter 708C returned zero sections, confirming the chapter does not exist in current law.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat this record as a research flag, not an operator requirement. Do not change field procedures unless a current controlling source confirms the issue; route any project-specific uncertainty to the identified agency or counsel.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** No current state equipment restriction is established by this research result. Do not treat that absence as permanent; check current solicitation terms, client policies, and independently applicable federal restrictions before committing a fleet to the work.
- **AEC Industry Legal Counsel:** Do not present this negative or unresolved research result as a legal conclusion. Preserve the research limitation, verify current authority for the specific project, and escalate only if the issue could materially affect scope, access, or liability.
## 4. Non-Regulatory Context

*The items below are drawn from news and secondary reporting, not primary legal authority. They are provided for situational awareness only and are not part of the verified source register.*

- **Iowa Senate advances bill to strengthen rules against drones over farmland, Iowa Capital Dispatch, March 17, 2025.** Reports the Iowa Senate's 46-3 passage of Senate File 491, broadening the 2024 "secured farmstead" drone restriction to a 40-acre/$15,000-farm-commodity-sales "farmstead" definition, following testimony that drones were being used to surveil livestock and dog-breeding facilities and that farmers viewed unauthorized drone flights as a privacy and animal-welfare concern. Directly relevant to AEC UAS programs planning rural or agricultural-corridor work, since it explains the policy background for the current §715E "farmstead" definition (IA-003). [Source](https://iowacapitaldispatch.com/briefs/iowa-senate-advances-bill-to-strengthen-rules-against-drones-over-farmland/)
- **Unauthorized drone 'surveillance' of Iowa farmsteads to be outlawed, Mix 94.7 KMCH, May 8, 2025.** Reports Governor Kim Reynolds' May 6, 2025 signing of Senate File 491, effective July 1, 2025, and summarizes the bill's 400-foot buffer around farm animals, equipment, and structures. Confirms the current effective date and signing details for the §715E amendment relied on in IA-003. [Source](https://www.kjan.com/index.php/2025/05/unauthorized-drone-surveillance-of-iowa-farmsteads-to-be-outlawed/)
- **Iowa Governor Reynolds Signs Law Prohibiting the Use of Drones, Dubuque In Pursuit News, May 4, 2024.** Reports Governor Reynolds' May 3, 2024 signing of House File 572 (2024 Acts ch. 1131), the original enactment creating Chapter 715E's homestead/secured-farmstead drone restrictions, effective July 1, 2024. Useful for confirming the enactment timeline underlying IA-003's original (pre-2025-amendment) provisions. [Source](https://dubuqueinpursuitnews.com/2024/05/04/iowa-governor-reynolds-signs-law-prohibiting-the-use-of-drones/)

## 5. Unresolved Operational Questions

- **§715E.6 commercial/agricultural exemption — outer bounds:** The exemption for commercial or agricultural UAS use "in compliance with Federal Aviation Administration regulations, authorizations, or exemptions" is the single most important AEC-relevant provision in Iowa's current UAS law, but its outer bounds (e.g., a Part 107 commercial flight for a non-agricultural purpose, such as a utility or transportation corridor survey, that nonetheless passes within 400 feet of a farmstead) have not been construed by any Iowa court or agency as of this research date. Confirm scope directly with Iowa counsel for a specific flight plan near a farmstead or homestead.
- **§481A.120 "drone" construction:** The DNR's hunting-regulations booklet construes the statutory term "aircraft" to include drones, but this construction appears only in non-codified agency guidance (which itself disclaims being a complete or legally authoritative statement of the law), not in the statute or an administrative rule. Relevance to AEC work is limited (wildlife-survey/agricultural-monitoring UAS flights during hunting seasons), but the legal weight of the DNR's construction, if contested, is unresolved.
- **Iowa Code §708C.1 — non-enactment:** As detailed in Section 3 above, this citation — appearing across numerous secondary drone-law sources — describes a UAV weaponization ban and state-agency search-warrant/reporting regime that was stricken from House File 2289 before its 2014 passage and does not exist in current Iowa law. Treat any secondary-source reference to "Iowa Code §708C.1" as describing an unenacted 2014 bill provision, not current law.
- **General trespass/surveillance-device statutes (Iowa Code §§727.8, 727.8A):** These general (non-UAS-specific) statutes criminalize using a surveillance device to observe, photograph, or eavesdrop where a person has an expectation of privacy, or using such a device while committing a trespass. No official source was located expressly applying either section to a UAV-mounted camera; they were excluded from the source register on that basis under the project's scope gate, but may be relevant background if a specific fact pattern is litigated.
- **State preemption of local ordinances:** No statewide preemption statute was located, and no Iowa city is reported to have adopted a standalone drone ordinance as of this research date; the Iowa League of Cities' advisory guidance (encouraging FAA consultation before any local ordinance) is persuasive custom, not binding law. AEC firms should still confirm the absence of a local ordinance for any specific Iowa project site, since this is a Phase 1, state-level-only pass.

## 6. Confidence Summary

| Finding | Confidence |
|---|---|
| Iowa Code §808.15 (UAV evidence-admissibility / search-warrant linkage) | High — verified directly against the Iowa Legislature's official Iowa Code PDF |
| Iowa Code §321.492B (UAV traffic-law-enforcement prohibition) | High — verified directly against the Iowa Legislature's official Iowa Code PDF |
| Iowa Code ch. 715E, §§715E.1–.6 (homestead/farmstead intrusion, surveillance, exceptions) | High — full current text of each section verified directly; 2024 and 2025 enactment/amendment history corroborated by independent news reporting |
| Iowa Code §719.9 (correctional-facility UAV prohibition, with commercial exemption) | High — verified directly against the Iowa Legislature's official Iowa Code PDF |
| Iowa Code §481A.120 (hunting-from-aircraft restriction) and DNR drone construction | Moderate — statute verified High directly; the drone-inclusive construction rests on DNR guidance, not codified rule text |
| Iowa Code §542B.2(10) (professional land surveying framework) | Low — general framework verified directly, but no UAS-specific board guidance located |
| Executive orders / AG opinions / court decisions / procurement / preemption / DNR park rule / DOT UAS page (negative findings) | Moderate (each individually reviewed and confirmed absent) to Low (negative research findings, not a comprehensive negative-search confirmation) |
| Iowa Code §708C.1 non-enactment (citation-discrepancy finding) | High — independently confirmed via the enrolled/chaptered 2014 bill text and a zero-result query of the current Code's chapter 708C section listing |

*This document combines objective legal/regulatory summaries with Phase 2 Practical Interpretation content, which is AI-generated operational opinion and not legal advice. Consult Iowa counsel for project-specific compliance determinations. Local ordinances and tribal UAS considerations are out of scope for this phase per current research instructions.*
