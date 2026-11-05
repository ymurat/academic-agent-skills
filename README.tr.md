# academic-agent-skills

[English version: README.md](README.md)

Yazılım mühendisliği, yapay zekâ yönetişimi, araştırma etiği ve Türk akademik sistemi için agent becerileri. Her beceri, bir AI agent’a ne zaman ve nasıl çalışacağını anlatan bir `SKILL.md` dosyası içeren klasördür. Her beceri klasöründe ayrıca iki dilli bir `README.md` (English ve Türkçe) vardır.

Sorumlu: Prof. Murat Yılmaz, Gazi Üniversitesi ([@ymurat](https://github.com/ymurat); [ORCID](https://orcid.org/0000-0002-2446-3224)).

## Amaç

Araştırmacıların, tez danışmanlarının, öğretim üyelerinin ve lisansüstü öğrencilerin literatür, çalışma tasarımı, istatistik, yazım, hakemlik, proje önerisi, öğretim, yapay zekâ yönetişimi ve kişisel veri konularında agent’a verebileceği yeniden kullanılabilir, denetlenebilir talimatlar sunmak. Kaynak veya hukuki sonuç uydurmamak temel kuraldır.

## Kime

- Yazılım mühendisliği ve bilgisayar bilimi araştırmacıları
- Tez danışmanları ve lisansüstü öğrenciler
- Ders, laboratuvar ve rubrik tasarlayan öğretim elemanları
- ÜAK doçentlik, TÜBİTAK ARDEB, TR Dizin, DergiPark, YÖK Tez veya KVKK soruları olan herkes

## Kurulum

Her `skills/<name>/` klasörü SKILL.md biçimindedir: `name` ve `description` içeren YAML ön yüz, ardından talimatlar. `SKILL.md` içindeki yollar o beceri klasörüne göredir. Bazı klasörlerde `resources/`, `references/` veya `scripts/` vardır.

### Claude Code

İstediğiniz klasörleri `~/.claude/skills/` (tüm projeler) veya `.claude/skills/` (tek proje) altına kopyalayın:

```bash
git clone https://github.com/ymurat/academic-agent-skills.git
cp -R academic-agent-skills/skills/empirical-se-standards ~/.claude/skills/
```

### Cursor

Skill klasörlerini Cursor kurulumunuzun belgelediği skills dizinine kopyalayın veya agent’ı belirli bir `SKILL.md` dosyasına yönlendirin.

### Codex ve diğer SKILL.md agent’ları

Klasörleri aracın belgelediği skills dizinine kopyalayın. Skill yükleyicisi yoksa `SKILL.md` içeriğini sistem istemine veya proje talimatına yapıştırın.

### Birbirini çağıran çiftler

Birini kullanıyorsanız çiftin diğerini de kurun: `panel-factory` ile `council-protocol`; `gdpr-compliance` ile `kvkk`; savunma hazırlığında `thesis-supervisor` ile `thesis-jury-prep` ve `talk-prep-2`.

## Hızlı başlangıç

1. Bu depoyu klonlayın.
2. Bir beceri klasörünü agent’ınızın skills dizinine kopyalayın.
3. Becerinin tanımına uyan bir iş isteyin (örnek istemler her becerinin `README.md` dosyasındadır).
4. Çıktıya güvenmeden önce o README ve `SKILL.md` içindeki Sınırlar bölümünü okuyun.

Örnek:

```text
empirical-se-standards kullan. Bu vaka çalışması el yazmasını ACM SIGSOFT
Empirical Standards’a göre kendi kendine denetle. Önce zayıf yönler.
Erişim tarihiyle atıf ver.
```

## Beceri kataloğu

`Özgün`, bu depo için MIT altında yazılmış demektir. `Özgün*`, başka MIT/CC0 malzemeyi kredilendiren veya paketleyen özgün metindir (`THIRD_PARTY.md`). `Uyarlama`, üst akış açık kaynak beceriden türetilmiştir; üst akış lisansı geçerlidir ve `THIRD_PARTY.md` içindedir.

### Araştırma yöntemleri

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`experimental-design`](skills/experimental-design/) | Veri öncesi tasarım seçimi (faktöriyel, bloklama, DOE). | Uyarlama | MIT |
| [`statistical-power`](skills/statistical-power/) | Örneklem, güç, MDE ve güç eğrileri. | Uyarlama | MIT |
| [`se-stats`](skills/se-stats/) | SE deneyleri ve rastgele algoritma benchmark istatistiği. | Uyarlama | MIT |
| [`qualitative-methods`](skills/qualitative-methods/) | Nitel ve anket tasarımı: kodlama, görüşme, ölçek. | Uyarlama | MIT |
| [`empirical-se-standards`](skills/empirical-se-standards/) | Ampirik SE çalışmalarını ACM SIGSOFT standartlarına göre tasarlar/inceler. | Özgün* | MIT |
| [`slr-prisma`](skills/slr-prisma/) | PRISMA 2020 ile sistematik literatür taraması. | Uyarlama | MIT |
| [`concept-brief`](skills/concept-brief/) | Konu veya kavram için kaynaklara dayalı yapılandırılmış brifing. | Özgün* | MIT |
| [`bib-hygiene`](skills/bib-hygiene/) | BibTeX/Zotero temizler, yinelenenleri ayıklar, DOI ile tamamlar. | Uyarlama | MIT |
| [`citation-check`](skills/citation-check/) | Atıf ve iddiaları gerçek kaynaklara karşı doğrular; DOI’den BibTeX. | Uyarlama | MIT |

### Yazım ve dil

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`scientific-writing`](skills/scientific-writing/) | Makale bölümü taslağı veya denetimi; gönderim paketi. | Uyarlama | MIT |
| [`academic-humanizer`](skills/academic-humanizer/) | Yapay zekâ destekli akademik metni yazar sesine yaklaştırır; sayı ve atıf korunur. | Uyarlama | MIT |
| [`humanizer`](skills/humanizer/) | İddiaları değiştirmeden yapay zekâ üslubunu temizler. | Uyarlama | MIT |
| [`turkish-native`](skills/turkish-native/) | İngilizceden çevrilmiş gibi duran Türkçeyi düzeltir. | Uyarlama | MIT |
| [`tr-academic-style`](skills/tr-academic-style/) | TR Dizin/DergiPark Türkçe biçim; APA 7 denetimi. | Uyarlama | MIT |
| [`latex-build`](skills/latex-build/) | LaTeX/Overleaf makale, tez veya Beamer kurar, derler, kontrol eder. | Özgün | MIT |
| [`book-consistency`](skills/book-consistency/) | Uzun el yazmasında terim sapması ve yinelenen pasajları kontrol eder. | Özgün* | MIT |
| [`reviewer-response-tracker`](skills/reviewer-response-tracker/) | Her revizyon yorumunu değişiklik ve yanıta bağlar. | Özgün | MIT |
| [`ai-use-disclosure`](skills/ai-use-disclosure/) | Makale, tez, hibe veya inceleme için YZ kullanım bildirimi yazar veya kontrol eder. | Özgün | MIT |
| [`icarus-figures`](skills/icarus-figures/) | Yeniden üretilebilir matplotlib veya TikZ yayın figürleri. | Uyarlama | MIT |

