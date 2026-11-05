---
name: empirical-se-standards
description: >-
  Use when designing, self-checking or reviewing an empirical software
  engineering study against the ACM SIGSOFT Empirical Standards, Runeson and
  Höst, Wohlin et al., and Kitchenham survey guidance.
---
# Empirical SE study design and review (ACM SIGSOFT Empirical Standards)

Rules: formal prose, no em dashes, tables for comparisons. Never invent citations, DOIs, sample sizes or statistics. Summarise the standards in your own words; quote only short phrases with attribution.

Local sources:
- `resources/empirical-se-standards/essential-attributes.md`: essential attribute checklists for all 19 standards, extracted from the repo on 2026-10-31. Read the relevant section before any check.
- `resources/empirical-se-standards/raw/*.md`: full standard files (desirable and extraordinary attributes, antipatterns, reviewer notes).
- `resources/empirical-se-standards/verified-refs.md`: verified citations.

## 1. The standards (repo master, last pushed 2026-10-26; no versioned releases, so cite with access date)

Every paper must meet the **General Standard** plus each method standard that applies.

| Standard | Use when | Key essential attributes (summary) |
|---|---|---|
| General | always | clear purpose and motivation; named, appropriate method; data collection and analysis described; results answer RQs; limitations, ethics, non-misleading visuals |
| Case Study and Ethnography | in-depth study of a real case | justified case selection, rich site description, case study type, unit of analysis, chain of evidence |
| Action Research | researcher intervenes in an organisation | researcher-host relation, interventions and how chosen and evaluated, cycles, longitudinal span, reactions, lessons, reflexivity |
| Questionnaire Surveys | quantitative questionnaires | population and sampling, instrument creation, validated scales where possible, response rate, missing data, power, instrument supplied |
| Qualitative Surveys | interview studies | interviewee selection and description, interviewer described, chain of evidence from quotes, saturation, reflexivity |
| Experiments | controlled experiments, quasi-experiments | formal hypotheses, variables and controls, sample-size justification, design and allocation, objects, appropriate statistics, effect sizes with CIs, validity types |
| Repository Mining | MSR studies | data sources and repo selection justified and validated, acquisition and preprocessing, annotation procedure, validated measures, external validity |
| Systematic Reviews | SLRs, mapping, meta-analysis | review type, replicable search, selection criteria, extraction and synthesis, coding, chain of evidence |
| Case Survey | aggregating published cases | replicable search, case criteria, coding scheme into variables, missingness, bias mitigation |
| Grounded Theory | GT studies | GT variant named, theoretical sampling and constant comparison, saturation, theoretical coding, grounding in data |
| Engineering Research | new artifact (tool, technique); closest fit for design science | artifact described and justified, conceptual and empirical evaluation, comparison with state of the art |
| Mixed Methods | multiple methods | justification, purpose, design, phasing, integration of findings |
| Longitudinal | repeated waves | at least two waves, identifiable subjects, analysis for dependent data, attrition |
| Data Science, Optimization, Benchmarking, Quantitative Simulation | computational studies | data and setup, baselines, stochasticity and repetitions, metrics with variation, validity |
| Replication, Meta-Science | replications, studies about research | replication type, original study details, differences, consistent vs inconsistent results |

There is no separate design science standard; use Engineering Research and say so. Supplements (sampling, ethics, open science, information visualisation) are under `docs/supplements` in the repo. For systematic reviews, also use the slr-prisma skill.

## 2. Method guidance beyond the standards

**Case study (Runeson and Höst 2009; Runeson et al. 2012).** Design (objective, case, unit of analysis, theory, RQs, data collection plan), protocol, data collection with triangulation (data, observer, method, theory), analysis with a chain of evidence, reporting. Distinguish holistic vs embedded and single vs multiple cases. Validity: construct, internal (for causal claims), external (analytical generalisation), reliability.

**Experiments (Wohlin et al.; 2012 and 2024 editions).** Scoping, planning (context, hypotheses, variables, subjects, design, instrumentation), operation, analysis and interpretation, presentation. Validity: conclusion, internal, construct, external. Cite the edition actually used.

**Surveys (Kitchenham and Pfleeger 2008).** Set objectives, design (cross-sectional or longitudinal), build and pilot the instrument, evaluate reliability and validity, define population and sampling frame, manage responses, analyse, report.

**Threats to validity: two schemes.**

| Wohlin et al. (experiments) | Runeson and Höst (case studies) |
|---|---|
| Conclusion | (not a separate type) |
| Internal | Internal |
| Construct | Construct |
| External | External |
| (not a separate type) | Reliability |

