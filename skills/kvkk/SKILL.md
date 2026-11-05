---
name: kvkk
description: >-
  Use when a task involves personal data processed in Turkey or about people in
  Turkey (KVKK, 6698 sayılı Kanun, aydınlatma metni, açık rıza, VERBİS, yurt
  dışına aktarım, veri ihlali bildirimi, öğrenci verisi, anket, araştırma
  verisi); load gdpr-compliance first and use this as the Turkey layer.
---
# KVKK (Turkey layer)

Full draft: `resources/kvkk/SKILL.md` (written and checked against mevzuat.gov.tr, resmigazete.gov.tr and kvkk.gov.tr on 2026-10-31).

1. Load gdpr-compliance first when EU rules may also apply, then read this file in full.
2. Verified anchors: Law 6698 (consolidated text on mevzuat.gov.tr); Law 7499 changes to Art. 6 and Art. 9, in force 1 June 2024; cross-border transfer regulation, RG 10/7/2024 no. 32598; standard contracts notified to the Authority within 5 business days; breach notification within 72 hours (Board decision 2019/10); 30-day reply to data subject requests (Art. 13); public bodies cannot use incidental transfer grounds (Art. 9/7).
3. Items marked "confirm" in the file are unverified: current Art. 18 fine amounts (revalued yearly), VERBİS exemption details for universities, later amendments to the destruction regulation, the Board's reading of the Art. 28/1-c research exemption, the legal basis for student data, and GDPR article numbers in the comparison table. Check the official source before stating them, and give the date checked.
4. For research, link to ethics-committee; aydınlatma and açık rıza are separate texts. Use the Turkish aydınlatma template in the file, adapted to the institution's own channels.
5. Never send personal data to outside services without a lawful transfer basis; keep it on local storage.
6. Guidance, not legal advice. Turkish follows TDK spelling; no em dashes, no buzzwords.

## Research data anonymisation (anonimleştirme)


1. **Pick the right term.** Under KVKK, anonymised data can no longer be linked to an identified or identifiable person, even when matched with other data, and is then outside the law's scope. Pseudonymised data (codes, a key kept apart) is still personal data. Say which one the dataset is. Open the primary texts live and cite them with URL and date: KVKK Law No. 6698 and the KVKK Kurumu regulation and guide on deletion, destruction and anonymisation (Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi). Do not quote article numbers from memory.
2. **Inventory.** List direct identifiers (name, TC kimlik no, e-mail, phone, student number, face and voice) and quasi-identifiers (age, gender, department, city, job title, dates, rare skills). For SE data also include commit author names and e-mails, usernames, issue texts, code comments and IP addresses in logs.
3. **Techniques.**
   - Remove direct identifiers.
   - Generalise quasi-identifiers (age bands, region instead of city).
   - Suppress rare values.
   - Add noise or aggregate.
   - Hash with a secret salt only for pseudonymisation; hashing alone does not anonymise.
   - Qualitative data: redact transcripts and replace places, institutions and people with role labels, then check the indirect clues in the story.
   - Small groups (one department, one course section) carry high re-identification risk. Report aggregates only, with a minimum cell size agreed with the ethics committee.
4. **Measure risk.** Check k-anonymity on the quasi-identifiers (state k), and l-diversity for sensitive attributes. Run a linkage test against public sources (LinkedIn, GitHub, university pages). Write down the residual risk.
5. **Keep the key separate.** If you pseudonymise, store the key apart from the data, encrypted, with limited access and a deletion date, and state this in the DMP (`research-grants`).
6. **Consent and sharing.** The consent form must say whether anonymised data will be shared openly (Zenodo, OSF). If the data cannot be anonymised fully, share under controlled access. Link to `ethics-committee` and `gdpr-compliance` for EU partners.
7. **Output.** An anonymisation log (field, identifier type, technique, parameter, who, date) and a short data statement for the paper.

Rule: never call a dataset "anonim" without the risk check in step 4.
