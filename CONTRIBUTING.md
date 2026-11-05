# Contributing / Katkı

## English

### What to contribute

- Fixes to `SKILL.md` instructions that contradict official sources
- Clearer Limitations text grounded in what the skill already does
- Missing bilingual README sections that stay faithful to `SKILL.md`
- Upstream license or attribution corrections in `THIRD_PARTY.md`
- Small, reviewed script fixes under a skill's `scripts/` folder

### What not to contribute

- Invented citations, DOIs, ORCID values, legal conclusions or ÜAK verdicts
- Exploit steps, attack payloads or offensive security content
- Large binary dumps or unexplained sample data
- Relicensing of adapted skills or removal of upstream attribution
- ISO or other standards body copyrighted text pasted from memory

### How to propose a change

1. Open an issue describing the gap and the official source you checked (URL + date).
2. Fork, create a branch, keep one concern per pull request.
3. If you change a `SKILL.md`, update that skill's `README.md` English and Türkçe sections to match. Do not invent features the skill does not implement.
4. Run a plain-text check: no em dashes, no buzzwords (leverage, robust, cutting-edge, delve, streamlined, game-changer), no fabricated numbers.
5. For adapted skills, keep the upstream `LICENSE*` file and the `THIRD_PARTY.md` entry accurate.

### Coding and writing style

- English: active voice, lead with substance.
- Turkish: TDK spelling, natural academic Turkish; keep established English technical terms (LLM, RAG, PRISMA, ADR) when there is no settled Turkish equivalent.
- Frontmatter must keep valid `name` and `description` fields; `name` must match the folder name.

### License of contributions

Unless you state otherwise, original contributions are offered under the MIT License for this repository. If your change touches CC-BY-SA-4.0 material under `skills/agile-v/`, that material stays CC-BY-SA-4.0.

---

## Türkçe

### Neler katkı olur

- Resmî kaynaklarla çelişen `SKILL.md` talimatlarının düzeltilmesi
- Becerinin gerçekten yaptığı işe dayanan daha açık Sınırlar metni
- `SKILL.md` ile uyumlu iki dilli README tamamlamaları
- `THIRD_PARTY.md` içinde üst akış lisans veya atıf düzeltmeleri
- Bir becerinin `scripts/` altındaki küçük, gözden geçirilmiş betik düzeltmeleri

### Neler katkı olmaz

- Uydurma atıf, DOI, ORCID, hukuki sonuç veya ÜAK kararı
- İstismar adımı, saldırı yükü veya saldırgan güvenlik içeriği
- Büyük ikili yığınlar veya açıklamasız örnek veri
- Uyarlanmış becerilerin yeniden lisanslanması veya üst akış atfının silinmesi
- ISO veya başka standart kuruluşunun telifli metninin bellekten yapıştırılması

### Değişiklik nasıl önerilir

1. Boşluğu ve kontrol ettiğiniz resmî kaynağı (URL + tarih) anlatan bir issue açın.
2. Fork edin, dal oluşturun; her pull request tek bir konuyu taşısın.
3. `SKILL.md` değiştiyse o becerinin `README.md` English ve Türkçe bölümlerini buna uydurun. Becerinin uygulamadığı özelliği uydurmayın.
4. Düz metin kontrolü: tire yağmuru yok, moda sözcük yok, uydurma sayı yok.
5. Uyarlanmış becerilerde üst akış `LICENSE*` dosyası ve `THIRD_PARTY.md` kaydı doğru kalsın.

### Yazım

- İngilizce: etken çatı, önce öz.
- Türkçe: TDK yazımı, doğal akademik Türkçe; yerleşik İngilizce teknik terimler korunabilir.
- Ön yüzde geçerli `name` ve `description` alanları olmalı; `name` klasör adıyla aynı olmalı.

### Katkıların lisansı

Aksi belirtilmedikçe özgün katkılar bu deponun MIT lisansı altındadır. `skills/agile-v/` altındaki CC-BY-SA-4.0 malzemeye dokunan değişiklikler o lisansı korur.
