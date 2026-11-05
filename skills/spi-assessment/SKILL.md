---
name: spi-assessment
description: >-
  Use when planning or reviewing a software process assessment (ISO/IEC 330xx,
  Automotive SPICE, CMMI, ISO/IEC 29110), rating process attributes, doing a gap
  analysis or improvement roadmap, or writing an SPI paper for EuroSPI or JSEP.
---
# SPI assessment and process capability

Rules: formal prose, no em dashes, tables for comparisons. Never invent clause numbers, indicator IDs, percentages, citations or DOIs. ISO, VDA and CMMI texts are copyrighted: paraphrase, cite clause numbers only when a copy confirms them, never quote long passages. Sections marked **[paraphrase]** summarise standards that cannot be quoted.

Raw notes and source table: `resources/spi-assessment/verified-facts.md`. ISO/IEC 33020:2019 official preview (clauses 1 to 5.4): `resources/spi-assessment/ISO-IEC-33020-2019-sample.txt`.

## 1. Model landscape (verified 2026-10-31; re-check before citing)

| Item | Current edition | Role |
|---|---|---|
| ISO/IEC 33001:2015 | Ed.1, confirmed 2026 | Concepts, terminology, guide to the 330xx family |
| ISO/IEC 33002:2015 | Ed.1, confirmed 2026 | Requirements for performing an assessment |
| ISO/IEC 33004:2015 | Ed.1, corr. 2017-04, confirmed 2026 | Requirements for PRMs, PAMs, maturity models |
| ISO/IEC 33020:2019 | Ed.2, confirmed 2026 | Measurement framework for process capability (levels, attributes, rating) |
| ISO/IEC TS 33061:2021 | Ed.1, confirmed 2024 | PAM for software life cycle processes (replaced 15504-5:2012) |
| ISO/IEC 29110 | 1-1:2024, 1-2:2024; 3-2:2018/Amd 1:2025 | Profiles for very small entities (VSEs) |
| Automotive SPICE | PAM 4.1 (2026-08-24), VDA QMC | Automotive PRM/PAM; Guidelines 3rd rev. ed. March 2026 |
| CMMI | V3.0 model; CMMI AIM V4.0 released 2026-05-21 | Maturity model and appraisal ecosystem (CMMI Institute, ISACA) |
| SPI Manifesto | A.1.2.2010 (EuroSPI) | 3 values, 10 principles |

History **[paraphrase]**: ISO/IEC 15504 (SPICE) was the earlier assessment series; the 330xx family replaces and extends its parts (mapping in ISO/IEC 33001 Annex A). Automotive SPICE 2.x was built on 15504-5; 3.x and 4.x align with the 330xx framework. Do not state 15504 withdrawal dates unless checked on iso.org.

CMMI note: CMMI uses its own appraisal method and maturity levels 1 to 5 rather than 330xx ratings. Verify on cmmiinstitute.com whether the whole model is now labelled V4.0 or only the AIM view.

## 2. Capability framework (ISO/IEC 33020:2019; clauses 5.2 to 5.4 verified 2026-10-31 against the official preview)

The standard permits users to reproduce clauses 5.2, 5.3, 5.4, 5.6 and Annex B as part of a process assessment.

| Level | Name | Process attributes |
|---|---|---|
| 0 | Incomplete process | none |
| 1 | Performed process | PA 1.1 Process performance |
| 2 | Managed process | PA 2.1 Performance management; PA 2.2 Documented information management |
| 3 | Established process | PA 3.1 Process definition; PA 3.2 Process deployment; PA 3.3 Process assurance |
| 4 | Predictable process | PA 4.1 Quantitative analysis; PA 4.2 Quantitative control |
| 5 | Innovating process | PA 5.1 Process innovation |

Older sources (ISO/IEC 15504 and secondary literature) use a different attribute list, for example "work product management" for PA 2.2 and two level 5 attributes. Use the 2019 list above unless the study explicitly uses another framework. Automotive SPICE 4.x has its own attribute set; check its PAM.

Rating scale (clause 5.3): N not achieved 0% to 15%; P partially achieved above 15% to 50%; L largely achieved above 50% to 85%; F fully achieved above 85% to 100%. Optional refinement: P- above 15% to 32.5%, P+ above 32.5% to 50%, L- above 50% to 67.5%, L+ above 67.5% to 85%.

Rating method (clause 5.4): the lead assessor decides which rating method to use; it must be specified in the assessment input and referenced in the assessment report. Aggregation methods are in clause 5.5.

