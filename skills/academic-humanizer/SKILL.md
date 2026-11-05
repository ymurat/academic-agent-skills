---
name: academic-humanizer
description: >-
  Use when editing AI-assisted academic prose (papers, theses, rebuttals, grant
  proposals) for clarity and the author's own voice while keeping scholarly
  conventions, every number, result, and citation unchanged.
---
# Academic Humanizer (from github.com/AIScientists-Dev/academic-humanizer, MIT, v0.3.3)

The full upstream skill is stored in `resources/`. Before editing:

1. Read `resources/academic-humanizer/SKILL.md` in full and follow it. Worked examples are in `resources/academic-humanizer/examples/before-after.md`.
2. Never change a number, result, citation, or claim strength beyond what the evidence supports. This is not a tool for evading AI-use disclosure.
3. Respect the target venue's conventions and the user's saved writing rules (language, citation style, banned words, no em dashes). For Turkish academic text follow TDK spelling and natural Turkish academic phrasing.
4. Return the revised text and a brief note on the substantive changes (claims softened or tightened, structure moved), flagging any claim that lacks support.
