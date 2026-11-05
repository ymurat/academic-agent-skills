---
name: reviewer-response-tracker
description: >-
  Use when the user handles a journal or conference revision across one or more
  rounds and needs every reviewer and editor comment tracked to a decision, a
  manuscript change with page and line, and a response letter entry.
---
# Reviewer response tracker

Bookkeeping for revisions. `rebuttal` writes the arguments and the letter tone; this skill makes sure nothing is missed and every claim in the letter matches the revised manuscript, across rounds.

## Files
- Template: `resources/reviewer-response-tracker/tracker-template.csv`
- Working folder per paper: `./work/revisions/<paper-short-name>/` with `tracker.csv`, `round<N>/decision-letter.txt`, `round<N>/manuscript-before.*`, `round<N>/manuscript-after.*`, `round<N>/response.md`.

## Workflow
1. **Split.** Paste or extract the decision letter. Split every reviewer and editor report into atomic comments; one request per row. ID as `R<round>.<reviewer>.<n>` (for example `R1.2.4`; editor = `E`). Quote the comment verbatim.
2. **Classify.** Major, minor, editorial; also mark duplicates across reviewers and conflicting requests (two reviewers asking opposite things). Conflicts go to the editor-facing summary.
3. **Decide with the user.** Accept, partial, or decline with reason. Declines need evidence or a citation verified by `citation-check`.
4. **Locate changes.** After the user revises, diff before and after (`latexdiff` for LaTeX, Word track changes or `pandoc` to text plus `diff` otherwise). Record old and new page, line, section, figure or table for each row.
5. **Draft the letter.** For each row: comment quote, response, change made with location, and quoted new text when short. Hand tone and argument work to `rebuttal`; final Turkish or English polish to `turkish-native` or `academic-humanizer`.
6. **Verify.** Before submission check: every row status done; every location exists in the final PDF (numbering changes after edits, re-check last); every promised experiment, figure or reference is present; no response claims a change that the diff does not show. Mark rows verified.
7. **Next round.** Carry open or partial items forward; link new comments to earlier IDs when a reviewer repeats a point. Keep a summary table of rounds: date, decision, counts per type, open items.

## Output
- `tracker.csv` (source of truth), `response.md` (letter), `summary.md` (round history and conflicts).
- For TR Dizin / DergiPark journals follow the journal's response form if it has one (`tr-academic-style`).

## Rules
- Never claim a change that is not in the manuscript. Never paraphrase a reviewer inside quotation marks.
- Keep the tone factual; no thanks inflation.
