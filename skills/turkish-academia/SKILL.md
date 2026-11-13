---
name: turkish-academia
description: >-
  Use for Turkish academic system tasks: TR Dizin, DergiPark, YÖK Tez, YÖK
  Akademik, TÜBİTAK ARDEB and BİDEB, doçentlik, akademik teşvik, KVKK data
  plans, Etik Kurul routing, TÜBİTAK open science (Aperta).
---
# Turkish academia (umbrella)

Upstream: AlterLab-IEU/AlterLab-Academic-Skills (MIT, snapshot 2026-09-23), at `../../common/alterlab/skills/turkish-academia/`. Pick the sub-skill, read its SKILL.md in full, then only the references it needs.

| Task | Sub-skill folder | Notes |
|---|---|---|
| Format a Turkish manuscript, Turkish APA 7 | `alterlab-tr-academic-style` | also its own skill: tr-academic-style |
| TR Dizin search and journal index status | `alterlab-trdizin` | **manual browser only** (automated client removed 2026-11-05); status changes yearly |
| DergiPark articles, journals, BibTeX | `alterlab-dergipark` | **manual browser only** (OAI/HTML scripts removed 2026-11-05); no bulk PDF downloads |
| YÖK Tez Merkezi search, originality check | `alterlab-yok-tez` | also its own skill: yok-tez; **manual browser only** (scripts removed 2026-11-05) |
| YÖK Akademik profile lookup | `alterlab-yok-akademik` | scrapes pages and handles personal data; use sparingly, only when asked |
| YÖK Atlas program data | `alterlab-yokatlas` | needs the third-party `yokatlas-py` package; install only if the user wants it |
| TÜBİTAK ARDEB proposals (1001, 1002-A, 3501) | `alterlab-tubitak-proposal` | also its own skill: tubitak-proposal |
| TÜBİTAK BİDEB scholarships (2219, 2218, 2221, 2232, 2236, 2224) | `alterlab-tubitak-bideb` | amounts and deadlines change each call |
| Doçentlik pre-screen | `alterlab-docentlik-eligibility` | also its own skill: docentlik-eligibility |
| Akademik teşvik score | `alterlab-akademik-tesvik` | based on Yönetmelik 2018/11834 as of 2026-09; verify the current text on mevzuat.gov.tr before giving any number |
| KVKK data management plan | `alterlab-kvkk-dmp` | Law 6698 as amended by 7499 |
| Etik Kurul or TİTCK routing, consent forms | `alterlab-tr-research-ethics` | use together with the ethics-committee skill |
| TÜBİTAK open science policy, Aperta | `alterlab-aperta` | policy PDF is dated 2016; check for a newer version |

Rules:
1. Offline helper scripts that remain (APA lint, proposal scaffold, teşvik score, etc.) run as `python3 <sub-skill>/scripts/<script>.py` (or `uv run python ...`), outputs to the current working directory or a path the user names. Don't run `pip install` unless a step needs it.
2. Do **not** run or reintroduce automated clients against tez.yok.gov.tr, dergipark.org.tr, or trdizin.gov.tr / search.trdizin.gov.tr. Those scripts were removed. Use the official web UI manually and cite the page URL and date checked.
3. Sub-skills mention AlterLab sibling skills that aren't installed. Map them: citation-mgmt to citation-check, paper-writer to scientific-writing, research-grants to research-grants, research-ethics to ethics-committee, statistical-analysis and venue-templates to your own judgment plus the venue's official guidelines.
4. Regulations, criteria, program caps and deadlines change. Before stating any rule or number, check the official source (ÜAK, YÖK, TÜBİTAK, ULAKBİM, mevzuat.gov.tr) and give the date checked.
5. Keep network use light: no bulk harvesting, no bulk PDF downloads.
6. Write Turkish in TDK spelling with natural academic phrasing; apply these writing rules (no em dashes, no buzzwords).
