"""Populate the four Phase 2 interpretation fields for one completed state packet.

The script deliberately drafts from the verified source-register packet only. It does
not fetch sources or alter objective fields. Run with a two-letter state abbreviation.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PENDING = "PENDING — Phase 2"


def has(text: str, *terms: str) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def has_survey_technical(text: str) -> bool:
    return bool(re.search(r"\bsurvey(?:s|ed|ing|or|ors)?\b", text, re.I)) or has(
        text, "photogram", "lidar", "mechanical shutter", "accuracy", "ground control", "checkpoint"
    )


def has_payload_restriction(text: str) -> bool:
    return has(text, "weapon", "projectile", "contraband", "payload") or bool(
        re.search(r"\b(?:drop|drops|dropped|dropping)\b", text, re.I)
    )


def combined(row: dict[str, str]) -> str:
    return " | ".join(
        row.get(k, "")
        for k in (
            "source_title", "citation", "uas_topic", "regulated_activity",
            "requirement_type", "permit_or_approval_required", "summary", "notes"
        )
    )


def approval_process(row: dict[str, str]) -> bool:
    text = combined(row)
    permit = row.get("permit_or_approval_required", "")
    if permit.strip().lower().startswith("no"):
        return False
    if permit.strip().lower().startswith("only the federal"):
        return False
    return (
        not permit.lower().startswith("no")
        and has(permit, "yes", "required", "approval", "permit", "license", "register", "consent", "notice", "authorization")
    ) or has(
        row.get("requirement_type", ""),
        "permit", "approval", "license", "registration", "notification", "application", "waiver", "certification"
    ) or has(text, "application form", "request procedure", "registration process")


def agency_process(row: dict[str, str]) -> bool:
    text = combined(row)
    focus = " | ".join(row.get(k, "") for k in ("source_title", "uas_topic", "regulated_party", "regulated_activity", "requirement_type"))
    permit = row.get("permit_or_approval_required", "")
    authority = row.get("issuing_authority", "")
    if has(permit, "landowner consent", "landowner or lessee permission", "owner or lessee consent", "property consent", "property owner consent", "owner's consent", "owner consent", "owner or occupant consent", "owner or lawful-occupant consent", "venue or fireworks-event owner", "consent of the people", "people being surveilled", "property right", "private-property permission") and has(authority, "legislature", "general assembly"):
        return False
    if has(permit, "no agency permit", "no statewide operator permit"):
        return False
    if has(permit, "no general state permit") and not has(focus, "facility", "correction", "school", "critical infrastructure"):
        return False
    return approval_process(row) or has(
        row.get("requirement_type", ""), "report", "filing", "submission"
    ) or has(text, "notify the agency", "report to the commission", "agency notification")


def aec_opinion(row: dict[str, str]) -> str:
    text = combined(row)
    focus = " | ".join(row.get(k, "") for k in ("source_title", "uas_topic", "regulated_party", "regulated_activity", "requirement_type"))
    scope = row["geographic_scope"].rstrip(".")
    authority = row["issuing_authority"]
    title = row["source_title"]
    if row.get("public_agency_only", "").lower().startswith("yes"):
        return (
            "This record does not directly regulate an ordinary privately controlled AEC flight, but it can govern a mission performed for or integrated into the named public agency's program. "
            "Define in the scope and flight plan who authorizes the mission, controls the aircraft, receives the data, and is responsible for the cited records or use restrictions."
        )
    if str(row.get("aec_relevance", "")).lower().startswith("low") or has(combined(row), "sex-offender", "sex offender", "registered offender", "protective order"):
        return (
            "This record has no routine effect on an AEC mission or ordinary fleet operation because it applies to a separately regulated person or activity. "
            "Do not treat it as a general UAS operating rule; address it only if the stated regulated-party condition is actually present."
        )
    if has(focus, "local regulation", "political subdivision", "municipal", "county", "preemption"):
        return (
            "Use the state rule to identify what a political subdivision may regulate, then check only the controlling property's published operating terms before launch. "
            "Record the applicable boundary, property owner, designated-use area, notice, and permission status in the flight packet without assuming that state preemption eliminates property-use conditions."
        )
    if has(focus, "ticketed event", "fireworks site", "stadium", "event venue"):
        return (
            f"Map the event or fireworks perimeter and active time window for {scope}, obtain any consent expressly available under the rule, and keep launch, route, return-to-home, and contingency areas outside the covered zone unless authorized. "
            "Recheck the event schedule immediately before flight because setup, rehearsal, or ignition activity can change the applicable operating boundary."
        )
    if has_payload_restriction(focus):
        return (
            f"Screen aircraft and payload configuration against {title} before deployment, including release devices, tethered tools, sample systems, and experimental attachments. "
            "Use configuration control so a field crew cannot inadvertently deploy a prohibited or ambiguous payload."
        )
    if has(focus, "livestock"):
        return (
            f"Plan the route and stand-off distance for {scope} so the aircraft does not chase, bunch, separate, distress, or injure livestock. "
            "Coordinate with the owner or handler, brief an immediate retreat or landing trigger, and document any owner-directed husbandry purpose before flight."
        )
    if has(focus, "state park", "state forest", "public land", "public reservation", "nature preserve", "natural area", "department land", "department property", "campus", "university property"):
        if approval_process(row):
            return (
                f"Treat property authorization for {scope} as a pre-mobilization gate and obtain conditions that cover launch, landing, route, dates, aircraft, crew, and sensor purpose. "
                "Confirm whether the approval is site-wide or location-specific and carry the written authorization and field contact with the crew."
            )
        return (
            f"Confirm the controlling land unit and current property-use rule for {scope} before selecting launch and recovery points. "
            "Record the boundary and any closures or site conditions in the flight packet rather than relying on a general statewide assumption."
        )
    if has(focus, "agency contract", "contracted pilot", "contract signing", "contractor approval") and approval_process(row):
        return (
            f"Complete the named agency's UAS coordination before contract execution or flight scheduling, and make the approved operating, privacy, cybersecurity, data, and documentation conditions part of the project plan. "
            "Confirm whether subcontractors and previously collected outside data require separate review rather than assuming the prime contractor's approval covers them."
        )
    if has(focus, "wildlife", "hunt", "game", "nest", "habitat", "fish"):
        return (
            f"Screen the mission for active hunting and wildlife sensitivity within {scope}; plan altitude, stand-off distance, route, observers, and abort criteria to avoid pursuit, harassment, surveillance of participants, or assistance to a taking. "
            "Document the project's environmental or infrastructure purpose and pause if animals materially react or the flight would disrupt lawful hunting or fishing."
        )
    if has(focus, "critical infrastructure", "critical facility", "correction", "prison", "jail", "military", "airport", "crewed aircraft", "school property", "school grounds"):
        lead = "Treat written facility coordination as a pre-mobilization gate" if approval_process(row) else "Map the covered facility and conservative stand-off area during desktop planning"
        return (
            f"{lead} for work within {scope}; do not rely only on flight-app geofencing or a client's general site-access instruction. "
            "Include lost-link, return-to-home, emergency landing, sensor-direction, and observer controls that prevent an unintended facility overflight, prohibited capture, loitering, or interference."
        )
    if has(focus, "state park", "state forest", "public land", "nature preserve", "natural area", "department land", "department property", "campus", "university property"):
        if approval_process(row):
            return (
                f"Treat property authorization for {scope} as a pre-mobilization gate and obtain conditions that cover launch, landing, route, dates, aircraft, crew, and sensor purpose. "
                "Confirm whether the approval is site-wide or location-specific and carry the written authorization and field contact with the crew."
            )
        return (
            f"Confirm the controlling land unit and current property-use rule for {scope} before selecting launch and recovery points. "
            "Record the boundary and any closures or site conditions in the flight packet rather than relying on a general statewide assumption."
        )
    privacy_focus = has(focus, "privacy", "surveillance", "stalk", "harass", "tracking", "voyeur") or (
        has(focus, "recording", "photograph") and has(focus, "person", "private", "dwelling", "occupant")
    )
    if privacy_focus:
        return (
            f"Use a mission-specific collection plan for {scope} that limits camera angle, dwell time, audio, zoom, thermal capture, and retention to the contracted purpose. "
            "Brief the crew on aborting or redirecting collection when people, residences, or unrelated activity enter the sensor footprint."
        )
    if has_survey_technical(focus):
        return (
            f"Translate {title} into the project flight plan and QA/QC checklist before mobilization, including the required control, collection, accuracy, retention, and deliverable items that apply to the work. "
            "Resolve any conflict between the agency guidance and the executed scope before collection so a technically successful flight does not produce an unacceptable survey deliverable."
        )
    if has(focus, "wildlife", "hunt", "game", "nest", "habitat", "fish", "livestock"):
        return (
            f"Screen the mission for active hunting and wildlife sensitivity within {scope}; plan altitude, stand-off distance, route, observers, and abort criteria to avoid pursuit, harassment, or assistance to a taking. "
            "Document the project's environmental or infrastructure purpose and pause if animals materially react to the aircraft."
        )
    if has(focus, "pesticide", "aerial application", "spray", "dispens"):
        return (
            f"Treat {title} as a separate mobilization track from ordinary imaging: verify the operator, every pilot, each aircraft, payload, product, and mission approval before scheduling field work. "
            "Build extra lead time for licensing, aircraft configuration, training records, label review, and sensitive-site coordination."
        )
    if has(row.get("requirement_type", ""), "exemption from state aircraft registration"):
        return (
            "Do not add a Virginia aircraft-registration task for the unmanned aircraft covered by this express exemption. "
            "Keep the exemption citation with the fleet compliance record while continuing to screen for mission-specific property, facility, wildlife, and client requirements."
        )
    if has(focus, "emergency", "firefight", "disaster", "incident", "search and rescue"):
        return (
            f"Make active emergency operations a dispatch and in-field stop-work check for {scope}. "
            "The remote pilot should have a clear deconfliction contact and an immediate land-or-relocate procedure if responders, temporary restrictions, or crewed aircraft appear."
        )
    if approval_process(row):
        if has(authority, "legislature", "general assembly"):
            return (
                f"Treat the applicable written consent or authorization under {row['citation']} as a pre-mobilization gate and ensure it covers the site, dates, aircraft, crew, payload, and purpose. "
                "Do not lock the field schedule until the approving person and any notice, boundary, insurance, or operating conditions are documented."
            )
        return (
            f"Treat the {authority} process as a pre-mobilization gate: confirm the current submission route and obtain written authorization that covers the site, dates, aircraft, pilots, payload, and purpose. "
            "Do not lock the field schedule until agency lead time and any insurance, notification, or site-condition requirements are known."
        )
    return (
        f"Add {title} to the mission-specific legal and site screening for {scope}. "
        "Brief the crew on the triggering conduct and document the operational boundary or exception relied upon before launch."
    )


def agency_opinion(row: dict[str, str]) -> str:
    if has(combined(row), "sex-offender", "sex offender", "registered offender"):
        return (
            "This is a personal reporting process for the specifically regulated population, not an aircraft or operator approval for an AEC mission. "
            "A covered individual should confirm the current UAS-identification reporting method and deadlines directly with the named registering agency."
        )
    focus = " | ".join(row.get(k, "") for k in ("source_title", "uas_topic", "regulated_activity", "requirement_type", "permit_or_approval_required"))
    if has(focus, "professional licensure", "professional-practice", "licensure boundary", "licensed surveyor", "professional surveying"):
        return (
            "The professional board does not approve an ordinary drone flight merely because a UAS is used; its process attaches when the resulting service is regulated professional practice. "
            "Confirm the responsible licensee, firm authorization, scope classification, required supervision, certification, recordation, and current board guidance before offering or sealing the deliverable."
        )
    if not agency_process(row):
        return "N/A — no agency process involved"
    if has(focus, "wildfire", "wildland fire", "incident commander"):
        return (
            "Coordinate through the current incident-command structure and obtain express mission permission plus every imposed operating restriction before entering the covered fire scene or restriction. "
            "Permission is operationally time-sensitive; confirm the incident contact and revalidate it immediately before launch rather than relying on an earlier client request."
        )
    if has(focus, "search warrant", "warrant"):
        return (
            "The public agency should route the warrant or exception determination through its established supervisory and legal process; the consultant should not assume it can supply that authority. "
            "Before collection, obtain written agency direction identifying the approved purpose, area, duration, data handling, and the agency official responsible for the determination."
        )
    if has(row.get("permit_or_approval_required", ""), "FAA written approval", "DOD permission", "federal contract"):
        return (
            "Use the specific federal or contracting authority named in the exception and retain its written approval or authorizing contract with the mission file. "
            "The state source does not create a general state waiver, so confirm that the exact aircraft, payload, location, operator, and activity fall within the relied-upon authorization."
        )
    periodic_reporting = has(row.get("regulated_activity", ""), "annual report", "periodic report", "submit report") or has(
        row.get("source_title", ""), "reporting"
    )
    if periodic_reporting and not approval_process(row):
        return (
            f"Use the current reporting instructions of {row['issuing_authority']} and calendar the stated event-driven or periodic deadline; retain the submitted data, transmittal, and acceptance receipt. "
            "Confirm the current form, reporting period, responsible agency contact, amendment method, and whether contractor-held flight or data records must be supplied to the reporting entity."
        )
    authority = row["issuing_authority"]
    focus = " | ".join(row.get(k, "") for k in ("source_title", "uas_topic", "regulated_party", "regulated_activity", "requirement_type"))
    if has(focus, "political subdivision", "local property", "local regulation"):
        authority = "controlling political subdivision or property manager"
    elif has(authority, "legislature", "general assembly") and not has(authority, "department", "commission", "UDOT", "DNR", "parks"):
        authority = row["jurisdiction_name"] if row["jurisdiction_type"].lower() != "state" else "named facility or administering agency"
    permit = row["permit_or_approval_required"].strip()
    text = combined(row)
    details = []
    if has(text, "insurance"):
        details.append("insurance evidence")
    if has(text, "flight plan", "mission plan"):
        details.append("a mission or flight plan")
    if has(text, "map", "location", "boundary"):
        details.append("a location map")
    if has(text, "pilot", "certificate"):
        details.append("pilot credentials")
    if has(text, "aircraft", "registration"):
        details.append("aircraft details")
    if has(text, "fee"):
        details.append("the current fee")
    detail_text = ", ".join(dict.fromkeys(details[:4])) or "the mission description, dates, aircraft, pilot, and requested operating area"
    lead = f"Use the current {authority} application or request channel and provide {detail_text}."
    if permit and len(permit) < 180:
        lead += f" The packet identifies the approval as: {permit.rstrip('.')} ."
    return (
        lead.replace(" .", ".")
        + " Because the verified source does not establish a dependable review time for every case, confirm completeness, reviewer, lead time, approval duration, and field-contact expectations directly with the agency."
    )


def procurement_opinion(row: dict[str, str]) -> str:
    text = combined(row)
    focus = " | ".join(row.get(k, "") for k in ("source_title", "uas_topic", "regulated_party", "regulated_activity", "requirement_type"))
    title = row["source_title"]
    if has(combined(row), "sex-offender", "sex offender", "registered offender", "protective order"):
        return "N/A — no procurement or equipment-selection implication identified"
    if has(focus, "privacy", "trespass") and not has(focus, "retention", "deletion", "biometric", "data security", "cybersecurity"):
        return "N/A — no procurement or equipment-selection implication identified"
    if has(focus, "seller notice", "seller disclosure", "dealer notice", "sale of a drone", "selling a drone"):
        return (
            "Retain the required point-of-sale notice with the purchase record and include it in receiving and asset-onboarding checks. "
            "The notice is not proof that the aircraft is registered or mission-eligible, so procurement should separately verify the model, serial number, applicable registrations, software account, and operating documentation."
        )
    if has(focus, "company-owned", "company owned", "equipment ownership", "contractor equipment"):
        return (
            "Maintain documentation showing which legal entity owns or controls each aircraft and payload assigned to the contract, including any lease, affiliate, or subcontractor arrangement. "
            "If the agency policy expects company-owned equipment, obtain a written project exception before mobilizing a rented, employee-owned, affiliated-company, or subcontractor system."
        )
    if has(row.get("requirement_type", ""), "exemption from state aircraft registration") or (
        row.get("permit_or_approval_required", "").lower().startswith("no") and has(focus, "aircraft registration")
    ):
        return (
            "Do not create a state-registration purchasing gate where this record expressly exempts unmanned aircraft. "
            "Keep federal registration and asset records current, and separately check whether a mission-specific permit, property rule, weight threshold, or public-client specification still affects the selected system."
        )
    if has(focus, "manufacturer", "country-of-origin", "country of origin", "covered foreign", "foreign-adversary", "foreign adversary", "cybersecurity", "approved list", "supply chain", "replacement program"):
        return (
            f"Treat {title} as a time-sensitive eligibility check at solicitation and again before purchase or assignment to a public project. "
            "Maintain manufacturer and component attestations, model and serial inventories, software and data-hosting details, funding-source restrictions, and a replacement path; do not assume a restriction on a public owner automatically binds a consultant unless the contract says so."
        )
    aircraft_registration = has(focus, "aircraft registration", "registered aircraft", "airworthiness", "operating weight", "55 pound", "55-pound", "uas state registration", "state registration requirement") or (
        has(focus, "uas registration", "uav registration") and not has(focus, "park", "forest", "property", "campus", "offender")
    )
    if aircraft_registration:
        return (
            "Maintain asset-level records for registration status, weight with each payload, serial number, airworthiness documents when applicable, and renewal dates before assigning an aircraft to this state. "
            "Fleet planning should account for fees, renewal lead time, and whether swapping an aircraft or payload changes the approval or registration basis."
        )
    if has(focus, "pesticide", "aerial application", "spray", "dispens") or has_payload_restriction(focus):
        return (
            "Use configuration-controlled payload interfaces and maintain documentation showing the purpose, operating limits, release safeguards, aircraft weight, and approved mission configuration. "
            "Avoid buying or fielding attachments whose capability could place an otherwise ordinary mapping aircraft within a weapon, projectile, contraband-delivery, or regulated dispensing provision."
        )
    if row.get("public_agency_only", "").lower().startswith("yes") and has(focus, "facility boundary", "publication", "fixed-site"):
        return "N/A — no procurement or equipment-selection implication identified"
    if has_survey_technical(focus):
        return (
            "Specify aircraft, positioning, camera, payload, processing software, and storage that can produce the cited accuracy evidence and deliverables without proprietary-format lock-in. "
            "Acceptance testing should verify the complete workflow—control, capture, processing, export, and archive—not only nominal aircraft or sensor specifications."
        )
    if has(focus, "retention", "deletion", "data security", "records", "public record", "disclosure", "facial recognition", "biometric"):
        return (
            "Select capture and processing systems that support role-based access, exportable audit logs, configurable retention and deletion, defensible redaction, and delivery in the agency's required format. "
            "Confirm cloud hosting, backup replication, account ownership, and vendor deletion behavior before the platform is approved for covered data."
        )
    if has(focus, "geofence", "remote identification", "remote id", "night", "lighting", "noise", "sound"):
        return (
            "Include the cited technical operating condition in acquisition and acceptance criteria, and verify it with the aircraft's actual firmware, payload, and mission software rather than a marketing specification. "
            "Keep configuration and test evidence with the asset record so field teams can show the assigned system supports the planned operation."
        )
    return "N/A — no procurement or equipment-selection implication identified"


def legal_opinion(row: dict[str, str]) -> str:
    text = combined(row)
    citation = row["citation"]
    title = row["source_title"]
    public_only = row.get("public_agency_only", "").lower() == "yes"
    if approval_process(row):
        return (
            f"Retain the current application, all attachments, written approval, conditions, amendments, and closeout records under {citation}; a client's verbal direction should not substitute for the named authority's authorization. "
            "Escalate if the approving official, property boundary, operating dates, data rights, insurance terms, or ability to use a contractor is unclear."
        )
    if has(text, "penalty", "misdemeanor", "felony", "criminal", "civil action", "liability", "inadmissible", "damages"):
        return (
            f"Treat {title} as a documented stop-work or redesign trigger because the packet identifies criminal, civil, evidentiary, or damage exposure. "
            "The contract and flight record should preserve the site screening, authority or exception relied upon, crew briefing, and incident/escalation path; obtain counsel where the facts sit near an undefined boundary or intent element."
        )
    if public_only:
        return (
            "State in the contract whether the public agency or the consultant is the operator and data custodian, and allocate authorization, disclosure, retention, and records-request duties accordingly. "
            "Do not represent an agency-only power or exception as authority for a privately controlled flight unless the verified source and written mission authorization support that relationship."
        )
    if has(text, "privacy", "surveillance", "recording", "photograph", "tracking", "harass", "stalk"):
        return (
            f"Preserve the mission purpose, property or participant permissions, sensor settings, collection boundary, retention rule, access log, and deletion record relevant to {citation}. "
            "Escalate before using zoom, audio, thermal, recognition, persistent tracking, or secondary data uses that materially expand the agreed collection."
        )
    if has(text, "guidance", "policy", "manual", "memorandum", "advisory"):
        return (
            "Identify whether the cited material is incorporated into the contract, permit, property-use approval, or agency standard before describing it as mandatory. "
            "Where it is not binding, record any deliberate deviation and the equivalent risk control or technical basis accepted by the client."
        )
    return (
        f"Preserve the mission screening and factual basis for compliance with {citation}, including the operating area, purpose, approvals, and any relied-upon exception. "
        "Escalate ambiguous scope, conflicting client direction, or facts that could change the regulated party or activity before flight."
    )


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def choose_record(block: str, rows: list[dict[str, str]], used: set[str]) -> dict[str, str] | None:
    for row in rows:
        if row["record_id"] in block:
            return row
    block_norm = normalize(block)
    best = None
    best_score = 0
    for row in rows:
        if row["record_id"] in used:
            continue
        score = 0
        summary_norm = normalize(row["summary"])
        citation_norm = normalize(row["citation"])
        title_norm = normalize(row["source_title"])
        if len(summary_norm) > 50 and summary_norm[:90] in block_norm:
            score += 100
        if len(citation_norm) > 5 and citation_norm in block_norm:
            score += 50
        title_tokens = set(title_norm.split())
        heading_tokens = set(normalize(block.splitlines()[0]).split())
        score += 3 * len(title_tokens & heading_tokens)
        if score > best_score:
            best_score, best = score, row
    return best if best_score >= 6 else None


def update_summary(path: Path, rows: list[dict[str, str]]) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"(?im)^\*\*Version:\*\*.*$", "**Version:** 2.0 (Phase 2 — practical interpretation complete)", text)
    text = re.sub(
        r"(?im)^\*\*Model\s*/?\s*checkpoint[^:]*:\*\*.*$",
        "**Model / checkpoint:** Objective research model retained from Phase 1; Phase 2 interpretations drafted with OpenAI GPT-5 (Codex; exact checkpoint unavailable)",
        text,
    )
    text = re.sub(
        r"(?ms)^> \*\*(?:Process note|AI research notice)[^\n]*\*\*.*?(?=\n\n)",
        "> **Process note:** Objective research is retained from the Phase 1 source packet. The four practical-interpretation roles were completed in Phase 2 on 2026-08-02 using OpenAI GPT-5 (Codex; exact checkpoint unavailable).",
        text,
    )
    text = re.sub(
        r"(?ms)^Each authority below is presented as.*?(?=\n\n## )",
        "Each authority below retains its verified objective summary and now includes the four Phase 2 practical-interpretation perspectives. The interpretations are AI-generated operational opinions, not legal advice.",
        text,
    )
    block_re = re.compile(r"(?ms)^### .+?(?=^### |^## |\Z)")
    used: set[str] = set()
    matched = 0

    def replace_block(match: re.Match[str]) -> str:
        nonlocal matched
        block = match.group(0)
        if not has(block, "AEC expert interpretation", "AEC Industry UAS Expert", "Practical Interpretation"):
            return block
        row = choose_record(block, rows, used)
        if not row:
            return block
        used.add(row["record_id"])
        matched += 1
        first_bullet = re.search(r"(?m)^- \*\*[^\n]*(?:AEC|Agency|Procurement|Legal)[^\n]*\*\*", block)
        marker = re.search(r"(?m)^\*\*Practical Interpretation\*\*\s*$", block)
        cut = first_bullet.start() if first_bullet else (marker.end() if marker else len(block))
        prefix = block[:cut].rstrip()
        if marker and marker.end() <= cut:
            prefix = block[:marker.end()].rstrip()
        elif not marker:
            prefix += "\n\n**Practical Interpretation**"
        bullets = (
            f"- **AEC Industry UAS Expert:** {row['practical_interpretation_aec_expert']}\n"
            f"- **Agency Practitioner:** {row['practical_interpretation_agency_practitioner']}\n"
            f"- **UAS Procurement Expert:** {row['practical_interpretation_uas_procurement_expert']}\n"
            f"- **AEC Industry Legal Counsel:** {row['practical_interpretation_legal_counsel']}\n\n"
        )
        return prefix + "\n\n" + bullets

    text = block_re.sub(replace_block, text)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    pending_blocks = [m.group(0).splitlines()[0] for m in block_re.finditer(text) if has(m.group(0), "PENDING — Phase 2", "Pending Phase 2 interpretation pass")]
    return matched, pending_blocks


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(r"[A-Za-z]{2}", sys.argv[1]):
        raise SystemExit("Usage: python scripts/apply_phase2.py XX")
    abbr = sys.argv[1].upper()
    dirs = list((ROOT / "States").glob(f"{abbr}_*"))
    if len(dirs) != 1:
        raise SystemExit(f"Expected one state directory for {abbr}, found {len(dirs)}")
    folder = dirs[0]
    csv_path = folder / f"{abbr}_UAS_Source_Register.csv"
    summary_path = folder / f"{abbr}_UAS_Regulatory_Summary.md"
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    if not fieldnames or len(fieldnames) != 33:
        raise SystemExit(f"{abbr}: source register is not the required 33-field schema")
    for row in rows:
        row["practical_interpretation_aec_expert"] = aec_opinion(row)
        row["practical_interpretation_agency_practitioner"] = agency_opinion(row)
        row["practical_interpretation_uas_procurement_expert"] = procurement_opinion(row)
        row["practical_interpretation_legal_counsel"] = legal_opinion(row)
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    matched, pending_blocks = update_summary(summary_path, rows)
    if pending_blocks:
        raise SystemExit(f"{abbr}: summary retains pending blocks: {pending_blocks}")
    print(f"{abbr}: populated {len(rows)} records; updated {matched} printable-summary authority blocks")


if __name__ == "__main__":
    main()
