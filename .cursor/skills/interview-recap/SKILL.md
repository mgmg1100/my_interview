---
name: interview-recap
description: Use for interview practice recaps, delayed full recaps after 12 new regular items, monthly interview exams after 30 completed items, unfinished recap continuation, or 3-question daily interview retention tests.
---

# Interview Recap

Synthesize recent interview practice one item at a time. Refresh, connect, and test retention without re-teaching.

## Tracker

`interview-tracker.md` at the repository root — read the `## Recap Log` section to find the latest full recap entry and any one-by-one partial recap entries after it.

## Steps

1. Read `interview-tracker.md`.
2. Find the most recent full recap entry in `## Recap Log` and use it as the baseline. A full recap entry covers a batch of 6 items; a one-item entry is a partial recap marker, not a new baseline.
3. Collect all regular-pillar `- [x]` items checked after that full recap baseline across all three regular pillars, or all checked regular-pillar items if no full recap entry exists yet.
4. A full recap is due only when there are at least 12 completed regular items after the latest full recap entry, or when a delayed 6-item recap batch has already started and remains unfinished.
5. Build the recap batch from the older 6 items in that 12-item window: items 12 through 7 back from the newest completed regular item.
6. Subtract items already listed in partial recap entries after the baseline for that delayed batch.
7. If the user asked for a new item and the delayed recap batch has uncovered items, ask for consent before continuing recap first.
8. Decide the single recap item for this turn before presenting anything. Use chronological order by completion date where possible; otherwise use tracker order.
9. Read the matching note in this repository for that one item when available.
10. Present one recap item and one retention question, then wait for the user's answer before continuing to another recap item.
11. After the user answers or asks follow-up questions, give concise feedback and identify any durable clarification, example, tradeoff, edge case, or answer wording that belongs in the item note.
12. Before marking the recap item done, update the same note if the discussion added useful knowledge.
13. Ask the user to confirm they are finished with the recap item before changing the tracker.
14. Only after explicit completion confirmation and any needed note update, append a partial recap entry: `- YYYY-MM-DD - [single item covered]`.
15. When all 6 items in the delayed recap batch are covered, append a full recap entry listing the 6 items in one line. Otherwise, ask whether to continue to the next recap item or start new practice.

## Presentation Format

### What We Covered

One line for the selected item:
`[Pillar] - [Item]: one-sentence reminder of the core idea`

### Connections Across Pillars

One useful link from the selected item to another interview skill. Example: connect a system design tradeoff to a behavioral story, or connect an algorithm invariant to system design correctness.

### Retention Check

Ask one practical question about the selected item. Ask the user to answer briefly. Give concise feedback on their response before moving on.

## Daily Recap

Daily recap is a lightweight retention test, not a full recap batch.

1. Pick 3 completed items from the tracker by actual random selection, preferring older items over recently completed ones.
2. Ask one practical test question for each selected item. Do not re-teach first.
3. Give concise feedback after the user's answers.
4. Update the original item notes when the daily test reveals a mistake, correction, durable clarification, reusable example, edge case, tradeoff, or sharper wording.
5. Do not append to `## Recap Log` unless the user explicitly asks to mark the daily recap.

## Monthly Exam

Monthly exam is a question-only assessment, not a recap.

1. Read `interview-tracker.md` and find the latest monthly exam entry in `## Exam Log`.
2. Collect completed items after that exam entry across regular sections and optional add-ons. If no exam entry exists, collect all completed items.
3. A monthly exam is due when there are at least 30 completed items after the latest exam entry. The exam batch is the oldest 30 unexamined completed items.
4. Tell the user: "Today we have a monthly interview exam." Do not summarize or remind them of the items before asking questions.
5. Ask exam questions only, one question at a time. Wait for the user's answer, silently track correctness and notes for final review, then ask the next question. Do not give correctness feedback, review, or a running score between questions.
6. Score and review only after the full 30-question exam. Use a clear core score such as `24/30`, plus a separate senior-signal score such as `18/30` for clarity, tradeoffs, judgment, scope, and communication. Use this review table format by default: `Q | Question | Your Answer | Score | Senior Signal | Review`.
7. If the exam reveals a durable mistake, correction, uncovered gap, sharper example, or reusable wording, update the original item note before marking the exam done.
8. After the user confirms the exam is finished, append an exam entry in `## Exam Log` with the date, score, and covered items.
9. If the exam covered items that are also pending regular recap items, append matching partial recap entries or a full recap entry in `## Recap Log` as covered.
10. Commit and push tracker and note changes after marking the exam done.

## Rules

- Always recap one by one: one item, one connection, and one retention question per turn.
- Monthly exam is separate from recap and asks questions only with no reminders.
- Full recap triggers after any 12 newly completed regular items since the latest full recap entry, and covers the older 6 items from that 12-item window.
- Daily recap is 3 randomly selected tests from previous items, with older items preferred.
- Keep it tight. Recap is retrieval practice, not re-teaching.
- Connections section is mandatory.
- Retention check is mandatory.
- Never append recap entries or otherwise mutate `interview-tracker.md` until the user explicitly confirms they finished the recap.
- Prefer saved notes in this repository as recap source material when they exist.
