# Washington UAS Research Checklist

- **State:** Washington (WA)
- **Original research date:** 2026-08-01
- **Retrofit date:** 2026-08-07 (Workstream 9 of `planning/AI_RESEARCH_QUALITY_AND_EFFICIENCY_IMPROVEMENT_PLAN.md`; model/checkpoint claude-sonnet-5)
- **Phase:** Phase 1/2 objective + interpretation retrofit — re-verified against current primary sources; original packet's own model/checkpoint was not recorded and is not retroactively guessed at.
- **Scope:** Statewide and state-agency UAS authorities only. Municipal, county, tribal, federal, and site-specific local layers are outside this pass.

| # | Coverage category | Status | Research note |
|---|---|---|---|
| 1 | State statutes and amendments | Applicable source found; one correction | RCW 47.68.250 (state UAS registration, WA-001) re-confirmed directly; its `practical_interpretation_agency_practitioner` field was corrected in this pass — it had incorrectly described the Legislature itself as running a registration/exemption channel, a template mismatch caught by `scripts/validate_research_semantics.py`. RCW 9A.44.115 (voyeurism, WA-005) re-confirmed unaffected. |
| 2 | Administrative rules and regulations | Applicable source found; one new authority added | WAC 352-32-130 (state park UAS rule, WA-003) and WAC 220-413-070 (wildlife-harassment rule, WA-006) re-confirmed directly. **New: Ch. 200-250 WAC (state capitol campus UAS prohibition, WA-011)** — a current, binding rule closing the entire capitol campus to UAS launch/landing except four narrow exclusions — was not previously captured in this register despite being directly relevant to any capitol-campus-sited AEC work. |
| 3 | Executive orders | Reviewed — no applicable UAS-specific source located | Searched 2026-08-07; no Washington governor's executive order specific to UAS located. (The Washington Office of Privacy and Data Protection has issued non-binding UAS policy-development guidelines aimed at legislators/policymakers, not an executive order and not directly applicable to commercial operators — noted but not retained as a register record.) |
| 4 | Court decisions and attorney-general materials | Reviewed — no applicable UAS-specific source located | Searched 2026-08-07; no controlling Washington appellate/supreme court decision or formal Washington Attorney General opinion applying a UAS-specific statute located. |
| 5 | Aviation and transportation agencies | Applicable source found | WSDOT Aviation Division's registration/exemption program (WA-002) re-confirmed directly, including the exemption categories and State UAS Coordinator contact. |
| 6 | Parks, public lands, forestry, fish, wildlife, and natural resources | Applicable source found | WAC 352-32-130 (WA-003) and WAC 220-413-070 (WA-006) re-confirmed. See also row 2 for the new capitol-campus rule (WA-011), which is grounds-based but not a "park" in the WA-003 sense. |
| 7 | Corrections, public safety, emergency management, and critical infrastructure | Resolved — confirmed never enacted | **WA-004 corrected in this retrofit pass.** 2016 Senate Bill 6437 (the proposed drone/correctional-facility felony provision) was verified directly against the Washington State Legislature's own bill-history page: the Senate Rules Committee "X-filed" the bill on 2016-02-25 (removed from further consideration), it never received a House reading, and no successor bill was identified. The prior pass's Low-confidence "UNCERTAIN — verify current codification" status is resolved: there is no current Washington statute specifically criminalizing drone operation near a correctional facility. Retained as an explicit myth-busting record (confidence upgraded Low → High) given the felony-level stakes if a reader assumed otherwise. |
| 8 | Privacy, surveillance, harassment, trespass, and interference | Applicable source found | RCW 9A.44.115 (voyeurism, WA-005) re-confirmed; general (not UAS-specific) but the operative privacy-law risk for aerial photography in Washington. |
| 9 | Procurement, equipment, cybersecurity, and manufacturer restrictions | Reviewed — no state-level source located | Searched 2026-08-07; no Washington-specific state UAS procurement/manufacturer restriction statute or executive order located. Washington public-safety agencies are subject to the federal FCC "Covered List" restriction, which is a federal action. **This negative finding was previously stored as a register record (WA-008); moved to this checklist row in this retrofit pass** per `Agent_Instructions.v6.md` §5.2 (negative findings belong in the checklist, not the source register) and the corresponding validator finding in `scripts/validate_research_semantics.py`. |
| 10 | Professional licensing-board materials | Reviewed — no applicable UAS-specific source located | Ch. 18.43 RCW (Washington's general land-surveyor/engineer licensing statute) was re-confirmed to exist, but despite multiple targeted searches, no standalone Board of Registration for Professional Engineers and Land Surveyors UAS-specific brochure, bulletin, or guidance document was located. A frequently-repeated secondary-source claim citing a "Rule 415" adopted by the Board addressing UAS mapping could not be verified against any WA Administrative Code numbering and appears to be a cross-state citation error (a near-identical unverifiable "Rule 415" citation was previously found and corrected during Arkansas's retrofit, for a different board entirely). **This general statute was previously retained as a register record (WA-007) despite no confirmed direct-UAS provision — a scope-gate risk under `Agent_Instructions.v6.md` §3.2. Moved to this checklist row in this retrofit pass**, consistent with the scope gate's requirement that a generally worded authority needs a direct UAS provision or an official source expressly applying it to UAS. |
| 11 | State preemption | Reviewed — no applicable UAS-specific source located | Searched 2026-08-07; no comprehensive statewide UAS-ordinance-preemption statute located. State law does not broadly preempt local UAS ordinances in Washington (unaffected finding from the prior pass). |

## News-aggregator pass (Section 4.7)

Run 2026-08-07 per `agents/roles/research-expert.md` Section 4.7, as the closing
step of this retrofit. Targeted searches covered: capitol campus (WA-011)
incidents, correctional-facility drone contraband (WA-004 context), state park
violations (WA-003), Fish & Wildlife harassment citations (WA-006), WSDOT
registration enforcement (WA-002), and a 2026 legislative-reintroduction check
for the never-enacted SB 6437 (WA-004). No genuine, precisely-matched Washington
item was found. One search ("prison drone contraband") returned results almost
entirely about a same-named facility in Washington County, Georgia -- correctly
excluded as a state-name collision, not a Washington finding. Per the
news-aggregator role's precision-over-recall principle, zero items is the
correct outcome here. `WA_UAS_News.yaml` was not created; no news-anchor spans
were added. Re-check on the next scheduled currency review (2026-09-07).

## Open verification items

1. Confirm whether the Washington Office of Privacy and Data Protection's UAS policy-development guidelines have been updated or superseded, and whether they warrant a future non-binding-guidance record if their scope changes to something more directly operator-facing.
2. If Washington's Board of Registration for Professional Engineers and Land Surveyors ever publishes a standalone UAS-specific guidance document, add it back to the register as a new record — the general Ch. 18.43 RCW licensing requirement itself remains real and worth mentioning to clients, it simply does not currently meet this register's scope-gate bar on its own.
3. Re-check WAC 200-250 (capitol campus, WA-011) periodically for amendments; it has not been updated since original 2016 adoption, per its own "last update" field.
