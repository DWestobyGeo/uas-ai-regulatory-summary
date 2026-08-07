# Colorado — Commercial UAS Regulatory Summary

**Prepared for:** AEC (surveying, mapping, construction, inspection) UAS program management
**Research date:** August 1, 2026 | **Version:** 2.2 (Workstream 9 retrofit — August 7, 2026)
**Model / checkpoint:** Objective research and Phase 2 model/checkpoint were not recorded in this legacy state packet. Retrofit pass performed with claude-sonnet-5.
**Interpretation scope:** Agent Instructions v6 (August 2, 2026)
**Scope note:** Federal FAA Part 107 is the baseline for all commercial sUAS operations nationwide and is not restated here. Per current research-phase scope (Agent Instructions v6), this summary covers Colorado **state and state-agency** UAS authorities only — local (municipal/county) ordinances and tribal rules are deferred to a later phase and are not included here. Colorado has **not** enacted a state preemption statute for local UAS ordinances (see Section 4), and secondary sources document an unusually dense and varied patchwork of municipal and county rules (Denver, Boulder, Colorado Springs, mountain resort communities, and more) — a project-specific municipal check will be necessary before this state-level picture can be treated as complete for any specific Colorado site. Full citations and metadata are in `CO_UAS_Source_Register.csv`.

> **Status:** A first pass of source collection, objective summaries, and practical interpretation is complete for this state. Ongoing work is expanding source coverage and improving quality review and processing efficiency across the project.

---

## 1. State UAS Regulatory Overview

Colorado has not enacted a comprehensive, standalone UAS act. Instead, it regulates drones through targeted amendments to existing criminal and administrative law: a 2018 amendment to the public-safety obstruction statute (Colo. Rev. Stat. § 18-8-104) that specifically addresses drones used to interfere with emergency responders, a camera-agnostic criminal-invasion-of-privacy statute, a civil-trespass/landowner-airspace-rights statute, and Colorado Parks and Wildlife (CPW) regulations restricting UAS use on state parks/outdoor recreation lands and for hunting-related wildlife scouting. Colorado has **not** enacted a critical-infrastructure or correctional-facility-specific UAS offense comparable to Texas's or New York's — several such bills have been introduced since 2015 and have all died in committee, most recently a broader bill (SB26-024) that would have also limited local regulatory authority, postponed indefinitely in February 2026. Colorado likewise has not enacted state preemption of local UAS ordinances, leaving a dense patchwork of municipal and county rules layered on top of the state-level picture below. The state maintains an active public-safety UAS program (the Center of Excellence for Advanced Technology Aerial Firefighting) but no state-agency procurement restriction or foreign-hardware ban comparable to Texas's Prohibited Technologies List was located.

## 2. Statewide UAS Laws and Regulations

### Colo. Rev. Stat. § 18-8-104 — Obstructing a Peace Officer, Firefighter, EMS Provider, Rescue Specialist, or Volunteer (drone-specific provision)
<span class="news-anchor" data-record-id="CO-001" hidden></span>
*Binding law | Current, amended by HB 18-1314 (2018) and SB 21-271 (2021)*

**Objective Summary:** Defines "obstacle" to include an unmanned aircraft system. A person commits the offense (class 2 misdemeanor) by using or threatening to use a UAS as an obstacle to knowingly obstruct, impair, or hinder a peace officer, firefighter, EMS provider, rescue specialist, or volunteer acting under color of official authority. A statutory exception applies if the UAS operator obtains permission from the coordinating entity, continues to communicate with it during the operation, and immediately complies with its instructions.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not fly at or near an active emergency, accident, or wildfire scene without first obtaining permission from the coordinating law enforcement or incident-command entity and maintaining communication throughout the flight — directly relevant to any post-disaster damage assessment or infrastructure-inspection flight near an active incident.
- **Agency Practitioner:** Before any planned UAS work near an active emergency response, establish contact with the law-enforcement, fire, EMS, or incident-command entity coordinating the scene and ask how it grants operating permission and maintains in-flight communications. Retain the permission and communication plan, brief the pilot on immediate-compliance expectations, and do not assume a client request substitutes for response-agency coordination.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the specific permission obtained from the coordinating entity (agency name, contact, time granted) before and during any flight near an active emergency response, since the exception is conditioned on ongoing communication and compliance, not merely initial permission.
### Colo. Rev. Stat. § 18-7-801 — Criminal Invasion of Privacy (camera-agnostic)
*Binding law | Current, amended 2010*

