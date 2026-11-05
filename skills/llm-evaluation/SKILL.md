---
name: llm-evaluation
description: >-
  Use when designing, running, analysing or reporting an evaluation of an LLM or
  LLM-based application (benchmarks, task evals, LLM-as-judge, human evaluation,
  red teaming), or when writing a model card, system card or datasheet.
---
# LLM evaluation and model cards

Full draft with a 9-step workflow, per-run reproducibility log and an 11-section model/system card template: `resources/llm-evaluation/SKILL.md` (written 2026-10-31).

1. Read that file in full.
2. Defer to installed skills where they fit: eu-ai-act (technical documentation, Annex IV), nist-ai-rmf, iso42001, empirical-se-standards (study design and reporting), scientific-writing (the paper itself).
3. Verified anchors: Mitchell et al., Model Cards for Model Reporting, DOI 10.1145/3287560.3287596; Gebru et al., Datasheets for Datasets, DOI 10.1145/3458723; Liang et al., HELM, TMLR 2023 (arXiv 2211.09110); EleutherAI lm-evaluation-harness and Inspect docs. Confirm full author lists before citing them in a manuscript.
4. The statistics and LLM-as-judge sections cite no sources yet. When the user needs citations there, find and verify them with a scholarly search tool such as Semantic Scholar or arXiv or official pages; never cite from memory.
5. Tool versions, model versions and benchmark leaderboards change fast. Check current docs and give the date checked.
6. Report weaknesses and threats to validity before strengths. Writing rules: no em dashes, no buzzwords, lead with the answer.

## Ek referans

pass@k, pass^k, grader türleri ve regresyon eval kuralları için `references/pass-at-k-and-graders.md` dosyasını oku.