### İnceleme, tez ve sunum

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`peer-review`](skills/peer-review/) | Yapılandırılmış hakem raporu veya eleştiri. | Uyarlama | MIT |
| [`ethics-committee`](skills/ethics-committee/) | Protokolü etik kurul bakışıyla inceler. | Uyarlama | MIT |
| [`talk-prep-2`](skills/talk-prep-2/) | Makaleden konuşma metni, slayt, soru-cevap ve poster. | Uyarlama | MIT |
| [`thesis-jury-prep`](skills/thesis-jury-prep/) | Savunma veya yeterlik hazırlığı (aday veya jüri). | Özgün | MIT |
| [`thesis-supervisor`](skills/thesis-supervisor/) | YL/doktora tez planı, zaman çizelgesi, ilerleme. | Uyarlama | MIT |
| [`venue-finder`](skills/venue-finder/) | Dergi/konferans seçimi; canlı ölçüm; yağmacı kontrolü. | Özgün | MIT |
| [`research-grants`](skills/research-grants/) | Hibe/araştırma önerisi yapısı, DMP ve inceleme. | Uyarlama | MIT |

### Yönetişim, etik ve hukuk

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`ai-governance-frameworks`](skills/ai-governance-frameworks/) | Sistem veya politikayı OECD, UNESCO veya Avrupa Konseyi AI belgelerine eşler. | Özgün | MIT |
| [`eu-ai-act`](skills/eu-ai-act/) | AB Yapay Zekâ Tüzüğü risk sınıfı, yasaklar, Ek III, GPAI, şeffaflık. | Uyarlama | MIT |
| [`gdpr-compliance`](skills/gdpr-compliance/) | GDPR denetimi, bildirim, DPA; Türkiye için kvkk ile birlikte. | Uyarlama | MIT |
| [`kvkk`](skills/kvkk/) | Türkiye kişisel veri katmanı (KVKK 6698); önce gdpr-compliance. | Özgün | MIT |
| [`iso42001`](skills/iso42001/) | ISO/IEC 42001 YZ yönetim sistemi maddeleri ve Uygulanabilirlik Beyanı. | Uyarlama | MIT |
| [`nist-ai-rmf`](skills/nist-ai-rmf/) | NIST AI RMF GOVERN/MAP/MEASURE/MANAGE ve Playbook. | Uyarlama | MIT |
| [`ai-threat-review`](skills/ai-threat-review/) | YZ/LLM/RAG/agent için savunma tehdit modeli (STRIDE, OWASP LLM, ATLAS). | Uyarlama | Apache-2.0 |

