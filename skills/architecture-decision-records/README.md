# architecture-decision-records

[Architecture Decision Records](./SKILL.md)

## English

### What it does

Records a significant architectural choice as a numbered ADR under docs/adr/ with context, alternatives and consequences.

### When to use

Load this skill when the task matches: a significant architectural choice is made or questioned (framework, database, pattern, API, deployment) and it should be recorded as a numbered ADR in docs/adr/ with context, alternatives, consequences and an index.

### Example prompts

- Write ADR-0007 for choosing PostgreSQL over MongoDB for the experiment store.
- Turn this Slack decision thread into a numbered ADR with alternatives and consequences.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Numbered ADR file under docs/adr/

### Origin and license

- Origin: Adapted from affaan-m/ECC (https://github.com/affaan-m/ECC)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- When to Activate
- ADR Format
- Context
- Decision
- Alternatives Considered
- Consequences
- Workflow
- Decision Detection Signals
- What Makes a Good ADR
- ADR Lifecycle
- Categories of Decisions Worth Recording
- Teaching and research use

### Related skills

- None named in SKILL.md

---

## Türkçe

### Ne yapar

Önemli bir mimari seçimi (çerçeve, veritabanı, desen, API, dağıtım) numaralı ADR olarak docs/adr/ altında kaydeder.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Önemli bir mimari seçimi (çerçeve, veritabanı, desen, API, dağıtım) numaralı ADR olarak docs/adr/ altında kaydeder.

### Örnek istemler

- Deney deposu için PostgreSQL tercihini ADR-0007 olarak yaz.
- Bu karar tartışmasını alternatifler ve sonuçlarla numaralı ADR’ye dönüştür.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Numbered ADR file under docs/adr/

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: affaan-m/ECC (https://github.com/affaan-m/ECC)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- When to Activate
- ADR Format
- Context
- Decision
- Alternatives Considered
- Consequences
- Workflow
- Decision Detection Signals
- What Makes a Good ADR
- ADR Lifecycle
- Categories of Decisions Worth Recording
- Teaching and research use

### İlgili beceriler

- SKILL.md içinde adlandırılmış ilgili beceri yok
