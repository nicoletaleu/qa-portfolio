---
name: test-data
description: Design test data for a function, a form, an API field or a data-driven test - boundary values, equivalence classes, invalid inputs, with an expected result for every row. Use when the user asks for test data, test inputs, a CSV or table for a data-driven test, edge cases, or "what should I test this with".
---

# Designing test data

Test data is only as good as its expected column. A thousand generated inputs
with no independent expected result test nothing except that the code runs.

## Before generating anything

1. **Find the rule.** A docstring, a spec, an acceptance criterion, a field's
   validation message. Write it down in one or two lines. If there is no rule,
   say so: the data then documents current behaviour, and that must be stated,
   not implied.
2. **Split the input into classes.** Valid and invalid, and inside each, the
   groups that should behave the same. One row per class is the floor.
3. **Find the edges of every class.** Just inside, on, and just outside every
   limit: a length of 8, 9, 15 and 16 when the rule says 9 to 15. Dates get the
   day before, the day of and the day after, plus month end, year end and
   29 February.

## Every row carries

| Column | Why |
|---|---|
| `case` | a name someone can find in a failure message |
| the input | exactly as it would arrive - with the spaces, the plus sign, the wrong case |
| `expected` | the output value, or `error` |
| `why` | which class or edge this row exists for. A row without a reason is a row nobody dares delete |
| `source` | `spec` if the expectation comes from the rule, `assumed` if the rule is silent and this is a guess |

## Discipline

- **Never compute the expected value with the code under test.** Work it out
  from the rule, by hand if necessary. An expected column produced by the
  function being tested can only ever agree with it.
- **Keep `assumed` rows visible.** When one of them fails, the finding is a
  question for whoever owns the rule, not a bug - and it gets reported as a
  question.
- **Fix every moving input.** A reference date, a random seed, a locale. Data
  that depends on today changes its own result on somebody's birthday.
- **Prefer a few rows that each mean something** over many that repeat a class.
  Ten valid phone numbers in ten formats that all hit the same branch is one
  test written ten times.
- **No real personal data.** Invented names, reserved domains such as
  `example.com`, numbers that cannot belong to anyone.
- **Unique where the system has memory.** Data that creates records needs a
  unique part, or the second run fails on a duplicate the first run left behind.

## After generating

Run it. Then sort every failure into one of three piles before calling any of
them a bug:

1. **the data was wrong** - the expected value was a mistake
2. **the rule was unclear** - an `assumed` row; this is a question
3. **the code disagrees with its own rule** - this is a bug, and the
   `bug-report` skill takes over

The first pile is the one that gets skipped, and it is the one that makes a
report into noise.
