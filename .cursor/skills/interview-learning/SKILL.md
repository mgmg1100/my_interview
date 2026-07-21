---
name: interview-learning
description: Use when user asks for interview practice, next interview lesson, LeetCode 75 practice, system design practice, behavioral interview practice, or a mock interview learning session.
---

# Interview Learning

Deliver exactly one new interview item per session, with no repeats. Before teaching anything, first decide and announce the single item for the session. If the user does not provide a topic, list a numbered menu with the next unchecked item from each configured regular rotation section plus the next unchecked item from each optional add-on section, then ask which one they want. If they do not choose, use the regular rotation order automatically and exclude optional add-ons.

## Tracker

`interview-tracker.md` at the repository root — sections with checkboxes. The first unchecked item in the selected section is the next item to teach or practice. Regular sections are listed under `Regular rotation sections:` and optional categories are listed under `Optional add-on sections:`.

## Steps

0. **Name the conversation** — At the start of the session, use the Cursor `rename_chat` MCP tool to set the conversation name to the session date in `YYYY-MM-DD` format.
1. **Check recap state before new learning** — Read `interview-tracker.md`:
   - First check monthly exam state in `## Exam Log`. If there are at least 30 completed items since the latest monthly exam entry, a monthly exam is due. If the user asked for new practice, tell them an exam is due today and ask for consent before continuing the exam first.
   - Find the latest full recap entry in `## Recap Log`. A full recap entry lists a batch of 6 items. One-item recap entries after that are partial coverage markers, not reset points.
   - Count regular-pillar `- [x]` items completed after the latest full recap entry. A full recap is due only when there are at least 12 completed regular items after that baseline, so the newest 6 items are not recapped immediately.
   - The recap batch is the older 6 items from that 12-item window: items 12 through 7 back from the newest completed regular item. Subtract one-item partial recap entries for that batch after the latest full recap entry.
   - If that delayed batch has uncovered items, ask for consent before continuing recap first.
   - Daily recap is separate: if the user asks for a daily recap or quick review, give 3 random tests from previously completed items, preferring older items.
2. Read `interview-tracker.md`.
3. **Select exactly one item before teaching**:
   - Read `Regular rotation sections:` and `Optional add-on sections:` from the tracker.
   - If the user does not specify a section or topic, find the first `- [ ]` item from each configured regular section and each optional add-on section. List them as a numbered menu grouped by "Regular Practice" and "Optional Drills", and ask the user which number they want. If they do not choose, find the regular section used by the most recent completed regular item, then choose the first `- [ ]` item from the next regular section in configured order. If no regular item has been completed yet, start with the first configured regular section.
   - If the user specifies algorithm, LeetCode, system design, behavioral, or mock, find the first unchecked item in that section.
   - If the user mentions multiple areas, pick only the first requested area unless they explicitly ask for a multi-part session.
4. Present the selected item using the appropriate format below, then pause for user Q&A. Do not start the practice test immediately after the concept content. Ask whether the user feels good about the item and answer their questions first. Start the practice test only after the user says they are ready, feel good, or otherwise asks to practice.
5. After the user completes or explicitly skips the practice test, give structured feedback (see pillar-specific formats). Then create or update a concise note for the item in this repository, following `CONTRIBUTING.md`. For algorithm items, also keep the practice `.py` file when one was created.
6. Ask the user to confirm they are finished with the session before changing the tracker. Do not update `interview-tracker.md` in the same response that presents new content unless the user has already explicitly said they finished the session.
7. Only after explicit completion confirmation, update tracker: `- [ ] Item` -> `- [x] Item - YYYY-MM-DD`.
8. After notes and tracker updates are complete, commit the session changes in this repository and push `main` to `origin/main` if a remote is configured. If credentials or network access are unavailable, report the blocker clearly and leave the local commit intact.

## Presentation Formats

### Algorithm - LeetCode 75

Walk through every algorithm item like a real onsite interview. Teach first, then practice only when the user is ready.

