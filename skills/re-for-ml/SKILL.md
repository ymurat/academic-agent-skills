---
name: re-for-ml
description: >-
  Use when the user writes or reviews requirements for a system with ML components: EARS statements, data requirements, ML-specific quality requirements, model and dataset documentation, and traceability to data and evaluation.
---
# Requirements engineering for ML

Complements `agile-v`. Agile V gives REQ IDs, verification criteria, approval gates and the requirements-to-test matrix. This skill adds what ML systems need on top: requirement syntax, data requirements, ML quality attributes and traceability to datasets, models and evaluations. Write the final requirements into the Agile V structure.

## Sources in `resources/`
- Structure adapted from SpecForge (MIT, credit: GodModeAI2025, https://github.com/GodModeAI2025/specforge-ai-skill): `resources/re-for-ml/upstream/checklists/ears-syntax.md`, `.../stride-guide.md`, `.../templates/`. Text is in German; the KRITIS and NIS2 parts are German critical-infrastructure rules and do not apply in Turkey. The name SpecForge is a trademark; do not reuse it.
- Verified references: `resources/re-for-ml/verified-references.md`.

## Workflow
1. **Context.** Business goal, decision the model supports, who is affected, what happens when it is wrong (cost of false positives and false negatives). Classify risk with `eu-ai-act` if it may be placed on the EU market.
2. **Functional requirements in EARS (Mavin et al. 2009).** Patterns: ubiquitous ("The system shall..."), event-driven ("When <trigger>, the system shall..."), state-driven ("While <state>..."), unwanted behaviour ("If <condition>, then the system shall..."), optional feature ("Where <feature>..."). Write fallbacks for low-confidence outputs as unwanted-behaviour requirements.
3. **Data requirements.** Source and licence, collection period, population and coverage, labelling procedure and inter-annotator agreement, quality thresholds (missing values, duplicates), split policy (temporal or grouped to avoid leakage), personal data and legal basis (`kvkk`, `gdpr-compliance`), retention. Document with a datasheet (Gebru et al. 2021).
4. **ML quality requirements (Horkoff 2019; Habibullah and Horkoff 2021).** Each with a measurable fit criterion and an evaluation set: effectiveness metric and threshold per subgroup, fairness metric and groups, robustness (perturbations, distribution shift), explainability (who needs which explanation), latency and cost, privacy, security (`ai-threat-review`), monitoring and retraining triggers. Avoid "accurate" or "fair" without a number.
5. **Model documentation.** Model card (Mitchell et al. 2019) with intended use and out-of-scope uses.
6. **Traceability.** Extend the Agile V matrix with columns: REQ ID, dataset version, model version, evaluation script, metric result, approver. Every ML requirement needs a reproducible evaluation.
7. **Review.** Check each requirement for ambiguity, testability and a stated owner; check that data and quality requirements cover what Vogelsang and Borg (2019) report data scientists need (data quality, performance measures, explainability, freedom from discrimination).

## Rules
- Do not invent thresholds; propose ranges and mark them for stakeholder decision.
- For TÜBİTAK proposals, map key requirements to work packages and success criteria (`tubitak-proposal`).
