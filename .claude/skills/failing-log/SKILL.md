---
name: failing-log
description: Read a failing test run - a Robot Framework output.xml or log.html, a pytest or Newman report, a CI log, a stack trace - and say what failed, where, and what kind of failure it is. Use when the user pastes or points at a failing log, a red CI run, or asks why a test failed.
---

# Reading a failing log

The goal is to answer three questions, in this order, from the evidence in the
log - not from what the test is probably about.

1. **What exactly failed?**
2. **What kind of failure is it?**
3. **What is the next thing to check?**

## What exactly failed

- **Go to the innermost failing step.** A test fails through a chain of
  keywords or functions; the top one only says that something below it broke.
  The bottom one has the real values.
- **Quote the message exactly**, with the expected and actual values as the log
  shows them.
- **Count.** How many tests ran, how many failed, and whether the failures share
  a message. Twelve failures with one message are usually one problem.
- **Find the first failure in time.** Later failures are often a consequence:
  a setup that failed, a browser that never opened, a server that was not up.

## What kind of failure it is

Put each failure in exactly one of these, and say why:

| Kind | Usual signs |
|---|---|
| **Product** - the code under test is wrong | the assertion ran, with sensible inputs, and got a wrong value |
| **Test** - the test or its data is wrong | the expected value is itself wrong, a locator no longer matches, the test depends on order |
| **Environment** - nothing to do with either | timeouts, connection refused, a missing file or dependency, a port in use |
| **Unclear rule** - no one has said what is right | the test expects something the spec never says |

A failure that could be two of these is reported as that, with what would tell
them apart. "Probably flaky" is not a kind; it is a failure no one has read yet.

## What to check next

One or two concrete steps, cheapest first: re-run the single test in isolation,
run it again with the same data, look at the value one step earlier, check the
spec line. Not a list of ten possibilities.

## Discipline

- **Evidence only.** Anything not in the log is labelled as a suspicion.
- **Do not fix the test to make it pass** while reading the log. Changing the
  expected value is a decision about the rule, and it belongs to whoever owns
  the rule.
- **A passing re-run proves nothing** about the first failure except that it
  does not always happen. Record both results.
- If the failure is a product bug, hand over to the `bug-report` skill with the
  test name, the innermost step and the values.
