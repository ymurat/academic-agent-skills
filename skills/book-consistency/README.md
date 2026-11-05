# book-consistency

[Book consistency audit](./SKILL.md)

## English

### What it does

Checks a long manuscript, book or thesis for terminology and abbreviation drift, repeated passages and broken cross-references.

### When to use

Load this skill when the task matches: the user wants a long manuscript, book, or thesis (many chapters, tens of thousands of words) checked for consistency: terminology and abbreviation drift, repeated passages across chapters, broken cross-references and numbering, and continuity or contradictions between chapters.

### Example prompts

- Check chapters 1-8 for terminology drift and repeated passages. Build book_bible.md first.
- Find inconsistent abbreviation expansions across this thesis.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- book_bible.md reference file
- Consistency report

### Origin and license

- Origin: Original (structure after chianglianglin/novel-hint, MIT) (https://github.com/chianglianglin/novel-hint)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Never process the whole book in one pass; work chapter by chapter and write intermediate results to files (for long jobs, hand chapters to background workers and merge).
- Do not change the manuscript unless the user asks; if asked, apply fixes on a copy and list every change.
- Respect the author's voice; style preferences are suggestions, not errors.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- 1. Prepare
- 2. Build the reference file (`book_bible.md`)
- 3. Checks
- 4. Report
- Rules

### Related skills

- `citation-check`
- `tr-academic-style`
- `turkish-native`

---

## Türkçe

### Ne yapar

Uzun bir el yazması, kitap veya tezde terim ve kısaltma tutarlılığını, yinelenen pasajları ve çapraz göndermeleri kontrol eder.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Uzun bir el yazması, kitap veya tezde terim ve kısaltma tutarlılığını, yinelenen pasajları ve çapraz göndermeleri kontrol eder.

### Örnek istemler

- 1-8. bölümlerde terim sapması ve yinelenen pasajları kontrol et. Önce book_bible.md oluştur.
- Bu tezde tutarsız kısaltma açılımlarını bul.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- book_bible.md reference file
- Consistency report

### Köken ve lisans

- Köken: Özgün (yapı: chianglianglin/novel-hint, MIT)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- 1. Prepare
- 2. Build the reference file (`book_bible.md`)
- 3. Checks
- 4. Report
- Rules

### İlgili beceriler

- `citation-check`
- `tr-academic-style`
- `turkish-native`
