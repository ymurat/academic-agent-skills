---
name: bib-hygiene
description: >-
  Use when the user wants a BibTeX or Zotero library cleaned, deduplicated,
  completed from DOIs, validated against Crossref, or formatted for a journal or
  thesis template.
---
# Bibliography hygiene (BibTeX and Zotero)

Keeps reference files correct. `citation-check` verifies that a claim matches its source; this skill fixes the reference records themselves.

## Sources in `resources/`
- Upstream (MIT, credit: K-Dense Inc., https://github.com/K-Dense-AI/scientific-agent-skills): `resources/bib-hygiene/upstream/citation-management/` (scripts `doi_to_bibtex.py`, `validate_citations.py`, `format_bibtex.py`, `extract_metadata.py`, `search_openalex.py`) and `resources/bib-hygiene/upstream/pyzotero/` (Zotero Web API notes).
- Safety review: `resources/bib-hygiene/README.md`. Scripts call only scholarly APIs (Crossref, DOI, DataCite, OpenAlex, PubMed, arXiv). Do not use `search_google_scholar.py`.

## Workflow
1. **Inventory.** Copy the user's `.bib` (or Zotero export) to `./work/bib/`; never edit the original. Count entries, types, missing DOIs.
2. **Duplicates.** Match on DOI, then normalised title plus first author plus year. List candidate merges; merge only after the user confirms.
3. **Complete and validate.** For each entry with a DOI run `validate_citations.py`; for entries without a DOI search Crossref or OpenAlex by title and propose a DOI only when title, first author and year all match. Flag mismatches (wrong year, page range, journal name, preprint cited instead of published version).
4. **Normalise.** Consistent keys (`firstauthorYEARword`), braces for acronyms and proper nouns in titles (`{UML}`, `{T{\"u}rkiye}`), Turkish characters as UTF-8 with `biblatex`/`biber` or escaped for `bibtex`, journal names full or ISO abbreviated per venue, page ranges with `--`.
5. **Venue style.** IEEE, ACM, APA 7, Springer LNCS, or a DergiPark/TR Dizin journal style (`tr-academic-style`). Check against the venue's template, not memory.
6. **Report.** A change log table (key, field, old, new, source URL) in `./work/bib/report.md` plus the cleaned file.

## Zotero
Use the Web API only with a key the user supplies through the vault or in-chat form; ask before any write (create, update, delete). Prefer read and export; return changes as an import file the user applies.

## Rules
- Never invent a DOI, volume, page or year. Unresolved entries stay flagged.
- Cite retracted papers only with a note; check Crossref `update-to` / Retraction Watch data when available.
