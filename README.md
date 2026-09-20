# QA Portfolio

Learning test automation in public, one tool at a time.

**The Robot Framework part has a repo of its own:
[robot-framework-learning](https://github.com/nicoletalucia/robot-framework-learning)**
— 30 days, 189 tests, a stub server and a local site so none of it touches the
network. It is the longest piece of this and the best place to start reading.

This repo is everything after that. The plan it follows is
[`LEARNING-PLAN.md`](LEARNING-PLAN.md).

## What is here

| Folder | What it covers | State |
|---|---|---|
| [`postman/`](postman/) | P1 — a collection over the same API the Robot suites use | done |

Nothing else yet. The table grows as the plan does, and an empty row is more
honest than a folder with a placeholder in it.

## Why one repo and not one per tool

Five repos with four commits each read as five abandoned projects. Progression
is the thing worth showing, and progression needs somewhere to accumulate: the
test plan written in P8 is about the same application P5 automates, and that
connection only exists if they share a repo.

Robot stays separate for the opposite reason — it is finished, and it reads as
one thing. Nested under a folder here it would stop reading as one thing.

## Running any of it

Each folder has its own README with its own command. There is no top-level
runner, on purpose: a Postman collection and a pytest suite have nothing to
share but a repo, and pretending otherwise means writing a script whose only
job is to hide which tool is running.
