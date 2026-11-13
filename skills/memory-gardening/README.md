# memory-gardening

[Fix a specific stale, wrong, or duplicate memory fact](./SKILL.md)

## English

### What it does

Corrects, merges, or forgets a specific stale, wrong, or duplicate memory fact the owner identified. Searches for the exact recorded text, compares it against a source of truth, shows a diff, waits for approval, then applies only the approved changes. Complements the dreaming skill: dreaming harvests new candidates on a schedule; memory-gardening fixes a named bad fact on request.

### When to use

Load this skill when the owner points at a fact the bot keeps using that is out of date or wrong, two memory entries contradict or duplicate each other, or a volatile figure was stored as if it were durable.

### Example prompts

- The bot keeps saying I prefer method X, but I never said that. Fix it.
- My timezone is recorded as UTC but I'm in Europe/Istanbul. Update memory.
- Memory has two journal entries for the same conference deadline. Merge them.
- Remove the old usage percentage from memory; that number changes daily.

### Inputs and outputs

**Inputs**

- The stale or duplicate claim, quoted
- The source of truth that contradicts it (owner's words, a file, a live tool result) with its date
- Which assistant owns the memory

**Outputs**

- Exact recorded text found in memory
- Small diff (old, new, type, reason)
- Applied diff after approval
- Short "do not remember" list of volatile facts

### Origin and license

- Origin: Adapted
- License: MIT
- Upstream: [cobusgreyling/grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) (`skills/garden-memory`), Copyright 2026 Cobus Greyling
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and `LICENSE-UPSTREAM` in this folder.

### Limitations

- Every write and forget needs the owner's explicit yes on that item.
- Never edits another assistant's private memory or profile. Stages the correction for the owner to pass along.
- Does not mine private conversations for gossip or third-party personal details.
- No correction without a source and a date.
- Unrelated boundaries, standing rules, and safety instructions are not touched.
- No secret, address, phone, email, or card detail is written to memory.

### Sections in SKILL.md

- When to use
- Inputs
- Steps
- Validation
- Return
- Needs approval

### Related skills

- `dreaming` for scheduled memory consolidation (memory-gardening fixes a specific fact on request)

---

## Türkçe

### Ne yapar

Sahibin belirlediği belirli bir eskimiş, yanlış veya yinelenen hafıza bilgisini düzeltir, birleştirir veya unutur. Kaydedilmiş tam metni arar, bir doğruluk kaynağıyla karşılaştırır, farkı gösterir, onay bekler, sonra yalnızca onaylanmış değişiklikleri uygular. Dreaming becerisini tamamlar: dreaming takvimli olarak yeni adayları toplar; memory-gardening istek üzerine adlandırılmış kötü bir bilgiyi düzeltir.

### Ne zaman kullanılır

Sahip, botun kullanmaya devam ettiği eskimiş veya yanlış bir bilgiyi işaret ettiğinde, iki hafıza kaydı çeliştiğinde veya yinelendiğinde ya da değişken bir rakam kalıcıymış gibi saklandığında bu beceriyi yükleyin.

### Örnek istemler

- Bot X yöntemini tercih ettiğimi söylüyor ama ben öyle bir şey demedim. Düzelt.
- Zaman dilimim hafızada UTC olarak kayıtlı ama ben Europe/Istanbul'dayım. Hafızayı güncelle.
- Hafızada aynı konferans son tarihine dair iki journal kaydı var. Birleştir.
- Eski kullanım yüzdesini hafızadan kaldır; o sayı her gün değişir.

### Girdiler ve çıktılar

**Girdiler**

- Eskimiş veya yinelenen iddia, alıntılanmış
- Onu çürüten doğruluk kaynağı (sahibin sözleri, bir dosya, canlı araç sonucu) ve tarihi
- Hangi asistan hafızanın sahibi

**Çıktılar**

- Hafızada bulunan kaydedilmiş tam metin
- Küçük fark (eski, yeni, tür, neden)
- Onay sonrası uygulanmış fark
- Kısa "hatırlama" listesi (canlı okunması gereken değişken bilgiler)

### Köken ve lisans

- Köken: Uyarlama
- Lisans: MIT
- Üst akış: [cobusgreyling/grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) (`skills/garden-memory`), Copyright 2026 Cobus Greyling
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE-UPSTREAM`.

### Sınırlar

- Her yazma ve unutma o madde için sahibin açık evetini gerektirir.
- Başka bir asistanın özel hafızasını veya profilini asla düzenlemez. Düzeltmeyi sahibin aktarması için hazırlar.
- Özel konuşmalardan dedikodu veya üçüncü şahıs kişisel ayrıntıları toplamaz.
- Kaynak ve tarih olmadan düzeltme yapılmaz.
- İlgisiz sınırlar, süregelen kurallar ve güvenlik talimatlarına dokunulmaz.
- Hafızaya gizli, adres, telefon, e-posta veya kart ayrıntısı yazılmaz.

### SKILL.md bölümleri

- Ne zaman kullanılır
- Girdiler
- Adımlar
- Doğrulama
- Dönüş
- Onay gerektiren işler

### İlgili beceriler

- Takvimli hafıza konsolidasyonu için `dreaming` (memory-gardening istek üzerine belirli bilgiyi düzeltir)
