---
name: council-protocol
description: Use when several agents must deliberate on one question and their views must be combined into a single, honest synthesis with recorded dissent.
---
# Council protocol

Run after `panel-factory`. The moderator runs the steps and writes the synthesis; it does not vote.

## Evidence in one paragraph
Most of the gain from multi-agent debate comes from independent answers plus majority vote, not from extra debate rounds (Debate or Vote, NeurIPS 2025, https://arxiv.org/abs/2508.17536). Debate methods do not reliably beat self-consistency and are sensitive to settings (https://arxiv.org/abs/2311.17371). Voting suits reasoning tasks, consensus suits knowledge tasks (ACL Findings 2025, https://arxiv.org/abs/2502.19130). Adversarial roles reduce early fixation (MAD, EMNLP 2024, https://arxiv.org/abs/2305.19118). Confidence-weighted rounds across diverse models help (ReConcile, https://arxiv.org/abs/2309.13007). So: protect independence, keep debate short, preserve dissent.

## Steps
1. Independent first round. Each member answers alone with: position, numbered findings (weaknesses first), evidence, open questions, confidence 1 to 5. No member sees another's answer.
2. Early stop check. If at least 4 of 5 members (80 percent) agree on the position and no member flags a factual error, skip to step 5.
3. Anonymized critique. Relabel answers A, B, C...; remove names and role hints. Each member ranks the others and lists the strongest and weakest point of each.
4. One rebuttal round at most, only on points of disagreement. A member may change position only by citing new evidence or a specific error; "the majority thinks so" is not a reason. Record every change and its reason.
5. Aggregate by task type:
   - Discrete answer (correct answer exists): majority vote of final positions; ties go to the side with stronger cited evidence, else reported as unresolved.
   - Judgment or prose: confidence-weighted synthesis; the moderator merges findings, weighting by confidence and evidence quality, never by count alone.
6. Dissent log. Every minority position stays in the output with its reasoning and confidence. Never delete it to make the result look unanimous.
7. Escalate. If mean confidence is below 3, or a high-stakes point stays split, hand the decision to the user.

## Guards against sycophancy and conformity
- Members never see the user's or moderator's preferred answer before round 1.
- Position changes need evidence (step 4); count and report them. Many changes toward the majority with no new evidence is a warning sign.
- The adversarial role must argue the strongest opposing case even if persuaded.
- The moderator checks that every factual claim in the synthesis has a source; unverified claims are labeled.
- Same-model panels share errors; say so in the output when diversity was low.

## Synthesis format
- Consensus: points all members accept, with evidence.
- Majority: points most accept, with count (e.g. 3/5) and mean confidence.
- Dissent: minority positions, reasoning, confidence.
- Unknowns: what nobody could verify and what would settle it.
- Recommendation: the moderator's action list, weaknesses first.
- Process note: rounds run, early stop or not, position changes and reasons.
