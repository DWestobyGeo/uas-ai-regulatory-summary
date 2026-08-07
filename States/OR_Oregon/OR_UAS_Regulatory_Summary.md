# Oregon — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 6, 2026 | **Version:** 2.2 (Workstream 9 retrofit — August 6, 2026)
**Model / checkpoint:** Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet; Workstream 9 retrofit research conducted August 6, 2026 (claude-sonnet-5).
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent_Instructions.md v3), this summary covers Oregon **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase and are not included here. Full citations and metadata are in `OR_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Oregon consolidates its UAS law in a single statutory chapter (ORS 837.300–837.998) and vests UAS regulatory authority solely in the legislature, preempting most local operational ordinances except for park takeoff/landing rules. This Workstream 9 retrofit pass found two significant, previously-uncaptured developments: **Senate Bill 1125 (2025 Oregon Laws chapter 604)**, effective 2026-01-01, which elevated the penalty for UAS interference with wildfire suppression, law enforcement, search-and-rescue, or emergency-response efforts to a standalone Class B misdemeanor (reckless) / Class C felony (knowing/intentional) tier — correcting a prior record that had (incorrectly) concluded this change failed to become law; and the **OPRD UAS Operation Areas rule** (OAR 736-010-0040(13)), finally adopted 2026-04-22 and effective 2026-05-01, which prohibits UAS takeoff/landing on state park and ocean-shore property outside designated areas and, critically, still requires a special use permit for any commercial or research UAS use even inside a designated area. This pass also added a previously-missing pair of civil-remedy statutes (ORS 837.375, 837.380) directly relevant to repeat-overflight AEC survey work, and upgraded the OSBEELS professional-licensing brochure to High confidence after direct primary-source verification.

## 2. Statewide UAS Laws and Regulations

### ORS 837.372 — Operation over critical infrastructure facility; ORS 837.370 — Operation over privately owned premises; ORS 837.385/.387 — Preemption
*Binding law | Current | Summary substantially expanded 2026-08-06 (Workstream 9 retrofit)*

**Objective Summary:** ORS 837.372 makes it a Class A violation to fly at/below 400 ft AGL over, or allow contact with, a fenced/posted critical infrastructure facility — a 14-category list including power generation/substation facilities, petroleum/alumina refineries, chemical/polymer/rubber manufacturing, water/wastewater facilities, natural gas compressor stations, LNG terminals, telecom switching offices, ports/rail yards/trucking terminals, gas processing plants, radio/TV transmission facilities, electric-arc-furnace steelmaking facilities, high-hazard dams, fenced aboveground pipelines, and correctional/law-enforcement facilities — subject to 9 exceptions (federal government; public body; law enforcement agency; their contractors; the facility owner/operator or a person with that owner/operator's written consent; the property owner/occupant or a person with that owner/occupant's written consent; and FAA-authorized commercial operation). ORS 837.370 prohibits operating a drone over private property in a manner that intentionally, knowingly, or recklessly harasses or annoys the owner/occupant, on a tiered scale: Class B violation (first offense), Class A violation (one prior conviction), Class B misdemeanor (two or more prior convictions, at which point a court may impose a no-UAS-possession probation condition). ORS 837.385 vests UAS regulatory authority solely in the legislature, preempting local operational ordinances except for park takeoff/landing rules under ORS 837.387 — which must still allow utility-provider line-inspection access, public-body emergency use, and an emergency-landing affirmative defense. ORS 837.360/.362 impose public-body UAS registration/data-policy requirements (not applicable to private operators). ORS 837.365 prohibits weaponized UAS, subject to a narrow notify-and-insure exception.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Rely on the 837.372(3)(i) commercial/FAA exemption for critical-infrastructure inspection work, but get written facility-owner consent when it's easy to obtain — it removes any field ambiguity, and the facility list is broader than intuition suggests (it includes steelmaking, gas processing, and LNG facilities). Because local ordinances are narrowly limited to park takeoff/landing, the main site-specific check for most projects is simply whether the launch/land point is inside a park — but see the OPRD entry below for a separate, more restrictive rule on OPRD property specifically.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Keep FAA authorization and commercial-purpose documentation on file for any critical-infrastructure flight, since establishing the exemption is the operator's burden if challenged. For private-property work, document flight altitude and duration to rebut any claim of intentional or reckless harassment under 837.370. See the new civil-remedies entry below (ORS 837.375/837.380) for separate civil exposure distinct from these criminal/violation provisions.
### ORS 837.374 — Interference with aircraft, wildfire suppression, law enforcement, or emergency response
<span class="news-anchor" data-record-id="OR-002" hidden></span>
*Binding law | Amended by 2025 Oregon Laws c.604 (SB 1125), eff. 2026-01-01 | Corrected 2026-08-06 (Workstream 9 retrofit)*

**Objective Summary:** Directing a laser at an aircraft, crashing into an aircraft, or preventing takeoff/landing remains a Class A violation (reckless) / Class A misdemeanor (knowing/intentional). **Senate Bill 1125 (2025 Oregon Laws chapter 604), approved by the Governor 2025-07-24 and effective 2026-01-01, split interference with a law enforcement, firefighting, search-and-rescue, or emergency-response effort into its own, more severe standalone tier: a Class B misdemeanor if reckless, and a Class C felony if knowing/intentional** (previously bundled into the same tier as the laser/crash/takeoff-prevention conduct). Conduct causing death or serious physical injury remains a Class A felony (up to 20 years) regardless of which underlying act caused it. Second-or-subsequent-conviction UAS forfeiture is unchanged.

**CORRECTION (2026-08-06 retrofit):** the prior record here tracked House Bill 3426 — a companion 2025-session bill proposing essentially the identical Class B misdemeanor/Class C felony restructuring — which did die at sine die on 2025-06-27, and concluded this change was "not current law." That conclusion was incorrect: Senate Bill 1125, a separate legislative vehicle carrying substantively the same change, passed and is now in force. A "died in committee" finding for one bill number does not establish that the underlying policy failed — the current codified statute's own amendment history should always be checked before reaching that conclusion.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Build active-incident awareness into wildfire-season scheduling — check for TFRs and coordinate with incident command before flying anywhere near a fire, law-enforcement operation, or emergency response, since "interference" is broadly defined and doesn't require actual contact with another aircraft. As of 2026-01-01, the standalone penalty tier for this specific conduct (Class B misdemeanor reckless / Class C felony knowing-intentional) is materially higher than the general laser/crash/takeoff-prevention tier.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document pre-flight airspace/TFR checks for any job scheduled during fire season, and train field crews that felony-level exposure now attaches to knowing/intentional interference with these specific efforts (not only to conduct causing serious injury) as of SB 1125's 2026-01-01 effective date. Update any pre-2026 client-facing compliance materials that still describe this as a failed 2025 bill.
### ORS 837.375, 837.380 — Civil Remedies for UAS Interference and Repeat Trespass Overflight
*Binding law | Current | New record added 2026-08-06 (Workstream 9 retrofit)*

**Objective Summary:** ORS 837.375 gives the owner of an FAA-licensed UAS (or one operated by the military, a federal agency, or law enforcement) a civil action against anyone who intentionally interferes with it or gains unauthorized control over it — statutory minimum damages of $5,000 plus mandatory attorney fees to a prevailing plaintiff. ORS 837.380 gives a property owner or lawful occupant a civil action against a UAS operator (person or public body) who has flown over the property on at least one prior occasion after being told the owner/occupant objects — treble damages plus injunctive relief, with attorney fees recoverable if damages pleaded are $10,000 or less. The action does not apply to UAS lawfully in an airport landing/takeoff flight path, or operated for commercial purposes under FAA authorization — though that FAA-authorization exception blocks only this specific statutory action, not other civil theories such as invasion of privacy, which subsection (3) expressly preserves. The Attorney General may separately bring a nuisance/trespass action on the state's behalf.

**Practical Interpretation**

- **AEC Industry UAS Expert:** For any project involving repeat flights over the same parcel(s) — corridor, pipeline, or multi-adjacent-parcel work especially — log any objection a property owner or occupant raises about overflight, since a second flight after a recorded objection is the trigger for 837.380 exposure regardless of Part 107 status for other civil theories.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Treat 837.380 as a distinct, notice-triggered civil-trespass exposure separate from the criminal/violation provisions above — it requires no criminal charge or conviction, only a documented prior objection and a subsequent overflight. Confirm whether a project's FAA-commercial-authorization status actually defeats an 837.380 claim (it does, per subsection (3)) versus other civil theories it does not defeat (e.g., invasion of privacy) before advising a client that Part 107 status resolves all private-property overflight exposure in Oregon.
## 3. State Agency UAS Requirements

### Aviation — Oregon Department of Aviation (ODA)
*Binding administrative regulation | Public-body only*

**Objective Summary:** OAR 738-080-0045 requires Oregon public bodies to register each UAS with ODA at $25 (under 55 lbs) or $50 (55 lbs+); educational institutions register as users rather than per-aircraft and pay no fee. Private/commercial operators are not required to register with ODA.

**Practical Interpretation**

- **AEC Industry UAS Expert:** No action needed for a private fleet; only relevant if the firm operates equipment issued or registered under a public agency's own UAS program.
- **Agency Practitioner:** Use Oregon Department of Aviation (ODA)'s current registration or exemption channel before the aircraft is placed on a covered mission. Confirm which aircraft and operator details, fees, renewal dates, and exemption evidence apply to this operation, and retain the registration or written exemption determination with the fleet record.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Confirm registration status in writing if flying agency-owned equipment under a public contract — noncompliance would be the agency's exposure, but could still affect project continuity.
### Parks and Public Lands — Oregon Parks and Recreation Department (OPRD)
<span class="news-anchor" data-record-id="OR-004" hidden></span>
*Binding administrative regulation | OAR 736-010-0040(13), effective May 1, 2026 | Citation, adoption date, and detail corrected 2026-08-06 (Workstream 9 retrofit)*

**Objective Summary:** OAR 736-010-0040(13) (Permanent Administrative Order PRD 4-2026, agency-approved 2026-04-22, filed 2026-04-30) prohibits UAS takeoff/landing on OPRD-administered property, including the entire public ocean shore, except wholly within a designated "UAS Operation Area." OPRD may designate, modify, suspend, or rescind areas (park-wide or partial, year-round or conditional) and must publish maps/conditions at least 30 days before a designation takes effect (except emergencies); it may also require a "UAS Pass" for a given area. Overnight-use facilities, areas within a half-mile of a federally/state protected-area boundary that prohibits UAS takeoff/landing, and areas closed by other statute/rule are permanently ineligible for designation. Public-safety agencies and utilities may operate without prior approval during emergencies, and with advance OPRD notice (no permit) for non-emergency official purposes. **Critically, subsection (14)(j) requires a special use permit for any commercial or research UAS use anywhere on OPRD property — including inside a designated Operation Area** — only recreational use is permit-free within a designated area. Effective 2026-08-08, OPRD opened roughly 19 initial park properties as Operation Areas for recreational use; more are being added and posted 30 days before opening.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not assume a designated UAS Operation Area means permit-free access for AEC work — a special use permit is required for any commercial or research UAS use anywhere on OPRD property, including inside a designated Operation Area; the area designations only remove the permit requirement for recreational flyers. Check the current OPRD UAS Operation Areas list (stateparks.oregon.gov) and the half-mile protected-area buffer before scoping any coastal, dune/erosion, or beach-access project, and build special-use-permit lead time into every OPRD-property schedule regardless of location.
- **Agency Practitioner:** Start with the site manager or permitting office for Oregon Parks and Recreation Department (OPRD) before scheduling fieldwork, because property-specific conditions may control the route and timing. Request the current form, lead time, fee, insurance and FAA-document checklist, and site restrictions, then keep the signed approval and conditions in the mission file.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Retain the permit approval in the project file before mobilizing a crew for any commercial/research OPRD-property work — a designated-area location does not substitute for the permit. Treat overnight-use facility sites and the half-mile protected-area buffer as absolute exclusions with no permit workaround.
### Professional Licensing — Oregon State Board of Examiners for Engineering and Land Surveying (OSBEELS)
*Advisory guidance issued by licensing board | Confidence upgraded to High 2026-08-06 (Workstream 9 retrofit)*

**Objective Summary:** OSBEELS, which regulates the practice of land surveying and photogrammetric mapping under ORS ch. 672 and OAR ch. 820, has published a brochure confirming UAS as a recognized tool for licensed practice, and warns that providing photogrammetry/mapping services without proper licensure can result in fines or further legal action. It lists five specific "potential areas of infraction for UAS owners" operating without a license: photogrammetric mapping, topographic mapping, volume computation, 3D mapping, and boundary surveys. To become a licensed Photogrammetrist, an applicant must meet OAR 820-010-3010's education/experience requirements, pass the NCEES Fundamentals of Land Surveying exam, and pass the CSBSR Photogrammetry exam; OAR 820-010-1000 and 820-010-2000 separately govern engineer and land surveyor qualifications.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Pull the current OSBEELS brochure directly and use its five-item infraction list (photogrammetric mapping, topographic mapping, volume computation, 3D mapping, boundary surveys) as the trigger checklist for which drone-derived deliverables require registered-professional sign-off in Oregon versus which can be produced without it.
- **Agency Practitioner:** Before relying on an unlicensed or exempt delivery path, give Oregon State Board of Examiners for Engineering and Land Surveying (OSBEELS) a written description of the proposed UAS-derived product, its stated accuracy, and whether it will establish or certify boundaries, elevations, or authoritative locations. Ask the board to confirm the applicable license, responsible-charge, certification, or exemption path and retain the response with the project quality plan.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Board-issued practice guidance is a strong indicator of how OSBEELS would evaluate a complaint, even though nonbinding — cite it in internal compliance documentation, but confirm current content directly with the Board before relying on specific thresholds in a client contract.
### Procurement / Equipment Restrictions
*Category reviewed — no Oregon-specific state law found | Reconfirmed 2026-08-06*

**Objective Summary:** No Oregon state law or executive order specifically restricting government UAS purchase/use by manufacturer or country of origin was located, reconfirmed in this retrofit pass. Secondary reporting (DroneXL, March 2026) indicates Oregon public-safety agencies have been significantly affected by the federal FCC "Covered List" ban on new foreign-made drone models/components, which took firmer effect with a 2025-12-22 restriction on federal-fund purchases from Covered Foreign Entities (including DJI and Autel).

**Practical Interpretation**

- **AEC Industry UAS Expert:** No equipment restriction currently limits fleet choice for private commercial work; public-safety-agency clients may be operating a reduced or aging fleet due to the federal covered-list disruption, which could create contract opportunities for compliant-equipment support work.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** No current state equipment restriction is established by this research result. Do not treat that absence as permanent; check current solicitation terms, client policies, and independently applicable federal restrictions before committing a fleet to the work.
- **AEC Industry Legal Counsel:** No state compliance obligation to build into contracts for private work; if contracting with an Oregon public-safety agency, confirm whether federal covered-list compliance is being passed through as a contract term.
## 4. Unresolved Operational Questions

- **"Oregon House Bill 4066" UAS definition cross-reference:** cited in OSBEELS's own brochure resource list as the source of the state's UAS definition, but not independently cross-checked in this pass against the codified ORS 837.300 definition; both should be consistent but this was not confirmed line-by-line.
- **OPRD UAS Operation Areas list:** actively expanding as of this retrofit's research date (initial ~19 sites opened 2026-08-08); re-check the current list, and the half-mile protected-area buffer, before each OPRD-property project.
- **SB 1186 (2025 session):** a companion law-enforcement-focused UAS bill that died at sine die alongside HB 3426 on 2025-06-27; out of scope for this private/commercial-operator register since it addressed only law enforcement agency use (ORS 837.310–.345), but noted here in case a future session revives it.

## 5. Confidence Summary

| Finding | Confidence |
|---|---|
| ORS 837.372 critical infrastructure / 837.370 private property / 837.385/.387 preemption | High — verified directly against current statute text; summary substantially expanded |
| ORS 837.374 interference statute (tiered penalties, as amended by SB 1125/2025 c.604) | High — verified directly against the enrolled 2025 c.604 PDF; corrects a prior "not current law" error |
| ORS 837.375/837.380 civil remedies (new record) | High — verified directly against current statute text |
| OAR 738-080-0045 public-body registration | High — verified directly; fee schedule reconfirmed |
| OPRD UAS Operation Areas rule (OAR 736-010-0040(13)) | High — verified directly against the Secretary of State's Permanent Administrative Order filing; citation and adoption date corrected |
| OSBEELS UAS/photogrammetry guidance brochure | High — verified directly against the primary PDF (upgraded from Moderate) |
| No Oregon-specific procurement/manufacturer restriction | Low — absence of a finding, not a confirmed negative |

*This document is objective legal/regulatory summary plus labeled practical interpretation. It is not legal advice; consult Oregon counsel for project-specific compliance determinations. Local and tribal UAS considerations are out of scope for this phase per current research instructions.*
