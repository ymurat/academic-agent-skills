# turkish-academia

[Turkish academia (umbrella)](./SKILL.md)

## English

### What it does

Handles Turkish academic system tasks: TR Dizin, DergiPark, YÖK Tez, YÖK Akademik, TÜBİTAK, doçentlik, akademik teşvik, Etik Kurul routing.

### When to use

Load this skill when the task matches: turkish academic system tasks: TR Dizin, DergiPark, YÖK Tez, YÖK Akademik, TÜBİTAK ARDEB and BİDEB, doçentlik, akademik teşvik, KVKK data plans, Etik Kurul routing, TÜBİTAK open science (Aperta).

### Example prompts

- Route this study: do we need Etik Kurul, KVKK aydınlatma, and a TR Dizin target journal?
- Explain akademik teşvik point rules for this publication type. Check the current circular.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Origin and license

- Origin: Adapted from AlterLab-IEU/AlterLab-Academic-Skills (https://github.com/AlterLab-IEU/AlterLab-Academic-Skills)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Regulations and circulars change. Record the official URL and date checked.
- Automated clients for tez.yok.gov.tr, dergipark.org.tr and trdizin.gov.tr were removed (2026-11-05). Use those sites manually; see root CHANGELOG and scripts/README.md notes.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.


### Sections in SKILL.md

- (flat instruction file; open SKILL.md)

### Related skills

- None named in SKILL.md

---

## Türkçe

### Ne yapar

Türk akademik sistemi işleri: TR Dizin, DergiPark, YÖK Tez, YÖK Akademik, TÜBİTAK, doçentlik, akademik teşvik, Etik Kurul yönlendirme.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Türk akademik sistemi işleri: TR Dizin, DergiPark, YÖK Tez, YÖK Akademik, TÜBİTAK, doçentlik, akademik teşvik, Etik Kurul yönlendirme.

### Örnek istemler

- Bu çalışma için Etik Kurul, KVKK aydınlatma ve TR Dizin hedef dergi gerekir mi yönlendir.
- Bu yayın türü için akademik teşvik puanını güncel genelgeye bakarak açıkla.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Structured output defined in SKILL.md
- Limitations and unverifiable items marked plainly

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: AlterLab-IEU/AlterLab-Academic-Skills (https://github.com/AlterLab-IEU/AlterLab-Academic-Skills)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Yönetmelik ve genelgeler değişir. Resmî URL ve kontrol tarihini yazın.
- tez.yok.gov.tr, dergipark.org.tr ve trdizin.gov.tr için otomatik istemciler kaldırıldı (2026-11-05). Bu siteleri elle kullanın; kök CHANGELOG ve scripts/README.md notlarına bakın.
- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.


### SKILL.md bölümleri

- (düz talimat dosyası; SKILL.md dosyasını açın)

### İlgili beceriler

- SKILL.md içinde adlandırılmış ilgili beceri yok
