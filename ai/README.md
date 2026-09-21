# AI as a working tool

Block 1 of [`LEARNING-PLAN.md`](../LEARNING-PLAN.md). Not "how to ask a chatbot
things" — the parts that survive contact with real work.

The deliverable is this write-up plus the two files it describes. The notes at
the bottom are from actual sessions, and the failures are the valuable half: a
list of things that went well teaches nothing about when to check.

## Context: what goes where

The single most useful thing learned so far, because it is the thing that stops
context being rebuilt from scratch every morning.

| Where | Loaded | Holds |
|---|---|---|
| `CLAUDE.md` (repo root) | always, every session | what is true for **all** work here — the plan comes first, verify before writing numbers down, never make anything public |
| `.claude/skills/<name>/SKILL.md` | only when the task matches | what is true for **one kind of task**. The bug-report standard is 60 lines and would be dead weight in every unrelated session |
| The prompt | this message only | what is true right now — the actual task |

Getting this wrong in either direction costs. Everything in `CLAUDE.md` means a
long file competing for attention with the work. Everything in the prompt means
retyping the same standards daily and getting different results each time.

**Why a long session degrades**: context is finite and older turns get
compacted. A decision made an hour ago can be summarised down to something
thinner than it was. Anything that must survive goes in a file — which is
exactly why the plan is a file and not a thing agreed in chat.

## What is in place

- [`../CLAUDE.md`](../CLAUDE.md) — always-on instructions for this repo
- [`../.claude/skills/bug-report/`](../.claude/skills/bug-report/) — a reusable
  standard for turning a failure into a report someone else can act on. It
  doubles as block 5's homework: writing the standard down forced the
  severity-versus-priority distinction and the "report the symptom, not the
  diagnosis" rule into words

## Running notes

### Where it earned its place

**Systematic checks over spot checks.** `robot --dryrun` over the whole repo
found an `Append To List` used without importing `Collections` — inside an `IF`
that had never executed, because every page was being served. The first missing
page would have crashed the test whose entire job was to name that page. Nothing
about that was clever; it was running a cheap check over everything instead of
looking where the bug seemed likely to be.

**Volume with verification after.** Day 29 needed a page server and sixteen HTML
fixtures. Generating them was fast. What made it trustworthy was running all 28
existing web tests against them unchanged before believing any of it.

### Where it was confidently wrong

**It wrote a false claim into a README.** While documenting Day 29, the CI
paragraph gained the sentence "since Day 29 not one of them needs anything but
this machine". Suites 11-15 were still calling the internet at that moment —
Day 30 had not happened yet. It reads fluently and it was not true.
*The lesson: fluent text is not checked text, and documentation gets checked far
less carefully than code.*

**A number from a single run.** The push-path runtime was written as "~44s" from
one measurement. A second run gave 57.5s. Neither was wrong; the claim was.
*Rule adopted: a number that varies gets a range and a reason, or it gets run
twice before it goes in a file.*

**It reordered the plan, twice, on its own initiative.** Once to pull a task up
because it seemed more concrete, once to restructure the whole thing while
transcribing someone's advice. Both times the reasoning was defensible and both
times nobody asked for it.
*Rule adopted, now the first line of `CLAUDE.md`: read the plan before proposing
what is next, and say it rather than start it.*

**It published someone's private message.** Advice that arrived in a LinkedIn DM
went into a repo file with the sender's name, profile link and direct quotes.
Not malicious, just never considered — the material was in front of it and the
task was "put this in the plan".
*Rule adopted: anything about a person, in a file, needs asking first.*

### The shape of it

The pattern in all four failures is the same: **it optimises for producing a good
answer to the task in front of it, and the things it drops are the ones outside
that frame** — a decision made earlier, a measurement's variance, whose words
those were. None of it was hard to catch. All of it needed someone to look.

Which sets what is worth delegating: work where **checking is cheaper than
doing**. Generating sixteen fixture pages, then running the suite. Drafting a
report, then reading it. Not: anything where the check costs as much as the work,
and not anything whose failure is silent.
