---
name: se-stats
description: >-
  Use when the user designs, analyses or reports statistics for a software
  engineering experiment, benchmark of randomized algorithms (search-based SE,
  ML models, test generation), survey, or needs a sample size or power analysis.
---
# SE statistics

Statistical design, analysis and reporting for empirical software engineering. Pair with `empirical-se-standards` (study design and reporting checklist) and `icarus-figures` (plots).

## Sources in `resources/`
- Upstream K-Dense skills (MIT, credit: K-Dense Inc., https://github.com/K-Dense-AI/scientific-agent-skills): `resources/se-stats/upstream/statistical-analysis/`, `.../statistical-power/`, `.../experimental-design/`. Read their `SKILL.md` and `references/` for general test selection, assumptions, power and APA reporting.
- SE script: `resources/se-stats/scripts/se_effects.py` (CSV with columns `algo,run,value`; add `--lower` when lower is better). Outputs Mann-Whitney p, Holm and BH adjusted p, A12, Cliff's delta.
- Verified references: `resources/se-stats/references/verified-references.md`. Cite only from this file or after a fresh Crossref check.

## Workflow
1. **Clarify the design.** Unit of analysis, independent and dependent variables, paired or independent samples, number of subjects or runs, hypotheses (stated before seeing data). If the study is not yet run, do a power analysis with the upstream `statistical-power` scripts and report the assumed effect size and its source.
2. **Randomized algorithms (Arcuri and Briand 2011, 2014).**
   - At least 30 independent runs per algorithm and problem instance unless cost forbids; report the number and the seeds.
   - Use non-parametric tests by default: Mann-Whitney U (Wilcoxon rank-sum) for independent runs, Wilcoxon signed-rank for paired data (same instances, same seeds).
   - Always report an effect size next to p: Vargha-Delaney A12 for "probability A beats B"; Cliff's delta (= 2*A12 - 1) when the venue expects it.
   - Report per instance, then summarise across instances; do not pool runs from different instances into one test.
3. **Many comparisons.** With k algorithms or many instances, correct p values: Holm (family-wise) when claims are confirmatory, Benjamini-Hochberg (FDR) when exploratory. For ranking many treatments (for example defect prediction classifiers), Friedman plus post hoc test, or Scott-Knott ESD (Tantithamthavorn et al. 2017; R package `ScottKnottESD`) which merges groups with negligible effect.
4. **Human-subject experiments and surveys.** Check assumptions with upstream `assumption_checks.py`; prefer robust methods (Kitchenham et al. 2017) for small, skewed samples. Likert items: treat as ordinal; report medians and distributions; do not average a single item. Combine with `qualitative-methods` for open answers.
5. **Report.** Descriptive table (median, IQR, mean, SD), test name, statistic, exact p, corrected p, effect size with magnitude label and confidence interval where available, and a threats-to-validity paragraph on conclusion validity. Put code and raw results in the replication package (`empirical-se-standards` artifact section).

## Rules
- Never invent data, p values or effect sizes. Run the computation and show the command.
- State the alpha level and correction method before results.
- Statistical significance is not practical significance; interpret the A12 magnitude.
- For Turkish manuscripts, use `tr-academic-style` terms (anlamlılık düzeyi, etki büyüklüğü) and keep test names in English.
- Holm 1979 citation is not yet verified; check before citing.
