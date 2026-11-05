# LLM evaluation and model cards

Description: Use when designing, running, analysing or reporting an evaluation of an LLM or LLM-based application (benchmarks, task evals, LLM-as-judge, human evaluation, red teaming), or when writing a model card, system card or datasheet.

## Defer to installed skills
- Study design and reporting standards: empirical-se-standards (ACM SIGSOFT Empirical Standards).
- Paper writing: scientific-writing. Disclosure of AI use in the paper: ai-use-disclosure.
- Regulation: eu-ai-act (Annex IV technical documentation, GPAI duties), nist-ai-rmf (MEASURE function), iso42001 (management system controls).

## Workflow
1. Write the evaluation question: which decision will the result inform? Name the system under test, the users, the failure that matters most.
2. Choose instruments. Public benchmarks give comparability; task-specific evals measure the actual use. Use both when you can, and say why each was chosen.
3. Check contamination and leakage: benchmark release date versus model training cutoff, search for test items in public training corpora when possible, paraphrase or rebuild a held-out set, keep private test data off public tools. Report what you checked and what you could not check.
4. Run with a harness and pin it: EleutherAI lm-evaluation-harness or Inspect. Record harness commit or version.
5. Statistics: run several seeds or samples per item where outputs vary; report mean with a confidence interval (bootstrap over items is a common choice); compare systems on the same items with paired tests; report number of items, runs and any filtering. No specific statistics source has been verified for this skill yet: cite a textbook or paper only after you open it.
6. LLM-as-judge: validate the judge against human labels on a sample and report agreement; randomise or swap answer order; hide system identity; control for length; avoid using the same model family as judge and candidate; publish the judge prompt.
7. Human evaluation: write a rubric with examples, train raters, blind them, use at least two raters on an overlap set, report inter-rater agreement (for example Cohen's or Krippendorff's alpha, chosen by data type) and how disagreements were resolved. Get ethics approval when humans are participants (ethics-committee skill).
8. Red teaming basics: define harms in scope, recruit varied testers, log every attack with prompt, output, severity, and fix status; retest after fixes. Do not publish working exploit prompts without a disclosure plan.
9. Report and card it (template below).

## Reproducibility log (one row per run)
model name and exact version or checkpoint hash, provider and API endpoint, access date, system prompt and user prompt templates (files), decoding settings (temperature, top_p, max tokens, stop sequences), seed, number of samples, harness name and version or commit, dataset name, version and split, scoring code commit, judge model and prompt if used, hardware, cost, date and time with time zone.

## Model card / system card template
Based on Mitchell et al. 2019 sections, extended for LLM systems.
1. Model or system details: developer, date, version, type, base model, license, contact.
2. Intended use: primary uses and users; out-of-scope uses.
3. Factors: groups, languages, domains, environments that may change performance.
4. Metrics: what is measured, why, thresholds, uncertainty method.
5. Evaluation data: source, version, preprocessing, contamination checks.
6. Training data: summary or pointer to a datasheet (Gebru et al.).
7. Quantitative results: disaggregated by factor, with intervals and run counts.
8. Safety and red-team findings: scope, method, open issues.
9. Ethical considerations and risks.
10. Caveats and recommendations.
11. Regulatory mapping when relevant: EU AI Act Annex IV items (use eu-ai-act skill), NIST AI RMF MEASURE outcomes (nist-ai-rmf skill).

## Verified anchors (checked 2026-10-31)
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., Gebru, T. (2019). Model Cards for Model Reporting. Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* 2019). https://doi.org/10.1145/3287560.3287596
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., Crawford, K. (2021). Datasheets for Datasets. Communications of the ACM. https://doi.org/10.1145/3458723
- Liang, P., Bommasani, R., Lee, T., et al. Holistic Evaluation of Language Models. Transactions on Machine Learning Research, 2023. arXiv:2211.09110, https://openreview.net/forum?id=iO4LZibEqW
- EleutherAI lm-evaluation-harness: https://github.com/EleutherAI/lm-evaluation-harness
- Inspect (UK AI Security Institute): https://inspect.aisi.org.uk/
- ACM SIGSOFT Empirical Standards: https://github.com/acmsigsoft/EmpiricalStandards
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act Annex IV (unofficial consolidated reader): https://artificialintelligenceact.eu/annex/4/ . Check text against EUR-Lex Regulation (EU) 2024/1689 via the eu-ai-act skill.

Writing rules: lead with the result, no em dashes, no buzzwords, never report a number you did not compute, never cite a source you did not open.
