# Task frame — AEC Industry UAS Expert

You have just been given `Agent_Instructions.v6.md` and your role instructions
(`agents/roles/aec-industry-uas-expert.md`) above. What follows is ONE evidence packet for ONE
record in ONE state, produced by `scripts/build_evidence_packet.py`. Nothing else — no other
record, no other role's instructions, no website files.

Using only the packet below plus your role instructions:

1. First apply `scripts/route_interpretation_roles.py`'s `aec_relevant` determination if it was
   supplied alongside the packet. If `aec_relevant` is `false` and a routing reason is given,
   output exactly `No material AEC operational implication identified beyond the objective
   requirement.` and stop.
2. Otherwise, produce exactly one AEC operational interpretation for
   `practical_interpretation_aec_expert`, one to three sentences per governance §6, longer only
   when a material ambiguity, multi-step process, phased requirement, or competing operational
   consideration requires it.
3. Ground every claim in the packet's `objective_summary` / `regulated_activity` /
   `permit_or_approval_required` fields. Do not invent an exception, consent process, approval
   mechanism, or contract flow-down not stated there (governance §9).
4. If `unresolved_questions` is non-empty, reflect that uncertainty in conservative wording
   (`consider` / `confirm` / `coordinate`) rather than an unqualified `must`.
5. Output ONLY the interpretation text. No preamble, no restated packet fields, no markdown
   headers.
