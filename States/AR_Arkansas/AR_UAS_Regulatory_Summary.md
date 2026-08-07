# Arkansas — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 5, 2026 | **Version:** 2.2 (Workstream 9 retrofit — Act 2025-597 incorporated August 5, 2026)
**Model / checkpoint:** Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet; Workstream 9 retrofit research conducted August 5, 2026.
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent Instructions v6, Amendment 2), this summary covers Arkansas **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase. No comprehensive statewide UAS-preemption statute was located for Arkansas, and no currently enforced local drone ordinance was identified either, though this was not independently confirmed against the full municipal-code landscape. Full citations and metadata are in `AR_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Arkansas's UAS-specific statutory framework was substantially expanded by **Act 2025-597 (the "Arkansas Privacy Act," HB1148, effective 2025-08-05)**, found and incorporated in this Workstream 9 retrofit pass. The framework now centers on two related but distinct offenses at Ark. Code Ann. § 5-60-103: the original critical-infrastructure surveillance restriction (a misdemeanor to use a UAS to surveil, gather evidence about, or record critical infrastructure — now expressly including natural gas facilities and lines — without the owner's written consent), and a newly created surveillance-intent images offense (purposely capturing an image of a person or private property for the purpose of surveillance). Act 2025-597 also added a new possession/disclosure offense (§ 5-60-126), a new civil action tied to the images offense (§ 16-118-119, alongside the pre-existing critical-infrastructure civil action at § 16-118-111), and — most significant for AEC work — a new statewide lawful-use safe harbor (§ 27-118-101) that names **Arkansas-licensed engineers and surveyors performing mapping, land-surveying, or infrastructure-supporting GIS work** as an express, enumerated lawful use. Two additional pre-existing criminal statutes name "unmanned vehicle or aircraft" as a covered instrument in voyeurism offenses, and a narrower statute restricts UAS possession by higher-tier registered sex offenders (now confirmed as Act 2023, No. 35). Arkansas State Parks is widely reported to require a Director's Special Use Permit for UAS use, though this remains unconfirmed against a primary source despite renewed attempts in this pass. No statewide UAS-preemption statute was located, including after Act 2025-597.

## 2. Statewide UAS Laws and Regulations

### Ark. Code Ann. § 5-60-103 — Unlawful Use of an Unmanned Aircraft System Related to Infrastructure — Unlawful Use of an Unmanned Aircraft System Related to Images
*Binding law | Current, enacted 2015, substantially amended and retitled by Act 2025-597 (eff. 2025-08-05) | Citation and detail corrected 2026-08-05 (Workstream 9 retrofit)*

**Objective Summary:** Act 2025-597 preserved the original critical-infrastructure offense — a Class B misdemeanor (Class A for a second or subsequent offense) to knowingly use a UAS to conduct surveillance of, gather evidence about, or record "critical infrastructure" without the owner's prior written consent — while expanding the "critical infrastructure" definition to expressly include natural gas distribution/transmission lines, facilities, and storage, and adding a new consent exception for ArDOT, the State Highway Commission, city/county public-works departments, and their contractors/consultants/employees performing authorized work. The Act also created an entirely new, separate offense (subsections (e)-(f)): purposely using a UAS to capture an "image" (broadly defined to include thermal, infrared, ultraviolet, or other electromagnetic-wave data, not just visible-light photography) of an individual or private property with the purpose of conducting surveillance on that individual or property, a Class C misdemeanor, with defenses for prompt image destruction, capture authorized under the new § 27-118-101 safe harbor, or law-enforcement duties. The pre-existing UAS-definition exclusions (federal/state-authorized surveillance, law-enforcement/emergency-management use) carry over, though the enrolled Act text's COA-exclusion clause contains an apparent uncorrected drafting anomaly (see Practical Interpretation and the source register notes) that should be rechecked once available against the official codified text.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Screen the project map for protected critical-infrastructure facilities (now including natural gas lines/facilities/storage) and active emergency operations before dispatch. Separately, because the new images offense turns on surveillance intent, document mission purpose (mapping/engineering/infrastructure documentation, not surveillance of a specific person or property) and rely on the new § 27-118-101 safe harbor — which expressly covers Arkansas-licensed engineers and surveyors doing mapping/GIS work — as the documented lawful-use basis.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat this as two distinct offenses sharing one code section, now paired with a new civil-liability exposure (§ 16-118-119) and a new possession/disclosure offense (§ 5-60-126). Preserve the facts supporting any exception, consent, or § 27-118-101 safe-harbor theory, and flag the noted COA-exclusion drafting anomaly for state counsel rather than assuming its effect.
### Ark. Code Ann. § 16-118-111 — Civil Actions Against UAS Operators (Critical Infrastructure)
*Binding law | Current, enacted 2015 | Reconfirmed 2026-08-05, unaffected by Act 2025-597*

**Objective Summary:** Gives a critical-infrastructure owner a private civil action against a person who violates § 5-60-103's critical-infrastructure offense, for the greater of actual damages or $10,000; three times actual damages (or $10,000, whichever is greater) where the violation resulted in profit or monetary gain; plus costs and reasonable attorney's fees. Act 2025-597 did not amend this section; it added a separate, additional civil action (§ 16-118-119, below) tied to the new images offense instead.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Add this authority to the state-specific preflight checklist and confirm its applicability to the project site, mission purpose, and client. Document the operational decision and any source-supported exception before dispatch.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the applicability analysis and any exception relied upon in the project file. Align the scope, client representations, and operator procedures with the verified authority, and seek state counsel if material facts fall outside its clear terms.
### Ark. Code Ann. § 16-118-119 — Civil Action for Damages Caused by Violation of the UAS Image-Capture and Possession/Disclosure Offenses
*Binding law | New — added by Act 2025-597, eff. 2025-08-05*

**Objective Summary:** Gives an owner or tenant of private real property a private civil action against a person who, in violation of § 5-60-103's images offense, captured an image of the property or of the owner/tenant while on the property with a reasonable expectation of privacy. Remedies: injunctive relief; statutory damages of $5,000 per episode of unlawful image capture, or $10,000 per episode of unlawful disclosure/display/distribution/other use in violation of § 5-60-126; or actual damages where disclosure/display/distribution was done with "malice" (specific intent to cause substantial injury or harm). All owners of a parcel are treated as a single owner and all tenants as a single tenant for damages purposes. The court must award costs and reasonable attorney's fees to the prevailing party. Two-year statute of limitations.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Screen flight plans and image-capture purpose against the surveillance-intent element of the § 5-60-103 images offense before any mission that could be read as targeting a specific private property or individual; document the project's mapping/engineering/GIS purpose and rely on the § 27-118-101 safe harbor as the operative defense, since this civil action attaches to the same underlying conduct.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** This is a companion civil-liability statute to the new images offense and the new possession/disclosure offense; it exposes an AEC operator to a statutory-minimum-damages claim, mandatory attorney's-fee shifting, and injunctive relief independent of any criminal misdemeanor charge, and is distinct from § 16-118-111's pre-existing critical-infrastructure-only civil action.
### Ark. Code Ann. § 5-60-126 — Unlawful Possession, Disclosure, Display, Distribution, or Use of an Image Captured by a UAS
*Binding law | New — added by Act 2025-597, eff. 2025-08-05*

**Objective Summary:** Makes it a separate offense to possess, disclose, display, distribute, or otherwise use an image captured in violation of § 5-60-103's images offense: a Class C misdemeanor for mere possession, or a Class B misdemeanor if the person otherwise discloses, displays, distributes, or uses it; each image is a separate offense. Defenses: prompt image destruction (possession charge), promptly stopping the disclosure/display/distribution/use (disclosure-type charge), or lawful capture under the new § 27-118-101 safe harbor.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Extend the same surveillance-intent screening and § 27-118-101 safe-harbor documentation used for the images offense to downstream data handling — storage, processing, and delivery of AEC-collected imagery — since this section separately criminalizes possession or downstream use of an unlawfully captured image even by a person other than the original operator.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Because each image is a separate offense, exposure can scale quickly with an AEC firm's data volume if the underlying capture were ever found unlawful, making the § 27-118-101 safe-harbor documentation practice correspondingly important.
### Ark. Code Ann. § 27-118-101 — Use of Unmanned Aircraft System to Capture Image (Statewide Lawful-Use Safe Harbor)
*Binding law | New — added by Act 2025-597, eff. 2025-08-05 | Most AEC-relevant new Arkansas authority identified in this retrofit pass*

**Objective Summary:** Declares it lawful to capture a UAS image in Arkansas under any of 25 enumerated circumstances, operating as a defense to the § 5-60-103 images offense and the § 5-60-126 possession/disclosure offense. Directly AEC-relevant categories include: **(23) capture by an engineer or surveyor licensed in the State of Arkansas for mapping/land-surveying tasks or GIS data collection supporting public or private infrastructure** — an express, named statutory safe harbor for core AEC drone survey/mapping work; (24) operation by or on behalf of a critical-infrastructure owner/operator for siting, deploying, inspecting, monitoring, operating, or maintaining the facility; (5) utility inspection/maintenance/vegetation-clearance/routing work; (21) work by persons acting on behalf of ArDOT, the State Highway Commission, the Arkansas Highway Police Division, or city/county public-works departments; (6) capture with the consent of the property owner/occupant; (14) sub-eight-foot-AGL unmagnified capture in a public place; and (15) capture of public real property or a person on such property. Other categories cover higher-education/Game & Fish research, FAA UAS test ranges, military operations, satellite mapping, search-warrant-authorized and various emergency/public-safety law-enforcement uses, licensed real-estate marketing (no identifiable individuals), pipeline safety, port-authority security, and consenting-owner assessor use. Subsection (c) clarifies the section does not apply to UAS manufacture, assembly, distribution, or sale.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This is the single most directly relevant new Arkansas authority for AEC UAS work: subdivision (b)(23) names Arkansas-licensed engineers and surveyors performing mapping, land-surveying, or infrastructure-supporting GIS data collection as an express statutory safe harbor. Confirm and document the licensee's current Arkansas PE/PS licensure, frame mission purpose and deliverables as mapping/surveying/GIS work, and keep that documentation on file alongside any project-specific consent or critical-infrastructure-operator authorization.
- **Agency Practitioner:** For public-agency or ArDOT-affiliated work, confirm the specific enumerated category relied upon (e.g., subdivision (21) for ArDOT/public-works-affiliated persons, or (15) for public real property) and retain the authorizing engagement or contract documentation.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified; subsection (c) expressly excludes UAS manufacture, assembly, distribution, or sale from this section.
- **AEC Industry Legal Counsel:** Treat this as an affirmative defense/safe-harbor structure rather than a permit system — the burden in practice will fall on demonstrating the capture fit an enumerated category. Build project files that map each AEC engagement to a specific subdivision (most often (23) or (24)) and preserve licensure and engagement records accordingly.
### Ark. Code Ann. §§ 5-16-101(b), 5-16-102(b) — Video Voyeurism and Voyeurism (Unmanned Vehicle or Aircraft)
*Binding law | Current, enacted 2015, last amended 2021 | Reconfirmed 2026-08-05, unaffected by Act 2025-597*

**Objective Summary:** § 5-16-101(b) makes it unlawful to knowingly use an unmanned vehicle or aircraft (among other listed recording devices) that is concealed, operated to escape detection, or disguised, to secretly/surreptitiously record or view another person's body where a reasonable expectation of privacy exists, without consent (Class B misdemeanor, elevated if distributed/posted or on a prior conviction). § 5-16-102(b) separately criminalizes using an unmanned vehicle or aircraft, for sexual arousal or gratification, to look without consent into a private place in a public accommodation or into a dwelling under specified privacy-invading circumstances (Class A misdemeanor up to Class C/D felony depending on victim age and prior convictions).

**Practical Interpretation**

- **AEC Industry UAS Expert:** Design acquisition and data-handling workflows to minimize unnecessary capture of people and private activity. Confirm the source-supported consent or project-purpose basis before flight and carry that limitation through processing, access control, retention, and delivery.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat the cited authority as a documented compliance gate where applicable. Preserve the facts supporting any exception or consent theory, allocate client and operator responsibilities clearly, and seek state counsel when project facts approach ambiguous or penal language.
## 3. State Agency and Facility-Specific UAS Requirements

### Ark. Code Ann. § 5-14-138 — UAS Restriction for Registered Sex Offenders
*Binding law | Enacted by Act 2023, No. 35, eff. 2023-08-01 | Citation and effective date corrected 2026-08-05 (Workstream 9 retrofit)*

**Objective Summary:** Prohibits a person required to register under the Sex Offender Registration Act who has been assessed as a Level 3 or Level 4 offender from purchasing, owning, possessing, using, or operating a UAS, unless required as part of employment. A violation is a Class D felony.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Add this restriction to the state preflight screen, brief the field crew on the prohibited conduct, and identify a stop-work or escalation point. Document any exception relied upon rather than assuming Part 107 authority resolves the state requirement.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat the cited authority as a documented compliance gate where applicable. Preserve the facts supporting any exception or consent theory, allocate client and operator responsibilities clearly, and seek state counsel when project facts approach ambiguous or penal language.
### Arkansas State Parks — Reported UAS Permit Requirement (Unconfirmed)

**Objective Summary:** Multiple secondary drone-law compilation sources consistently report that Arkansas State Parks prohibits UAS operation absent a Director-issued Special Use Permit, with a reported application process requiring FAA drone registration and proof of liability insurance, reportedly submitted to parks.info@arkansas.gov. No primary Arkansas State Parks document, administrative rule, or statute was located to independently confirm this reported policy despite renewed attempts in this retrofit pass.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Build the issuing agency approval into pre-mobilization planning. Confirm the property boundary, current submission materials, operating dates, and issued conditions before dispatch, and leave schedule contingency because the captured source does not guarantee processing time.
- **Agency Practitioner:** Start with the site manager or permitting office for Arkansas Department of Parks, Heritage and Tourism / Arkansas State Parks (research result) before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Make the required approval and compliance with its conditions a documented mobilization gate. Allocate responsibility for applications and schedule impacts in the contract, and obtain counsel if the project's facts do not fit the stated authorization pathway.
### Professional Licensing — Board of Licensure for Professional Engineers and Professional Surveyors
*Binding general regulation | No UAS-specific board guidance located | Citation corrected 2026-08-05 (Workstream 9 retrofit)*

**Objective Summary:** Article 20, Section B(1) of the Board's current Rules of Professional Conduct (codified at 235.01.20 Ark. Code R. § 004) requires a licensee to "undertake assignments only when qualified by education or experience in the specific technical fields of engineering or surveying involved." This corrects a prior citation to a superseded "Rule 415" numbering that could not be independently located in the Board's current rules text; the underlying substantive requirement is unchanged. Secondary sources describe this general rule as applicable to UAS-based mapping work, but no standalone UAS-specific Board guidance was located.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Classify the intended UAS-derived deliverable before mobilization and place licensed-professional review where the verified authority requires it. Keep flight acquisition, analysis, and final professional deliverable responsibilities explicit in the project workflow.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Describe this source as guidance or policy, not a generally binding statute. Check whether the client or property owner incorporates it contractually, preserve the version relied upon, and escalate conflicts with controlling authority.
### State Preemption, Executive Orders, AG Opinions, Procurement, and DOT/Aeronautics
*Categories reviewed — none additional located, including after Act 2025-597*

**Objective Summary:** No comprehensive statewide UAS-preemption statute was located; no currently enforced local drone ordinance was identified in secondary sources, though this was not independently confirmed. No Arkansas executive order, Attorney General opinion, state-agency UAS procurement restriction, or separate DOT/aeronautics-office UAS program distinct from FAA requirements was located. Act 2025-597, while substantially expanding state UAS criminal and civil law, likewise did not enact a preemption provision.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Treat this record as a research flag, not an operator requirement. Do not change field procedures unless a current controlling source confirms the issue; route any project-specific uncertainty to the identified agency or counsel.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** No current state equipment restriction is established by this research result. Do not treat that absence as permanent; check current solicitation terms, client policies, and independently applicable federal restrictions before committing a fleet to the work.
- **AEC Industry Legal Counsel:** Do not present this negative or unresolved research result as a legal conclusion. Preserve the research limitation, verify current authority for the specific project, and escalate only if the issue could materially affect scope, access, or liability.
## 4. Non-Regulatory Context

No enforcement-action, incident, or not-yet-enacted-legislation news items met the Section 9 inclusion bar for Arkansas during this research pass; this section is omitted per the "omit when nothing material was found" rule.

## 5. Unresolved Operational Questions

- **§ 5-60-103 COA-exclusion drafting anomaly:** The enrolled Act 2025-597 text's UAS-definition exclusion at subdivision (a)(3)(B)(iv) contains apparently uncorrected drafting language ("certificate of authorization issued by the operated by a person for a commercial purpose..."); recheck against the official codified text once available, and do not assume it changes the ordinary Part 107 analysis without confirmation.
- **Arkansas State Parks UAS policy:** Reported by multiple secondary sources but not confirmed against a primary Arkansas State Parks document despite renewed attempts in this pass; confirm directly with the parks system before planning UAS work at a specific Arkansas state park.
- **Local ordinances:** Out of scope for this phase; the reported absence of currently enforced local ordinances was not independently confirmed against the full Arkansas municipal-code landscape.
- **§ 27-118-101(b)(20) "Department of Transformation and Shared Services" surveyor reference:** Independently confirm this reference against that department's current organization before relying on it for a project outside the ArDOT/public-works context already covered by subdivision (21).
- **Board of Licensure Article 20 numbering:** Recommend a direct inquiry to the Board (or its official current rules handbook PDF) to confirm Article 20, Section B(1) remains its current, in-force numbering before citing it to a client on a UAS-derived-product certification question.

## 6. Confidence Summary

| Finding | Confidence |
|---|---|
| § 5-60-103 (critical infrastructure + images offenses, as amended by Act 2025-597) | High — verified directly against the official enrolled Act 597 PDF |
| § 16-118-111 (civil liability companion, critical infrastructure) | High — verified directly against Justia's codification |
| § 16-118-119 (civil liability companion, images offense — new) | High — verified directly against the official enrolled Act 597 PDF |
| § 5-60-126 (possession/disclosure offense — new) | High — verified directly against the official enrolled Act 597 PDF |
| § 27-118-101 (statewide lawful-use safe harbor — new) | High — verified directly against the official enrolled Act 597 PDF |
| §§ 5-16-101(b), 5-16-102(b) (voyeurism statutes naming UAS) | High — verified directly against Justia's codification |
| § 5-14-138 (sex-offender UAS restriction) | High — verified directly against Justia's codification, with Act citation and effective date corrected |
| Arkansas State Parks UAS permit requirement | Low — reported consistently by secondary sources; no primary source located despite renewed attempts |
| Professional licensing competency rule (Article 20, Section B(1), formerly cited as "Rule 415") | Moderate — verified directly against a current-rules mirror; not yet cross-checked against the Board's own official handbook |
| No state preemption statute located, including after Act 2025-597 | Low — negative research finding based on secondary sources |
| No EO/AG-opinion/procurement/DOT-aeronautics source located | Low — negative finding, not a comprehensive search |

*This document combines objective legal/regulatory summaries with Phase 2 Practical Interpretation content, which is AI-generated operational opinion and not legal advice. Consult Arkansas counsel for project-specific compliance determinations. Local ordinances and tribal UAS considerations are out of scope for this phase per current research instructions.*
