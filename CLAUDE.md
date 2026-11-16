# Working in this repo

Instructions that apply to every session here. This file is loaded automatically
and stays in context the whole time, so it holds the things that are true for all
work in this repo — and nothing else. Anything needed only sometimes belongs in a
skill (`.claude/skills/`), not here.

## What this repo is

Learning QA automation one tool at a time. One folder per tool. The Robot
Framework work is a separate, finished repo: `robot-framework-learning`.

The plan is `LEARNING-PLAN.md`. **Read it before proposing what to work on
next.** The order is deliberate and has been re-argued twice. If something
outside the current block looks more urgent or more concrete, say so and let me
decide — do not start it.

This repo and `robot-framework-learning` are both public. Do not make anything
else public without asking.

## How work is delivered here

- **The write-up is the deliverable, not the code.** A folder with a working
  collection and no README explaining what the tool does differently is half a
  block. This is a learning repo; the reasoning is the product.
- **Verify before writing it down.** If a number goes into a README it came from
  a run, not an estimate. If something could not be verified, the text says so.
- **Say plainly when something is not done**, or was skipped, or failed. A block
  reported as finished with a broken part in it is worse than an unfinished one.

## Writing style

- Explain **why**, not what. "Pinned the dependencies" is a changelog; "pinned
  them because an unpinned CI can go red with no change to any file" is the part
  worth reading in six months.
- Record mistakes and why they were mistakes. The most useful paragraphs in the
  Robot repo are the ones admitting a test checked the wrong thing.
- No marketing voice. No "seamlessly". No exclamation marks.
- Never put someone's name or private message into a file here without asking me
  first.

## Git

- Commit messages explain the reasoning. The diff already shows the what.
- **Branches and pull requests are block 2 and are not yet habit.** Until then,
  ask before pushing to `main`.
- Never force-push. Never rewrite published history.

## Ask first

- Making anything public
- Creating repositories, changing repository settings, adding or removing
  collaborators
- Installing tools on this machine
