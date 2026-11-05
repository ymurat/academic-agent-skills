# statistical-power

[Statistical Power & Sample Size](./SKILL.md)

## English

### What it does

Computes sample size, statistical power, minimum detectable effect or power curves (t-test, ANOVA, proportions, correlation, regression or simulation).

### When to use

Load this skill when the task matches: planning a study and you need a sample size, statistical power, minimum detectable effect or power curve (t-test, ANOVA, proportions, correlation, chi-square, regression, or simulation-based power for GLMs, mixed models, cluster designs).

### Example prompts

- Compute sample size for a two-sample t-test with d=0.5, alpha=0.05, power=0.8.
- Simulate power for this unbalanced ANOVA before we recruit developers.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- n, power or MDE with assumptions stated

### Origin and license

- Origin: Adapted from K-Dense-AI/scientific-agent-skills (https://github.com/K-Dense-AI/scientific-agent-skills)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Assumptions (effect size, variance) drive results; wrong inputs produce wrong n.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Overview
- When to Use This Skill
- Installation
- The one decision that drives everything: the effect size
- Quick recipes (closed-form)
- When analytical assumptions do not fit: simulate
- Adjustments people forget
- Workflow
- Reporting template
- Common pitfalls
- Resources
- Software engineering examples

### Related skills

- None named in SKILL.md

---

## Türkçe

### Ne yapar

Örneklem büyüklüğü, istatistiksel güç, minimum tespit edilebilir etki veya güç eğrisi hesaplar (t-test, ANOVA, oran, korelasyon, regresyon veya simülasyon).

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Örneklem büyüklüğü, istatistiksel güç, minimum tespit edilebilir etki veya güç eğrisi hesaplar (t-test, ANOVA, oran, korelasyon, regresyon veya simülasyon).

### Örnek istemler

- d=0.5, alpha=0.05, power=0.8 iki örneklemli t-test için örneklem büyüklüğü hesapla.
- Dengesiz ANOVA için geliştirici toplamadan önce güç simülasyonu yap.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- n, power or MDE with assumptions stated

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: K-Dense-AI/scientific-agent-skills (https://github.com/K-Dense-AI/scientific-agent-skills)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Sonuçları etki büyüklüğü ve varyans varsayımları belirler; yanlış girdi yanlış n üretir.
- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Overview
- When to Use This Skill
- Installation
- The one decision that drives everything: the effect size
- Quick recipes (closed-form)
- When analytical assumptions do not fit: simulate
- Adjustments people forget
- Workflow
- Reporting template
- Common pitfalls
- Resources
- Software engineering examples

### İlgili beceriler

- SKILL.md içinde adlandırılmış ilgili beceri yok
