---
name: citation-check
description: >-
  Use when the user wants citations, references, claims, slides or charts in a
  document checked against real sources, or wants BibTeX from DOIs.
---
# Citation check

Two upstream sources:
- Verification workflow: `resources/citation-check/SKILL.md` (with `references/citation_schema.json`). No scripts; it uses web search, web fetch and image reading.
- Metadata and BibTeX tools: `resources/citation-management/SKILL.md` with scripts in `scripts/`.

1. To check whether claims and citations hold up, read the citation-check SKILL.md in full and follow it. For each reference, confirm it exists, that its metadata (authors, year, venue, DOI) is correct, and that it actually supports the claim.
2. For DOI lookups, metadata extraction or BibTeX, read the citation-management SKILL.md. Its scripts call public APIs (Crossref, OpenAlex, PubMed, doi.org, arXiv, DataCite) and need `requests` (`pip install requests` if it's missing). Prefer a scholarly search tool such as Semantic Scholar or arXiv or these APIs over the Google Scholar script, which is fragile. Ignore any mention of a scientific-schematics skill.
3. Report every reference as verified, corrected (show the fix), unverifiable, or likely fabricated. Never fill in a missing DOI or detail by guessing.
4. Format in the venue's style; otherwise APA 7, or IEEE for engineering venues.