Discuss threats concretely, with the mitigation actually taken, not generic lists.

## 3. Workflow A: design a study

1. Write the RQs and the intended contribution type.
2. Choose the method; name every applicable standard (General plus method standards; Mixed Methods if more than one).
3. For each essential attribute of those standards, write the design decision that satisfies it (table: attribute, decision, where reported).
4. Add a sampling plan, ethics (Etik Kurul approval, KVKK if personal data is processed in Turkey; see ethics-committee and turkish-academia), data management and an open science plan.
5. Plan validity threats with the matching scheme.
6. Output: protocol document and the attribute table.

## 4. Workflow B: self-check a manuscript

1. Identify the method(s) from the paper text; flag any mismatch between the claimed and actual method.
2. Load the matching sections of `essential-attributes.md`.
3. For each attribute: Met / Partly / Missing, with section or page reference.
4. Check citations of method sources against `verified-refs.md` or Crossref.
5. List fixes ordered by severity: missing essential attributes first, then desirable ones.

## 5. Workflow C: review someone else's paper

Follow the standards' reviewer guidance (see each raw file):
1. Summarise the paper and its claimed method in two or three sentences.
2. Apply the General and method standards' essential attributes. Distinguish fixable omissions from flaws that undermine validity; don't reject for missing desirable attributes.
3. Don't demand a different method if the chosen one is appropriate.
4. Note antipatterns listed in the raw files.
5. Separate must-fix items from suggestions; be specific and courteous. Use the peer-review skill for the report format.

## 6. Verified references (Crossref and GitHub, checked 2026-10-31)

- Runeson, P., Höst, M. (2009). Guidelines for conducting and reporting case study research in software engineering. *Empirical Software Engineering*, 14, 131-164. https://doi.org/10.1007/s10664-008-9102-8
- Runeson, P., Höst, M., Rainer, A., Regnell, B. (2012). *Case Study Research in Software Engineering: Guidelines and Examples*. Wiley. https://doi.org/10.1002/9781118181034
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., Wesslén, A. (2012). *Experimentation in Software Engineering*. Springer. https://doi.org/10.1007/978-3-642-29044-2
- Wohlin, C., et al. (2024). *Experimentation in Software Engineering* (verify the edition label on springer.com). Springer. https://doi.org/10.1007/978-3-662-69306-3
- Kitchenham, B., Pfleeger, S. L. (2008). Personal opinion surveys. In *Guide to Advanced Empirical Software Engineering* (pp. 63-92). Springer. https://doi.org/10.1007/978-1-84800-044-5_3
- Kitchenham, B., et al. (2002). Preliminary guidelines for empirical research in software engineering. *IEEE TSE*, 28(8), 721-734. https://doi.org/10.1109/TSE.2002.1027796
- Ralph, P., et al. (2020). Empirical Standards for Software Engineering Research. arXiv:2010.03525. https://arxiv.org/abs/2010.03525
- ACM SIGSOFT Empirical Standards repository. https://github.com/acmsigsoft/EmpiricalStandards (accessed 2026-10-31)

Re-check editions and the standards' current text before citing; the repository changes without versioned releases.

## 7. Artifact evaluation and open science package
Use when preparing code, data or tools for an artifact track (ACM badges at ICSE, FSE, ISSTA, MSR, etc.) or for the paper's open science statement. Check the current track call and ACM's "Artifact Review and Badging" policy page (note version and access date) before citing badge names.
1. Badge targets: Available (permanent archive with DOI, e.g. Zenodo or Software Heritage; GitHub alone is not enough), Functional (documented, consistent, complete, exercisable), Reusable (functional plus well structured and documented for reuse), and Results Reproduced/Replicated awarded by evaluators. Confirm the exact names in the current policy.
2. Package checklist: README (purpose, claims supported, requirements, setup in under 30 minutes, a small "kick the tires" run, full run with expected time and outputs, mapping from paper tables/figures to commands); LICENSE (MIT/Apache-2.0 code, CC BY 4.0 data); pinned dependencies (requirements lock, Dockerfile or container image); data with provenance and anonymisation (kvkk, gdpr-compliance if personal data); random seeds and hardware notes; CITATION.cff.
3. Archive a tagged release on Zenodo (GitHub integration) and cite the DOI in the paper; keep anonymised links for double-blind review (e.g. anonymous.4open.science) until acceptance.
4. Self-test in a clean container by following only the README; record time and any failures.
5. Open Science supplement of the Empirical Standards: state what is shared, what is not and why.
