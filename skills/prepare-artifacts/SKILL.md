---
name: prepare-artifacts
description: >-
  Use when preparing a reproducibility artifact (code, data, scripts) for
  artifact evaluation or badging: ACM Artifacts Available, Evaluated, Functional
  or Reusable, Results Reproduced or Replicated, ICSE/FSE/MSR/ISSTA/USENIX
  artifact tracks, an artifact appendix, a Zenodo DOI, Software Heritage,
  anonymizing a repo, or packaging code for submission. Builds a packaging plan,
  README and appendix drafts, a claim-to-command matrix, and a file-level
  readiness checklist. Re-verifies the venue's current artifact rules live.
  Advisory only; never submits or deposits.
---
# Prepare artifacts

Prepare a research codebase or dataset as a submittable reproducibility artifact: README, appendix or checklist drafts, a claim-to-command matrix, anonymization guidance for double-blind review, archival deposit guidance, and a file-level readiness checklist. This skill packages and inspects the bundle. It does not run the author's experiments, does not decide whether results reproduce, and does not award or promise a badge.

For study design, method standards and the paper's open-science statement, use empirical-se-standards. This skill takes over when the job is to package code, data and scripts for an artifact track or a data-availability deposit. If the package includes personal data, also use kvkk and gdpr-compliance before recommending a public archive.

## When to use

- The paper was accepted and the author needs artifact evaluation or a badge.
- Package or clean a repository for submission.
- Anonymize a repository for double-blind review.
- Explain Artifacts Available, Functional, Reusable, Results Reproduced or Results Replicated.
- Choose a Zenodo version DOI versus a concept DOI, or a Software Heritage SWHID.
- Build an artifact appendix or fill a reproducibility checklist.

## Inputs

1. Path to the artifact directory (code, data, scripts).
2. Target venue, year and track (for example ICSE 2027 artifact evaluation).
3. Whether this is a review-phase package (often double-blind) or the final deposit.
4. The paper's major claims, so each claim can be mapped to a command and an expected output.

If any of these is missing, ask. Do not invent claims, expected numbers, hardware limits or deadlines.

## Process

### 1. Fetch the venue's current Call for Artifacts

This step is mandatory and must be live. Badge offerings and artifact deadlines change per venue per year. Do not reuse last year's rules or memory.

Search for that venue and year's "artifact evaluation", "call for artifacts" or "reproducibility" page. Prefer the official conference page or the acceptance email over secondary summaries. Software engineering venues such as ICSE, FSE, ASE, ISSTA, MSR and ICSME follow this rule too: offerings vary by year even when the conference uses the ACM taxonomy.

From the live page record, with the URL and the date checked:

- which badges are offered this cycle
- whether participation is optional or mandatory
- the separate artifact deadline (usually after paper notification)
- archival hosting requirements
- appendix template, page limit and format
- the review blind model (double-blind, single-blind, cooperative)
- size caps and how to submit

If the live page cannot be fetched, say so and stop short of firm advice.

### 2. Resolve the badge taxonomy and the era trap

