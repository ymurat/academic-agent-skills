---
name: slr-prisma
description: >-
  Use when the user plans, writes, structures, or audits a systematic literature
  review (SLR): PRISMA 2020 checklist or flow diagram, search strings for
  Scopus/WoS/IEEE Xplore, inclusion/exclusion criteria, screening, risk of bias,
  narrative synthesis. Not for meta-analysis.
---
# Systematic Literature Review with PRISMA 2020 (from github.com/keemanxp/slr-prisma by Chuah Kee Man, MIT)

The full upstream skill and its references are stored in `resources/`:
- `resources/slr-prisma/SKILL.md` (the workflow: interview, section-by-section drafting, flow diagram, referencing, .docx output, checklist audit)
- `resources/slr-prisma/references/prisma-2020-checklist.md` (all 27 items)
- `resources/slr-prisma/references/flow-diagram.md` (templates A to D)

Steps:
1. Read the upstream SKILL.md in full and follow its phases, adapting to the request (partial requests are covered there).
2. Adaptations for this environment:
   - Its paths under `/mnt/skills/...` and `/mnt/user-data/outputs/` don't exist here. Build .docx files with python-docx or docx-js in a local working folder and attach them; draw the flow diagram as SVG/PNG or a mermaid block.
   - Citation style: use the target venue's style if named, else APA 7 (IEEE for engineering venues) unless the user says otherwise.
   - For software-engineering reviews, conduct the review per Kitchenham and Charters' SLR guidelines and report it per PRISMA 2020; name both in Methods. Don't impose PRISMA on narrative reviews.
3. Verify every reference with web search (DOI, Crossref, publisher page) before using it; never fabricate a reference, count, or DOI. Use placeholders (n = ?) for missing flow-diagram numbers.
4. Present each drafted section for feedback before moving on.
