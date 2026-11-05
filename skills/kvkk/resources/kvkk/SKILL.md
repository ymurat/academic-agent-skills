<!-- Use when: a task involves personal data processed in Turkey or about people in Turkey (KVKK, 6698 sayılı Kanun, aydınlatma metni, açık rıza, VERBİS, yurt dışına aktarım, veri ihlali bildirimi, öğrenci verisi, anket, araştırma verisi); load the gdpr-compliance skill first and use this as the Turkey layer. -->

# KVKK katmanı (Türkiye)

Bu beceri `gdpr-compliance` becerisinin üstünde çalışır. Önce GDPR becerisini yükle (`../gdpr-compliance/skills/gdpr-compliance/SKILL.md`), sonra Türkiye'ye özgü kuralları buradan uygula. İkisi çelişirse Türkiye'deki işleme için KVKK metni esastır.

## Çalışma kuralları
- Her madde, süre ve tutarı kullanıcıya söylemeden önce resmi kaynağı o an aç ve kontrol tarihini yaz. Aşağıdaki bilgiler 31 Ekim 2026'da kontrol edildi.
- "confirm" işaretli satırları doğrulamadan kesin bilgi gibi sunma.
- Hukuki görüş verme. Sonucu "metne göre" diye çerçevele, bağlayıcı karar için kurumun KVKK birimine veya hukuk müşavirliğine yönlendir.
- Öğrenci, katılımcı veya personel verisini kutudan (box) dışarı çıkarma.
- Yazım kuralları: Türkçe, TDK yazımı, uzun tire yok, moda sözcük yok, cevapla başla.

## Temel kaynaklar (kontrol: 2026-10-31)
| Kaynak | URL |
|---|---|
| 6698 sayılı KVKK, konsolide metin (RG 7/4/2016, sayı 29677; 7499 değişiklikleri işlenmiş) | https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf |
| Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik (RG 10/7/2024, sayı 32598) | https://www.resmigazete.gov.tr/eskiler/2024/07/20240710-2.htm |
| Standart sözleşme bildirim modülü duyurusu (Kurul kararı 17/10/2024, 2024/1793) | https://www.kvkk.gov.tr/Icerik/8043/Standart-Sozlesme-Bildirim-Modulu-Hakkinda-Kamuoyu-Duyurusu |
| Veri ihlali bildirimi, Kurul kararı 24/1/2019, 2019/10 | https://www.kvkk.gov.tr/Icerik/5362/Veri-Ihlali-Bildirimi |
| İhlal bildirim sistemi | https://ihlalbildirim.kvkk.gov.tr/ |
| VERBİS istisnası, 2023/1154 | https://www.kvkk.gov.tr/Icerik/7647/2023-1154 |
| VERBİS istisnası, 2025/1572 duyurusu | https://www.kvkk.gov.tr/Icerik/8388/KAMUOYU-DUYURUSU |
| VERBİS istisnası uygulama esası, 2025/2393 | https://www.kvkk.gov.tr/Icerik/8577/kisisel-verileri-koruma-kurulunun-04-09-2025-tarihli-ve-2025-1572-sayili-kararinin-uygulama-esaslarina-iliskin-kamuoyu-duyurusu |
| Aydınlatma Tebliği (RG 10/3/2018, sayı 30356) | https://www.kvkk.gov.tr/Icerik/4132/aydinlatma-yukumlulugunun-yerine-getirilmesinde-uyulacak-usul-ve-esaslar-hakkinda-teblig |
| Silme, Yok Etme veya Anonim Hâle Getirme Yönetmeliği (RG 28/10/2017, sayı 30224) | https://www.resmigazete.gov.tr/eskiler/2017/10/20171028-10.htm |

