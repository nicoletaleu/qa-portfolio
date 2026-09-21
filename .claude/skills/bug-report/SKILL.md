---
name: bug-report
description: Turn a failing test, a log, a screenshot or a description of something going wrong into a structured bug report. Use when the user reports a defect, pastes a failure or a stack trace, asks for a bug report or a defect report, or says something is broken and should be written up.
---

# Writing a bug report

A bug report has one job: let someone who was not there reproduce the problem
and decide how urgent it is. Everything below serves that, and anything that
does not serve it is padding.

## Before writing anything

1. **Reproduce it, or say that you could not.** A report that begins "I could
   not reproduce this, here is what I saw once" is honest and useful. A report
   that implies reproduction that never happened wastes somebody's afternoon.
2. **Reduce it.** Remove every step that is not required. "Log in, go to
   Reports, set a filter, export, then delete a row" often turns out to be
   "delete a row". The minimal reproduction is the single most valuable thing in
   the report.
3. **Check it is one bug.** Two problems in one report means one of them gets
   fixed and the report gets closed.

## The report

**Title** — what breaks and where, in one line someone can scan in a list.
Not "Export is broken". Not a description of the whole scenario. Something like
"Export produces an empty CSV when the date filter spans a month boundary."

**Environment** — build or commit, browser and version, OS, URL or
environment name, account or role used. A bug that only happens on one of these
is invisible without them.

**Preconditions** — the state the system has to be in. Data that must exist,
feature flags, permissions.

**Steps to reproduce** — numbered, minimal, each one an action. Written so
someone can follow them without knowing the feature.

**Expected result** — and where that expectation comes from: the acceptance
criterion, the spec, the documented behaviour, or consistency with the rest of
the product. "Expected: it works" is not an expectation.

**Actual result** — what happened, precisely. The exact error text, the exact
wrong value. Not "it fails".

**Evidence** — screenshot, screen recording, log excerpt, HAR, the failing
test's output. Trim logs to the relevant part and keep the timestamps.

**Frequency** — always, intermittently (how often), or once.

**Severity and priority, kept separate.** Severity is how bad the damage is when
it happens; priority is how soon it should be fixed. A cosmetic typo on the
landing page can be low severity and high priority. Give the reasoning for both,
in one line each.

## Discipline

- **Report the symptom, not the diagnosis.** If a cause is suspected, label it
  as a suspicion in its own section. A report that states a wrong cause as fact
  sends people to the wrong file, and the cause is the developer's territory.
- **No blame, no adjectives.** "Obviously broken", "terrible behaviour" and
  "the developer forgot" all cost credibility and buy nothing.
- **Quote exact strings**, do not paraphrase error messages. A paraphrased error
  cannot be searched for.
- **Say what you already ruled out.** Cache cleared, different browser, another
  account, incognito. It stops someone repeating the work.
- **A regression gets extra weight**: say which version last worked, if known.

## When the input is a failing automated test

Additional things that belong in the report, because they are available and
usually omitted:

- the test name and what it was asserting, in plain language
- the **innermost** failing step, not the wrapper that reported it
- actual versus expected values as the test saw them
- whether it fails consistently or only sometimes, and whether it fails in
  isolation or only in a full run — an order-dependent failure is a different
  bug from a broken feature
- whether the test itself might be wrong. Sometimes the bug is in the test, and
  a report that has not considered that is a report that might be noise
