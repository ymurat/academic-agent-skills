# academic-agent-skills

[Türkçe sürüm: README.tr.md](README.tr.md)

Agent skills for academic work in software engineering, AI governance, research ethics and Turkish academia. Each skill is a folder with a `SKILL.md` file that tells a coding or research agent when to use the skill and which steps to follow. Every skill folder also has a bilingual `README.md` (English and Türkçe).

Maintainer: Prof. Murat Yılmaz, Gazi University ([@ymurat](https://github.com/ymurat); [ORCID](https://orcid.org/0000-0002-2446-3224)).

## Purpose

Give researchers, supervisors, lecturers and graduate students reusable, checkable instructions so an AI agent can help with literature work, study design, statistics, writing, peer review, grant proposals, teaching, AI governance and data protection without inventing sources or legal conclusions.

## Audience

- Software engineering and computer science researchers
- Thesis supervisors and graduate students
- Lecturers who design courses, labs and rubrics
- Anyone working with ÜAK doçentlik, TÜBİTAK ARDEB, TR Dizin, DergiPark, YÖK Tez or KVKK questions

## Install

Each `skills/<name>/` folder follows the SKILL.md format: YAML frontmatter with `name` and `description`, then instructions. Paths inside a `SKILL.md` are relative to that skill's folder. Some folders also have `resources/`, `references/` or `scripts/`.

### Claude Code

Copy the folders you want into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project):

```bash
git clone https://github.com/ymurat/academic-agent-skills.git
cp -R academic-agent-skills/skills/empirical-se-standards ~/.claude/skills/
```

### Cursor

Copy skill folders into the skills directory your Cursor setup documents, or point the agent at a specific `SKILL.md`. Project-local copies under a skills path that Cursor already loads also work.

### Codex and other SKILL.md agents

Copy the folders into the skills directory your tool documents, or paste `SKILL.md` into the system prompt or project instructions when the tool has no skill loader.

### Pairs that call each other

Install both sides of a pair when you use one of them: `panel-factory` with `council-protocol`; `gdpr-compliance` with `kvkk`; `thesis-supervisor` with `thesis-jury-prep` and `talk-prep-2` when preparing a defense.

## Quick start

1. Clone this repository.
2. Copy one skill folder into your agent's skills directory.
3. Ask a task that matches the skill description (see example prompts in each skill's `README.md`).
4. Read the Limitations section in that README and in `SKILL.md` before trusting the output.

Example:

```text
Use empirical-se-standards. Self-check this case study manuscript against the
ACM SIGSOFT Empirical Standards. Weaknesses first. Cite with access dates.
```

## Skill catalog

Origin `Original` means written for this repository under MIT. `Original*` means original skill text that credits or bundles other MIT/CC0 material (see `THIRD_PARTY.md`). `Adapted` means derived from an upstream open-source skill; upstream license applies and is listed in `THIRD_PARTY.md`.

### Research methods

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`experimental-design`](skills/experimental-design/) | Choose study design before data collection (factorial, blocking, DOE). | Adapted | MIT |
| [`statistical-power`](skills/statistical-power/) | Sample size, power, MDE and power curves. | Adapted | MIT |
| [`se-stats`](skills/se-stats/) | Statistics for SE experiments and randomized algorithm benchmarks. | Adapted | MIT |
| [`qualitative-methods`](skills/qualitative-methods/) | Qualitative and survey design: coding, interviews, scales. | Adapted | MIT |
| [`empirical-se-standards`](skills/empirical-se-standards/) | Design or review empirical SE studies against ACM SIGSOFT standards. | Original* | MIT |
| [`slr-prisma`](skills/slr-prisma/) | Systematic literature reviews with PRISMA 2020. | Adapted | MIT |
| [`concept-brief`](skills/concept-brief/) | Source-backed structured brief on a topic or concept. | Original* | MIT |
| [`bib-hygiene`](skills/bib-hygiene/) | Clean, dedupe and DOI-complete BibTeX or Zotero libraries. | Adapted | MIT |
| [`citation-check`](skills/citation-check/) | Verify citations and claims against real sources; BibTeX from DOIs. | Adapted | MIT |

### Writing and language

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`scientific-writing`](skills/scientific-writing/) | Draft or audit paper sections and submission packages. | Adapted | MIT |
| [`academic-humanizer`](skills/academic-humanizer/) | Edit AI-assisted academic prose toward the author's voice; keep numbers and citations. | Adapted | MIT |
| [`humanizer`](skills/humanizer/) | Remove AI-sounding prose patterns without changing claims. | Adapted | MIT |
| [`turkish-native`](skills/turkish-native/) | Fix Turkish that reads as translated from English. | Adapted | MIT |
| [`tr-academic-style`](skills/tr-academic-style/) | Turkish manuscript format for TR Dizin/DergiPark; APA 7 lint. | Adapted | MIT |
| [`latex-build`](skills/latex-build/) | Build, compile and check LaTeX/Overleaf papers, theses or Beamer. | Original | MIT |
| [`book-consistency`](skills/book-consistency/) | Check long manuscripts for terminology drift and repeated passages. | Original* | MIT |
| [`reviewer-response-tracker`](skills/reviewer-response-tracker/) | Track every revision comment to a change and a reply. | Original | MIT |
| [`ai-use-disclosure`](skills/ai-use-disclosure/) | Draft or check AI-use disclosure for papers, theses, grants or reviews. | Original | MIT |
| [`icarus-figures`](skills/icarus-figures/) | Reproducible matplotlib or TikZ publication figures. | Adapted | MIT |