## Kanunun ana maddeleri
- **Md. 3:** Açık rıza "belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan rıza"dır.
- **Md. 4:** Hukuka ve dürüstlük kurallarına uygunluk, doğruluk, belirli ve meşru amaç, amaçla sınırlılık ve ölçülülük, gerekli süre kadar saklama.
- **Md. 5:** Kural açık rızadır. Rıza aranmayan şartlar: kanunda açıkça öngörülme, hayati menfaat, sözleşme, hukuki yükümlülük, alenileştirme, hakkın tesisi ve korunması, meşru menfaat.
- **Md. 6 (7499 ile değişik, yürürlük 1/6/2024):** Özel nitelikli veriler ırk, etnik köken, siyasi düşünce, felsefi inanç, din, mezhep veya diğer inançlar, kılık ve kıyafet, dernek, vakıf ya da sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti ve güvenlik tedbirleri, biyometrik ve genetik verilerdir. İşleme yasaktır. İstisnalar (fıkra 3): (a) açık rıza, (b) kanunda açıkça öngörülme, (c) fiili imkânsızlıkta hayati menfaat, (ç) alenileştirme iradesine uygunluk, (d) hakkın tesisi, (e) sır saklama yükümlülüğü altındakilerce sağlık hizmetleri, (f) istihdam, iş sağlığı, sosyal güvenlik gibi alanlarda hukuki yükümlülük, (g) vakıf, dernek ve benzerlerinin üyelerine yönelik işleme. Eski "sağlık ve cinsel hayat dışındakiler kanunda öngörülürse" ayrımı kaldırıldı. Kurulun belirlediği yeterli önlemler ayrıca şarttır (fıkra 4).
- **Md. 7:** Şartlar ortadan kalkınca silme, yok etme veya anonim hâle getirme.
- **Md. 8:** Yurt içi aktarım. Kural açık rıza, ayrıca Md. 5(2) ve yeterli önlemle Md. 6(3) şartları.
- **Md. 9 (7499 ile değişik):** Yurt dışına aktarım üç kademelidir.
  1. **Yeterlilik kararı:** Md. 5 veya 6 şartı ile birlikte. Kurul verir, Resmî Gazete'de yayımlanır, en geç dört yılda bir değerlendirilir.
  2. **Uygun güvenceler** (yeterlilik yoksa; ilgili kişinin karşı ülkede hak arama imkânı olmalı): (a) kamu kurumları arası anlaşma ve Kurul izni, (b) Kurulca onaylı bağlayıcı şirket kuralları, (c) Kurulun ilan ettiği standart sözleşme, (ç) yazılı taahhütname ve Kurul izni.
  3. **Arızi aktarım** (ilk ikisi yoksa, yalnızca arızi olmak kaydıyla): riskler bildirilerek açık rıza, sözleşmenin ifası, ilgili kişi yararına sözleşme, üstün kamu yararı, hakkın tesisi, hayati menfaat, kamuya açık sicil. (a), (b), (c) bentleri kamu kurumlarının kamu hukukuna tâbi faaliyetlerine uygulanmaz (fıkra 7). Bu, devlet üniversitesi için önemlidir.
  - **Standart sözleşme:** imzaların tamamlanmasından itibaren 5 iş günü içinde Kuruma bildirilir (Kanun Md. 9/5; Yönetmelik Md. 14/5). Metin değiştirilmeden kullanılır. Kimin bildireceği yazılmamışsa veri aktaran bildirir. Bildirim fiziki, KEP veya Kurulun belirlediği yöntemle yapılır; 2024/1793 kararıyla çevrim içi modül açıldı. Bildirmemenin cezası Md. 18(1)(d).
  - Geçiş: eski Md. 9(1) 1/9/2024'e kadar yeni hâliyle birlikte uygulandı (Geçici Md. 3).
- **Md. 10:** Aydınlatma yükümlülüğü (aşağıda).
- **Md. 11:** İlgili kişinin hakları: işlenip işlenmediğini öğrenme, bilgi talep etme, amacı ve amaca uygun kullanımı öğrenme, yurt içi ve yurt dışında aktarılan üçüncü kişileri bilme, düzeltme, Md. 7'ye göre silme veya yok etme, bunların üçüncü kişilere bildirilmesi, münhasıran otomatik analizle aleyhe sonuca itiraz, zararın giderilmesi.
- **Md. 12:** Teknik ve idari tedbirler; veri işleyenle müşterek sorumluluk; ihlalde "en kısa sürede" ilgiliye ve Kurula bildirim.
- **Md. 13:** Başvuru yazılı veya Kurulun belirlediği yöntemle yapılır. Veri sorumlusu en geç **30 gün** içinde, kural olarak ücretsiz sonuçlandırır.
- **Md. 14:** Ret veya cevapsızlıkta, cevabı öğrenmeden itibaren 30 gün, her hâlde başvurudan itibaren 60 gün içinde Kurula şikâyet. Önce veri sorumlusuna başvuru şarttır.
- **Md. 16:** VERBİS kaydı (aşağıda).
- **Md. 18:** İdari para cezaları. Kanun metnindeki tutarlar her yıl yeniden değerleme oranıyla güncellenir. Güncel tutarı kullanıcıya söylemeden önce o yılın tutarını kvkk.gov.tr'den doğrula (confirm). Kamu kurumlarında ceza yerine personele disiplin işlemi uygulanır (Md. 18/4).
- **Md. 28:** İstisnalar (araştırma kısmında).

