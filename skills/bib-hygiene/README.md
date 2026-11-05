# bib-hygiene

[Bibliography hygiene (BibTeX and Zotero)](./SKILL.md)

## English

### What it does

Cleans, deduplicates and DOI-completes a BibTeX or Zotero library, validates against Crossref, or formats for a template.

### When to use

Load this skill when the task matches: the user wants a BibTeX or Zotero library cleaned, deduplicated, completed from DOIs, validated against Crossref, or formatted for a journal or thesis template.

### Example prompts

- Deduplicate this refs.bib and complete missing fields from DOIs via Crossref.
- Reformat this Zotero export for the IEEE Transactions template.

### Inputs and outputs

**Inputs**

- BibTeX or Zotero export
- Target style or template if known

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Adapted from K-Dense-AI/scientific-agent-skills (https://github.com/K-Dense-AI/scientific-agent-skills)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Never invent a DOI, volume, page or year.
- Never invent a DOI, volume, page or year. Unresolved entries stay flagged.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Sources in `resources/`
- Workflow
- Zotero
- Rules

### Related skills

- `citation-check`
- `tr-academic-style`

---

## Türkçe

### Ne yapar

BibTeX veya Zotero kütüphanesini temizler, yinelenenleri ayıklar, DOI üzerinden tamamlar, Crossref ile doğrular veya şablona göre biçimler.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: BibTeX veya Zotero kütüphanesini temizler, yinelenenleri ayıklar, DOI üzerinden tamamlar, Crossref ile doğrular veya şablona göre biçimler.

### Örnek istemler

- Bu refs.bib dosyasındaki yinelenenleri ayıkla ve eksik alanları DOI ile tamamla.
- Bu Zotero dışa aktarımını IEEE Transactions şablonuna göre biçimlendir.

### Girdiler ve çıktılar

**Girdiler**

- BibTeX or Zotero export
- Target style or template if known

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: K-Dense-AI/scientific-agent-skills (https://github.com/K-Dense-AI/scientific-agent-skills)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Sources in `resources/`
- Workflow
- Zotero
- Rules

### İlgili beceriler

- `citation-check`
- `tr-academic-style`
