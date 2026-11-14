# Changelog

All notable changes to this repository are listed here.

## 1.6.2 - 2026-11-14

- Added Zenodo DOI (concept DOI 10.5281/zenodo.24203674) to README.md and CITATION.cff.
- Deduplicated vendored files across skill folders into common/ directory, saving approximately 707 KB. Eleven skills now require common/ alongside when copied separately (citation-check, bib-hygiene, scientific-writing, academic-humanizer, humanizer, slr-prisma, citation-management, icarus-figures, experimental-design, statistical-power, se-stats).
- Slimmed teaching-skills README by removing redundant boilerplate (51 lines, 50% reduction) while preserving all substantive guidance.
- Added GitHub Actions CI workflow with consistency checks for SKILL.md frontmatter, README catalog integrity, LICENSE file presence, email address policies, em dash usage, and CITATION.cff validation.
- Added 30 missing LICENSE-upstream files in adapted skills to comply with repository licensing conventions.
- Fixed YAML frontmatter in experimental-design SKILL.md.
- Removed personal email addresses from vendored scripts (excluded upstream vendor files in resources/).

## 1.6.1 (2026-11-13)
Enabled Zenodo archiving; no skill changes. / Zenodo arşivlemesi açıldı; skill değişikliği yok.

## 1.6.0 (2026-11-13)
- New skill `dreaming`: propose-then-apply memory consolidation for agents with typed memory stores (profile, journal, shared stores) or MEMORY.md sections. Harvest, score, reflect, stage, apply workflow. Original work. / Yeni beceri `dreaming`: tür belirtilmiş hafıza depoları veya MEMORY.md bölümleri olan agent'lar için öner-sonra-uygula hafıza konsolidasyonu. Toplama, puanlama, düşünme, hazırlama, uygulama. Özgün çalışma.
- New skill `promise-log`: extract and track commitments from emails, meeting notes, chats or transcripts into a sourced log. Adapted from cobusgreyling/grok-bot-templates (MIT). / Yeni beceri `promise-log`: e-posta, toplantı notları, sohbet veya kayıtlardan sözleri çıkarır ve kaynaklı günlükte takip eder. cobusgreyling/grok-bot-templates'ten uyarlama (MIT).
- New skill `memory-gardening`: fix a specific stale, wrong, or duplicate memory fact on request. Complements dreaming. Adapted from cobusgreyling/grok-bot-templates (MIT). / Yeni beceri `memory-gardening`: istek üzerine belirli bir eskimiş, yanlış veya yinelenen hafıza bilgisini düzeltir. Dreaming'i tamamlar. cobusgreyling/grok-bot-templates'ten uyarlama (MIT).

### Housekeeping / Bakım

- LICENSE: Replaced with canonical MIT text. Scope notice (MIT applies to original skills, vendored material keeps its own license) moved to README.md, README.tr.md (License section) and THIRD_PARTY.md. / LICENSE: Standart MIT metniyle değiştirildi. Kapsam notu (MIT özgün beceriler için geçerli, paketlenmiş malzeme kendi lisansını korur) README.md, README.tr.md (Lisans bölümü) ve THIRD_PARTY.md'ye taşındı.
- THIRD_PARTY.md: Added entry for Council of Europe CETS 225 (official treaty text, public domain with attribution). Added inspiration credits for task-graph and council-protocol (@hanakoxbt / Karpathy structure). Added LICENSE-upstream reference for empirical-se-standards bundled material (ACM SIGSOFT Empirical Standards, CC0). / THIRD_PARTY.md: Avrupa Konseyi CETS 225 için kayıt eklendi (resmi antlaşma metni, atıfla kamu malı). task-graph ve council-protocol için ilham kaynağı kredileri eklendi (@hanakoxbt / Karpathy yapısı). empirical-se-standards paketli malzemesi için LICENSE-upstream referansı eklendi (ACM SIGSOFT Empirical Standards, CC0).
- README files: 11 original skills (concept-brief, ai-use-disclosure, council-protocol, kvkk, latex-build, llm-evaluation, panel-factory, reviewer-response-tracker, spi-assessment, thesis-jury-prep, venue-finder) now state "Original work; no third-party material" instead of pointing to THIRD_PARTY.md. / README dosyaları: 11 özgün beceri (concept-brief, ai-use-disclosure, council-protocol, kvkk, latex-build, llm-evaluation, panel-factory, reviewer-response-tracker, spi-assessment, thesis-jury-prep, venue-finder) artık THIRD_PARTY.md'ye işaret etmek yerine "Özgün çalışma; üçüncü taraf malzeme yok" belirtiyor.
- Hardcoded paths: Removed private build paths from CHANGELOG.md provenance section. Replaced hardcoded `/workspace` output paths in 6 wrapper SKILL.md files (peer-review, scientific-writing, tr-academic-style, docentlik-eligibility, tubitak-proposal, turkish-academia) with "current working directory or a path the user names". / Sabit yollar: CHANGELOG.md köken bölümünden özel yapı yolları kaldırıldı. 6 sarmalayıcı SKILL.md dosyasındaki (peer-review, scientific-writing, tr-academic-style, docentlik-eligibility, tubitak-proposal, turkish-academia) `/workspace` çıktı yolları "mevcut çalışma dizini veya kullanıcının adlandırdığı yol" ile değiştirildi.
- Vendored metadata: Removed 5 `.github/` directories from resources/ (c4-model, humanizer, icarus-figures, teaching-skills, turkish-native). Moved `icarus-figures/resources/Icarus-Figures/.claude/` to `references-claude/` and updated all references. Added `skills/**/resources/**/.github/` to .gitignore. / Paketli üst veri: resources/ altından 5 `.github/` dizini kaldırıldı (c4-model, humanizer, icarus-figures, teaching-skills, turkish-native). `icarus-figures/resources/Icarus-Figures/.claude/` dizini `references-claude/` olarak taşındı ve tüm referanslar güncellendi. .gitignore'a `skills/**/resources/**/.github/` eklendi.
- CONTRIBUTING.md: Documented LICENSE-upstream naming convention for adapted skills. / CONTRIBUTING.md: Uyarlanmış beceriler için LICENSE-upstream adlandırma kuralı belgelendi.
- CHANGELOG.md: Replaced three em dashes (lines 37-39, terms-of-use section) with colons and periods. / CHANGELOG.md: Üç tire çizgisi (satır 37-39, kullanım koşulları bölümü) iki nokta üst üste ve noktalarla değiştirildi.

