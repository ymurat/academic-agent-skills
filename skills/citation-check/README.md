# citation-check

[Citation check](./SKILL.md)

## English

### What it does

Checks citations, references, claims, slides or charts against real sources, or builds BibTeX from DOIs.

### When to use

Load this skill when the task matches: the user wants citations, references, claims, slides or charts in a document checked against real sources, or wants BibTeX from DOIs.

### Example prompts

- Verify every citation in this Related Work section against a real source.
- Make BibTeX entries from these DOIs and flag any that do not resolve.

### Inputs and outputs

**Inputs**

- Manuscript, slides or claim list
- Optional DOI list

**Outputs**

- Verification table with pass/fail and sources
- Optional BibTeX

### Origin and license

- Origin: Adapted from serenakeyitan/citation-check-skill and K-Dense-AI/scientific-agent-skills (https://github.com/serenakeyitan/citation-check-skill)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Unresolved DOIs and unverifiable claims must be marked; do not invent citations.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- (flat instruction file; open SKILL.md)

### Related skills

- None named in SKILL.md

---

## Türkçe

### Ne yapar

Belgedeki atıfları, iddiaları, slaytları veya grafikleri gerçek kaynaklara karşı kontrol eder; DOI üzerinden BibTeX üretir.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Belgedeki atıfları, iddiaları, slaytları veya grafikleri gerçek kaynaklara karşı kontrol eder; DOI üzerinden BibTeX üretir.

### Örnek istemler

- Bu Related Work bölümündeki her atıfı gerçek kaynağa karşı doğrula.
- Bu DOI’lerden BibTeX üret; çözülmeyenleri işaretle.

### Girdiler ve çıktılar

**Girdiler**

- Manuscript, slides or claim list
- Optional DOI list

**Çıktılar**

- Verification table with pass/fail and sources
- Optional BibTeX

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: serenakeyitan/citation-check-skill and K-Dense-AI/scientific-agent-skills (https://github.com/serenakeyitan/citation-check-skill)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Çözülmeyen DOI’ler ve doğrulanamayan iddialar işaretlenmelidir; atıf uydurulmaz.
- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- (düz talimat dosyası; SKILL.md dosyasını açın)

### İlgili beceriler

- SKILL.md içinde adlandırılmış ilgili beceri yok