## Veri ihlali bildirimi (Kurul kararı 2019/10)
- "En kısa sürede" ifadesi **72 saat** olarak yorumlanır. Süre veri sorumlusunun ihlali öğrendiği andan başlar.
- Etkilenen kişiler belirlendikten sonra makul en kısa sürede onlara da bildirilir. Adrese ulaşılamıyorsa web sitesinde ilan gibi yöntemler kullanılır.
- 72 saat aşılırsa gecikmenin nedeni bildirime eklenir. Bilgiler aşamalı verilebilir.
- Kurulun "Kişisel Veri İhlal Bildirim Formu" kullanılır (ihlalbildirim.kvkk.gov.tr).
- Veri işleyen, ihlali gecikmeksizin veri sorumlusuna bildirir.
- İhlaller, etkileri ve tedbirler kayıt altına alınır. Bir veri ihlali müdahale planı hazırlanır ve düzenli gözden geçirilir.

## VERBİS (Md. 16 ve Kurul kararları)
- Kural: veri işlemeye başlamadan önce Sicile kayıt.
- İstisna (2018/87, 2023/1154 ve 2025/1572 ile değişik): yıllık çalışan sayısı 50'den az **ve** yıllık mali bilanço toplamı 100 milyon TL'den az olup ana faaliyeti özel nitelikli veri işleme olmayanlar; ana faaliyeti özel nitelikli veri işleme olup çalışan sayısı 10'dan az ve bilanço toplamı 10 milyon TL'den az olanlar.
- 2025/2393 (25/12/2025): bilanço esasına göre defter tutmayanlarda yalnızca çalışan sayısı ölçütü uygulanır.
- Kurul başka istisnalar da getirdi (ör. noterler, dernekler, siyasi partiler gibi). Bir kurumun bunlara girip girmediğini kvkk.gov.tr'deki güncel listeden doğrula (confirm). Devlet üniversiteleri kamu kurumu olarak kayıt yükümlüsüdür; tek bir öğretim üyesi kurum adına ayrıca kayıt yaptırmaz. Bunu kurumun KVKK birimiyle doğrula (confirm).

## Aydınlatma ve açık rıza
- Aydınlatma, açık rızaya veya başka bir şarta dayanan **her** işlemede yapılır. İlgili kişinin talebine bağlı değildir. İspat yükü veri sorumlusundadır (Tebliğ Md. 5).
- Asgari içerik (Kanun Md. 10, Tebliğ Md. 4): veri sorumlusunun kimliği, amaç, aktarım alıcıları ve amacı, toplama yöntemi ve hukuki sebep, Md. 11 hakları.
- Hukuki sebep, Md. 5 ve 6'daki şartlardan hangisine dayanıldığı açıkça yazılarak belirtilir. Genel ve muğlak ifade kullanılmaz.
- **Açık rıza ile aydınlatma ayrı ayrı yapılır** (Tebliğ Md. 5/1-f). Rıza metni aydınlatma metnine gömülmez; ayrı onay kutusu veya ayrı imza kullanılır.
- Amaç değişirse işlemeden önce yeniden aydınlatma yapılır.
- Veri ilgili kişiden elde edilmediyse: makul sürede, ilk iletişimde veya en geç ilk aktarımda aydınlatılır (Tebliğ Md. 6).
- Hizmet koşulu olarak rıza istemek ve meşru menfaat varken gereksiz rıza toplamak sorunludur. Bu konudaki Kurul rehberini güncel hâliyle doğrula (confirm).

