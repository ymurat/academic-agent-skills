---
name: scientific-writing
description: >-
  Use when the user drafts, revises or audits a paper or paper section
  (abstract, introduction, related work, methods, results, declarations) or a
  submission package.
---
# Scientific writing

Full upstream skill (K-Dense `scientific-writing`): `resources/scientific-writing/` (SKILL.md, `scripts/`, `templates/`, `references/`).

1. Read the upstream SKILL.md in full first, then only the references and templates the task needs.
2. Its scripts (lint, reference, consistency, claim and authorship checks, scaffold, reporting-guideline selection) use only the standard library and work offline. Run them as `python3 resources/scientific-writing/scripts/<script>.py` with outputs to the current working directory or a path the user names.
3. Use this skill for structure, evidence provenance and consistency checks. For voice and naturalness, also apply the academic-humanizer skill.
4. Follow the target venue's format and citation style; otherwise APA 7, or IEEE for engineering venues. Use PRISMA 2020 or Kitchenham only for systematic reviews.
5. Never fabricate data, results, citations or DOIs. Mark gaps with placeholders.
6. For Turkish texts, follow TDK spelling and natural Turkish academic conventions. Follow these writing rules: no em dashes, no buzzwords, active voice, varied sentence length.
