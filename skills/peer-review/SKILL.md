---
name: peer-review
description: >-
  Use when the user is reviewing a manuscript, proposal or preprint and needs a
  structured reviewer report or critique.
---
# Peer review

Full upstream skill (K-Dense scientific-agent-skills, `peer-review`): `resources/peer-review/` (SKILL.md, `scripts/`, `assets/`, `references/`).

1. Read `resources/peer-review/SKILL.md` in full first, then only the references it points to for this task.
2. Its helper scripts use only the Python standard library and work offline. Run them as `python3 resources/peer-review/scripts/<script>.py`, writing outputs under `/workspace`.
3. Confidentiality: a manuscript under review is confidential. Keep it on local storage, don't paste it into outside services or connectors, and remind the user to check the venue's policy on AI-assisted reviewing.
4. Ground every criticism in the text. Separate major from minor issues, and name weaknesses and methodological gaps before strengths.
5. Follow these writing rules: formal and precise, no em dashes, no buzzwords or formulaic AI phrasing.
