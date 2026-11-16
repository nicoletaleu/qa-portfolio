# QA Portfolio

Learning test automation in public, one tool at a time.

**The Robot Framework part has a repo of its own:
[robot-framework-learning](https://github.com/nicoletaleu/robot-framework-learning)**
— 30 days, 189 tests, a stub server and a local site so none of it touches the
network. It is the longest piece of this and the best place to start reading.

**Playwright has one too:
[playwright-typescript-tests](https://github.com/nicoletaleu/playwright-typescript-tests)**
— three of the Robot web suites ported to Playwright and TypeScript, against
the same local site, with a write-up of what changed between the two tools.

This repo is the plan both of them came out of, and the work that is smaller
or still moving. The plan is [`LEARNING-PLAN.md`](LEARNING-PLAN.md).

## What is here

| Where | What it covers | State |
|---|---|---|
| [`ai/`](ai/) | Using AI on QA work — reusable instructions, a skill, and an honest record | in progress |
| [`postman/`](postman/) | A collection over the same API the Robot suites use, run by newman in CI | done |
| [playwright-typescript-tests](https://github.com/nicoletaleu/playwright-typescript-tests) | Robot suites 13-15 ported to Playwright + TypeScript | done, own repo |

## Built with

| Part | Tools |
|---|---|
| `postman/` | Postman, tests in JavaScript (`pm.test`, `pm.expect`); newman in GitHub Actions, htmlextra and JUnit reports |
| `ai/` | Claude Code: `CLAUDE.md` and skills written in Markdown, plus a small Python script and a Robot Framework file for test data |
| CI | GitHub Actions, one workflow per tool, each started only by changes to its own folder (`paths:` filters) |
| Playwright | in its own repo: Playwright Test, TypeScript, Node.js |

## Where each tool lives

This section used to say every new tool would live here, in one repo, because
five repos with four commits each read as five abandoned projects. That is
still true of small pieces, which is why Postman and the AI work are folders.

What changed the rule is that a finished port reads as one thing, the way the
Robot repo does. The Playwright work has its own README, its own CI and its
own site, and someone looking for Playwright on a profile should find it by
name rather than inside a folder of a repo called something else. So: a tool
gets its own repo once it is a finished, self-contained project; until then
it is a folder here.

## Running any of it

Each folder has its own README with its own command. There is no top-level
runner, on purpose: a Postman collection and a Playwright suite have nothing to
share but a repo, and pretending otherwise means writing a script whose only
job is to hide which tool is running.
