---
name: test-cases-from-ac
description: Draft test cases from an acceptance criterion, a user story or a requirement - positive, negative and boundary cases, each traced to the clause it checks, plus the questions the criterion leaves open. Use when the user pastes an acceptance criterion or a user story, or asks for test cases, test scenarios or a test checklist for a feature.
---

# Test cases from an acceptance criterion

A draft, not a verdict. Its value is speed and breadth; its risk is that it
reads as complete. Everything below is about keeping that risk visible.

## Read the criterion first

Split it into **numbered clauses**, each one a single thing that must be true.
Then write two short lists before a single case:

- **What it says** - the behaviour that is explicitly required
- **What it does not say** - the gaps. Error wording, limits, what happens
  twice, what happens logged out, what happens on the second attempt. These
  become questions, not test cases with invented answers

## Each case carries

| Field | Rule |
|---|---|
| ID | short and stable, e.g. `TC-03` |
| Traces to | the clause number it checks. A case that traces to nothing is either a missing clause or scope creep - say which |
| Type | positive, negative, boundary |
| Preconditions | the state before the first step |
| Steps | numbered actions, minimal |
| Expected | observable - a URL, a message, a value. "It works" is not an expected result |
| Basis | `AC` when the expected result is in the criterion, `assumed` when it is not |

## Coverage, in this order

1. One positive case per clause - the thing the criterion is about
2. The negative case for each clause - the input it should refuse
3. Boundaries - empty, too long, wrong case, surrounding spaces, the same action
   twice
4. State - before login, after logout, the back button, a second tab
5. Only then anything cross-cutting: security, accessibility, performance. Keep
   these few, and mark them as outside the criterion

## Discipline

- **Do not invent requirements.** If the criterion does not give the error
  text, the expected result is "an error is shown and the user stays on the
  page", and the exact text goes into the questions.
- **An existing suite is input.** If there are automated tests for the feature,
  read them and mark which cases are already covered. A draft that duplicates
  the suite has doubled the maintenance and added nothing.
- **Run what can be run.** A case whose expected result was never checked is
  still a guess. Say which ones were executed and which were not.
- **End with the questions.** A short list for whoever owns the criterion. They
  are often the most useful part of the output.