**Objective Summary:** Makes it a class 2 misdemeanor to knowingly observe or photograph another person's intimate parts without consent, where the person has a reasonable expectation of privacy. The definition of "photograph" expressly includes drone-capable capture methods (motion picture, videotape, live feed, digitally reproduced visual material), though the statute does not name drones specifically.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Routine aerial mapping, inspection, and construction-progress photography is far outside the conduct this statute targets, but avoid incidental capture of private outdoor spaces (yards, pools, windows) where individuals might have a reasonable expectation of privacy.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** This is an intent-based statute requiring knowing observation of intimate parts specifically — document the professional/survey purpose of a flight near residential property, but this presents low practical risk for standard commercial AEC UAS work.
### Colo. Rev. Stat. § 41-1-107 — Landowner Airspace Rights and Civil Trespass
*Binding law | Current*

**Objective Summary:** Recognizes a surface landowner's interest in the airspace above their land, providing a statutory basis for civil trespass claims arising from intrusive overflights. Federal law controls the navigable airspace itself; this statute addresses civil liability for overflights that unreasonably interfere with a landowner's use and enjoyment of their property.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Obtain landowner consent or a documented right of access before flying low-altitude survey or inspection missions over adjacent private parcels outside the project boundary.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** This is a civil-liability statute distinct from FAA compliance and the criminal statutes above; the exact contours of "interference" sufficient to support a claim were not independently verified against Colorado case law in this pass.
## 3. State Agency and Land-Management UAS Requirements

### Parks — Colorado Parks and Wildlife (CPW) Commission (Manned-Aircraft Prohibition; No Verifiable UAS-Specific Subsection)
*Binding administrative regulation | Current for the confirmed manned-aircraft provision; a widely-cited UAS-specific citation could not be verified*

**Objective Summary:** CPW's complete Chapter P-1 regulation (2 CCR 405-1, effective May 1, 2017, remaining in force until repealed, amended, or superseded) was fetched and read in full directly from cpw.state.co.us in this retrofit pass — not just the single subsection reviewed originally. It prohibits landing or taking off with any "aircraft" on Parks and Outdoor Recreation Lands absent specific authorization or an emergency (#100.b.15); "aircraft" is expressly defined as manned-flight equipment (airplanes, helicopters, gliders, balloons, hang gliders, parachutes, etc.) and does not on its face include UAS. A UAS-specific prohibition — repeated across numerous secondary drone-law compilation sites (dronelaws.us, flyusi.org, pilotinstitute.com, uavcoach.com, dronesgator.com, propelrc.com) as "Regulation #100-c.24," effective January 1, 2018 — could not be located anywhere in CPW's own published text in this pass, and the cited subsection format does not match Chapter P-1's actual lettering scheme (subsection "c" does not exist under #100 at all). None of the secondary sources repeating this citation point to a primary CPW document. This project treats an unsourced citation repeated verbatim across many mutually-reinforcing secondary sites, with no primary document ever cited by any of them, as a red flag for citation-chain drift or fabrication rather than a verified rule.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Continue to treat CPW-administered state parks, state wildlife areas, and state trust lands as effectively off-limits for UAS as a conservative operating posture, but do not cite "Regulation #100-c.24" to a client as a verified provision — it could not be confirmed against CPW's own text in two independent research passes. CPW may still act against UAS operators under general trespass or unauthorized-use theories even without a UAS-specific aircraft subsection.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Advise that the frequently-cited "CPW Regulation #100-c.24" cannot currently be verified as an existing provision based on a direct, full read of CPW's own published Chapter P-1 text; recommend written confirmation from CPW's Office of the Regulations Manager before either relying on or discounting a UAS-specific state-park prohibition for a specific project.
### Wildlife — CPW Prohibition on Using UAS to Aid Hunting or Wildlife Scouting (2 CCR 406-0, Art. IV, #004(C))
*Binding administrative regulation | Effective January 1, 2018; full current text confirmed directly in this retrofit*

**Objective Summary:** The current text of 2 CCR 406-0, Article IV, #004(C) was fetched and read directly from the Colorado Secretary of State's CCR database in this retrofit pass, confirming the exact operative text: "It shall be unlawful to use a drone to look for, scout, or detect wildlife as an aid in the hunting or taking of wildlife," with "drone" defined to include any unmanned or remotely guided flight contrivance (also called a UAV or UAVS). This applies to pre-hunt scouting as well as active hunting. Separately, using a drone to harass wildlife remains unlawful. Reported penalties range from $70 (small game) up to $125,000 for trophy species under Colorado's "Samson Law" framework (not independently re-verified against a primary penalty schedule in this pass).

**Practical Interpretation**