### Review, thesis and talks

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`peer-review`](skills/peer-review/) | Structured reviewer report or critique. | Adapted | MIT |
| [`ethics-committee`](skills/ethics-committee/) | Review a protocol as an ethics committee would. | Adapted | MIT |
| [`talk-prep-2`](skills/talk-prep-2/) | Talk scripts, slides, Q&A prep and posters from a paper. | Adapted | MIT |
| [`thesis-jury-prep`](skills/thesis-jury-prep/) | Defense or proficiency prep for candidate or jury member. | Original | MIT |
| [`thesis-supervisor`](skills/thesis-supervisor/) | Master/PhD thesis planning, timeline and progress reviews. | Adapted | MIT |
| [`venue-finder`](skills/venue-finder/) | Journal/conference choice with live-checked metrics; predatory checks. | Original | MIT |
| [`research-grants`](skills/research-grants/) | Grant or research proposal structure, DMP and review. | Adapted | MIT |

### Governance, ethics and law

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`ai-governance-frameworks`](skills/ai-governance-frameworks/) | Map a system or policy to OECD, UNESCO or Council of Europe AI instruments. | Original | MIT |
| [`eu-ai-act`](skills/eu-ai-act/) | EU AI Act risk class, bans, Annex III, GPAI and transparency questions. | Adapted | MIT |
| [`gdpr-compliance`](skills/gdpr-compliance/) | GDPR audits, notices, DPAs; pair with kvkk for Turkey. | Adapted | MIT |
| [`kvkk`](skills/kvkk/) | Turkey personal-data layer (KVKK 6698); load gdpr-compliance first. | Original | MIT |
| [`iso42001`](skills/iso42001/) | ISO/IEC 42001 AI management system clauses and SoA. | Adapted | MIT |
| [`nist-ai-rmf`](skills/nist-ai-rmf/) | NIST AI RMF GOVERN/MAP/MEASURE/MANAGE and Playbook. | Adapted | MIT |
| [`ai-threat-review`](skills/ai-threat-review/) | Defensive threat model for AI/LLM/RAG/agent systems (STRIDE, OWASP LLM, ATLAS). | Adapted | Apache-2.0 |

### Turkish academia

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`docentlik-eligibility`](skills/docentlik-eligibility/) | Pre-screen publications against ÜAK doçentlik criteria (no final verdict). | Adapted | MIT |
| [`turkish-academia`](skills/turkish-academia/) | TR Dizin, DergiPark, YÖK, TÜBİTAK, doçentlik routing. | Adapted | MIT |
| [`tubitak-proposal`](skills/tubitak-proposal/) | TÜBİTAK ARDEB 1001/1002-A/3501 draft and limit checks. | Adapted | MIT |
| [`yok-tez`](skills/yok-tez/) | Search YÖK Ulusal Tez Merkezi; originality notes before a proposal. | Adapted | MIT |

### Teaching

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`teaching-skills`](skills/teaching-skills/) | Syllabi, labs, exams, rubrics and bilingual course materials. | Adapted | MIT |
| [`homework-grader`](skills/homework-grader/) | Grade against a rubric with local-only student data. | Adapted | MIT |

### Software engineering

| Skill | What it does | Origin | License |
|---|---|---|---|
| [`agile-v`](skills/agile-v/) | Traceable requirements (REQ IDs, verification), ambiguity review, tests from baseline. | Adapted | CC-BY-SA-4.0 |
| [`architecture-decision-records`](skills/architecture-decision-records/) | Record significant architecture choices as numbered ADRs. | Adapted | MIT |
| [`c4-model`](skills/c4-model/) | Design or update C4 architecture diagrams in Mermaid. | Adapted | MIT |
| [`re-for-ml`](skills/re-for-ml/) | Requirements for ML systems (EARS, data, model docs). | Adapted | MIT |
| [`spi-assessment`](skills/spi-assessment/) | Software process assessment (ISO/IEC 330xx, ASPICE, CMMI). | Original | MIT |
| [`llm-evaluation`](skills/llm-evaluation/) | Design and report LLM or agent evaluations. | Original | MIT |
| [`panel-factory`](skills/panel-factory/) | Choose deliberative panel roles; hand off to council-protocol. | Original | MIT |
| [`council-protocol`](skills/council-protocol/) | Multi-agent deliberation with synthesis and recorded dissent. | Original | MIT |
| [`task-graph`](skills/task-graph/) | Split a large research or writing job into gated, resumable steps. | Original (structure adapted from a public prompt by @hanakoxbt) | MIT |


## Limitations and disclaimer

- These skills guide an agent. They are **not legal advice**, not an ethics committee decision, and not a funder's official ruling.
- Regulations, ÜAK tables, TÜBİTAK calls, publisher AI policies and indexing lists change. Skills tell the agent to open the official source and record the date checked.
- **Do not fabricate** data, citations, DOIs, license texts, ORCID values, budget figures or article numbers. Mark unverifiable items plainly.
- Some upstream material was snapshotted and may be out of date. Check the upstream repository for newer versions.
- Python scripts under `scripts/` were reviewed for safety before inclusion but come without warranty. Read them before running.
- `skills/agile-v/` is CC-BY-SA-4.0; reuse must credit Agile V and stay under that license.
- `ai-threat-review` is defensive only: no exploit steps, payloads or attack procedures.

## How to cite

See [`CITATION.cff`](CITATION.cff). Example APA-style cite:

> Yılmaz, M. (2026). academic-agent-skills (Version 1.2.0) [Computer software]. Gazi University. https://github.com/ymurat/academic-agent-skills

No ORCID is listed here because none was verified in this repository's files.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) (English and Türkçe).

## License

Original skills: MIT (`LICENSE`). Adapted skills keep their upstream license; see `THIRD_PARTY.md` and the `LICENSE*` files inside each adapted skill folder. `skills/agile-v/` is CC-BY-SA-4.0. `skills/ai-threat-review/` includes Apache-2.0 upstream material.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md).
