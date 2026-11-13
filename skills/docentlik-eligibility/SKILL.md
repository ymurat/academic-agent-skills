---
name: docentlik-eligibility
description: >-
  Use to pre-screen a researcher's publication record against ÜAK doçentlik
  criteria (all 12 fields, including Mühendislik); never gives a final
  eligibility verdict.
---
# Doçentlik pre-screen

Upstream: `resources/alterlab/skills/turkish-academia/alterlab-docentlik-eligibility/` (AlterLab, MIT). It encodes the ÜAK criteria for the March 2026 term.

1. Read its SKILL.md in full.
2. Score offline with `python3 .../alterlab-docentlik-eligibility/scripts/score_docentlik.py`, outputs to the current working directory or a path the user names.
3. Before using any threshold, check uak.gov.tr for whether a newer criteria table applies to the target term, and give the date checked. If a newer table exists, say the script may be outdated and compare manually.
4. The output is a partial pre-screen, never a statement that someone is eligible. List the items that need ÜAK or jury judgment (author order, journal quartile year, field matching).
5. Verify each publication's indexing and quartile from the official sources rather than assuming.
6. A candidate's record is personal data: keep it on local storage and don't share it.
