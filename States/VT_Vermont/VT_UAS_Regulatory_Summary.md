# Vermont UAS Regulatory Summary

**Prepared for:** Commercial AEC consultants conducting UAS-supported work in Vermont  
**Research date:** 2026-08-02  
**Version:** 2.0 (Phase 2 — practical interpretation complete)
**Model / checkpoint:** Objective research model retained from Phase 1; Phase 2 interpretations drafted with OpenAI GPT-5 (Codex; exact checkpoint unavailable)
**Scope note:** Statewide and state-agency authorities only. Municipal, county, tribal, federal, land-manager-specific federal, property-specific, site-specific, and live-airspace requirements are outside this summary.

> **Process note:** Objective research is retained from the Phase 1 source packet. The four practical-interpretation roles were completed in Phase 2 on 2026-08-02 using OpenAI GPT-5 (Codex; exact checkpoint unavailable).

## 1. State overview

Vermont's central UAS statutes appear in 20 V.S.A. chapter 205. They require compliance with applicable FAA requirements, regulate law-enforcement drone use and reporting, prohibit knowing overflight of identifiable correctional property subject to commercial and other exceptions, and impose civil penalties for specified private-property surveillance without prior written consent. A separate criminal statute prohibits weaponizing a drone or firing a projectile from it. The private-property law, effective June 6, 2024, is especially relevant to imagery projects because it defines surveillance and creates a reasonable-expectation-of-privacy presumption based on ground-level observability.

For state parks and forests, a January 2025 Department of Forests, Parks and Recreation procedure requires written Commissioner permission in the form of a Special Use Permit or License for covered launch and landing, including commercial operations. Applications receive case-specific resource, use-conflict, liability, safety, insurance, and payment review. Fish and Wildlife rules separately prohibit using drones to take, locate, surveil, drive, or harass wild animals for hunting purposes. No current statewide UAS manufacturer, country-of-origin, or cybersecurity procurement restriction or express UAS preemption provision was located.

## 2. Statewide laws

### VT-001 — State incorporation of FAA requirements

**Authority:** 20 V.S.A. § 4623  
**Status:** Current / in force

Section 4623 provides that any drone use by any person, including a law-enforcement agency, must comply with all applicable FAA requirements and guidelines. It separately states legislative intent that a person using a model aircraft, as defined in the FAA Modernization and Reform Act of 2012, operate according to community-based-organization guidelines such as the Academy of Model Aeronautics safety code. The section creates no separate Vermont commercial UAS registration, pilot credential, or operating permit.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Add Use of drones; Federal Aviation Administration requirements to the mission-specific legal and site screening for Statewide. Brief the crew on the triggering conduct and document the operational boundary or exception relied upon before launch.
- **Agency Practitioner:** N/A — no agency process involved
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Preserve the mission screening and factual basis for compliance with 20 V.S.A. § 4623, including the operating area, purpose, approvals, and any relied-upon exception. Escalate ambiguous scope, conflicting client direction, or facts that could change the regulated party or activity before flight.

### VT-002 — Law-enforcement drone use and data limits

**Authority:** 20 V.S.A. § 4622  
**Status:** Current / in force; public-agency rule

Section 4622 generally prohibits a defined law-enforcement agency, including a person or entity acting for one, from using a drone or drone-acquired information to investigate, detect, or prosecute crime except under stated conditions. Permitted paths include noncriminal purposes such as search and rescue or damage assessment, a Vermont Rule 41 warrant, or a judicially recognized warrant exception. The statute restricts collection outside the surveillance target, limits biometric matching, requires a warrant within 48 hours after exigent use, and makes improperly gathered evidence inadmissible.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This record does not directly regulate an ordinary privately controlled AEC flight, but it can govern a mission performed for or integrated into the named public agency's program. Define in the scope and flight plan who authorizes the mission, controls the aircraft, receives the data, and is responsible for the cited records or use restrictions.
- **Agency Practitioner:** Use the current named facility or administering agency application or request channel and provide the mission description, dates, aircraft, pilot, and requested operating area. The packet identifies the approval as: Rule 41 warrant or a stated alternative is required for covered investigative use. Because the verified source does not establish a dependable review time for every case, confirm completeness, reviewer, lead time, approval duration, and field-contact expectations directly with the agency.
- **UAS Procurement Expert:** Select capture and processing systems that support role-based access, exportable audit logs, configurable retention and deletion, defensible redaction, and delivery in the agency's required format. Confirm cloud hosting, backup replication, account ownership, and vendor deletion behavior before the platform is approved for covered data.
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under 20 V.S.A. § 4622; a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

### VT-003 — Law-enforcement drone reporting

**Authority:** 20 V.S.A. § 4624; 2026 Act 157  
**Status:** Current / in force; public-agency rule