### Türk akademik sistemi

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`docentlik-eligibility`](skills/docentlik-eligibility/) | Yayınları ÜAK doçentlik ölçütlerine göre ön elemeye sokar (nihai karar yok). | Uyarlama | MIT |
| [`turkish-academia`](skills/turkish-academia/) | TR Dizin, DergiPark, YÖK, TÜBİTAK, doçentlik yönlendirme. | Uyarlama | MIT |
| [`tubitak-proposal`](skills/tubitak-proposal/) | TÜBİTAK ARDEB 1001/1002-A/3501 taslak ve sınır kontrolü. | Uyarlama | MIT |
| [`yok-tez`](skills/yok-tez/) | YÖK Ulusal Tez Merkezi araması; öneri öncesi özgünlük notu. | Uyarlama | MIT |

### Öğretim

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`teaching-skills`](skills/teaching-skills/) | Müfredat, laboratuvar, sınav, rubrik, iki dilli materyal. | Uyarlama | MIT |
| [`homework-grader`](skills/homework-grader/) | Rubriğe göre notlama; öğrenci verisi yalnızca yerel. | Uyarlama | MIT |

### Yazılım mühendisliği

| Beceri | Ne yapar | Köken | Lisans |
|---|---|---|---|
| [`agile-v`](skills/agile-v/) | İzlenebilir gereksinimler (REQ, doğrulama), belirsizlik incelemesi, tabandan test. | Uyarlama | CC-BY-SA-4.0 |
| [`architecture-decision-records`](skills/architecture-decision-records/) | Önemli mimari seçimleri numaralı ADR olarak kaydeder. | Uyarlama | MIT |
| [`c4-model`](skills/c4-model/) | Mermaid ile C4 mimari diyagramları tasarlar veya günceller. | Uyarlama | MIT |
| [`re-for-ml`](skills/re-for-ml/) | ML sistemleri için gereksinim (EARS, veri, model belgeleri). | Uyarlama | MIT |
| [`spi-assessment`](skills/spi-assessment/) | Yazılım süreç değerlendirmesi (ISO/IEC 330xx, ASPICE, CMMI). | Özgün | MIT |
| [`llm-evaluation`](skills/llm-evaluation/) | LLM veya agent değerlendirmesi tasarlar ve raporlar. | Özgün | MIT |
| [`panel-factory`](skills/panel-factory/) | Müzakere paneli rollerini seçer; council-protocol’e verir. | Özgün | MIT |
| [`council-protocol`](skills/council-protocol/) | Çoklu agent müzakeresi; sentez ve kayda geçen muhalefet. | Özgün | MIT |


## Sınırlar ve sorumluluk reddi

- Bu beceriler agent’a rehberlik eder. **Hukuki görüş değildir**, etik kurul kararı değildir, fon verenin resmî kararı değildir.
- Yönetmelikler, ÜAK tabloları, TÜBİTAK çağrıları, yayınevi YZ politikaları ve indeks listeleri değişir. Beceriler agent’a resmî kaynağı açmasını ve kontrol tarihini yazmasını söyler.
- Veri, atıf, DOI, lisans metni, ORCID, bütçe rakamı veya madde numarası **uydurulmaz**. Doğrulanamayanlar açıkça işaretlenir.
- Üst akış anlık kopyaları güncel olmayabilir. Yeni sürüm için üst akış deposunu kontrol edin.
- `scripts/` altındaki Python betikleri güvenlik açısından gözden geçirilmiştir; garanti yoktur. Çalıştırmadan önce okuyun.
- `skills/agile-v/` CC-BY-SA-4.0’tır; yeniden kullanımda Agile V anılmalı ve aynı lisans korunmalıdır.
- `ai-threat-review` yalnızca savunma içindir: istismar adımı, yük veya saldırı yordamı yoktur.

## Nasıl atıf verilir

[`CITATION.cff`](CITATION.cff) dosyasına bakın. APA tarzı örnek:

> Yılmaz, M. (2026). academic-agent-skills (Version 1.2.0) [Computer software]. Gazi Üniversitesi. https://github.com/ymurat/academic-agent-skills

Bu depo dosyalarında doğrulanmış ORCID bulunmadığı için ORCID yazılmamıştır.

## Katkı

[`CONTRIBUTING.md`](CONTRIBUTING.md) (English ve Türkçe).

## Lisans

Özgün beceriler: MIT (`LICENSE`). Uyarlanan beceriler üst akış lisansını korur; `THIRD_PARTY.md` ve her uyarlanmış klasördeki `LICENSE*` dosyalarına bakın. `skills/agile-v/` CC-BY-SA-4.0. `skills/ai-threat-review/` Apache-2.0 üst akış malzemesi içerir.

## Değişiklik günlüğü

[`CHANGELOG.md`](CHANGELOG.md).
