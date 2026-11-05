# reviewer-response-tracker

[Reviewer response tracker](./SKILL.md)

## English

### What it does

Tracks every reviewer and editor comment across revision rounds to a decision, a page/line change and a reply.

### When to use

Load this skill when the task matches: the user handles a journal or conference revision across one or more rounds and needs every reviewer and editor comment tracked to a decision, a manuscript change with page and line, and a response letter entry.

### Example prompts

- Build a tracker for all R1/R2 comments with decisions, page changes and reply text.
- Turn this decision letter into a revision checklist linked to latexdiff.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Comment tracker with decisions, page/line changes and reply text

### Origin and license

- Origin: Original
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Never claim a change that is not in the manuscript.
- Never claim a change that is not in the manuscript. Never paraphrase a reviewer inside quotation marks.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Files
- Workflow
- Output
- Rules

### Related skills

- `academic-humanizer`
- `citation-check`
- `tr-academic-style`
- `turkish-native`

---

## Türkçe

### Ne yapar

Dergi veya konferans revizyonunda her hakem ve editör yorumunu karara, sayfa/satır değişikliğine ve yanıt metnine bağlar.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Dergi veya konferans revizyonunda her hakem ve editör yorumunu karara, sayfa/satır değişikliğine ve yanıt metnine bağlar.

### Örnek istemler

- Tüm R1/R2 yorumları için karar, sayfa değişikliği ve yanıt metni izleyici tablosu kur.
- Bu karar mektubunu latexdiff’e bağlı düzeltme kontrol listesine çevir.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Comment tracker with decisions, page/line changes and reply text

### Köken ve lisans

- Köken: Özgün
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Files
- Workflow
- Output
- Rules

### İlgili beceriler

- `academic-humanizer`
- `citation-check`
- `tr-academic-style`
- `turkish-native`