#### Phase 1 — Teach (before practice)

Present in this order:

1. **Problem** — Full LeetCode-style prompt: statement, examples with inputs/outputs, constraints, and function signature.
2. **Clarifying questions** — 2–3 questions an interviewer would expect you to ask aloud (input bounds, edge cases, return format, duplicates, empty input).
3. **Think out loud — opening** — Give a short script the candidate can say to start strong, e.g. "I'll restate the problem, ask a couple clarifying questions, start with a brute force, then optimize."
4. **Brute force** — Describe the naive approach in plain English, pseudocode or sketch, then state time and space complexity. Note why it works but why you'd improve it.
5. **Optimal solution** — Pattern name, core invariant or state definition, why the pattern applies, walkthrough on a small example, then clean Python implementation.
6. **Complexity** — Explicit time and space for the optimal solution; one sentence comparing to brute force.
7. **Edge cases** — Empty input, single element, duplicates, overflow, off-by-one — whatever applies.
8. **Think out loud — during coding** — Bullet phrases to say while coding: restating the invariant, announcing the loop structure, naming variables, checking edge cases before running.
9. **Think out loud — closing** — How to wrap up: summarize approach, restate complexity, mention one tradeoff or follow-up you'd expect.
10. **Full brute-force think-out-loud example** — End the teaching section with a complete spoken example of how a candidate could propose the brute-force solution in an interview. Include problem restatement, brute-force idea, why it is correct, complexity, why it may be insufficient, and the transition sentence into optimization.

Pause for Q&A. Do not create a practice file or start the timed exercise until the user says they are ready to practice.

#### Phase 2 — Practice (when user is ready)

1. **Create a practice file** at `algorithm/leetcode-75/<kebab-case-problem-name>.py`:
   - Module docstring with problem name, one-line pattern, full LeetCode-style problem statement, examples, constraints, and expected function signature
   - `Solution` class or top-level function matching the LeetCode signature
   - A `if __name__ == "__main__":` block with test cases covering: given examples, edge cases, and at least one non-trivial case
   - Use plain `assert` statements or `unittest`; keep tests runnable with `python algorithm/leetcode-75/<file>.py`
   - Leave the solution body as a stub (`pass` or `...`) unless the user asks to see the reference implementation in the file
2. **Interview simulation** — Ask the user to think out loud and implement the solution in the file (or paste their code). Treat it like a live interview: do not give hints unless they are stuck for more than one exchange.
3. **Run tests** — Execute the file after the user submits code. Report pass/fail per test case.
4. **Follow-up questions** — Ask 1–2 interviewer-style follow-ups after the first working solution, such as:
   - What if constraints changed (larger input, streaming data, sorted input)?
   - Can you do it in O(1) extra space?
   - What breaks if we remove a constraint?
   - How would you test this in production?
5. **Feedback** — Give structured feedback in four parts:
   - **Correctness** — Did tests pass? Missed edge cases?
   - **Complexity** — Did they state and achieve the target time/space?
   - **Communication** — Did they think out loud, clarify, and explain tradeoffs?
   - **Code quality** — Naming, structure, invariant clarity; one concrete improvement

#### Phase 3 — Notes

After practice, create or update `algorithm/leetcode-75/<kebab-case-problem-name>.md` with: pattern, invariant, brute force vs optimal complexity, edge cases, full brute-force think-out-loud example, think-out-loud phrases that worked, follow-up question answers, and any mistakes from the session.

Keep the `.py` practice file in the repo when created so future sessions can re-run tests.

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

Run every behavioral item like a real mock interview. Teach the answer structure first, then evaluate the user's answer as an interviewer would.

#### Phase 1 — Teach (before practice)

Present in this order:

