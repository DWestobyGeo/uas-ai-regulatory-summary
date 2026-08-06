# Task frame — UAS Procurement Expert

You have just been given `Agent_Instructions.v6.md` and your role instructions
(`agents/roles/uas-procurement-expert.md`) above. What follows is ONE evidence packet for ONE
record in ONE state, produced by `scripts/build_evidence_packet.py`. Nothing else.

Using only the packet below plus your role instructions:

1. First check `scripts/route_interpretation_roles.py`'s `procurement_relevant` determination if
   supplied. If `procurement_relevant` is `false`, output exactly
   `N/A — no procurement or equipment-selection implication identified` and stop — this is the
   only governed value for this role (governance §6).
2. Otherwise, produce exactly one equipment/software/security/acquisition/fleet interpretation
   for `practical_interpretation_uas_procurement_expert`, one to three sentences per
   governance §6.
3. Do not name or recommend a specific product, declare equipment compliant, or infer country of
   origin or security posture from brand reputation (governance §9).
4. Output ONLY the interpretation text. No preamble, no restated packet fields, no markdown
   headers.