Level achievement rule (clause 5.6, not in the preview): commonly stated as all attributes of the level rated at least L and all lower-level attributes rated F. Confirm against a full copy before citing.

## 3. Workflow A: plan an assessment **[paraphrase of ISO/IEC 33002]**

1. Purpose: improvement, capability determination, or supplier selection. Record the sponsor.
2. Scope: organisational unit, projects or instances, processes, target levels, PAM and its version (e.g. ASPICE PAM 4.1, TS 33061).
3. Class and team: assessor competence, independence, lead assessor; for ASPICE, intacs certification.
4. Constraints: confidentiality, availability of people, evidence that may not leave the site.
5. Plan: schedule, interviews, document review, data collection, rating method, how results are reported and validated.
6. Output: an assessment plan table (scope, roles, schedule, evidence sources, risks).

## 4. Workflow B: rate process attributes

1. For each process instance and attribute, list indicators from the PAM (base practices and work products for PA 1.1; generic practices and resources above).
2. Map objective evidence to each indicator: document IDs, interview notes, tool data. No evidence, no credit.
3. Characterise each indicator, then aggregate to an attribute rating, recording the rating method and aggregation rule.
4. Record strengths and weaknesses per attribute, with traceable evidence.
5. Derive the capability level per section 2. Present a profile table: process by attribute with N/P/L/F.
6. Validate findings with participants before finalising.

## 5. Workflow C: gap analysis

| Process | Target level | Current rating | Gap (attributes below target) | Evidence | Impact on business goal |
|---|---|---|---|---|---|

Rank gaps by business impact and dependency (lower-level gaps first). Link each gap to a business objective, following the SPI Manifesto.

## 6. Workflow D: improvement roadmap

1. Tie each action to a gap and a measurable goal (GQM is a common choice).
2. Sequence: quick wins, foundation (PA 1.1, PA 2.1, PA 2.2), then institutionalisation (PA 3.1 to PA 3.3).
3. Each action: owner, pilot project, effort, success measure, review date.
4. Change management: use the Manifesto principles (know the culture, motivate people, manage change, do not lose focus) as an explicit checklist.
5. Plan a re-assessment and the measurement of effect.
6. For very small entities, prefer ISO/IEC 29110 profiles (Entry, Basic) over a full 330xx assessment.

## 7. Workflow E: write up an SPI study

| Venue | Notes (verify the current call before submission) |
|---|---|
| EuroSPI | Springer CCIS proceedings; the call asks papers to map contributions to SPI Manifesto values or principles. Industry and research tracks; check the year's page limit. |
| Journal of Software: Evolution and Process (Wiley) | Full empirical papers; follow the author guidelines and a method standard (see the empirical-se-standards skill). |

Structure: context and organisation profile (anonymised), model and version, assessment method and team, evidence and rating rules, results profile, improvement actions, measured effect, threats to validity (construct, internal, external, reliability), Manifesto mapping. Report standard editions exactly (e.g. "ISO/IEC 33020:2019"). For action research or case study designs, apply the matching ACM SIGSOFT Empirical Standard.

Self-check before submission:
- Every standard cited with its edition year, checked on iso.org, vda-qmc.de or cmmiinstitute.com with a date.
- No verbatim indicator text from paid standards beyond short identifiers.
- Rating rules and aggregation stated; evidence traceable; consent and confidentiality addressed.

## 8. Verified references (checked 2026-10-31)

- ISO/IEC 33001:2015. https://www.iso.org/standard/54175.html
- ISO/IEC 33002:2015. https://www.iso.org/standard/54176.html
- ISO/IEC 33004:2015. https://www.iso.org/standard/54178.html
- ISO/IEC 33020:2019. https://www.iso.org/standard/78526.html
- ISO/IEC TS 33061:2021. https://www.iso.org/standard/80362.html
- ISO/IEC 29110-3-2:2018/Amd 1:2025. https://www.iso.org/standard/91116.html
- VDA QMC. Automotive SPICE PAM 4.1, 2026-08-24. https://vda-qmc.de/en/automotive-spice/automotive-spice-veroeffentlichungen/
- CMMI Institute. CMMI Acquisition Handbook v4.0, August 2026 (states CMMI AIM V4.0 released 2026-05-21). cmmiinstitute.com
- Pries-Heje, J., Johansen, J. (eds.). SPI Manifesto, version A.1.2.2010. https://conference.eurospi.net/images/eurospi/spi_manifesto.pdf

Re-check editions, confirmation status and version numbers on the issuing body's site before every citation; ISO reviews standards every five years.