## Saklama ve imha (Yönetmelik, RG 28/10/2017)
- İşleme şartlarının tamamı ortadan kalkınca silme, yok etme veya anonim hâle getirme gerekir (Md. 7).
- Tüm bu işlemler kayıt altına alınır ve en az 3 yıl saklanır.
- Saklama ve imha politikası olan veri sorumlusu periyodik imha yapar; aralık en fazla **6 ay**dır (Md. 11).
- Politika yükümlülüğü olmayanlar, yükümlülük doğduktan sonraki **3 ay** içinde imha eder.
- Politika yükümlülüğünün VERBİS kaydına bağlı olup olmadığını ve yönetmeliğin 2017 sonrası değişikliklerini mevzuat.gov.tr'den doğrula (confirm).

## GDPR ve KVKK farkları (yalnızca doğrulanmış satırlar)
| Konu | GDPR | KVKK |
|---|---|---|
| İşleme şartı yapısı | Altı hukuki sebep eşit düzeyde (Md. 6) | Kural açık rıza, diğer şartlar istisna olarak sayılmış (Md. 5) |
| Kamu görevi hukuki sebebi | Var (Md. 6/1-e) | Ayrı bir şart olarak yok; "kanunlarda açıkça öngörülme" veya "hukuki yükümlülük" kullanılır |
| Özel nitelikli veri listesi | Ceza verisi ayrı maddede (Md. 10) | Ceza mahkûmiyeti ve güvenlik tedbirleri ile kılık kıyafet, dernek ve vakıf üyeliği de listede (Md. 6/1) |
| Yurt dışına aktarımda sözleşme | SCC'ler | Kurulun ilan ettiği standart sözleşme, değiştirilmeden; 5 iş günü içinde Kuruma bildirim zorunlu |
| İhlal bildirimi | 72 saat, Tüzük metninde | 72 saat, Kanunda değil Kurul kararında (2019/10); "en kısa süre" yorumu |
| Kayıt yükümlülüğü | İşleme faaliyetleri kaydı iç belge (Md. 30) | Kamuya açık Sicil (VERBİS), işleme başlamadan önce kayıt |
| Başvuruya cevap süresi | 1 ay, uzatılabilir (Md. 12/3) | En geç 30 gün (Md. 13/2) |
| Veri taşınabilirliği | Var (Md. 20) | Md. 11'de sayılmamış |
| Veri koruma görevlisi (DPO) | Belirli hâllerde zorunlu (Md. 37) | Kanunda DPO yükümlülüğü yok |

GDPR tarafındaki madde numaraları GDPR becerisinin referanslarından alındı; Tüzük metniyle karşılaştırmadan dış belgeye koyma (confirm).

## Araştırma ve üniversite
- **Md. 28/1-b:** Kanun, kişisel verilerin resmi istatistik ile **anonim hâle getirilerek** araştırma, planlama ve istatistik amacıyla işlenmesine uygulanmaz. Kimliği belirlenebilir veriyle yapılan araştırma bu istisnaya girmez.
- **Md. 28/1-c:** Bilimsel amaçla işleme, millî savunma, millî güvenlik, kamu güvenliği, kamu düzeni, ekonomik güvenlik, özel hayatın gizliliği veya kişilik haklarını ihlal etmemek ya da suç oluşturmamak kaydıyla Kanun dışındadır. Bu şart dar yorumlanmalı: anket ve görüşmede katılımcıların özel hayatı söz konusu olduğundan istisnaya güvenmek yerine aydınlatma metni ve gerekiyorsa açık rıza al. Kurulun bu istisnaya ilişkin yorumunu doğrula (confirm).
- **Öğrenci verisi:** not, devam ve ödev gibi eğitim süreçleri genelde kanunda öngörülme veya hukuki yükümlülük şartına dayanır (2547 sayılı Kanun ve ilgili mevzuat). Kurumun aydınlatma metnine bak; kendi kurumunu veri sorumlusu olarak varsay (confirm).
- **Yapay zekâ ile not verme (homework-grader):** öğrenci ödevini yurt dışındaki bir API'ye göndermek Md. 9 kapsamında yurt dışına aktarımdır. Kamu kurumunda arızi aktarımın (a)-(c) bentleri kullanılamaz (Md. 9/7). Bu yüzden önce adları ve numaraları metinden çıkar, mümkünse yerel işleme yap, kurumun KVKK birimine danış.
- **Anketler:** IP, e-posta, açık uçlu yanıtlar kişiyi belirlenebilir kılabilir. Sağlık, din, siyasi görüş gibi soru varsa Md. 6 uygulanır ve kural olarak açık rıza gerekir. Anket aracı yurt dışında barındırılıyorsa Md. 9 aktarımıdır.
- **Etik kurul:** etik kurul onayı KVKK uyumunun yerine geçmez; ikisi ayrı yükümlülüktür. Protokol için `ethics-committee` becerisini kullan ve veri yönetimi bölümüne bu becerideki aydınlatma, saklama süresi ve aktarım bilgilerini ekle.
- **Saklama süresi:** araştırma verisinin ne kadar saklanacağını protokolde ve aydınlatma metninde açıkça yaz; süre bitince imha et veya anonim hâle getir.

