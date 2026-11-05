---
name: c4-model
description: >-
  Use when designing, documenting, reviewing or updating a software architecture
  as C4 diagrams in Mermaid.
---
# C4 model

Full upstream skill (cheriftj/c4-model-skill, vetted low risk on 2026-10-31): `resources/c4-model-skill/`.

1. Read `resources/c4-model-skill/skills/c4-model/SKILL.md` in full and follow it, including any reference files it names. Ignore `tests/claude-code/`; those scripts need a CLI that is not used here.
2. Diagrams are Mermaid text, which renders directly in chat and most Markdown tools. To export PNG or SVG, install mermaid-cli (`npm i -g @mermaid-js/mermaid-cli`) only when an image file is needed.
3. For teaching use, pair diagrams with short prose explaining each level (context, container, component, code) and keep notation consistent across levels.
4. When reviewing an existing architecture, list weaknesses and missing elements before strengths.
5. Prose follows these writing rules: no em dashes, no buzzwords, lead with the answer.