## 1.5.0 (2026-11-07)
- New skill `prepare-artifacts`: package research code and data for artifact evaluation and badging (Apache-2.0 adaptation). / Yeni beceri `prepare-artifacts`: artifact evaluation ve rozet için araştırma kodu ve verisini paketler (Apache-2.0 uyarlaması).
- README cite section: removed the leftover sentence that said no ORCID was listed; ORCID is already in the author line and CITATION.cff.

## 1.4.0 (2026-11-05)
- New skill `task-graph`: gated, resumable task graphs for research and writing work. / Yeni beceri `task-graph`: araştırma ve yazım işleri için kontrol kapılı, sürdürülebilir iş grafı.

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

- Local evidence of authorship: matching `SKILL.md` trees built from local workflow copies with dates matching development sessions; vetting notes kept privately.
- Web / GitHub search for near-identical skill text (unique phrases such as "Guards against sycophancy and conformity", "Feed its output to `council-protocol`", "Every metric comes from a page opened this turn", and repo names `panel-factory` / `council-protocol` / `latex-build` / `venue-finder` as SKILL.md names): no near-identical upstream found. Thematically related skills exist (e.g. other "council" or "panel" or LaTeX setup skills) with different wording and structure.
- Cross-session `ReadTranscript` of this bot could not page other owner sessions by keyword (tool supports `in` / `limit` / `before` only; this session's transcript covers the packaging work, not the original UpdateSkill turns). Creation method is therefore inferred from local workflow/skillvet artifacts + absence of matching upstream, not from a recovered chat log of UpdateSkill. **Conclusion: leave Origin as Original (MIT). No THIRD_PARTY or LICENSE change required for these.**
- Other Original / Original* skills (ai-governance-frameworks, ai-use-disclosure, book-consistency, concept-brief, empirical-se-standards, kvkk, llm-evaluation, reviewer-response-tracker, spi-assessment, thesis-jury-prep) likewise have local workflow copies and no near-identical GitHub SKILL.md match found in the same search pass. Skills marked Original* document design credits or bundled CC0 text in README / THIRD_PARTY.

### Terms of use / robots (site query scripts)

Checked 2026-11-05 (Europe/Istanbul):

1. **DergiPark** https://dergipark.org.tr/robots.txt: `User-agent: *` Disallow `/login`, `/search` (and TR/EN variants); AhrefsBot Disallow `/`. Policy https://dergipark.org.tr/tr/pub/page/dergipark-politikasi (v1.0, 2026-05-05) covers users/journals, supports metadata harvesting in principle (harmanlama) but does not clearly license third-party redistributed scrapers of HTML search (which robots.txt blocks). Public API docs exist under `/api/public/`, but bulk client redistribution remains unclear-risky.
2. **YÖK Ulusal Tez Merkezi** https://tez.yok.gov.tr/UlusalTezMerkezi/: FAQ https://tez.yok.gov.tr/UlusalTezMerkezi/sss.jsp (free search / full text for permitted theses; no photocopy). No official public API. `robots.txt` not reliably fetchable from this environment (TLS EOF via curl). No published automation ToS found. Unclear-risky for redistributed automated clients.
3. **TR Dizin** https://trdizin.gov.tr/robots.txt: mostly `Allow: /` with a few static Disallows plus sitemap. A live "Kullanım Şartları" HTML page was not reachable at the previously indexed `/kullanim-sartlari/` URL (HTTP 404 from this environment). The unofficial Elasticsearch search surface at `search.trdizin.gov.tr` has no published API terms found. Unclear-risky for redistributed automated search clients.

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
