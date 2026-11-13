# dreaming

[Propose-then-apply memory consolidation](./SKILL.md)

## English

### What it does

Consolidates conversation traces into durable memory proposals through a harvest, score, and apply workflow. Reviews memory candidates, proposes additions, corrections, and deletions, then applies only the items the user explicitly approves. Never writes to live memory during harvest or review.

### When to use

Load this skill when running a nightly or on-demand memory hygiene sweep, reviewing staged memory candidates, applying approved memory updates, or reverting memory changes. Do not use for a single explicit "remember this" request.

### Example prompts

- Dream: scan recent conversations and propose new memory facts.
- Review memory candidates and show me what would be added to profile and journal.
- Apply items 2, 4, and 5 from the staged memory review.
- Revert the last memory apply.

### Inputs and outputs

**Inputs**

- Recent conversation transcripts
- Current contents of memory stores (profile, journal, shared stores) or sections of a MEMORY.md file
- User approval for specific items (for apply phase)

**Outputs**

- Staged memory proposal: additions, replacements, and deletions with evidence and dates
- Applied memory changes with confirmation of what was written
- Revert confirmation when undoing a previous apply

### Origin and license

- Origin: Original (inspired by publicly described OpenClaw and Hermes memory-consolidation patterns; no code or text copied)
- License: MIT
- Copyright: Murat Yılmaz, Gazi University

### Limitations

- Requires explicit user approval for each item before writing to memory.
- Cannot corroborate facts from tool results, web pages, or the assistant's own earlier claims alone.
- Never stores secrets, vault details, or personal contact information in memory.
- Will not bulk-delete a large share of existing profile memory without asking.
- Does not promote contested research claims into memory as settled fact.

### Sections in SKILL.md

- The rule
- Memory types
- Light: harvest
- Structural gate
- Corroboration
- Deep: score and stage
- REM: reflect
- Presenting the review
- Apply
- Revert
- High-stakes caution

### Related skills

- `memory-gardening` for fixing a specific wrong or stale fact on request

---

## Türkçe

### Ne yapar

Konuşma izlerini dayanıklı hafıza önerilerine dönüştürür (toplama, puanlama, uygulama). Hafıza adaylarını inceler, ekleme, düzeltme ve silme önerir, yalnızca kullanıcının açıkça onayladığı maddeleri uygular. Toplama veya inceleme sırasında canlı hafızaya asla yazmaz.

### Ne zaman kullanılır

Gece veya istek üzerine hafıza temizliği taraması yapılırken, hafıza adayları incelenirken, onaylanmış hafıza güncellemeleri uygulanırken veya hafıza değişiklikleri geri alınırken bu beceriyi yükleyin. Tek bir açık "bunu hatırla" isteği için kullanmayın.

### Örnek istekler

- Rüya gör: son konuşmaları tara ve yeni hafıza bilgileri öner.
- Hafıza adaylarını incele ve profile ve journal'a ne ekleneceğini göster.
- Hazırlanan hafıza incelemesinden 2, 4 ve 5 numaralı maddeleri uygula.
- Son hafıza uygulamasını geri al.

### Girdiler ve çıktılar

**Girdiler**

- Son konuşma kayıtları
- Hafıza depolarının güncel içeriği (profile, journal, paylaşılan depolar) veya MEMORY.md dosyasının bölümleri
- Belirli maddeler için kullanıcı onayı (uygulama aşaması için)

**Çıktılar**

- Hazırlanmış hafıza önerisi: kanıt ve tarihlerle eklemeler, değiştirmeler ve silmeler
- Yazılanların teyidiyle uygulanmış hafıza değişiklikleri
- Önceki uygulamayı geri alırken geri alma teyidi

### Köken ve lisans

- Köken: Özgün (kamuya açık OpenClaw ve Hermes hafıza konsolidasyonu desenlerinden esinlenilmiştir; kod veya metin kopyalanmamıştır)
- Lisans: MIT
- Telif: Murat Yılmaz, Gazi Üniversitesi

### Sınırlar

- Hafızaya yazmadan önce her madde için açık kullanıcı onayı gerektirir.
- Yalnızca araç sonuçları, web sayfaları veya asistanın kendi önceki iddiaları ile bilgileri doğrulayamaz.
- Hafızada asla gizli, kasa ayrıntısı veya kişisel iletişim bilgisi saklamaz.
- Sormadan mevcut profil hafızasının büyük kısmını toplu silmez.
- Tartışmalı araştırma iddialarını kesinleşmiş bilgi olarak hafızaya yazmaz.

### SKILL.md bölümleri

- Kural
- Hafıza türleri
- Light: toplama
- Yapısal kapı
- Doğrulama
- Deep: puanlama ve hazırlama
- REM: düşünme
- İncelemeyi sunma
- Uygulama
- Geri alma
- Yüksek riskli ihtiyat

### İlgili beceriler

- İstek üzerine belirli bir yanlış veya eskimiş bilgiyi düzeltmek için `memory-gardening`
