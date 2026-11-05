# ai-threat-review

[AI threat review (defensive)](./SKILL.md)

## English

### What it does

Produces a defensive threat model or security review for AI, LLM, RAG or agent systems (STRIDE, OWASP Top 10 for LLM Applications, MITRE ATLAS).

### When to use

Load this skill when the task matches: the user wants a defensive threat model or security review of an AI, LLM, RAG or agent system: STRIDE, OWASP Top 10 for LLM Applications, MITRE ATLAS, prompt injection and tool misuse.

### Example prompts

- Run a defensive STRIDE and OWASP LLM Top 10 review of this RAG agent design.
- List prompt-injection and tool-misuse threats for this agent architecture.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Adapted from inerthel-agi/security-hardening (https://github.com/inerthel-agi/security-hardening)
- License: Apache-2.0
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- State assumptions; mark threats not validated by testing as hypotheses.
- Defensive review only. No exploit steps, payloads or attack procedures.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Sources in `resources/`
- Workflow
- Teaching and research use
- Rules
- Ek referans

### Related skills

- `c4-model`
- `eu-ai-act`
- `gdpr-compliance`
- `homework-grader`
- `iso42001`
- `kvkk`
- `nist-ai-rmf`

---

## Türkçe

### Ne yapar

Yapay zekâ, LLM, RAG veya agent sistemi için savunma amaçlı tehdit modeli veya güvenlik incelemesi yapar (STRIDE, OWASP LLM Top 10, MITRE ATLAS).

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Yapay zekâ, LLM, RAG veya agent sistemi için savunma amaçlı tehdit modeli veya güvenlik incelemesi yapar (STRIDE, OWASP LLM Top 10, MITRE ATLAS).

### Örnek istemler

- Bu RAG agent tasarımına savunma amaçlı STRIDE ve OWASP LLM Top 10 uygula.
- Bu mimari için prompt injection ve araç kötüye kullanımı tehditlerini listele.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: inerthel-agi/security-hardening (https://github.com/inerthel-agi/security-hardening)
- Lisans: Apache-2.0
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yalnızca savunma incelemesidir. İstismar adımı, yük veya saldırı yordamı vermez.
- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Sources in `resources/`
- Workflow
- Teaching and research use
- Rules
- Ek referans

### İlgili beceriler

- `c4-model`
- `eu-ai-act`
- `gdpr-compliance`
- `homework-grader`
- `iso42001`
- `kvkk`
- `nist-ai-rmf`
