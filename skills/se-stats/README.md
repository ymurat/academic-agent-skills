# se-stats

[SE statistics](./SKILL.md)

## English

### What it does

Designs, analyses or reports statistics for SE experiments, randomized algorithm benchmarks, surveys or similar studies.

### When to use

Load this skill when the task matches: the user designs, analyses or reports statistics for a software engineering experiment, benchmark of randomized algorithms (search-based SE, ML models, test generation), survey, or needs a sample size or power analysis.

### Example prompts

- Choose and report the right statistics for this randomized algorithm benchmark.
- Check whether our pairwise tests and effect sizes match SE reporting practice.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Adapted from K-Dense-AI/scientific-agent-skills (https://github.com/K-Dense-AI/scientific-agent-skills)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Never invent data, p values or effect sizes.
- Never invent data, p values or effect sizes. Run the computation and show the command.
- Statistical significance is not practical significance; interpret the A12 magnitude.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Sources in `resources/`
- Workflow
- Rules

### Related skills

- `empirical-se-standards`
- `icarus-figures`
- `qualitative-methods`
- `statistical-power`
- `tr-academic-style`

---

## Türkçe

### Ne yapar

Yazılım mühendisliği deneyi, rastgele algoritma benchmark’ı, anket veya benzeri için istatistik tasarlar, analiz eder veya raporlar.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Yazılım mühendisliği deneyi, rastgele algoritma benchmark’ı, anket veya benzeri için istatistik tasarlar, analiz eder veya raporlar.

### Örnek istemler

- Bu rastgele algoritma benchmark’ı için doğru istatistiği seç ve raporla.
- Çiftli testlerimiz ve etki büyüklüklerimiz SE raporlama pratiğine uyuyor mu kontrol et.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

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
- Rules

### İlgili beceriler

- `empirical-se-standards`
- `icarus-figures`
- `qualitative-methods`
- `statistical-power`
- `tr-academic-style`
