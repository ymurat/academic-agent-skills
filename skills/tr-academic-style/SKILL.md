---
name: tr-academic-style
description: >-
  Use to format a Turkish manuscript for TR Dizin or DergiPark journals and to
  lint Turkish APA 7 references (ve ark., aktaran, t.y., bilingual öz and
  abstract).
---
# Turkish academic style

Upstream: `../../common/alterlab/skills/turkish-academia/alterlab-tr-academic-style/` (AlterLab, MIT; TR Dizin rules checked 2026-09-23).

1. Read its SKILL.md in full, then only the references needed.
2. Lint references offline with `python3 ../../common/alterlab/skills/turkish-academia/alterlab-tr-academic-style/scripts/tr_apa_lint.py`, outputs to the current working directory or a path the user names.
3. The target journal's own yazım kuralları override the general rules. Ask for them or fetch them from the journal's DergiPark page.
4. For current TR Dizin criteria, check trdizin.gov.tr and give the date checked.
5. To verify that references exist, use the citation-check skill. Never invent references or DOIs.
6. Write in TDK spelling with natural Turkish academic phrasing, using the passive or impersonal voice only when the discipline expects it. No em dashes, no literal translations from English.