ACM Artifact Review and Badging Version 1.1 (policy dated 24 August 2020; checked 7 November 2026 against the official current page) defines three independent badge families. A paper can receive any subset. Re-open the current page this turn before stating a definition as fact: [Artifact Review and Badging (current)](https://www.acm.org/publications/policies/artifact-review-and-badging-current). Terminology history: [badging terms](https://www.acm.org/publications/badging-terms).

| Family | Badge (v1.1) | Meaning |
|---|---|---|
| Artifacts Available | Available | Author-created artifacts are on a publicly accessible archival repository with a DOI or other persistent identifier. Evaluation is not required. Personal web pages are not acceptable. |
| Artifacts Evaluated | Functional | Documented, consistent, complete and exercisable, with evidence of verification or validation. Public release is not required; reviewers must be able to access the artifacts. |
| Artifacts Evaluated | Reusable | The higher tier; it includes Functional and is carefully documented and structured so others can reuse or repurpose it. |
| Results Validated | Reproduced | A different team obtained the main results using, in part, the author-supplied artifacts. |
| Results Validated | Replicated | A different team obtained the main results without the author-supplied artifacts. |

Era trap: ACM swapped the definitions of Results Reproduced and Results Replicated. Badges issued through 14 May 2020 follow Version 1.0, in which the two names mean the opposite of today. Badges issued after 15 May 2020 follow Version 1.1. Always check the badge version before interpreting those two words on an older paper. The Version 1.0 page is at [Artifact Review and Badging v1.0](https://www.acm.org/publications/policies/artifact-review-badging).

Exact numerical match is never required. Results must agree within a tolerance that does not change the paper's main claims.

A GitHub, GitLab, Bitbucket or personal web page is not an archival repository. ACM's Available badge requires a publicly accessible archival host with a persistent identifier and a declared plan for permanent access. Some venues, especially in the USENIX family, state this even more strictly and reject GitHub for the permanent copy. Confirm on that year's call.

### 3. Inspect the artifact directory (files only)

Walk the directory and report findings with file paths. This is a file-level check. It cannot prove that the build runs or that results reproduce.

Completeness (adapted from the [Papers with Code ML Code Completeness checklist](https://github.com/paperswithcode/releasing-research-code), also useful for empirical software engineering artifacts):

1. Pinned dependency specification (a lock file, frozen requirements, or a container file that pins versions or image digests).
2. Code needed to produce the paper's results (analysis, training or the system under study).
3. Evaluation or experiment-running code.
4. Data, models or a documented way to obtain them, with license and provenance.
5. A README that includes a results table and the exact command for each main result.

Also check:

- a LICENSE (and a separate data license if data are included)
- CITATION.cff or equivalent citation metadata
- upload size against the venue cap
- secrets, credentials, `.env` files and private keys (must not ship)
- personal data (resolve this before any public archive)
- for double-blind review: author names, emails, institutional paths, identifying URLs, a `.git` directory, PDF or appendix metadata, acknowledgments, funding numbers and first-person self-citation

### 4. Build a claim-to-command matrix

For each major claim in the paper, draft a row:

| Claim (as in the paper) | Command | Expected output or figure/table | Agreement rule | Approximate runtime and hardware |
|---|---|---|---|---|

The author owns the expected values and the tolerance. Do not invent them. If a claim cannot be exercised from the package, mark it as a gap rather than writing a fake command.

### 5. Draft the package the venue asked for

Work with the author, not instead of them.

**README.** Purpose, supported claims, requirements, setup intended to finish quickly, a short kick-the-tires run, the full run with expected time and outputs, the claim-to-command matrix, hardware notes, random seeds and the license.

**Artifact appendix.** If the venue supplies a template, follow it. Typical contents: hardware and software configuration, major claims, a per-claim reproduction procedure and how results will be compared.

**Checklists.** If the venue uses a NeurIPS-style, ACL-style or other reproducibility checklist, fetch the current form. An honest "no" or "n/a" with a short justification is safer than a missing or misleading "yes". Do not game boxes.

### 6. Plan anonymization for double-blind review

If the review is double-blind, ship an anonymized ZIP without `.git`, or use an anonymizing GitHub proxy such as [Anonymous GitHub](https://anonymous.4open.science), listing every identifying term to scrub. The proxy only removes terms it is given plus the obvious repository identity.

At camera-ready, restore names, URLs, acknowledgments, funding and PDF metadata, then deposit the final version.

### 7. Plan the archival deposit

- Zenodo version DOI: points to one immutable release. Use this for the final archived artifact.
- Zenodo concept DOI: always resolves to the latest version. It may be acceptable during evaluation if the venue says so; it is the wrong identifier for "evaluate exactly what is published".
- Software Heritage SWHID: a content-addressed pin of exact source. Complementary to a DOI, not a substitute. If you cite the identifier standard, confirm ISO/IEC 18670 on the official ISO or Software Heritage page this turn.
- Add CITATION.cff or codemeta.json so archives can emit citation metadata.

Do not enable GitHub-Zenodo integration, cut a release or create a deposit unless the author explicitly asks for that action.

### 8. Propose a clean-environment smoke test

Describe a test that follows only the README in a fresh virtual environment or container: install, kick-the-tires, then (if time allows) the first main result. Record intended duration and what success looks like. Prefer that the author run it. If you run commands, report what actually happened and still do not claim that the paper's results have been reproduced or that a badge has been earned.

### 9. Write the readiness report

Produce an artifact-readiness checklist (PASS / PASS-WITH-WARNINGS / FAIL) ordered by severity, citing each finding's source (the directory inspection, the live call for artifacts, or the badge policy). Add a packaging plan:

1. Target badges offered this year and which the author will pursue
2. Review-phase hosting versus final version DOI and optional SWHID
3. Completeness gaps
4. Appendix or checklist still to fill
5. The separate artifact deadline
6. Anonymization status

Write the report next to the project (for example `artifact-readiness.md` in the artifact directory) unless the author names another path. A PASS on file-level checks is not a prediction that the artifact evaluation committee will award a badge.

## Guardrails

- Re-verify the venue's current artifact rules live. Step 1 is not optional.
- Never claim that a result reproduces or that a badge will be awarded.
- Never demand bit-exact reproduction.
- Check the badge era before interpreting Reproduced versus Replicated.
- Never submit to an artifact-evaluation system, never deposit to an archive, and never complete a venue form on the author's behalf unless the author explicitly asked for that exact action.
- Quote at most a flagged path or short line; do not copy the author's artifact into a skills repository.
- Do not invent DOIs, expected numerical results, hardware limits or deadlines.

## Attribution

This skill is a modified derivative of `prepare-artifacts` from [research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) (Copyright 2026 Shaishav Maisuria), licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0

Changes made in this adaptation: removed the parent collection's `.paper-memory` convention, venue YAML profiles, sibling skills and bundled Python helpers; replaced scripted linting with an agent-run file checklist; added a claim-to-command matrix, dependency locking and a clean-environment smoke-test plan for software engineering artifact tracks; added an explicit rule that packaging readiness does not imply a badge will be awarded; and rechecked ACM Artifact Review and Badging Version 1.1 against the official pages on 7 November 2026.
