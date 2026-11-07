# prepare-artifacts

[Prepare research artifacts for evaluation and badging](./SKILL.md)

## English

### What it does

Turns a research codebase or dataset into a submittable reproducibility package: README and appendix drafts, a claim-to-command matrix, anonymization guidance for double-blind review, archival deposit guidance (Zenodo version DOI versus concept DOI, Software Heritage SWHID), and a file-level readiness checklist. It inspects the bundle. It does not run the author's experiments, decide whether results reproduce, or award or promise a badge.

### When to use

Load this skill when preparing a reproducibility artifact for artifact evaluation or badging (ACM Artifacts Available, Evaluated, Functional or Reusable; Results Reproduced or Replicated; ICSE, FSE, MSR, ISSTA, USENIX and similar tracks), writing an artifact appendix, choosing a Zenodo DOI or Software Heritage identifier, anonymizing a repository, or packaging code for submission.

### Example prompts

- Our ICSE paper was accepted. Package this repository for artifact evaluation and say which badges the current call offers.
- Draft an anonymized review-phase ZIP checklist and a final Zenodo version-DOI plan for this artifact.
- Build a claim-to-command matrix for the three main results in this paper.

### Inputs and outputs

**Inputs**

- Path to the artifact directory
- Target venue, year and track
- Whether the package is for double-blind review or the final deposit
- The paper's major claims

**Outputs**

- Artifact-readiness checklist (PASS / PASS-WITH-WARNINGS / FAIL)
- Packaging plan (badges, hosting, gaps, appendix, deadline, anonymization)
- Draft README, appendix and claim-to-command matrix for the author to edit

### Origin and license

- Origin: Adapted
- License: Apache-2.0
- Upstream: [ShaishavMaisuria/research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) (`skills/prepare-artifacts/`), Copyright 2026 Shaishav Maisuria
- Details: see [`THIRD_PARTY.md`](../../THIRD_PARTY.md), `LICENSE` and `NOTICE` in this folder.

### Limitations

- Advisory only. Never submit to an artifact track or deposit to an archive unless the author explicitly asks for that exact action.
- File-level checks cannot prove that a build runs or that results reproduce.
- A PASS does not mean a badge will be awarded.
- Re-verify the venue's current Call for Artifacts; badge offerings change by year.
- Do not fabricate DOIs, expected numerical results, hardware limits or deadlines.

### Related skills

- `empirical-se-standards` for study design and the paper's open-science statement
- `kvkk` and `gdpr-compliance` if the artifact includes personal data

---

## Türkçe

### Ne yapar

Araştırma kodunu veya veri setini teslim edilebilir bir yeniden üretilebilirlik paketine çevirir: README ve ek taslakları, iddia-komut matrisi, çift kör inceleme için anonimleştirme, arşiv yatırma rehberi (Zenodo sürüm DOI'si ile kavram DOI'si, Software Heritage SWHID) ve dosya düzeyinde hazırlık listesi. Paketi inceler. Yazarın deneylerini çalıştırmaz, sonuçların yeniden üretildiğine karar vermez ve rozet vadetmez.

### Ne zaman kullanılır

Artifact evaluation veya rozet için bir yeniden üretilebilirlik paketi hazırlanırken (ACM Artifacts Available, Evaluated, Functional veya Reusable; Results Reproduced veya Replicated; ICSE, FSE, MSR, ISSTA, USENIX ve benzeri izlekler), artifact appendix yazılırken, Zenodo DOI veya Software Heritage kimliği seçilirken, bir depo anonimleştirilirken veya kod teslim için paketlenirken bu beceriyi yükleyin.

### Örnek istemler

- ICSE makalemiz kabul edildi. Bu depoyu artifact evaluation için paketle ve bu yılki çağrının hangi rozetleri sunduğunu söyle.
- Bu artifact için çift kör inceleme ZIP listesi ve nihai Zenodo sürüm DOI planı yaz.
- Makaledeki üç ana sonuç için iddia-komut matrisi çıkar.

### Girdiler ve çıktılar

**Girdiler**

- Artifact dizininin yolu
- Hedef yayın yeri, yıl ve izlek
- Paketin çift kör inceleme için mi yoksa nihai yatırma için mi olduğu
- Makalenin ana iddiaları

**Çıktılar**

- Hazırlık listesi (PASS / PASS-WITH-WARNINGS / FAIL)
- Paketleme planı (rozetler, barındırma, eksikler, ek, son tarih, anonimleştirme)
- Yazarın düzenleyeceği README, ek ve iddia-komut matrisi taslakları

### Köken ve lisans

- Köken: Uyarlama
- Lisans: Apache-2.0
- Üst akış: [ShaishavMaisuria/research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) (`skills/prepare-artifacts/`), Copyright 2026 Shaishav Maisuria
- Ayrıntı: [`THIRD_PARTY.md`](../../THIRD_PARTY.md) ve bu klasördeki `LICENSE` ile `NOTICE`.

### Sınırlar

- Yalnızca rehberlik. Yazar açıkça o işlemi istemedikçe artifact izleğine teslim etmeyin ve arşive yatırmayın.
- Dosya düzeyi denetim, derlemenin çalıştığını veya sonuçların yeniden üretildiğini kanıtlamaz.
- PASS, rozetin verileceği anlamına gelmez.
- Yayın yerinin güncel artifact çağrısını yeniden doğrulayın; rozetler yıldan yıla değişir.
- DOI, beklenen sayısal sonuç, donanım sınırı veya son tarih uydurmayın.

### İlgili beceriler

- Çalışma tasarımı ve açık bilim ifadesi için `empirical-se-standards`
- Pakette kişisel veri varsa `kvkk` ve `gdpr-compliance`