Section 4624 requires a law-enforcement agency that used a drone during the prior 12 months to report annually to the Department of Public Safety. Required information includes deployments and rationales, information collected, investigations and arrests aided, incidental collection involving nontarget persons or places, program cost, and funding source. DPS then reports the collected information to specified legislative committees. Act 157 of 2026 lists this report among reports exempted from a general statutory report-sunset mechanism; it does not create a new private-operator duty.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This record does not directly regulate an ordinary privately controlled AEC flight, but it can govern a mission performed for or integrated into the named public agency's program. Define in the scope and flight plan who authorizes the mission, controls the aircraft, receives the data, and is responsible for the cited records or use restrictions.
- **Agency Practitioner:** Use the current reporting instructions of Vermont General Assembly and Department of Public Safety and calendar the stated event-driven or periodic deadline; retain the submitted data, transmittal, and acceptance receipt. Confirm the current form, reporting period, responsible agency contact, amendment method, and whether contractor-held flight or data records must be supplied to the reporting entity.
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under 20 V.S.A. § 4624; 2026 Act 157; a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

### VT-004 — Correctional-facility overflight

**Authority:** 20 V.S.A. § 4625  
**Status:** Current / in force

Section 4625 prohibits knowingly operating a drone over a correctional facility or surrounding property readily recognizable as correctional property or reasonably identified by fencing or signs. A violation carries a civil penalty up to $500. The prohibition does not apply to the Department of Corrections, written consent from the supervising officer, or a commercial-purpose operation conducted in compliance with an FAA authorization, rule, or exemption. Buildings and General Services and its contractors, law enforcement, and specified emergency users receive separate exceptions with prior notice.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat written facility coordination as a pre-mobilization gate for work within Correctional facilities and readily recognizable or identified surrounding correctional property; do not rely only on flight-app geofencing or a client's general site-access instruction. Include lost-link, return-to-home, emergency landing, sensor-direction, and observer controls that prevent an unintended facility overflight, prohibited capture, loitering, or interference.
- **Agency Practitioner:** Use the current named facility or administering agency application or request channel and provide the mission description, dates, aircraft, pilot, and requested operating area. The packet identifies the approval as: Written consent or prior notice applies to specified paths; qualifying commercial FAA-compliant use is separately excepted. Because the verified source does not establish a dependable review time for every case, confirm completeness, reviewer, lead time, approval duration, and field-contact expectations directly with the agency.
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under 20 V.S.A. § 4625; a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

### VT-005 — Private-property surveillance and written consent

**Authority:** 20 V.S.A. § 4626(a)–(b), (d)–(f)  
**Status:** Current / in force; effective June 6, 2024

Section 4626 prohibits recreational drone flight below 100 feet over private real property without prior written owner consent. Separately, it prohibits any person from using a drone, without prior written owner or occupant consent, to record imagery of private property or its owner or occupant with intent to conduct surveillance violating a reasonable expectation of privacy. The section defines surveillance, presumes privacy when a person is not observable from a lawful ground-level position, sets civil penalties, and excepts qualifying utility reliability/resiliency work and legitimate law-enforcement use.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Use a mission-specific collection plan for Privately owned real property statewide that limits camera angle, dwell time, audio, zoom, thermal capture, and retention to the contracted purpose. Brief the crew on aborting or redirecting collection when people, residences, or unrelated activity enter the sensor footprint.
- **Agency Practitioner:** N/A — no agency process involved
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under 20 V.S.A. § 4626(a)–(b), (d)–(f); a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

### VT-006 — Drone-seller notice duty

**Authority:** 20 V.S.A. § 4626(c)–(d)  
**Status:** Current / in force; effective June 6, 2024

A person engaged in the business of selling drones must give each purchaser of a drone required to be registered by the U.S. Department of Transportation written notice about § 4626(a) and (b), which address low recreational flight and surveillance over private property without prior written consent. A violation is subject to a civil penalty of up to $50 for a first violation and $250 for a later violation. The provision regulates seller disclosure; it does not establish an approved-product list or make the purchaser's aircraft ineligible for commercial work.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Add Drone-seller notice duty to the mission-specific legal and site screening for Retail transactions involving federally registrable drones. Brief the crew on the triggering conduct and document the operational boundary or exception relied upon before launch.
- **Agency Practitioner:** N/A — no agency process involved
- **UAS Procurement Expert:** Retain the required point-of-sale notice with the purchase record and include it in receiving and asset-onboarding checks. The notice is not proof that the aircraft is registered or mission-eligible, so procurement should separately verify the model, serial number, applicable registrations, software account, and operating documentation.
- **AEC Industry Legal Counsel:** Treat Drone-seller notice duty as a documented stop-work or redesign trigger because the packet identifies criminal, civil, evidentiary, or damage exposure. The contract and flight record should preserve the site screening, authority or exception relied upon, crew briefing, and incident/escalation path; obtain counsel where the facts sit near an undefined boundary or intent element.

### VT-007 — Weaponized drones and projectiles

**Authority:** 13 V.S.A. § 4018  
**Status:** Current / in force

