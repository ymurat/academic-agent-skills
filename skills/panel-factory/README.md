# panel-factory

[Panel factory](./SKILL.md)

## English

### What it does

Chooses deliberative panel roles for a review, research question or legal/policy draft and hands briefs to council-protocol.

### When to use

Load this skill when the task matches: a task (paper review, research question, legal or policy draft) needs a deliberative panel of agents and you must decide which roles to convene.

### Example prompts

- Propose a 5-role panel to review this grant proposal. Reuse existing agents where possible.
- Build role briefs for a legal draft review including one adversarial role.

### Inputs and outputs

**Inputs**

- Task type and stakes
- Available evidence and existing teammate agents

**Outputs**

- Role plan table and role briefs for council-protocol

### Origin and license

- Origin: Original
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Do not: out-of-scope topics, fabricating sources, softening findings to please, deferring to other roles.
- Does not create or register agents without user approval.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- 1. Task profile
- 2. Role plan
- 3. Diversity and independence check
- 4. Reuse before create
- 5. Role brief template
- 6. Hand-off
- Basis

### Related skills

- `council-protocol`

---

## Türkçe

### Ne yapar

Bir iş (makale incelemesi, araştırma sorusu, hukuk veya politika taslağı) için müzakere paneli rollerini seçer; çıktıyı council-protocol’e verir.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Bir iş (makale incelemesi, araştırma sorusu, hukuk veya politika taslağı) için müzakere paneli rollerini seçer; çıktıyı council-protocol’e verir.

### Örnek istemler

- Bu hibe önerisini incelemek için 5 rollü panel öner. Var olan agent’ları yeniden kullan.
- Hukuk taslağı incelemesi için biri karşıt olmak üzere rol brifingleri yaz.

### Girdiler ve çıktılar

**Girdiler**

- Task type and stakes
- Available evidence and existing teammate agents

**Çıktılar**

- Role plan table and role briefs for council-protocol

### Köken ve lisans

- Köken: Özgün
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Kullanıcı onayı olmadan agent oluşturmaz veya kaydetmez.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- 1. Task profile
- 2. Role plan
- 3. Diversity and independence check
- 4. Reuse before create
- 5. Role brief template
- 6. Hand-off
- Basis

### İlgili beceriler

- `council-protocol`
