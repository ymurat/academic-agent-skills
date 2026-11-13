# promise-log

[Extract and track commitments from conversations](./SKILL.md)

## English

### What it does

Extracts binding commitments from emails, meeting notes, chats, or transcripts into a sourced log (promise-log.md). Tracks what the owner owes, what is owed to the owner, due dates, status, and evidence. Flags overdue items. Updates an existing log or creates a new one.

### When to use

Load this skill after a meeting, email thread, call, or chat where someone committed to something; when the owner asks "what did I promise", "what is overdue", or "who owes me what"; or from a routine that sweeps recent mail and meetings.

### Example prompts

- Extract commitments from this email thread into the promise log.
- What am I overdue on? Check the promise log.
- Update the promise log with the notes from today's co-author meeting.
- Who owes me what, according to the promise log?

### Inputs and outputs

**Inputs**

- Source material: email thread, meeting notes, transcript, chat
- Path to existing log (default: `promise-log.md` in working directory)

**Outputs**

- Updated promise-log.md (single markdown table sorted by due date)
- Summary of changes: new, closed, became overdue
- Overdue items listed first

### Origin and license

- Origin: Adapted
- License: MIT
- Upstream: [cobusgreyling/grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) (`skills/log-promises`), Copyright 2026 Cobus Greyling
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and `LICENSE-UPSTREAM` in this folder.

### Limitations

- Never emails, messages, or reminds a counterparty. Offers a draft instead.
- Never writes memory from this log; it is a working file, not durable memory.
- Does not add calendar events or reminders unless the owner asks.
- Does not infer or invent due dates. Dates not stated in the source are marked `unknown`.
- Closed items require evidence (a sent reply, a delivered file, the owner saying so).

### Sections in SKILL.md

- When to use
- Inputs
- Steps
- Validation
- Return
- Needs approval

### Related skills

- `dreaming` for durable memory consolidation (promise-log is a working file, not memory)
- `teaching-skills` for student supervision commitments

---

## Türkçe

### Ne yapar

Bağlayıcı sözleri (co-author deadlines, reviewer invitations, student supervision, project deliverables) e-posta, toplantı notları, sohbet veya kayıtlardan kaynaklı bir günlüğe (promise-log.md) çıkarır. Sahibin ne borçlu olduğunu, kendisine ne borçlanıldığını, son tarihleri, durumu ve kanıtı takip eder. Gecikmiş maddeleri işaretler. Mevcut günlüğü günceller veya yeni oluşturur.

### Ne zaman kullanılır

Birinin bir şey taahhüt ettiği toplantı, e-posta dizisi, arama veya sohbet sonrasında; sahip "ne söz verdim", "neyi geçiktirdim" veya "kim bana ne borçlu" diye sorduğunda; veya son e-posta ve toplantıları tarayan bir rutinden bu beceriyi yükleyin.

### Örnek istemler

- Bu e-posta dizisinden sözleri promise log'a çıkar.
- Neyi geçiktirdim? Promise log'u kontrol et.
- Promise log'u bugünkü yazar toplantısı notlarıyla güncelle.
- Promise log'a göre kim bana ne borçlu?

### Girdiler ve çıktılar

**Girdiler**

- Kaynak materyal: e-posta dizisi, toplantı notları, kayıt, sohbet
- Mevcut günlüğün yolu (varsayılan: çalışma dizininde `promise-log.md`)

**Çıktılar**

- Güncellenmiş promise-log.md (son tarihe göre sıralanmış tek markdown tablosu)
- Değişikliklerin özeti: yeni, kapandı, gecikti
- Gecikmiş maddeler önce listelenir

### Köken ve lisans

- Köken: Uyarlama
- Lisans: MIT
- Üst akış: [cobusgreyling/grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) (`skills/log-promises`), Copyright 2026 Cobus Greyling
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE-UPSTREAM`.

### Sınırlar

- Karşı tarafa asla e-posta, mesaj göndermez veya hatırlatma yapmaz. Bunun yerine taslak sunar.
- Bu günlükten asla hafıza yazmaz; çalışma dosyasıdır, dayanıklı hafıza değil.
- Sahip istemediği sürece takvim etkinliği veya hatırlatıcı eklemez.
- Son tarihleri çıkarsamaz veya uydurmaz. Kaynakta belirtilmeyen tarihler `unknown` işaretlenir.
- Kapalı maddeler kanıt gerektirir (gönderilmiş yanıt, teslim edilmiş dosya, sahibin söylemesi).

### SKILL.md bölümleri

- Ne zaman kullanılır
- Girdiler
- Adımlar
- Doğrulama
- Dönüş
- Onay gerektiren işler

### İlgili beceriler

- Dayanıklı hafıza konsolidasyonu için `dreaming` (promise-log çalışma dosyasıdır, hafıza değil)
- Öğrenci danışmanlığı sözleri için `teaching-skills`