## Aydınlatma metni şablonu (araştırma katılımcıları)
Köşeli parantezleri doldur. Açık rıza gerekiyorsa ayrı rıza formu kullan, bu metne ekleme.

---
**[Araştırma Adı] Kişisel Verilerin İşlenmesine İlişkin Aydınlatma Metni**

**Veri sorumlusu:** [Gazi Üniversitesi / ilgili birim], [adres]. Araştırma yürütücüsü: [unvan, ad soyad], [e-posta].

**İşlenen kişisel veriler:** [ör. yaş aralığı, bölüm, anket yanıtları, görüşme ses kaydı]. [Özel nitelikli veri işlenmiyorsa: "Sağlık, din veya siyasi görüş gibi özel nitelikli veriler toplanmamaktadır."]

**İşleme amacı:** Verileriniz yalnızca [araştırmanın amacı] amacıyla, bilimsel analiz ve yayın için işlenecektir. Yayınlarda kimliğiniz açıklanmayacak, sonuçlar toplu ve anonim olarak raporlanacaktır.

**Hukuki sebep ve toplama yöntemi:** Verileriniz [çevrim içi anket formu / yüz yüze görüşme / ses kaydı] yoluyla, [tamamen veya kısmen otomatik / otomatik olmayan] yöntemlerle toplanmaktadır. Hukuki sebep: 6698 sayılı Kanunun [5. maddesinin 1. fıkrası uyarınca açık rızanız / 5. maddesinin 2. fıkrasının (...) bendi]. [Açık rızaya dayanılıyorsa: "Açık rızanız ayrı bir formla alınmaktadır."]

**Aktarım:** Verileriniz [yalnızca araştırma ekibiyle paylaşılacaktır / şu alıcılarla, şu amaçla paylaşılacaktır: ...]. [Yurt dışındaki bir hizmet kullanılıyorsa: hizmetin adı, ülkesi ve 6698 sayılı Kanunun 9. maddesindeki dayanak.]

**Saklama süresi:** Veriler [süre] boyunca [güvenli ortam] üzerinde saklanacak, süre sonunda silinecek veya anonim hâle getirilecektir.

**Haklarınız:** 6698 sayılı Kanunun 11. maddesi uyarınca verilerinizin işlenip işlenmediğini öğrenme, bilgi talep etme, işleme amacını öğrenme, aktarıldığı üçüncü kişileri bilme, düzeltilmesini ve silinmesini isteme, bu işlemlerin aktarılan kişilere bildirilmesini isteme, otomatik analizle aleyhinize çıkan sonuca itiraz etme ve zararınızın giderilmesini talep etme haklarına sahipsiniz. Başvurularınızı [başvuru yolu, ör. KEP adresi veya ıslak imzalı dilekçe] ile iletebilirsiniz. Başvurunuz en geç 30 gün içinde sonuçlandırılır.

Katılım gönüllüdür. Araştırmadan istediğiniz zaman, gerekçe göstermeden çekilebilirsiniz.
---

Şablonu kullanmadan önce kurumun kendi aydınlatma metni ve başvuru yolu ile uyumunu kontrol et (confirm).
