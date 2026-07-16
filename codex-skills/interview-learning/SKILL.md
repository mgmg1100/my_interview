---
name: interview-learning
description: Use when user asks for interview practice, next interview lesson, LeetCode 75 practice, system design practice, behavioral interview practice, or a mock interview learning session.
---

# Interview Learning

Deliver exactly one new interview item per session, with no repeats. Before teaching anything, first decide and announce the single item for the session. If the user does not provide a topic, list a numbered menu with the next unchecked item from each configured regular rotation section plus the next unchecked item from each optional add-on section, then ask which one they want. If they do not choose, use the regular rotation order automatically and exclude optional add-ons.

## Tracker

`~/my_interview/interview-tracker.md` - sections with checkboxes. The first unchecked item in the selected section is the next item to teach or practice. Regular sections are listed under `Regular rotation sections:` and optional categories are listed under `Optional add-on sections:`.

## Steps

0. **Name the conversation** - At the start of the session, mark the current conversation name with the session date in `YYYY-MM-DD` format.
1. **Check recap state before new learning** - Read `~/my_interview/interview-tracker.md`:
   - First check monthly exam state in `## Exam Log`. If there are at least 30 completed items since the latest monthly exam entry, a monthly exam is due. If the user asked for new practice, tell them an exam is due today and ask for consent before continuing the exam first.
   - Find the latest full recap entry in `## Recap Log`. A full recap entry lists a batch of 6 items. One-item recap entries after that are partial coverage markers, not reset points.
   - Count regular-pillar `- [x]` items completed after the latest full recap entry. A full recap is due only when there are at least 12 completed regular items after that baseline, so the newest 6 items are not recapped immediately.
   - The recap batch is the older 6 items from that 12-item window: items 12 through 7 back from the newest completed regular item. Subtract one-item partial recap entries for that batch after the latest full recap entry.
   - If that delayed batch has uncovered items, ask for consent before continuing recap first.
   - Daily recap is separate: if the user asks for a daily recap or quick review, give 3 random tests from previously completed items, preferring older items.
2. Read `~/my_interview/interview-tracker.md`.
3. **Select exactly one item before teaching**:
   - Read `Regular rotation sections:` and `Optional add-on sections:` from the tracker.
   - If the user does not specify a section or topic, find the first `- [ ]` item from each configured regular section and each optional add-on section. List them as a numbered menu grouped by "Regular Practice" and "Optional Drills", and ask the user which number they want. If they do not choose, find the regular section used by the most recent completed regular item, then choose the first `- [ ]` item from the next regular section in configured order. If no regular item has been completed yet, start with the first configured regular section.
   - If the user specifies algorithm, LeetCode, system design, behavioral, or mock, find the first unchecked item in that section.
   - If the user mentions multiple areas, pick only the first requested area unless they explicitly ask for a multi-part session.
4. Present the selected item using the appropriate format below, then pause for user Q&A. Do not start the practice test immediately after the concept content. Ask whether the user feels good about the item and answer their questions first. Start the practice test only after the user says they are ready, feel good, or otherwise asks to practice.
5. After the user completes or explicitly skips the practice test, give concise feedback. Then create or update a concise note for the item in `~/my_interview`, following `CONTRIBUTING.md`.
6. Ask the user to confirm they are finished with the session before changing the tracker. Do not update `interview-tracker.md` in the same response that presents new content unless the user has already explicitly said they finished the session.
7. Only after explicit completion confirmation, update tracker: `- [ ] Item` -> `- [x] Item - YYYY-MM-DD`.
8. After notes and tracker updates are complete, commit the session changes in `~/my_interview` and push `main` to `origin/main` if a remote is configured. If credentials or network access are unavailable, report the blocker clearly and leave the local commit intact.

## Presentation Formats

### Algorithm - LeetCode 75

- **Problem name** as a heading
- Pattern and why it applies
- Invariant or state definition
- Walkthrough on a small example
- Complexity
- Clean implementation when useful
- Edge cases
- Growth signal: one question testing the core invariant

When starting algorithm practice, use an actual LeetCode-style prompt: include the problem statement, examples with inputs and outputs, constraints, and the expected function signature. Ask the user to solve it as code, not only compute one sample output.

### System Design - System Design Interview Book

- **Design prompt** as a heading
- Functional and non-functional requirements
- Capacity assumptions or estimation shape
- API sketch
- Data model
- High-level architecture diagram
- Bottlenecks, tradeoffs, and failure modes
- Growth signal: one constraint-change question

### Behavioral Interview - Common Questions

- **Question** as a heading
- What the interviewer is testing
- Strong answer shape
- Muscle-memory wording template
- Example outline using STAR or another clear structure
- Senior-level signals
- Growth signal: one prompt to make the story sharper

## Rules

- Always practice one by one: deliver one item total per session.
- For algorithm items, prioritize the invariant, edge cases, and clean implementation.
- Algorithm practice tests must look like real LeetCode prompts and require the user to write the solution.
- For system design items, never copy book text. Use interview-ready reasoning in your own words.
- For behavioral items, emphasize ownership, scope, judgment, ambiguity, influence without authority, tradeoff communication, organizational impact, and durable follow-through.
- If a section is exhausted, say so and prompt to add more items.
- Keep explanations concise. This is interview training, not a textbook.
- Use today's date when checking off items.
- Never mark items complete, append recap entries, or otherwise mutate `interview-tracker.md` until the user explicitly confirms they finished the session.
- Every session must end with a concise practice exercise unless the user explicitly skips it.
- At the end of learning, always create or update notes before marking the tracker complete so future recaps can use the notes.
