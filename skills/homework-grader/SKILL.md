---
name: homework-grader
description: >-
  Use when grading student assignments against a rubric, writing feedback,
  calibrating scores against the instructor's own, or exporting grades to Excel;
  student data stays on local storage.
---
# Homework grader (local-only)

Upstream skill (ChantillyAn/homework-grader, MIT, vetted 2026-10-31): `resources/homework-grader/`.

**Data rule, non-negotiable:** never run `scripts/batch_score.py` or `calibrate.py` scoring calls. They send submission text to an outside API, which is a cross-border transfer under KVKK Art. 9 and not available to a state university through incidental-transfer exceptions. Grade inside this session instead.

1. Read `SKILL.md`, `templates/` and `references/` in full. Follow the rubric, prompt templates and bias checks, but do the scoring yourself.
2. Work in a copy under `./work/grading/<course>/`. Before any processing, replace student names and student numbers in the text and filenames with `anon-NNN` and keep the key file only on local storage, outside the shared work folder. `preprocess.py` anonymises filenames but not text, so redact text yourself.
3. Local scripts allowed: `preprocess.py`, `stats.py`, `export_excel.py`. Install only the dependencies they need (`pip install pyyaml jsonschema python-docx pymupdf pillow pandas openpyxl scipy tqdm`), never `anthropic`.
4. Ask for the instructor's rubric and a few instructor-graded samples to calibrate; report disagreements rather than hiding them.
5. Grades are suggestions; the instructor decides. Feedback is specific, respectful and in the course language (Turkish in TDK spelling).
6. Load kvkk when the question of storing or sharing grades comes up.