- **AEC Industry UAS Expert:** Plan environmental-monitoring, habitat-mapping, or resource-inventory flights to avoid any activity that could be read as scouting or detecting wildlife for hunting purposes, with a conservative standoff buffer near known wildlife concentrations during hunting seasons.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document the survey/mapping purpose of any UAS flight over wildlife habitat; CPW has been reported to actively monitor social media for evidence of violations, so retain flight logs establishing a non-hunting purpose.
### Public Safety — Center of Excellence for Advanced Technology Aerial Firefighting (CDPS)
*Official agency policy / binding statutory program | Ongoing, established 2017*

**Objective Summary:** HB 17-1070 (2017) directed the Center of Excellence, within the Colorado Department of Public Safety, to study and pilot UAS integration for firefighting, search and rescue, accident reconstruction, crime-scene documentation, and other public-safety functions. SB 19-020 (codified at § 24-33.5-1228, C.R.S.) provided ongoing funding for a system to patrol wildland-fire airspace using drones.

**Practical Interpretation**

- **AEC Industry UAS Expert:** This governs state/local government operations rather than private commercial operators directly, but AEC firms performing wildfire-related mapping or damage-assessment work for a Colorado public-safety agency should coordinate directly with the CoE to deconflict airspace, particularly during active TFRs.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Confirm whether a specific state or local government contract incorporates CoE protocols as binding contract terms.
### Professional Licensing — DORA State Board of Licensure for Architects, Professional Engineers and Professional Land Surveyors
*Binding general regulation | No Colorado-specific UAS guidance located, now confirmed across two independent research passes*

**Objective Summary:** Colorado's licensing framework (Title 12, Article 120, C.R.S., re-confirmed directly against Justia's current codification in this pass) requires PE/PLS licensees to practice only in fields in which they are, by education and/or experience, competent and proficient. No standalone Colorado-specific board guidance addressing UAS-derived photogrammetry, LiDAR, or mapping products was located — a fresh, independent search (including the 3 CCR 720 rule series) was re-run in this retrofit pass and again found none. A frequently-cited secondary source describing a "Rule 415" UAS competency standard was found to actually reference California's licensing framework, not Colorado's.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Route UAS-derived photogrammetry/LiDAR mapping products through a Colorado-licensed PE or PLS for review under the existing general competency framework before delivery on any official deliverable.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Document licensed-professional review and QA/QC of UAS-derived deliverables; do not cite the "Rule 415" language found in some secondary sources as a Colorado authority, since it traces to California law.
## 4. State Preemption of Local Ordinances

**Objective Summary:** No Colorado statute broadly preempting local UAS regulation was located. A 2026 bill that would have limited local regulatory authority over UAS ownership, operation, design, and similar matters (SB26-024, the "Unmanned Aircraft Systems Rights and Authorities Act") was postponed indefinitely by the Senate Local Government & Housing Committee on February 25, 2026 (Section 5 below). Secondary sources document an extensive municipal/county ordinance patchwork, including Denver, Boulder, Boulder County, Colorado Springs, Village of Cherry Hills, Telluride, Lakewood, Aurora, Fort Collins, Loveland, Windsor, and Vail, plus private ski-resort UAS prohibitions (Aspen Skiing Company, Vail Resorts).

**Practical Interpretation**
- **AEC Industry UAS Expert:** Do not assume Colorado state law displaces local drone ordinances — the local-ordinance landscape is unusually dense and varied, spanning major population centers and mountain resort communities with materially different rules. A project-specific municipal/county ordinance check will be necessary in a later research phase.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Flag for the client that Colorado's local-ordinance landscape is at least as significant as — and likely more consequential than — the state-level rules summarized here; advise local counsel or a jurisdiction-specific ordinance check before relying on this state-level summary alone.

## 5. Non-Enacted Proposals

### No Enacted Critical-Infrastructure or Correctional-Facility-Specific Drone Statute
*Research result | Bills died in committee: HB 15-1555, HB 15-059, HB 16-1026*

**Objective Summary:** Unlike Texas or New York, Colorado has not enacted a standalone statute prohibiting UAS operation over or near critical infrastructure, correctional facilities, airports, or sports venues as such. HB 16-1026 (drones near airports and correctional facilities), HB 15-1555 (criminal trespass/harassment by drone), and HB 15-059 (limiting law enforcement drone use) all died in committee.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not apply a Texas- or New York-style 500-ft-buffer facility-protection framework to Colorado projects — no equivalent statute currently exists, though standard site-access, safety, trespass, and FAA airspace considerations still apply near such facilities.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Do not represent to a client that Colorado imposes facility-specific UAS criminal exposure comparable to Texas or New York; monitor for future legislative activity given the pattern of repeated bill introductions.
### SB26-024 — "Unmanned Aircraft Systems Rights and Authorities Act" (Postponed Indefinitely)
*Proposed or pending authority | Not enacted — postponed indefinitely Feb. 25, 2026*

