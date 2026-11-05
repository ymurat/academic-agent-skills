---
name: panel-factory
description: Use when a task (paper review, research question, legal or policy draft) needs a deliberative panel of agents and you must decide which roles to convene.
---
# Panel factory

Build a small, diverse, independent panel fitted to the task. Feed its output to `council-protocol`.

## 1. Task profile
Write three lines before choosing roles:
- Task type: review/evaluation, research debate, legal or policy drafting, or other.
- Answer type: discrete (a correct answer exists: an error, a rule, a yes/no) or judgment (prose, accept/revise/reject, strategy).
- Stakes and evidence available: what documents, data and sources the panel may use.

## 2. Role plan
Derive roles from the task, not from habit:
1. List the distinct questions the task raises (method, validity, law, ethics, impact, statistics, citations, counter-arguments).
2. One role per question cluster. Always include one adversarial role that argues the strongest opposing case.
3. Size: 4 to 6 roles. Larger panels add cost without evidence of extra gain.

## 3. Diversity and independence check
- No two roles share the same scope; merge or drop duplicates (repeating the same role reduces benefit; ChatEval).
- Each role has a different evidence lens or source set; prefer different model families when available (ReConcile).
- Roles do not see each other's output in the first round.
- Flag missing perspectives (for example, the opposing party's likely defense in a legal draft).

## 4. Reuse before create
1. Map each role to an existing teammate agent whose scope fits at least 80 percent. Reuse it, adding a task-specific brief.
2. Propose a new agent only for a real gap. State the gap in one line and draft its brief (below). Do not create or register agents without the user's approval.

## 5. Role brief template
For every panel member write:
- Scope: what this role judges, in one or two sentences.
- Evidence standard: what counts as support (cited document, statute article, verified DOI, data); unsupported claims must be marked as such.
- Do not: out-of-scope topics, fabricating sources, softening findings to please, deferring to other roles.
- Output format: verdict or position; numbered findings, weaknesses first; evidence for each; open questions; confidence 1 to 5 with one line of reasoning.

## 6. Hand-off
Pass the profile, panel list (reused vs proposed) and briefs to `council-protocol`. Show the user the panel in a short table before running when the task is high-stakes.

## Basis
AutoAgents (IJCAI 2024, https://arxiv.org/abs/2309.17288) and AgentVerse (https://arxiv.org/abs/2308.10848): plan roles from the task, then check the plan. ChatEval (https://arxiv.org/abs/2308.07201): role diversity matters. ReConcile (ACL 2024, https://arxiv.org/abs/2309.13007): diverse models outperform copies of one.
