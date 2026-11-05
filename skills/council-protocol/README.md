# council-protocol

[Council protocol](./SKILL.md)

## English

### What it does

Runs multi-agent deliberation on one question and merges views into a synthesis with recorded dissent.

### When to use

Load this skill when the task matches: several agents must deliberate on one question and their views must be combined into a single, honest synthesis with recorded dissent.

### Example prompts

- Run a council on whether this manuscript is ready for submission. Record dissent.
- Synthesize these five independent agent reviews into consensus, majority and dissent.

### Inputs and outputs

**Inputs**

- Panel briefs from panel-factory
- Independent first-round answers

**Outputs**

- Synthesis: consensus, majority, dissent, unknowns, recommendation

### Origin and license

- Origin: Original
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Moderator does not vote. Low-confidence or split high-stakes points escalate to the user.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Evidence in one paragraph
- Steps
- Guards against sycophancy and conformity
- Synthesis format

### Related skills

- `panel-factory`

---

## Türkçe

### Ne yapar

Birden fazla agent aynı soruyu tartışır; görüşler tek bir sentezde birleştirilir, muhalefet kayda geçer.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Birden fazla agent aynı soruyu tartışır; görüşler tek bir sentezde birleştirilir, muhalefet kayda geçer.

### Örnek istemler

- Bu el yazmasının gönderime hazır olup olmadığına dair kurul çalıştır. Muhalefeti kaydet.
- Bu beş bağımsız agent incelemesini uzlaşı, çoğunluk ve muhalefet olarak sentezle.

### Girdiler ve çıktılar

**Girdiler**

- Panel briefs from panel-factory
- Independent first-round answers

**Çıktılar**

- Synthesis: consensus, majority, dissent, unknowns, recommendation

### Köken ve lisans

- Köken: Özgün
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Moderatör oy kullanmaz. Düşük güven veya bölünmüş yüksek riskli noktalar kullanıcıya yükseltilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Evidence in one paragraph
- Steps
- Guards against sycophancy and conformity
- Synthesis format

### İlgili beceriler

- `panel-factory`
