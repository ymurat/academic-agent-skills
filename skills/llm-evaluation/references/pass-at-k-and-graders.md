# Addendum for llm-evaluation: pass@k, pass^k, grader types, regression evals

## Eval types

**Capability eval**: can the system do something new?
```
[CAPABILITY EVAL: <name>]
Task: <what must be accomplished>
Success criteria:
  - [ ] <criterion 1>
  - [ ] <criterion 2>
Expected output: <description>
```

**Regression eval**: did a change (prompt, model version, retrieval, tool) break what worked?
```
[REGRESSION EVAL: <name>]
Baseline: <model+prompt version, commit or checkpoint>
Cases:
  - case-1: PASS/FAIL
  - case-2: PASS/FAIL
Result: X/Y passed (baseline Y/Y)
```
Rules: freeze the baseline set and its config; rerun on every prompt or model change; store results with version, date, seed and temperature; a regression is any case that passed at baseline and fails now, reported separately from the aggregate score.

## Grader types

1. **Code-based (deterministic)**: exact match, regex, schema validation, unit tests, build success. Preferred whenever the criterion is checkable.
2. **Model-based (LLM-as-judge)**: rubric prompt with an explicit 1-5 scale and required reasoning. Validate against human labels on a sample (report agreement, e.g. Cohen's kappa), fix the judge model and version, randomize answer order to reduce position bias.
3. **Human**: for high-risk or ambiguous outputs. Record reason and risk level (LOW/MEDIUM/HIGH); use at least two raters on a subset to estimate reliability.

## Metrics

- **pass@k**: probability that at least one of k attempts succeeds. With n samples per task and c correct, use the unbiased estimator (Chen et al., 2021): pass@k = 1 - C(n-c, k) / C(n, k), averaged over tasks. Do not compute it as "success in the first k runs".
- **pass^k**: probability that all k independent attempts succeed; estimate per task as C(c, k) / C(n, k) (or (c/n)^k as an approximation). Use for reliability claims and critical paths.
- Report both: pass@k measures capability under retries, pass^k measures consistency. A system with pass@5 = 0.9 and pass^5 = 0.3 is capable but unreliable.
- Give per-task n, temperature and confidence intervals (bootstrap over tasks); compare systems with paired tests on the same tasks.

---
Adapted from [affaan-m/ECC eval-harness](https://github.com/affaan-m/ECC/tree/main/skills/eval-harness), MIT License. pass@k estimator from Chen et al. (2021), arXiv:2107.03374.
