---
name: teaching-skills
description: >-
  Use when the user designs a course or syllabus, or builds lessons, labs,
  exams, rubrics, student feedback, slides, TA plans, accreditation mappings, or
  bilingual course materials.
---
# Teaching skills

Full upstream suite (YujxZJCN/teaching-skills): `resources/teaching-skills/`.

1. Start by reading `resources/teaching-skills/teaching-pipeline/SKILL.md`, the orchestrator, plus `shared/` (it holds the Course Passport schema the sub-skills build on).
2. Then read only the sub-skill(s) the task needs, each at `<sub>/SKILL.md` with its own `agents/`, `templates/` and `references/`: course-designer, lesson-builder, assessment-architect, submission-auditor, student-mentor, teaching-reflector, cohort-analyst, accreditation-mapper, bilingual-courseware, course-publisher, deck-studio, lab-forge, media-scripter, ta-coordinator.
3. bilingual-courseware defaults to English and Chinese. Use English and Turkish for this user unless told otherwise. Ignore Chinese-specific terms that don't apply.
4. Optional tools (pandoc, marp, tectonic, python-pptx) may need installing; install them only when a step actually needs them. Skip `build_codex.py`, which is repo build tooling.
5. course-publisher only writes drafts. Never send email or announcements; show drafts to the user.
6. Treat student data as personal data: keep it on local storage, anonymize it in examples, and never upload it anywhere.
7. Fit materials to Turkish higher education where relevant (ECTS credits, program outcomes, MÜDEK accreditation for engineering) and check current requirements before citing them.
