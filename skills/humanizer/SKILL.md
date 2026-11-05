---
name: humanizer
description: >-
  Use when editing or reviewing prose so it stops sounding AI-written (dashes
  everywhere, forced triads, stock AI words, staged openers, one-line closers,
  inflated claims, sales language) without changing what it says.
---
# Humanizer (from github.com/blader/humanizer, MIT, v3.1.0)

The full upstream skill is stored in `resources/`. Before rewriting anything:

1. Read `resources/humanizer/SKILL.md` in full and follow it. It catalogs the AI-writing patterns (based on Wikipedia's "Signs of AI writing"), each with before/after examples.
2. Keep the meaning, facts, numbers, and citations exactly; never invent content.
3. Apply the user's own saved writing rules on top (for example no em dashes, banned buzzwords), and match the user's language. For Turkish text, apply the same principles with natural Turkish phrasing.
4. Return the rewritten text, plus a short list of the main patterns you removed when the user asked for a review.

Do not run anything from the repo's `scripts/` folder unless the user asks.
