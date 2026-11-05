---
name: thesis-jury-prep
description: >-
  Use when the user prepares for a thesis defense or proficiency exam, either as candidate (mock jury questions, weak points, answer notes) or as a jury member (reading report, question list, decision justification).
---
# Thesis jury preparation

Deep preparation for one defense event. `thesis-supervisor` covers the whole thesis process and gives brief defense advice; this skill produces the full question bank, weak-point analysis and the jury member's report.

## Inputs
Thesis PDF (or chapters), degree (yüksek lisans, doktora, doktora yeterlik, tez izleme komitesi), the user's role (candidate's advisor, jury member, or the candidate), the university's graduate school regulations (Gazi Üniversitesi Lisansüstü Eğitim ve Öğretim Yönetmeliği or the relevant one, opened live), date and duration.

## Workflow
1. **Read and map.** Extract research questions or hypotheses, claimed contributions, method, data, main results, limitations. Build a one-page claim map: each contribution, where it is supported, by which evidence.
2. **Weak-point analysis.** Check in order: problem and gap justification; alignment of RQs, method and results; validity threats (internal, external, construct, conclusion; for SE use `empirical-se-standards`); statistics (`se-stats`); reproducibility; literature currency and missing key works (verify with `citation-check`); ethics approval and KVKK compliance when human data is used (`ethics-committee`, `kvkk`); originality claims versus overlap (similarity report if the user has it); writing and format against the institute's thesis template.
3. **Question bank.** 25 to 40 questions grouped: opening ("summarise your contribution in two minutes"), motivation, method choice and alternatives, data and validity, results interpretation, limitations, generalisation, publications from the thesis, future work, and field-wide questions. Mark each with difficulty and the evidence page the answer should cite.
4. **Role output.**
   - Candidate or advisor: answer notes (bullet points, not scripts), a 20 to 30 minute presentation outline (use `talk-prep-2`), a mock session plan with timed rounds.
   - Jury member: a reading report (summary, strengths after weaknesses, required and suggested corrections, decision recommendation: kabul, düzeltme, ret) written formally, and 8 to 12 prioritised questions for the session.
5. **After the defense.** Turn jury requests into a correction checklist with page references; for düzeltme decisions note the regulation's deadline (check the regulation text, do not state from memory).

## Rules
- Formal Turkish (TDK) for reports, `turkish-native` for polish; critique weaknesses before strengths.
- Do not invent regulation articles or deadlines; quote the opened regulation with URL and date.
- Keep the candidate's personal data out of shared files.
