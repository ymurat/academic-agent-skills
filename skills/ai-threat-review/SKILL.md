---
name: ai-threat-review
description: >-
  Use when the user wants a defensive threat model or security review of an AI,
  LLM, RAG or agent system: STRIDE, OWASP Top 10 for LLM Applications, MITRE
  ATLAS, prompt injection and tool misuse.
---
# AI threat review (defensive)

Threat modeling and design review for systems that contain ML models, LLMs, retrieval or autonomous agents. Defensive only: produce threats, controls and test ideas, never working exploits or attack payloads against systems the user does not own.

## Sources in `resources/`
- Upstream (Apache-2.0, credit: Inerthel, https://github.com/inerthel-agi/security-hardening): `resources/ai-threat-review/upstream/references/ai/` (llm-agent-security, mcp-security, rag-retrieval-security, prompt-and-tool-evidence-handling, agent-approval-patterns, multi-agent-boundaries-and-delegation, ai-agent-incident-response, agent-evals-red-teaming) and `.../threat-modeling.md`. License and NOTICE in `.../upstream/`.
- OWASP LLM Top 10 (2025) list and ATLAS link: `resources/ai-threat-review/owasp-llm-2025.md`. Re-check the OWASP page for a newer edition before citing.

## Workflow
1. **Scope.** System purpose, users, assets (data, model weights, prompts, credentials, tools), trust boundaries, deployment. Draw a data flow diagram (Mermaid or `c4-model` container view) marking every boundary: user to app, app to model API, model to tools, retrieval store, external content.
2. **STRIDE per element.** For each process, store, flow and boundary: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. Add AI-specific lenses:
   - untrusted content reaching the model (direct and indirect prompt injection via web pages, emails, files, retrieved chunks);
   - excessive agency (tools with write, send, pay or delete rights; no human approval);
   - data and model poisoning, supply chain (models, datasets, plugins, MCP servers);
   - sensitive data and system prompt leakage; improper output handling (model output into SQL, shell, HTML);
   - unbounded consumption (cost, rate limits); misinformation in high-stakes outputs.
3. **Map.** Tag each threat with its OWASP LLM ID (for example LLM01:2025) and, where useful, a MITRE ATLAS technique looked up live on atlas.mitre.org. Do not guess ATLAS IDs.
4. **Controls.** Least privilege for tools, allow-lists, human approval for irreversible actions, separating instructions from data, output encoding, sandboxing, secrets outside the context window, logging for repudiation, rate and spend limits, eval and red-team tests (upstream `agent-evals-red-teaming.md`).
5. **Rate and report.** Table: ID, element, STRIDE, OWASP/ATLAS, scenario, likelihood, impact, existing controls, recommended control, test. Then residual risks and owner. Link governance obligations to `eu-ai-act`, `nist-ai-rmf` (MANAGE), `iso42001` and, for personal data, `kvkk` / `gdpr-compliance`.

## Teaching and research use
For courses, generate a case system and a blank STRIDE table for students; grade with `homework-grader`. For papers, keep threat taxonomies cited to their primary pages with access dates.

## Rules
- No exploit code, jailbreak strings or instructions for attacking third-party systems.
- State assumptions; mark threats not validated by testing as hypotheses.

## Ek referans

Bir MCP yapılandırması veya bağımlılığı incelenirken `references/mcp-dependency-review.md` statik kontrol listesini uygula.
