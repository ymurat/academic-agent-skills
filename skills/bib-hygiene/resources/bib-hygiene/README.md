upstream/citation-management and upstream/pyzotero from https://github.com/K-Dense-AI/scientific-agent-skills
(MIT, commit 5f2bc0341354fd5590aef76a533ada1e1e5b4e62, copied 2026-11-01). License: upstream/LICENSE-K-Dense.
Script review: network calls only to api.crossref.org, doi.org, api.datacite.org, api.openalex.org, NCBI eutils, export.arxiv.org,
pmc idconv; search_google_scholar.py uses the third-party `scholarly` scraper (avoid: Scholar terms, fragile).
Env vars read: NCBI_EMAIL, NCBI_API_KEY, OPENALEX_EMAIL, OPENALEX_API_KEY (optional). No exfiltration, no shell exec.
pyzotero has docs only (no scripts); it needs a Zotero API key the user must provide.
