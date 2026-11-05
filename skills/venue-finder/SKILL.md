---
name: venue-finder
description: >-
  Use when the user wants to choose a journal or conference for a manuscript,
  compare candidate venues (scope, indexing, quartile, TR Dizin, APC, review
  time, acceptance), or check whether a journal or publisher is predatory or
  questionable.
---
# Venue finder

Recommend publication venues for a manuscript and check their legitimacy. Every metric comes from a page opened this turn, with the date checked; never state a quartile, impact factor, APC, or review time from memory.

## Inputs
- Title, abstract, keywords, or the manuscript; article type (full paper, short, review, SLR, replication, dataset).
- Constraints: target indexing (SCI-E/SSCI, Scopus, ESCI, TR Dizin), quartile, open access or APC budget, deadline or speed, ACM/IEEE/Springer preference, language (Turkish or English), purpose (e.g. doçentlik or academic incentive points). Infer what you can; state assumptions.

## Step 1: Candidate list (8-15)
- Look where the manuscript's own references were published, and where close recent papers appeared (Semantic Scholar, Google Scholar, DBLP for CS venues).
- Use publisher journal finders (Elsevier JournalFinder, Springer Journal Suggester, IEEE Publication Recommender, Wiley) as inputs, not answers.
- For conferences: CORE ranking (portal.core.edu.au), DBLP history, and the current call for papers with deadlines.
- For Turkish venues: TR Dizin journal list and DergiPark pages (see `turkish-academia`).

## Step 2: Verify each candidate
Open and record (with access date):
- Scope fit: aims and scope page plus 2-3 recent similar articles.
- Indexing: Clarivate Master Journal List (SCI-E/SSCI/ESCI), Scopus source list, TR Dizin, DOAJ for OA journals.
- Quartile/metrics: JCR if accessible, otherwise SJR quartile from scimagojr.com and CiteScore from Scopus; name which metric you used (JCR Q and SJR Q differ).
- APC and OA model (gold, hybrid, diamond, transformative agreement; check whether Turkish institutions have a read-and-publish agreement covering it, e.g. via ULAKBİM/TÜBİTAK EKUAL).
- Speed: time to first decision and to publication if the journal publishes it; else say unknown.
- Acceptance rate only if officially published.
- Special issues currently open, and their deadlines.

## Step 3: Predatory or questionable check
Flag any of: not actually indexed where it claims; fake or misleading metrics ("Global Impact Factor" and similar); aggressive solicitation; very fast acceptance promises; editorial board unverifiable or off-field; hijacked journal websites (compare URL with Scopus/Clarivate/ISSN portal listing; check the Retraction Watch Hijacked Journal Checker); scope too broad; publisher on known watch lists. Check Think.Check.Submit criteria, DOAJ status, COPE membership, ISSN at portal.issn.org. Note that Beall-style lists are outdated and unofficial; treat them as weak evidence. Also check whether Clarivate recently delisted the journal ("on hold" or removed). Report findings with evidence, not just a label.

## Step 4: Output
1. Recommendation first: top 3 with a one-line reason each, plus a safer fallback and an ambitious reach option.
2. Comparison table: venue | publisher | indexing | quartile (metric, year) | APC/OA | review time | scope fit (high/medium/low) | risks | source links.
3. Notes on fit: what to adapt in the manuscript for each top venue (length limits, format, structure).
4. Anything unverifiable marked "doğrulanamadı".
Use a table for the comparison and prose for the reasoning. No em dashes, no buzzwords.