**Objective Summary:** Would have authorized statewide recreational and lawful commercial drone operation, prohibited local UAS registration requirements beyond state/federal law, and established/limited state and local regulatory authority — local governments would have retained authority only over their own drones, drones launching/landing on their property, and generally applicable nuisance-type ordinances. The Senate Local Government & Housing Committee adopted twelve amendments before voting 5-2 to postpone the bill indefinitely.

**Practical Interpretation**

- **AEC Industry UAS Expert:** Do not rely on SB26-024 for any current compliance purpose — it did not pass, and Colorado's current local-ordinance patchwork (Section 4) remains in full force.
- **Agency Practitioner:** Not applicable — no agency process.
- **UAS Procurement Expert:** Not applicable — no procurement or equipment-selection implication identified.
- **AEC Industry Legal Counsel:** Monitor for reintroduction in a future session; if a similar bill passes, revisit the local-ordinance research category since the compliance landscape would change materially.
## 6. Unresolved Operational Questions

- **CPW state park UAS regulation citation:** RESOLVED IN THIS RETROFIT PASS to the extent verifiable: the full current Chapter P-1 (2 CCR 405-1) text was fetched and read directly, confirming no UAS-specific subsection exists in CPW's own published document and that the widely-cited "Regulation #100-c.24" cannot be traced to any primary source. Direct written confirmation with CPW's Office of the Regulations Manager is still recommended before a specific client engagement turns on this point.
- **§ 41-1-107 full text:** RESOLVED IN THIS RETROFIT PASS — full current statutory text fetched and read directly against Justia's codification, confirming the register's description.
- **CPW wildlife regulation (2 CCR 406-0) full text:** RESOLVED IN THIS RETROFIT PASS — full current rule text (Article IV, #004(C)) fetched and read directly against the Colorado Secretary of State's official CCR database.
- **State-agency UAS procurement policy:** No Colorado-specific state-agency drone procurement restriction or foreign-hardware ban (comparable to Texas's Prohibited Technologies List) was located; federal FAR restrictions on covered foreign entities (e.g., DJI, Autel) apply independently to federally funded work. Not independently re-searched in this pass.
- **Local ordinances:** Out of scope for this phase, but flagged as materially significant and unusually dense — see Section 4.
- **Critical-infrastructure/correctional-facility and state-preemption negative findings:** Moved to `CO_UAS_Research_Checklist.md` in this retrofit pass per the project's negative-finding-in-register governance principle (`Agent_Instructions.v6.md` §5.2); no longer separate register rows (previously CO-006 and CO-007).

## 7. Confidence Summary

| Finding | Confidence |
|---|---|
| CRS § 18-8-104 (drone obstruction of public safety operations) | High — verified directly against Justia's codification |
| CRS § 18-7-801 (criminal invasion of privacy) | High — verified directly against Justia's codification |
| CRS § 41-1-107 (landowner airspace rights / civil trespass) | High — full current text fetched and read directly against Justia's codification in this retrofit |
| CPW manned-aircraft state-park prohibition (2 CCR 405-1, #100.b.15) confirmed; UAS-specific "#100-c.24" citation unverifiable | Moderate — full regulation text read directly; the secondary-source UAS-specific citation could not be traced to any primary document |
| CPW wildlife-scouting UAS restriction (2 CCR 406-0, Art. IV, #004(C)) | High — full current rule text fetched and read directly against the Colorado Secretary of State's CCR database |
| No enacted critical-infrastructure/correctional-facility statute | Moderate — negative finding corroborated across official issue brief and bill-history searches; now in checklist |
| No state preemption of local ordinances | Low — negative finding; municipal-ordinance survey based on secondary source; now in checklist |
| SB26-024 (postponed indefinitely) | High — verified directly against the Colorado General Assembly's official bill-tracking page |
| Center of Excellence UAS program (§ 24-33.5-1228) | High — verified directly against Legislative Council Staff issue brief |
| General professional-licensing competency framework | Moderate — framework re-confirmed directly; no Colorado-specific UAS guidance located across two independent search passes |

*This document is objective legal/regulatory summary plus labeled practical interpretation. It is not legal advice; consult Colorado counsel for project-specific compliance determinations. Local ordinances — which are unusually significant in Colorado — and tribal UAS considerations are out of scope for this phase per current research instructions.*
