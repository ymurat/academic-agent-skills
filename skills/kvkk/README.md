# kvkk

[KVKK (Turkey layer)](./SKILL.md)

## English

### What it does

Handles personal-data tasks processed in Turkey or about people in Turkey (KVKK Law 6698, aydınlatma, açık rıza, VERBİS, cross-border transfer). Load gdpr-compliance first.

### When to use

Load this skill when the task matches: a task involves personal data processed in Turkey or about people in Turkey (KVKK, 6698 sayılı Kanun, aydınlatma metni, açık rıza, VERBİS, yurt dışına aktarım, veri ihlali bildirimi, öğrenci verisi, anket, araştırma verisi); load gdpr-compliance first and use this as the Turkey layer.

### Example prompts

- Write an aydınlatma metni for this student survey under KVKK. Pair with GDPR for EU partners.
- Plan anonymisation for commit-log data collected in Turkey. Keep keys separate.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Original
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Guidance only, not legal advice. Items marked confirm in the skill must be re-checked on official pages with the date recorded.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Research data anonymisation (anonimleştirme)

### Related skills

- `ethics-committee`
- `gdpr-compliance`
- `research-grants`

---

## Türkçe

### Ne yapar

Türkiye’de veya Türkiye’deki kişiler hakkında işlenen kişisel veri işleri (KVKK 6698, aydınlatma, açık rıza, VERBİS, yurt dışına aktarım). Önce gdpr-compliance yüklenir.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Türkiye’de veya Türkiye’deki kişiler hakkında işlenen kişisel veri işleri (KVKK 6698, aydınlatma, açık rıza, VERBİS, yurt dışına aktarım). Önce gdpr-compliance yüklenir.

### Örnek istemler

- Bu öğrenci anketi için KVKK aydınlatma metni yaz. AB ortakları için GDPR ile eşle.
- Türkiye’de toplanan commit günlüğü verisi için anonimleştirme planı yap. Anahtarı ayrı tut.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Özgün
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yalnızca rehberliktir; hukuki görüş değildir. Beceride "confirm" işaretli maddeler resmî sayfada tarih yazılarak yeniden kontrol edilmelidir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Research data anonymisation (anonimleştirme)

### İlgili beceriler

- `ethics-committee`
- `gdpr-compliance`
- `research-grants`