1. **Question** — State the behavioral prompt exactly.
2. **What the interviewer is testing** — Name the signal: ownership, judgment, conflict handling, ambiguity, leadership, execution, communication, or learning.
3. **STAR schema template** — Give a fill-in template:
   - **Situation:** "When I was working on [project/context], we faced [specific challenge]."
   - **Task:** "I was responsible for [your ownership], and success meant [measurable or observable outcome]."
   - **Action:** "I [specific actions], because [judgment/tradeoff]. I aligned [stakeholders] by [communication/influence]."
   - **Result:** "As a result, [metric/customer/team/system impact]. I learned [durable behavior change]."
4. **Templated example answer** — Provide a concise sample answer using STAR. Keep it realistic, specific, and senior-leaning without inventing personal details about the user. Label each STAR part.
5. **Strong wording bank** — Give reusable sentence shapes for ownership, tradeoffs, disagreement, ambiguity, and impact.
6. **Signal checklist** — List what a strong answer must prove: scope, personal contribution, judgment, collaboration, measurable result, reflection, and seniority signal.
7. **Common traps** — Warn against vague "we" language, too much background, blaming others, missing result, and shallow reflection.

Pause for Q&A. Do not start the mock answer until the user says they are ready to practice.

#### Phase 2 — Mock Interview Practice (when user is ready)

1. Ask the behavioral question as an interviewer and request a spoken-style answer.
2. Let the user answer without interruption unless they ask for help.
3. Ask 1–2 realistic follow-up questions before scoring, such as:
   - "What was the hardest tradeoff you made?"
   - "How did you know your approach worked?"
   - "What would you do differently now?"
   - "How did you influence people who did not report to you?"
4. Score the answer like an actual mock interview:
   - **Overall score:** `1–5`
   - **Signal score:** `1–5` for seniority, ownership, judgment, scope, ambiguity handling, influence, and impact
   - **Structure score:** `1–5` for STAR completeness, focus, pacing, and clarity
   - **Wording score:** `1–5` for crispness, specificity, active verbs, and interviewer-ready phrasing
5. Give feedback in this format:
   - **Hire signal:** what level/signal the answer currently projects
   - **What worked:** 2–3 concrete strengths
   - **What weakened the answer:** missing evidence, vague wording, unclear stakes, weak metric, overuse of "we", or shallow reflection
   - **Wording upgrades:** rewrite 2–4 specific phrases into stronger interview wording
   - **Stronger answer shape:** a tighter STAR outline using the user's actual content
   - **Next drill:** one targeted practice prompt to improve the answer

#### Phase 3 — Notes

After practice, create or update `behavioral-interview/<kebab-case-question-or-tip>.md` with: the prompt, tested signal, STAR schema template, reusable wording, strong answer outline, scoring notes, follow-up questions, and the user's durable mistakes or upgrades.

## Rules

- Always practice one by one: deliver one item total per session.
- For algorithm items, follow the full interview walkthrough: clarifying questions, brute force, optimal solution, complexity, think-out-loud scripts, a full brute-force spoken example, then practice with a `.py` file and test cases when the user is ready.
- Algorithm practice must use a LeetCode-style prompt and require the user to implement code, not only describe the answer.
- Always run the practice file tests and give structured feedback (correctness, complexity, communication, code quality) plus 1–2 follow-up questions.
- For system design items, never copy book text. Use interview-ready reasoning in your own words.
- For behavioral items, use the full mock interview workflow: STAR schema template, templated example answer, realistic follow-ups, signal/structure/wording scores, wording upgrades, and a tighter rewritten answer shape.
- Behavioral feedback must evaluate actual interview signal, not just correctness. Emphasize ownership, scope, judgment, ambiguity, influence without authority, tradeoff communication, organizational impact, and durable follow-through.
- If a section is exhausted, say so and prompt to add more items.
- Keep explanations concise. This is interview training, not a textbook.
- Use today's date when checking off items.
- Never mark items complete, append recap entries, or otherwise mutate `interview-tracker.md` until the user explicitly confirms they finished the session.
- Every session must end with a concise practice exercise unless the user explicitly skips it.
- At the end of learning, always create or update notes before marking the tracker complete so future recaps can use the notes.
