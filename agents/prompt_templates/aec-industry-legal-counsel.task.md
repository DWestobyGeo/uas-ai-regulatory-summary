# Task frame — AEC Industry Legal Counsel

You have just been given `Agent_Instructions.v6.md` and your role instructions
(`agents/roles/aec-industry-legal-counsel.md`) above. What follows is ONE evidence packet for
ONE record in ONE state, produced by `scripts/build_evidence_packet.py`. Nothing else.

Using only the packet below plus your role instructions:

1. First check `scripts/route_interpretation_roles.py`'s `legal_analysis_relevant`
   determination if supplied. If `legal_analysis_relevant` is `false` and a routing reason is
   given, output exactly `No separate legal-risk implication identified beyond compliance with
   the stated authority.` and stop.
2. Otherwise, produce exactly one legal-risk interpretation for
   `practical_interpretation_legal_counsel`, one to three sentences per governance §6, covering
   contract, documentation, liability, or escalation implications grounded in the packet.
3. Use `must` only for what the packet's `status` / `binding_level` actually establishes as
   binding; use `consider` / `confirm` / `escalate` for prudent risk-management steps. Never
   state that this is legal advice.
4. Output ONLY the interpretation text. No preamble, no restated packet fields, no markdown
   headers.
