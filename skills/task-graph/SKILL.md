---
name: task-graph
description: Use when a large research or writing job (a paper, a proposal, a book chapter, a review) should be split into small checked steps that agents can run, verify and resume across sessions.
---
# Task graph

Break one large job into bounded nodes, run each with only the context it needs, pass every output through an evidence gate, and keep files that let another session resume. Use `panel-factory` and `council-protocol` inside a node when that node needs a debate.

Origin: structure adapted in our own words from a public graph prompt by @hanakoxbt, which was inspired by Karpathy's autoresearch (https://github.com/karpathy/autoresearch). Not written or endorsed by Karpathy.

## Inputs (fill before starting)
- Task and deliverable path.
- Acceptance checks: what must be true for the job to count as done.
- Sources the work may use.
- Allowed changes: which files or sections may be edited.
- Limit: maximum rounds, time or calls.
If a missing detail would change the outcome, ask one focused question; otherwise state the assumption and proceed.

## 1. Split
- A node is one bounded job: one input, one output, one check. Split by what the step must read, not by folder or chapter order.
- Draw an edge only where one node uses another's output. Nodes with no edge between them can run in parallel.
- Write nodes, edges and checks to `graph.md` and get the user's approval before running.

## 2. Run nodes
Give each node its spec, inputs and check, nothing more. It returns the output path, a verdict and the evidence. Keep node specs reusable on new source sets.

## 3. Mechanical nodes are code
Any step with exactly one correct answer (merging or deduplicating references, counting, sorting, format and DOI checks) is a script, never a model call. If the tool is missing, name the blocker and keep the nodes that can still finish.

## 4. Permissions
Ask before publishing, sending or spending. Two sessions never edit the same file. Keep a recoverable copy before risky merges.

## 5. Gates
Every edge that carries risky work has a gate. Open it on evidence in this order: deterministic checks first, the node's own report second, the model's confidence last. Save `checks.md` with one row per requirement: `node | requirement | pass, fail or unresolved | evidence` (file path, link or command output). Leave missing evidence visible.

## 6. Return paths
- Correction: a failed gate sends only that unit back to its node with the reason, the evidence and the scope ("fix this only"). Cap at three attempts, then escalate to the user with options.
- Learning: after an accepted result, write the rule it confirms into `graph.md` so the next run starts from it.

## 7. Completion
Before running, turn the acceptance checks into a checklist where every item points to observable evidence: every output exists and opens; every gate ran on the saved version; failures are fixed or reported. If a limit or blocker stops the run, return a partial status with the exact steps left.

## Loop
Read `graph.md`, pick ready nodes, run independent ones in parallel, gate every output, return only failed nodes, merge accepted outputs, run the full checks, repeat until done, blocked or at the limit. Never weaken a gate to get a pass.

## Handoff
After each stage update `progress.md`: nodes done, running and blocked; output paths; decisions and why; open failures and uncertainties; next node. A resumed session reads `graph.md` and `progress.md` first.

## Delivery
Return the deliverable, `graph.md`, `checks.md` and `progress.md`. State what was checked, what passed and what remains unresolved. Report measured usage only when available; never infer savings.

## Academic example
Journal paper revision: nodes for (a) parse reviewer comments into a table, code; (b) map each comment to a manuscript section; (c) draft each response, one node per comment group; (d) verify every new citation, code plus citation checker; (e) statistics recheck; (f) assemble response letter. Gates on (c) to (e); (a) and (d) are scripts.
