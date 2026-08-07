# Louisiana UAS Research Checklist

- **State:** Louisiana (LA)
- **Original research date:** 2026-08-02
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. Local ordinances and tribal rules are outside this pass.

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found | La. R.S. 14:337 (unlawful UAS use / mitigation authority, LA-001) and La. R.S. 2:2 (state preemption, LA-002) re-fetched directly against legis.la.gov and Justia and confirmed to match the register exactly, including the 2025 amendments. Corrected LA-001's and LA-002's interpretation fields, which had a generic "build Legislature approval into pre-mobilization planning" template — wrong, since both are criminal prohibitions/preemption provisions with no permitting process. |
| 2 | Administrative rules and regulations | Applicable source found; one material reversal | LAC 76:III.113 (LDWF land drone ban, LA-003) re-confirmed directly via Justia. **LAC 76:XIX.111(D)(14) (wounded-game drone recovery) REVERSED**: the register previously described a flat prohibition; LWFC passed a Notice of Intent Feb. 5, 2026 permitting FAA-certified drone recovery of mortally wounded deer/bear (with hours/no-weapon/leave-immediately conditions to stay inside the federal Airborne Hunting Act), and LDWF's official 2026-2027 Hunting Regulations (published July 2026) confirm this is now in effect. Confirmed via LWFC's own press release, the Louisiana Illuminator's detailed report, and WBRZ's direct quote of the official regulations pamphlet. The exact final codified paragraph text was not independently fetched (the PDF could not be parsed as text) — confidence held at Moderate. |
| 3 | Executive orders | Reviewed — no applicable UAS-specific source located | Re-searched 2026-08-07; no Louisiana executive order specifically addressing UAS located (Governor Landry's Chinese-AI-platform executive order does not address UAS). **Previously stored as part of a combined negative-finding register record (LA-008); moved to this checklist row** per `Agent_Instructions.v6.md` §5.2 and the corresponding `scripts/validate_research_semantics.py` finding (`check_negative_finding_in_register`). |
| 4 | Court decisions and attorney-general materials | Reviewed — no applicable UAS-specific source located | Re-searched 2026-08-07; no Louisiana appellate/supreme court decision or formal Attorney General opinion directly construing a UAS-specific statute located. Also previously part of LA-008; moved to this row for the same reason as row 3. |
| 5 | Aviation and transportation agencies | Applicable source found | DOTD's Office of Multimodal Commerce Aviation Division UAS page (LA-006) re-confirmed directly against dotd.la.gov — matches the register (drone registration links, "Know Before You Fly," FAA resources; no independent state operating rules stated). |
| 6 | Parks, public lands, forestry, fish, wildlife, and natural resources | Applicable source found | See rows 2 (LA-003, LA-004) and Louisiana Office of State Parks Drone/UAV Policy (LA-005, Field Memo 2018-001) — the field memo PDF could not be re-parsed as text in this pass; confidence held at the existing Moderate level rather than upgraded. |
| 7 | Corrections, public safety, emergency management, and critical infrastructure | Applicable source found | See row 1 (LA-001) — governor's mansion, correctional facilities, and "targeted facility"/critical-infrastructure protections, plus the 2025 law-enforcement mitigation-measures authority (Subsection G). |
| 8 | Privacy, surveillance, harassment, trespass, and interference | Applicable source found | See row 1 (LA-001) — surveillance-of-targeted-facility restriction is the operative record; no separate general privacy/voyeurism UAS statute was located. |
| 9 | Procurement, equipment, cybersecurity, and manufacturer restrictions | Reviewed — no state-level source located | Re-searched 2026-08-07; no enacted Louisiana state-agency UAS procurement/country-of-origin restriction located. 2024 HB 915 (Chinese-manufactured UAS procurement ban) re-confirmed died in House committee, never enacted. This negative finding was previously part of register record LA-008; moved to this checklist row for the same reason as rows 3-4. |
| 10 | Professional licensing-board materials | Applicable source found (general statute); no board-specific UAS guidance | La. R.S. 37:682 (LA-007) re-fetched directly from legis.la.gov/Justia and confirmed to match the register exactly. No standalone LAPELS UAS-specific guidance located after a fresh search; LAPELS's full posted Board Rules (Title 46, Chapter 27) were not reviewed section-by-section in this pass either. |
| 11 | State preemption | Applicable source found | See row 1 (LA-002, La. R.S. 2:2). |

## Open verification items

1. Confirm the exact final codified text of LAC 76:XIX.111(D)(14) as amended for the 2026-2027 season directly with LDWF or the Louisiana Register — this retrofit relied on the agency's own regulations-pamphlet summary and commission meeting record, not a directly quoted administrative-code paragraph.
2. Fully retrieve and parse the Louisiana Office of State Parks 2018 Field Memo (LA-005) to confirm whether a public-facing commercial-UAS/filming permit process exists, analogous to other states' park permit regimes.
3. If LAPELS ever publishes standalone UAS-specific guidance, add it to the register as a new record.
4. R.S. 14:337 Subsection G's law-enforcement mitigation-measures trigger does not expressly exempt a compliant commercial Part 107 flight — AEC firms operating near "targeted facility" sites should pre-coordinate with facility owners/operators and local law enforcement where practicable.

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/research-expert.md` Section 4.7, as the closing step of this
retrofit. Searched: LA-001 (targeted-facility surveillance / mitigation-measures enforcement),
LA-002 (preemption/local-ordinance disputes), LA-003 (WMA drone-ban enforcement), LA-004
(wounded-game drone recovery rollout), LA-006 (DOTD registration enforcement).

One genuine match found: the Governor's Office's own June 18, 2025 announcement of HB 261 (the
"We Will Act" Act) signing, framing Louisiana as the first state to authorize local law
enforcement to directly neutralize dangerous drones — directly on point for LA-001's Subsection G
mitigation-measures authority. This was already present in the narrative's Section 4
"Non-Regulatory Context" from the original research pass; added to `LA_UAS_News.yaml` and
anchored inline under LA-001 per the now-standard workflow.

Other candidates considered and rejected: the Louisiana Illuminator's and WBRZ's wounded-game
drone-recovery coverage (genuine news, but describes the underlying rule change itself, which
belongs in the register per Section 5 of `agents/roles/news-aggregator.md`, not a news item
layered on top of an unchanged rule — already folded directly into LA-004's objective content
instead); the Chinese-AI-platform executive order (not about UAS).
