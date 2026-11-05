# concept-brief

[Concept brief](./SKILL.md)

## English

### What it does

Produces a structured, source-backed summary of a topic or concept (definition, origin, mechanism, debates, current state, key sources).

### When to use

Load this skill when the task matches: the user gives a topic or concept and wants a structured, source-backed summary or explainer (definition, origin, mechanism, related concepts, debates, current state, key sources), e.g. "X kavramını özetle", "explain concept Y", "bana Z hakkında brif çıkar".

### Example prompts

- Write a source-backed brief on "construct validity in software experiments".
- Explain differential privacy for a methods chapter: definition, origin, debates, key sources.

### Inputs and outputs

**Inputs**

- The concept or topic (required).
- Reader level: general, student, or specialist (default: specialist/academic).
- Language: the user's language (default Turkish, TDK spelling; keep technical terms in English when no established Turkish term exists, giving the English term in parentheses on first use).
- Length: short (about 1 page) or full (default full).

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Original (design credits: dgagf111/multi-perspective-research, guicortei/feynman-technique, both MIT)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Inputs
- Research (before writing)
- Evidence grades
- Output structure
- Writing rules
- Delivery

### Related skills

- `citation-check`
- `humanizer`
- `turkish-native`

---

## Türkçe

### Ne yapar

Bir konu veya kavram için kaynaklara dayalı yapılandırılmış özet üretir (tanım, köken, mekanizma, tartışmalar, güncel durum).

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Bir konu veya kavram için kaynaklara dayalı yapılandırılmış özet üretir (tanım, köken, mekanizma, tartışmalar, güncel durum).

### Örnek istemler

- "Yazılım deneylerinde yapı geçerliği" için kaynaklara dayalı kısa brifing yaz.
- Differential privacy’yi yöntem bölümü için açıkla: tanım, köken, tartışmalar, ana kaynaklar.

### Girdiler ve çıktılar

**Girdiler**

- The concept or topic (required).
- Reader level: general, student, or specialist (default: specialist/academic).
- Language: the user's language (default Turkish, TDK spelling; keep technical terms in English when no established Turkish term exists, giving the English term in parentheses on first use).
- Length: short (about 1 page) or full (default full).

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Özgün (tasarım kredisi: dgagf111/multi-perspective-research, guicortei/feynman-technique, ikisi de MIT)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Inputs
- Research (before writing)
- Evidence grades
- Output structure
- Writing rules
- Delivery

### İlgili beceriler

- `citation-check`
- `humanizer`
- `turkish-native`
