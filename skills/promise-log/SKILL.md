---
name: promise-log
description: >-
  Use when commitments made by or to the owner (co-author deadlines, reviewer
  invitations, student supervision, project deliverables, 'I'll send it by
  Friday') must be extracted from emails, meeting notes, chats or transcripts
  into a sourced log, or when the owner asks what is overdue.
---
# Promise log (söz takibi)

Adapted from cobusgreyling/grok-bot-templates `log-promises` (MIT) for academic and project work.

## When to use
- After a meeting, email thread, call, or chat where someone committed to something.
- When the owner asks "what did I promise", "what is overdue", or "who owes me what".
- From a routine that sweeps recent mail/meetings (the routine names the sources, not this skill).

## Inputs
- The source material: email thread, meeting notes, transcript, chat.
- The existing log, if any (default `promise-log.md` in the working directory; a routine may name another path).

## Steps
1. Extract only binding statements: an action plus a person or a date ("I'll send the revised draft", "reviews due 30 Nov", "we'll add the partner to the budget"). Ignore pleasantries, hopes, and vague intentions.
2. For each row record: direction (owner owes / owed to owner), counterparty, the commitment in one line, an exact short quote, due date, source (link, message id, or file + date), status (open / done / overdue / unknown).
3. A due date that the source does not state is `unknown`. Never infer or invent a date. Relative dates ("next Friday") are resolved against the source's own date and the resolution is shown.
4. Deduplicate against the existing log by counterparty + commitment; update status rather than add a twin row.
5. Mark rows overdue only against today's date in the owner's timezone.
6. Append or update the log file. Keep it a single markdown table sorted by due date, unknowns last.

## Validation
- Every row has a quote and a source.
- No date, name, or amount appears that is not in the source.
- Closed items are closed only with evidence (a sent reply, a delivered file, the owner saying so).

## Return
- Changes since the last run (new, closed, became overdue), then the open table.
- Overdue items first, in one short list.
- Stay silent from a routine when nothing changed.

## Needs approval
- Never email, message, or remind a counterparty. Offer a draft instead.
- Never write memory from this log; it is a working file, not durable memory.
- Do not add calendar events or reminders unless the owner asks.
