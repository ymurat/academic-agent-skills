---
name: agile-v
description: >-
  Use when writing traceable software requirements (REQ IDs, verification
  criteria), reviewing them for ambiguity, deriving tests from baselined
  requirements, building a requirements-to-test traceability matrix, or setting
  up human approval gates.
---
# Agile V: requirements and traceability

Upstream subset of Agile-V/agile_v_skills (CC-BY-SA-4.0, vetted low risk on 2026-10-31, no scripts): `resources/agile-v/`.

1. Always read `agile-v-core/SKILL.md` first, then the sub-skill that fits. Read `SKILL_ROUTING_GUIDE.md` when unsure.

| Sub-skill | Use when |
|---|---|
| `discovery-analyst` | Turning user research into candidate requirements (OBS/INS lineage IDs) |
| `requirement-architect` | Main entry: intent to REQ-XXXX requirements with verification and done criteria, Gate 1, baselining |
| `logic-gatekeeper` | Independent review of draft requirements for ambiguity, conflicts, testability |
| `test-designer` | Test cases from baselined requirements only, never from code |
| `red-team-verifier` | Independent verification against requirements, with approval evidence |
| `validation-agent` | Intended-use validation with representative users |
| `agile-v-human-oversight` | Blind human precommit and approval-gate evidence (draft status upstream) |
| `skills/graph-traceability-agent` | REQ to component to test matrices, orphan detection |

2. Runtime contracts cited by the sub-skills are in `docs/agile-v-runtime/`.
3. References to skills not kept (pipeline, lifecycle, compliance, aibom, gxp): ignore them, or map compliance questions to eu-ai-act, iso42001, nist-ai-rmf, spi-assessment; test design questions stay with test-designer.
4. Human approval gates are real decisions: present them to the user, never approve on their behalf.
5. Attribution: any reused or adapted Agile V text must credit "Agile V, agile-v.org", link CC-BY-SA-4.0, and stay under that license. Keep `LICENSE` and `CITATION.cff` with any shared copy.
6. Prose follows these writing rules: no em dashes, no buzzwords, lead with the answer.
