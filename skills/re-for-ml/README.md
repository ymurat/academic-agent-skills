# re-for-ml

[Requirements engineering for ML](./SKILL.md)

## English

### What it does

Writes or reviews requirements for systems with ML components: EARS statements, data requirements, ML quality requirements, model and dataset documentation.

### When to use

Load this skill when the task matches: the user writes or reviews requirements for a system with ML components: EARS statements, data requirements, ML-specific quality requirements, model and dataset documentation, and traceability to data and evaluation.

### Example prompts

- Write EARS requirements and data requirements for this defect-prediction service.
- Review these ML quality requirements and the model card gaps.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Adapted from GodModeAI2025/specforge-ai-skill (https://github.com/GodModeAI2025/specforge-ai-skill)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Do not invent thresholds; propose ranges and mark them for stakeholder decision.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Sources in `resources/`
- Workflow
- Rules

### Related skills

- `agile-v`
- `ai-threat-review`
- `eu-ai-act`
- `gdpr-compliance`
- `kvkk`
- `tubitak-proposal`

---

## Türkçe

### Ne yapar

ML bileşenli sistem için gereksinim yazar veya gözden geçirir: EARS ifadeleri, veri gereksinimleri, model ve veri seti belgelemesi.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: ML bileşenli sistem için gereksinim yazar veya gözden geçirir: EARS ifadeleri, veri gereksinimleri, model ve veri seti belgelemesi.

### Örnek istemler

- Bu kusur tahmin servisi için EARS ve veri gereksinimleri yaz.
- Bu ML kalite gereksinimlerini ve model card boşluklarını gözden geçir.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: GodModeAI2025/specforge-ai-skill (https://github.com/GodModeAI2025/specforge-ai-skill)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Sources in `resources/`
- Workflow
- Rules

### İlgili beceriler

- `agile-v`
- `ai-threat-review`
- `eu-ai-act`
- `gdpr-compliance`
- `kvkk`
- `tubitak-proposal`
