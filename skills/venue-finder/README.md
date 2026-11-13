# venue-finder

[Venue finder](./SKILL.md)

## English

### What it does

Chooses or compares journals and conferences (scope, indexing, quartile, TR Dizin, APC, review time) and checks predatory or questionable venues with live-verified metrics.

### When to use

Load this skill when the task matches: the user wants to choose a journal or conference for a manuscript, compare candidate venues (scope, indexing, quartile, TR Dizin, APC, review time, acceptance), or check whether a journal or publisher is predatory or questionable.

### Example prompts

- Suggest journals for this SE empirical paper: SCI-E preferred, APC under our budget. Verify live.
- Is this invited journal predatory? Check indexing claims and Think.Check.Submit.

### Inputs and outputs

**Inputs**

- Title, abstract, keywords, or the manuscript; article type (full paper, short, review, SLR, replication, dataset).
- Constraints: target indexing (SCI-E/SSCI, Scopus, ESCI, TR Dizin), quartile, open access or APC budget, deadline or speed, ACM/IEEE/Springer preference, language (Turkish or English), purpose (e.g. doçentlik or academic incentive points). Infer what you can; state assumptions.

**Outputs**

- Top recommendations
- Comparison table with live-checked metrics

### Origin and license

- Origin: Original
- License: MIT
- Original work; no third-party material.

### Limitations

- Every metric must come from a page opened this turn. Never state quartile, APC or acceptance rate from memory.
- Agent guidance only. Verify outputs; do not fabricate data, licenses, sources or citations.

### Sections in SKILL.md

- Inputs
- Step 1: Candidate list (8-15)
- Step 2: Verify each candidate
- Step 3: Predatory or questionable check
- Step 4: Output

### Related skills

- `turkish-academia`

---

## Türkçe

### Ne yapar

El yazması için dergi veya konferans seçer; adayları kapsam, indeks, çeyreklik, TR Dizin, APC ve inceleme süresi açısından karşılaştırır; yağmacı dergi riskini kontrol eder.

### Ne zaman kullanılır

İş şu tanıma uyduğunda bu beceriyi yükleyin: El yazması için dergi veya konferans seçer; adayları kapsam, indeks, çeyreklik, TR Dizin, APC ve inceleme süresi açısından karşılaştırır; yağmacı dergi riskini kontrol eder.

### Örnek istemler

- Bu ampirik SE makalesi için SCI-E tercih eden dergi öner; APC bütçemizin altında. Canlı doğrula.
- Bu davetli dergi yağmacı mı? İndeks iddialarını ve Think.Check.Submit’i kontrol et.

### Girdiler ve çıktılar

**Girdiler**

- Title, abstract, keywords, or the manuscript; article type (full paper, short, review, SLR, replication, dataset).
- Constraints: target indexing (SCI-E/SSCI, Scopus, ESCI, TR Dizin), quartile, open access or APC budget, deadline or speed, ACM/IEEE/Springer preference, language (Turkish or English), purpose (e.g. doçentlik or academic incentive points). Infer what you can; state assumptions.

**Çıktılar**

- Top recommendations
- Comparison table with live-checked metrics

### Köken ve lisans

- Köken: Özgün
- Lisans: MIT
- Özgün çalışma; üçüncü taraf malzeme yok.

### Sınırlar

- Her ölçüm bu turda açılan sayfadan gelmelidir. Çeyreklik, APC veya kabul oranını bellekten söylemeyin.
- Yalnızca agent rehberliğidir. Çıktıları doğrulayın; veri, lisans, kaynak veya atıf uydurmayın.

### SKILL.md bölümleri

- Inputs
- Step 1: Candidate list (8-15)
- Step 2: Verify each candidate
- Step 3: Predatory or questionable check
- Step 4: Output

### İlgili beceriler

- `turkish-academia`
