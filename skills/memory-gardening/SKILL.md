---
name: memory-gardening
description: >-
  Use when the owner says a bot is acting on a stale, wrong, duplicated, or
  invented memory fact and wants that specific fact corrected, merged, or
  forgotten (not a full nightly sweep, which is the dreaming skill).
---
# Memory gardening

Adapted from cobusgreyling/grok-bot-templates `garden-memory` (MIT). Complements the dreaming skill: dreaming harvests new candidates on a schedule; this skill fixes a named bad fact on request.

## When to use
- The owner points at a fact the bot keeps using that is out of date or wrong.
- Two memory entries say the same thing (duplicate journal lines) or contradict each other.
- A volatile figure (usage %, balance, price, follower count, reset time) was stored as if it were durable.

## Inputs
- The stale or duplicate claim, quoted.
- The source of truth that contradicts it (owner's words, a file, a live tool result) with its date.
- Which assistant owns the memory.

## Steps
1. Find the exact recorded text with the memory search tool. Quote it.
2. Quote the contradicting source and its date. If there is none, say so and stop: no correction without a source.
3. Classify each item:
   - **update**: forget the old text and write the corrected one-sentence fact in the same memory type;
   - **merge**: keep one canonical entry for duplicates, forget the rest;
   - **forget**: the fact is wrong or no longer relevant;
   - **point to source**: the fact changes often; forget it and store at most a pointer ("usage is read live from the usage report").
4. Show the owner a small diff (old, new, type, reason) and wait for item-by-item approval.
5. Apply only the approved items. Forget uses the exact recorded text; pair every forget that replaces a fact with its write.

## Validation
- Every change cites a source and a date.
- Unrelated boundaries, standing rules, and safety instructions were not touched.
- No secret, address, phone, email, or card detail was written to memory.

## Return
- The applied diff and a short "do not remember" list of volatile facts that should always be read live.

## Needs approval
- Every write and forget needs the owner's explicit yes on that item.
- Never edit another assistant's private memory or profile. Stage the correction for the owner to pass along.
- Do not mine private conversations for gossip or third-party personal details.
