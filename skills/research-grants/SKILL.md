---
name: research-grants
description: >-
  Use when the user is writing or reviewing a grant or research proposal (aims,
  objectives, review criteria, budget, impact, resubmission, data management
  plan).
---
# Research grants

Full upstream skill (K-Dense `research-grants`): `resources/research-grants/` (SKILL.md, `references/`, `assets/` templates).

1. Read the upstream SKILL.md in full first, then only the references relevant to the task.
2. It covers NSF, NIH, DOE, DARPA and Taiwan NSTC. For Horizon Europe, ERC, TÜBİTAK or other funders, use only its general principles and take structure, page limits, evaluation criteria and deadlines from the funder's current call documents on the web, noting the date checked. For TÜBİTAK ARDEB forms use the `tubitak-proposal` skill.
3. Skip its optional diagram step that calls a scientific-schematics script and needs an outside API key. That skill isn't installed.
4. Never invent budget figures, preliminary results, partner commitments or citations. Use placeholders for anything the user has to provide.
5. Follow these writing rules: formal and evidence-based, no em dashes, no buzzwords, answer-first, tables for comparisons.

## Data management plan (DMP)
Write one when the funder requires it (Horizon Europe: DMP deliverable within the first months, using the current Horizon Europe DMP template; ERC; many national calls) or when the project produces data or software. Check the current template on the funder's site and note the date.
1. Data inventory: each dataset or software artifact with type, format, volume, origin (new or reused), and who owns it.
2. FAIR: Findable (persistent identifiers such as DOI via Zenodo or an institutional repository, rich metadata, standard vocabularies); Accessible (repository, access conditions, embargo, open by default with justified exceptions); Interoperable (open formats, metadata standards); Reusable (licence such as CC BY 4.0 for data, MIT/Apache-2.0 for code, documentation, provenance).
3. Personal and sensitive data: lawful basis, consent, anonymisation or pseudonymisation, storage location, retention and deletion, transfer outside Turkey or the EU. Use the `kvkk` skill for data processed in Turkey and `gdpr-compliance` for EU data; ethics approval via `ethics-committee`.
4. Storage and security during the project: backup, access control, encryption.
5. Preservation after the project: repository, minimum retention period, costs.
6. Responsibilities and resources: named roles, budgeted costs for curation and repository fees.
Output a table per dataset plus short prose sections; flag every item the user must confirm.

## Budget (bütçe)


1. **Get the rules first.** Open the current call text and the funder's budget guide before you draft anything. For TÜBİTAK ARDEB that means the program's call page and its budget forms (ARDEB proposal guide, PBS). For Horizon Europe it means the work programme topic, the Annotated Model Grant Agreement and the call's budget form (actual costs or lump sum). Record the URLs and the date you opened them. Never state ceilings, rates or eligible cost rules from memory.
2. **Build from the work plan.** Every cost line must point to a work package and a task, with a one-line justification ("WP2 T2.3, 6 person-months, data labelling").
3. **Usual categories (check the names against the call).**
   - **TÜBİTAK:** personnel and bursiyer (scholarship researcher) support, equipment, consumables, service procurement, travel, and the program's project incentive and institutional share where they apply.
   - **Horizon Europe:** personnel, subcontracting, purchase costs (travel, equipment, other goods and services), other cost categories, and indirect costs as the grant agreement defines them.
4. **Personnel effort.** Write effort as person-months per person per WP and check it against each person's other projects (no over-commitment). Use the institution's real salary rules. If the rate is unknown, put a placeholder and do not estimate.
5. **Justify equipment.** Explain why existing infrastructure is not enough, and for Horizon how depreciation applies. Use quotes (proforma) the user supplies.
6. **Consistency check.** The budget table, the WP effort table, the Gantt chart and the narrative must agree. Totals must add up (recompute in a script). Every partner has a line.
7. **Output.** A budget table (category, item, WP, amount, justification) as CSV/XLSX, plus a justification text in the funder's language. Turkish text follows TDK spelling (`turkish-native`).

Rule: amounts, rates and limits come only from the user or from documents opened this session. Unknown values stay as `[TBD]`.
