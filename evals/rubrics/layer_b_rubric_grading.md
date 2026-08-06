# Layer B — Rubric-Based Model Grading

Per Workstream 4 Layer B of the improvement plan. Apply this rubric to a completed record (one
authority: objective summary plus its four practical-interpretation fields) using a separate
grading pass (human or a different model/context than the one that drafted the record). This is
a process document, not automatable code — `evals/run_fixture_checks.py` only covers Layer A.

## Scale

Score each axis 1-4. A score of 1 or 2 on any axis is a blocking finding for that record; do not
average axis scores into a single pass/fail number, since a single serious defect (e.g.
unsupported inference) should not be hidden by otherwise-strong writing.

| Score | Meaning |
|---|---|
| 4 | Fully meets the standard; no material issue. |
| 3 | Meets the standard with a minor, non-blocking wording issue. |
| 2 | Falls short in a way that should be corrected before publication. |
| 1 | Falls short in a way that creates a compliance or accuracy risk. |

## Axes

### 1. Fidelity to objective evidence
Does every factual claim in the four interpretation fields trace back to the objective summary,
citation, or a fact already established by the record? Flag any claim about process, fee,
timeline, or consequence that is not supported by the objective packet.

### 2. Unsupported inference
Does any field invent an exception, consent process, approval mechanism, defense, retention
requirement, or contract flow-down not stated by the authority (`Agent_Instructions.v6.md` §9)?
Does any field imply that permission cures a prohibition unless the authority says so?

### 3. Role relevance
Is the interpretation specific to what that role actually does (AEC field operations, agency
process, procurement/equipment, legal risk) rather than a generic restatement of the objective
summary in different words? Compare against `evals/pilot_states/{ABBR}_role_applicability.yaml`
for the record's expected relevance.

### 4. Conservative wording
Does the field use `must` only for actual requirements and `consider` / `confirm` / `coordinate`
/ `escalate` for prudent recommendations (`Agent_Instructions.v6.md` §9)? Does confidence-level
hedging match the record's `confidence_level` (compare against
`scripts/validate_research_semantics.py`'s `check_low_confidence_mandatory_language`)?

### 5. Mandatory vs. prudent distinction
Would a reader be able to tell, from the field text alone, which actions are legally required and
which are risk-management best practice? A field that blends both without signaling the
difference fails this axis even if each individual claim is separately accurate.

### 6. Cross-role consistency
Do the four role fields agree on the underlying facts (status, applicability, public/private
scope, permit requirement)? A disagreement between, say, the AEC field and the legal field about
whether a permit is required is a blocking finding regardless of which one is correct.

### 7. Omission of material exceptions
Does the objective summary or interpretation omit an exception, carve-out, or conditional
applicability that the underlying authority actually contains? This is most often caught by
comparing against the full statutory/regulatory text, not just the register row — this axis
often requires the grader to open the cited source, not just read the record.

## Recording results

Drop a dated `{utc_timestamp}_{state_abbr}_layer_b.json` (or `.md`) summary of blocking findings
under `evals/results/` when a Layer B pass is run, per `evals/results/README.md`.