Section 4018 prohibits any person from equipping a drone with a dangerous or deadly weapon or firing a projectile from a drone. The statute incorporates chapter 205's drone definition and § 4016's dangerous-or-deadly-weapon definition. A violation may be punished by imprisonment for not more than one year, a fine of not more than $1,000, or both. The provision does not state an exception for ordinary commercial work, testing, public agencies, or a nonweapon payload that could be characterized as a projectile.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Map the covered facility and conservative stand-off area during desktop planning for work within Statewide; do not rely only on flight-app geofencing or a client's general site-access instruction. Include lost-link, return-to-home, emergency landing, sensor-direction, and observer controls that prevent an unintended facility overflight, prohibited capture, loitering, or interference.
- **Agency Practitioner:** N/A — no agency process involved
- **UAS Procurement Expert:** Use configuration-controlled payload interfaces and maintain documentation showing the purpose, operating limits, release safeguards, aircraft weight, and approved mission configuration. Avoid buying or fielding attachments whose capability could place an otherwise ordinary mapping aircraft within a weapon, projectile, contraband-delivery, or regulated dispensing provision.
- **AEC Industry Legal Counsel:** Treat Drones; dangerous or deadly weapons and projectiles as a documented stop-work or redesign trigger because the packet identifies criminal, civil, evidentiary, or damage exposure. The contract and flight record should preserve the site screening, authority or exception relied upon, crew briefing, and incident/escalation path; obtain counsel where the facts sit near an undefined boundary or intent element.

### VT-008 — Aerial hunting and wildlife surveillance

**Authority:** 10 App. V.S.A. § 20  
**Status:** Current / in force

Fish and Wildlife Board Rule § 20 prohibits taking or attempting to take wild animals with a UAV. It also prohibits using a drone or UAV to locate, surveil, or assist in locating or surveilling a wild animal for the purpose of taking it, and to drive or harass wildlife or otherwise assist a take. The rule does not apply to qualified personnel carrying out lawful duties in compliance with applicable state and federal regulations and permits, and it does not alter other aircraft or UAS compliance requirements.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Screen the mission for active hunting and wildlife sensitivity within Statewide wildlife activity; plan altitude, stand-off distance, route, observers, and abort criteria to avoid pursuit, harassment, or assistance to a taking. Document the project's environmental or infrastructure purpose and pause if animals materially react to the aircraft.
- **Agency Practitioner:** Use the current Vermont Fish and Wildlife Board application or request channel and provide aircraft details. The packet identifies the approval as: Applicable permits may be required for qualified personnel; no general UAS permit stated. Because the verified source does not establish a dependable review time for every case, confirm completeness, reviewer, lead time, approval duration, and field-contact expectations directly with the agency.
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under 10 App. V.S.A. § 20; a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

## 3. State agency requirements and guidance

### VT-009 — Drone use on state park and forest lands

**Authority:** FPR Drone Usage on FPR State Lands Procedure (Jan. 29, 2025); CVR 12-020-009 I.17  
**Status:** Current official procedure and property-use requirement

FPR's January 2025 procedure requires written Commissioner permission through a Special Use Permit or License before a person launches and lands a drone on state park or forest lands or facilities. Commercial operations require a permit or license, requested through the online state-lands application. Regional staff review completeness, insurance, payment, mission alignment, parcel management, conflicts with public uses, resource impacts, safety, liability, and prior performance; approval is discretionary and may include time or day restrictions. Emergency response, certain state-agency work, qualified ANR staff, and lawful law-enforcement activity have stated exceptions.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat property authorization for FPR state parks, forests, lands, and facilities as defined in the procedure as a pre-mobilization gate and obtain conditions that cover launch, landing, route, dates, aircraft, crew, and sensor purpose. Confirm whether the approval is site-wide or location-specific and carry the written authorization and field contact with the crew.
- **Agency Practitioner:** Use the current Vermont Department of Forests, Parks and Recreation application or request channel and provide insurance evidence. The packet identifies the approval as: Yes — online Special Use Permit or License application for covered commercial use. Because the verified source does not establish a dependable review time for every case, confirm completeness, reviewer, lead time, approval duration, and field-contact expectations directly with the agency.
- **UAS Procurement Expert:** N/A — no procurement or equipment-selection implication identified
- **AEC Industry Legal Counsel:** Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under FPR Procedure dated Jan. 29, 2025; CVR 12-020-009 I.17; a client's verbal direction should not substitute for the named authority's authorization. Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear.

## 4. Unresolved questions

1. **FPR applications:** What are the current insurance, fee, documentation, and lead-time requirements, and will the proposed duration and commercial activity require a Special Use Permit or a License?
2. **Private-property imagery:** How will enforcement distinguish ordinary project documentation from imagery captured with the statutory intent to conduct surveillance, particularly when adjoining owners or occupants appear in the collection area?
3. **Correctional facilities:** Does the supervising facility request advance written confirmation or notice for a commercial operation relying on § 4625(c)(1)(C), even though that subsection states an exception based on FAA compliance?
4. **Fish and Wildlife lands:** What approval route applies to a nonrecreational AEC launch or landing on Fish and Wildlife Department property when the mission is unrelated to taking or harassing wildlife?
5. **Local authority:** Does a municipality or other local entity claim UAS-specific authority in the absence of an express state preemption provision? Local-ordinance research is deferred from this phase.
