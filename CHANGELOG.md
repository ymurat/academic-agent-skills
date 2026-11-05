# Changelog

All notable changes to this repository are listed here.

## 1.3.0 (2026-11-05)
- council-protocol: added "Gates, retries and handoff" (evidence order at gates, mechanical work as code, three-attempt correction loop, progress.md handoff). Adapted from a public prompt by @hanakoxbt inspired by Karpathy's autoresearch.
- council-protocol: "Kapılar, yeniden deneme ve devir" bölümü eklendi (kapılarda kanıt sırası, mekanik işlerin koda verilmesi, üç denemeli düzeltme döngüsü, progress.md devir notu).

## [1.2.0] - 2026-11-05

### Changed

- Removed the personal email address from `CITATION.cff`. Added ORCID `https://orcid.org/0000-0002-2446-3224` (orcid field) and to the author lines in `README.md` / `README.tr.md`. Affiliation remains Gazi University. No other contact channels added.
- Slimmed `skills/icarus-figures/`: deleted upstream `examples/` gallery (~13 MB of PNGs). Skill runtime paths (`SKILL.md`, `paperfig/`, `scripts/`, MIT `LICENSE`) kept. Note in skill README and `EXAMPLES_REMOVED.md`. Git history still contains old blobs; history was not rewritten and was not force-pushed.
- `yok-tez` and `turkish-academia`: removed automated query / harvest scripts for tez.yok.gov.tr, dergipark.org.tr and trdizin.gov.tr (and the unofficial TR Dizin search API). Kept manual-use instructions. See terms findings below and `scripts/README.md` stubs.

### Provenance (Original skills)

Verified 2026-11-05 for skills marked Original / Original* (focus: panel-factory, council-protocol, latex-build, venue-finder; also other Originals):

- Local evidence of authorship: matching `SKILL.md` trees under `/home/box/agent-data/workflows/` with mtimes in Europe/Istanbul: venue-finder 2026-11-01 01:56, latex-build 2026-11-01 02:16, panel-factory and council-protocol 2026-11-04 04:02; drafts also under `/workspace/skillvet/out/panel-factory` and `council-protocol` (2026-11-04 04:01). Build report `/workspace/academic-agent-skills-report.md` lists them as Original with no upstream URL.
- Web / GitHub search for near-identical skill text (unique phrases such as "Guards against sycophancy and conformity", "Feed its output to `council-protocol`", "Every metric comes from a page opened this turn", and repo names `panel-factory` / `council-protocol` / `latex-build` / `venue-finder` as SKILL.md names): no near-identical upstream found. Thematically related skills exist (e.g. other "council" or "panel" or LaTeX setup skills) with different wording and structure.
- Cross-session `ReadTranscript` of this bot could not page other owner sessions by keyword (tool supports `in` / `limit` / `before` only; this session's transcript covers the packaging work, not the original UpdateSkill turns). Creation method is therefore inferred from local workflow/skillvet artifacts + absence of matching upstream, not from a recovered chat log of UpdateSkill. **Conclusion: leave Origin as Original (MIT). No THIRD_PARTY or LICENSE change required for these.**
- Other Original / Original* skills (ai-governance-frameworks, ai-use-disclosure, book-consistency, concept-brief, empirical-se-standards, kvkk, llm-evaluation, reviewer-response-tracker, spi-assessment, thesis-jury-prep) likewise have local workflow copies and no near-identical GitHub SKILL.md match found in the same search pass; book-consistency / concept-brief / empirical-se-standards already document design credits or bundled CC0 text in README / THIRD_PARTY.

### Terms of use / robots (site query scripts)

Checked 2026-11-05 (Europe/Istanbul):

1. **DergiPark** https://dergipark.org.tr/robots.txt — `User-agent: *` Disallow `/login`, `/search` (and TR/EN variants); AhrefsBot Disallow `/`. Policy https://dergipark.org.tr/tr/pub/page/dergipark-politikasi (v1.0, 2026-05-05) covers users/journals; supports metadata harvesting in principle (harmanlama) but does **not** clearly license third-party redistributed scrapers of HTML search (which robots.txt blocks). Public API docs exist under `/api/public/`, but bulk client redistribution remains unclear-risky.
2. **YÖK Ulusal Tez Merkezi** https://tez.yok.gov.tr/UlusalTezMerkezi/ — FAQ https://tez.yok.gov.tr/UlusalTezMerkezi/sss.jsp (free search / full text for permitted theses; no photocopy). No official public API. `robots.txt` not reliably fetchable from this environment (TLS EOF via curl). No published automation ToS found. Unclear-risky for redistributed automated clients.
3. **TR Dizin** https://trdizin.gov.tr/robots.txt — mostly `Allow: /` with a few static Disallows + sitemap. A live "Kullanım Şartları" HTML page was not reachable at the previously indexed `/kullanim-sartlari/` URL (HTTP 404 from this environment). The unofficial Elasticsearch search surface at `search.trdizin.gov.tr` has no published API terms found. Unclear-risky for redistributed automated search clients.

**Action taken:** remove those scripts; keep manual browser instructions.

### Türkçe özet (1.2.0)

- `CITATION.cff` ve kök README’lerden gmail kaldırıldı; ORCID eklendi (Gazi Üniversitesi).
- `icarus-figures` örnek galerisi silindi (~13 MB); MIT lisans duruyor; git geçmişi yeniden yazılmadı.
- `yok-tez` / `turkish-academia` otomatik sorgu betikleri kaldırıldı (site koşulları / robots belirsiz veya riskli); elle kullanım talimatı kaldı.
- Original becerilerin kökeni yerel workflow + web araması ile doğrulandı; uyarlama kanıtı yok, etiket Original kaldı.

## [1.1.0] - 2026-11-05

### Added

- Bilingual `README.md` per skill (English and Türkçe): what it does, when to use, example prompts, inputs/outputs, origin and license, limitations
- Root `README.tr.md` (full Turkish mirror) with cross-links to `README.md`
- `CONTRIBUTING.md` (English and Türkçe)
- `CITATION.cff` (Murat Yılmaz, Gazi University; no ORCID listed)
- `CHANGELOG.md`
- Turkish section in `THIRD_PARTY.md`

### Fixed

- `skills/talk-prep-2/SKILL.md` frontmatter `name` aligned to folder name `talk-prep-2`
- Root README expanded with install paths (Claude Code, Cursor, Codex), quick start, grouped catalog, disclaimer and cite section
- `.gitignore` extended for common editor and Python noise

## [1.0.0] - 2026-11-05

### Added

- Initial public release of 47 academic agent skills
- Root `README.md`, `LICENSE` (MIT), `THIRD_PARTY.md`
