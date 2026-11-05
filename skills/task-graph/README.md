# task-graph

## English
**What it does.** Splits a large job (paper revision, grant proposal, book chapter, literature review) into small nodes with one input, one output and one check each. Every output passes an evidence gate (deterministic checks first, the agent's report second, model confidence last). Failed items go back for at most three fixes, then to the user. `graph.md`, `checks.md` and `progress.md` let another session resume the work.

**When to use.** Multi-step work that spans sessions or several agents, where you need to show what was checked.

**Example prompts.** "Run this revision as a task graph." "Resume the proposal from progress.md."

**Origin and license.** Our own text, MIT. The structure is adapted from a public graph prompt by @hanakoxbt, inspired by Karpathy's autoresearch (https://github.com/karpathy/autoresearch). Not written or endorsed by Karpathy.

**Limits.** Gates are only as good as the checks you define. Overkill for short tasks.

## Türkçe
**Ne yapar.** Büyük bir işi (makale revizyonu, proje önerisi, kitap bölümü, literatür taraması) her biri tek girdi, tek çıktı ve tek kontrolden oluşan küçük düğümlere böler. Her çıktı bir kanıt kapısından geçer: önce kesin kontroller, sonra ajanın raporu, en son modelin güveni. Kontrolden geçemeyen iş en fazla üç kez düzeltmeye döner, sonra kullanıcıya sorulur. `graph.md`, `checks.md` ve `progress.md` dosyaları işin başka bir oturumda kaldığı yerden sürmesini sağlar.

**Ne zaman kullanılır.** Birkaç oturuma ya da birkaç ajana yayılan, neyin kontrol edildiğinin gösterilmesi gereken işlerde.

**Örnek istekler.** "Bu revizyonu task graph olarak yürüt." "Öneriye progress.md'den devam et."

**Kaynak ve lisans.** Metin bizim, MIT. Yapı @hanakoxbt'nin Karpathy'nin autoresearch çalışmasından esinlenen açık prompt'undan uyarlandı; Karpathy tarafından yazılmadı ya da onaylanmadı.

**Sınırlar.** Kapılar tanımlanan kontroller kadar iyidir. Kısa işler için fazla ağırdır.
