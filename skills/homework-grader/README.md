# homework-grader

[Homework grader (local-only)](./SKILL.md)

## English

### What it does

Grades student assignments against a rubric, writes feedback, calibrates scores, optionally exports to Excel. Student data stays on local storage.

### When to use

Load this skill when the task matches: grading student assignments against a rubric, writing feedback, calibrating scores against the instructor's own, or exporting grades to Excel; student data stays on local storage.

### Example prompts

- Grade these Python labs against this rubric and write short feedback. Keep files local.
- Calibrate my draft scores against these three gold-standard solutions.

### Inputs and outputs

**Inputs**

- User task and relevant documents
- Constraints stated by the user

**Outputs**

- Scores and feedback
- Optional Excel export; local files only

### Origin and license

- Origin: Adapted from ChantillyAn/homework-grader (https://github.com/ChantillyAn/homework-grader)
- License: MIT
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md) and any `LICENSE*` files inside this folder.

### Limitations

- Student data stays on local storage. Calibrate against instructor gold scores.
- Adapted from upstream open-source material; see THIRD_PARTY.md. Upstream snapshots may lag newer releases.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- (flat instruction file; open SKILL.md)

### Related skills

- None named in SKILL.md

---

## Türkçe

### Ne yapar

Öğrenci ödevlerini rubriğe göre notlar, geri bildirim yazar, puanları eğitmen notuna göre kalibre eder; öğrenci verisi yerel kalır.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: Öğrenci ödevlerini rubriğe göre notlar, geri bildirim yazar, puanları eğitmen notuna göre kalibre eder; öğrenci verisi yerel kalır.

### Örnek istemler

- Bu Python laboratuvarlarını rubriğe göre notla ve kısa geri bildirim yaz. Dosyalar yerel kalsın.
- Taslak puanlarımı bu üç altın çözümle kalibre et.

### Girdiler ve çıktılar

**Girdiler**

- User task and relevant documents
- Constraints stated by the user

**Çıktılar**

- Scores and feedback
- Optional Excel export; local files only

### Köken ve lisans

- Köken: Şu kaynaktan uyarlandı: ChantillyAn/homework-grader (https://github.com/ChantillyAn/homework-grader)
- Lisans: MIT
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE*` dosyaları.

### Sınırlar

- Öğrenci verisi yerel depoda kalır. Puanları eğitmen altın skorlarıyla kalibre edin.
- Üst akış açık kaynak malzemesinden uyarlanmıştır; bkz. THIRD_PARTY.md. Anlık kopyalar yeni sürümlerin gerisinde kalabilir.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- (düz talimat dosyası; SKILL.md dosyasını açın)

### İlgili beceriler

- SKILL.md içinde adlandırılmış ilgili beceri yok
