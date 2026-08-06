# Task frame — Agency Practitioner

You have just been given `Agent_Instructions.v6.md` and your role instructions
(`agents/roles/agency-practitioner.md`) above. What follows is ONE evidence packet for ONE
record in ONE state, produced by `scripts/build_evidence_packet.py`. Nothing else.

Using only the packet below plus your role instructions:

1. First check `scripts/route_interpretation_roles.py`'s `agency_process_relevant`
   determination if supplied. If `agency_process_relevant` is `false`, output exactly
   `N/A — no agency process involved` and stop — this is the only governed value for this role
   (governance §6).
2. Otherwise, produce exactly one agency-process interpretation for
   `practical_interpretation_agency_practitioner`, one to three sentences per governance §6,
   describing the actual government-administered application, registration, permit, waiver, or
   approval process indicated by `permit_or_approval_required` and `issuing_authority`.
3. Do not describe a private-party consent (landowner, lessee) as an agency process. Do not
   invent a fee, portal, or reviewing office not stated in the packet.
4. Output ONLY the interpretation text. No preamble, no restated packet fields, no markdown
   headers.
