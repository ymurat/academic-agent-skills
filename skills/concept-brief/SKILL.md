---
name: concept-brief
description: >-
  Use when the user gives a topic or concept and wants a structured,
  source-backed summary or explainer (definition, origin, mechanism, related
  concepts, debates, current state, key sources), e.g. "X kavramını özetle",
  "explain concept Y", "bana Z hakkında brif çıkar".
---
# Concept brief

Produce an evidence-based brief on one concept or topic. Accuracy beats completeness: a section with no verified source says so instead of being filled from memory.

Design credits: evidence grading and audit trail adapted from dgagf111/multi-perspective-research (MIT); explanation layer adapted from guicortei/feynman-technique (MIT).

## Inputs
- The concept or topic (required).
- Reader level: general, student, or specialist (default: specialist/academic).
- Language: the user's language (default Turkish, TDK spelling; keep technical terms in English when no established Turkish term exists, giving the English term in parentheses on first use).
- Length: short (about 1 page) or full (default full).

If the concept is ambiguous (same name in several fields), ask one focused question or state the reading you chose and proceed.

## Research (before writing)
1. Disambiguate: identify field(s) and common synonyms, acronyms, and the English term.
2. Find the authoritative definition: for software/systems topics check SWEBOK v4, ISO/IEC/IEEE standards and glossaries (e.g. ISO/IEC/IEEE 24765), NIST; for AI/governance check NIST AI RMF, OECD, EU AI Act text, ISO/IEC 22989; otherwise a major handbook, encyclopedia of the field, or highly cited review.
3. Find the origin: who introduced or named the concept, in which work, which year. Open the source (publisher page, DOI landing page, archive). If only secondary sources attribute it, say "secondary attribution" and name them.
4. Gather 5-10 key sources: seminal work, a recent review (prefer the last 3 years), standards, and critiques. Prefer peer-reviewed, primary, or official sources; flag preprints, blogs, and vendor material as weaker.
5. Search deliberately for criticism, competing definitions, and failed replications, not only supportive material.
6. Verify every reference exists: resolve the DOI (doi.org or Crossref) or find it on Semantic Scholar / arXiv / the publisher. Never invent a DOI, page number, quote, or year. If the `citation-check` skill is available, run the final reference list through it.
7. Keep a short working log (queries run, sources opened, what each supports) so the brief can be audited; include it only if the user asks or the output is a file.

## Evidence grades
Tag each substantive claim:
- [ÇS] converged: two or more independent reliable sources agree.
- [TK] single source.
- [T] disputed: reliable sources disagree (name both sides).
- [B] not found: no reliable source located; state it plainly rather than guess.
Use the user's language for the tags (English equivalents: [MS], [SS], [D], [NF]). Explain the tags once at the top.

## Output structure
1. **Tek cümlelik tanım** (one-sentence definition in plain words), then the authoritative definition quoted or closely paraphrased with its source.
2. **Köken** (origin): person, work, year, context, with the source.
3. **Nasıl çalışır** (mechanism): explain the mechanism before the label; define every term at first use; at most one analogy, marked as an analogy and with where it breaks. Simplify, never falsify.
4. **Türler ve sınıflandırma** (variants), if any.
5. **İlişkili ve karıştırılan kavramlar**: comparison table (concept | difference | source).
6. **Tartışmalar ve eleştiriler**: each with a source; name who holds which position.
7. **Güncel durum**: developments after 2023, with dates; note regulation or standards updates checked against current sources.
8. **Alan için anlamı**: implications for the user's field (e.g. software engineering, AI, digital governance) only when grounded; mark inference as inference.
9. **Açık sorular / bilinmeyenler**.
10. **Temel kaynaklar**: 5-10 verified references in the target style (APA 7 by default, IEEE for engineering venues), each with DOI or stable URL and a one-line note on why it matters.

For a short brief keep sections 1, 2, 3, 6 and 10.

## Writing rules
- Lead with the definition; no meta opener or closing summary.
- Prose for argument, tables for comparison; varied sentence length, active voice.
- No em dashes, no buzzwords, no stock transitions; hedges only for real uncertainty.
- For Turkish output, apply the `turkish-native` skill if available; for any language, a final `humanizer` pass if available.

## Delivery
- Short briefs go in chat. Long briefs, or when the user wants to keep or share it, go to a document (docx/markdown) or a Page.
- End by naming any section marked [B] or [T] so the user sees the gaps.
