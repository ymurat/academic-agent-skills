---
name: talk-prep-2
description: >-
  Use when the user needs to present a paper or research (conference talk,
  seminar, journal club, defense rehearsal, invited talk) or make a poster:
  timed talk script, slides distilled from it, Q&A preparation, rehearsal, and
  print-ready speaker notes.
---
# Talk and poster preparation

Adapted from mimaowang/paper-to-podium (MIT). Full upstream skill with references and scripts: `resources/paper-to-podium/` (SKILL.md, `references/script-writing.md`, `references/slide-craft.md`, `references/qa-and-rehearsal.md`, `scripts/`, `assets/beamer-skeleton.tex`).

Core rule from upstream: the script is the talk; slides are an excerpt of the script, never the other way round.

## Talk workflow
1. **Intake**: occasion (conference, seminar, defense, invited, class), audience expertise, duration including Q&A, language, venue template, required extras. Infer from context; ask only if duration or audience is unknown.
2. **Read and research**: read the whole paper; keep a source list separating paper-internal claims (table/figure/section) from external facts. Every number said aloud must be traceable.
3. **Script**: plain spoken language at the speaker's pace. For Turkish use about 100-110 words/minute (slow) or 120-130 (normal); English 120 / 140. Check length with `python3 resources/paper-to-podium/scripts/estimate_talk_length.py script.md --rate en-normal` (its zh rates do not fit Turkish; count words instead). Leave margin for questions.
4. **Slides**: one idea per slide, the paper's 2-4 argument-carrying figures on their own slides, readable from the back row. Use the user's institutional template if any; else the bundled Beamer skeleton, the `slides` skill for .pptx/Google Slides, or `icarus-figures` for redrawn figures. For Turkish in Beamer, use XeLaTeX with fontspec and a font with Turkish glyphs; drop the CJK block.
5. **Visual QA**: render every page (`render_pdf_pages.sh`) and look at it; fix crowding and overflow.
6. **Verify**: fact-check numbers against the source list; proofread the script (use `turkish-native` for Turkish); blind review by a fresh reader who sees only the slides.
7. **Stage**: script aligned to slide numbers with page-turn cues; print-ready script (`script_to_print_pdf.py`).

## Q&A preparation (always include)
- 10-15 likely questions grouped as: clarifying, methodological (validity threats, sample, baselines), novelty and related work, generalisability, ethics and data, "what next".
- For each: a 20-40 second answer, the evidence it rests on, and a backup slide if needed.
- The 3 hardest questions get a frank answer that concedes the limitation where real.
- Optionally ask the debate agents (Metodolog, Şeytanın Avukatı, Etki ve Etik) to play hostile audience members.

## Poster workflow (not covered upstream)
1. Get the venue's size and orientation (e.g. A0 portrait) and any template.
2. Write a one-sentence takeaway as the title or headline; the poster must make sense in 10 seconds from 2 m away.
3. Layout: 3 or 4 columns, reading order left-to-right top-to-bottom; about 300-800 words total; one main figure as the visual anchor; QR code to the paper or artifact.
4. Body text at least about 24 pt and titles about 72 pt or larger at A0 (scale for other sizes); check by rendering at 25% and reading.
5. Build in LaTeX (tikzposter/beamerposter), PowerPoint, or Figma as the user prefers.
6. Prepare a 1-minute and a 3-minute spoken walk-through plus the Q&A list above.

## Done means
Script within time with margin; every slide visually checked; numbers traced; Q&A sheet ready; print-ready notes. No em dashes, no buzzwords, no fabricated numbers.
