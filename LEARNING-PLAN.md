# Learning Plan — beyond Robot Framework

The Robot repo covers one tool deeply. This plan covers the rest of the craft:
the tools I have not touched yet, and the half of testing that never shows up
in a test suite at all.

Numbered `P1, P2, …` so these never get confused with the Robot days. **The
numbers are labels, not an order** — the sections below are in the order I am
doing them, and P8–P10 has moved up. The reason is written into its own section,
and it is the plan's own argument: it is the part that changes how I think
rather than what I can operate, and *last in the list means first to be dropped*.

## Where I am

| Area | Where it stands |
|---|---|
| Framework design & maintenance | done — resources, page objects, listeners, pabot |
| API testing | done — RequestsLibrary, stub server, contracts, DB checks |
| Python | done — eight modules: two listeners, two servers, four helper libraries |
| CI | done — GitHub Actions, three run paths, a nightly job |
| Test isolation | done — 189 tests, none of them touching the network |
| A second API tool | P1 done — Postman + newman |
| **Test design on paper** | missing — everything so far is automation, nothing is a written test |
| **A second automation stack** | missing — one tool deeply is not the same as knowing the trade-offs |
| Performance testing | missing |
| Security testing | missing |
| Containers | missing |

## P1–P2 — Postman + Newman

The cheapest thing on the list: the practice already exists in the Robot repo's
`tests/api/`, only the tool is new. Worth doing because a GUI client makes
different mistakes easy than a code client does — which `postman/README.md`
writes up, and that write-up is the actual deliverable.

- [x] P1 — a collection over the same public API: environments, variables,
  assertions in the Tests tab, pre-request scripts
- [ ] P2 — `newman` running it in GitHub Actions, with a `paths:` filter so a
  change here does not start every other tool's workflow

## P8–P10 — test design on paper

Moved up to second, ahead of a whole block of Selenium, because the argument for
doing it early is stronger than the argument for doing more automation. Thirty
days and 189 tests answer *does this work*. None of them answer **what should be
tested, and why that and not something else** — and no third framework is going
to start answering it.

- [ ] P8 — a test plan for one application under test: scope, risk, entry and
  exit criteria
- [ ] P9 — formal test cases, and one good bug report: steps, expected, actual,
  severity
- [ ] P10 — traceability matrix, and a smoke/regression tag strategy (pairs
  directly with Robot Day 23, which enforced one in code without ever writing
  one down)

## P3–P7 — Selenium + pytest

Python is already known, so only the tool changes — which is exactly what makes
it useful: the same test, written twice, shows what belongs to the tool and what
belongs to testing. pytest comes along for free.

- [ ] P3 — driver setup, explicit waits, first test
- [ ] P4 — locators and a Page Object as a Python class
- [ ] P5 — `conftest.py`, fixtures, parametrize (setup/teardown and templates
  again, in a different dialect)
- [ ] P6 — screenshot on failure, pytest-html, parallel runs with `pytest-xdist`
- [ ] P7 — port three web tests from the Browser library and write up where the
  two approaches differ. This is the one that pays for the block

## P11–P16 — JavaScript + Cypress

Breadth, and the first block where returns start diminishing: after Playwright
and Selenium, Cypress is a third way to do the same job. If time runs short,
this is the block to cut — not P17–P20, which at least cover things nothing
else here does.

- [ ] P11–P12 — the JavaScript that is actually needed: `const/let`, arrow
  functions, promises/async, npm
- [ ] P13 — first Cypress test, commands and assertions
- [ ] P14 — `cy.intercept()` and fixtures (stubbing again — same idea as Robot
  Day 21)
- [ ] P15 — custom commands, page objects in Cypress
- [ ] P16 — Cypress in CI, with video and screenshot artefacts

## P17–P20 — nice-to-have

- [ ] P17–P18 — k6: a first load test, thresholds, a report
- [ ] P19 — OWASP ZAP baseline scan against a demo application
- [ ] P20 — the suites running in Docker, so they do not depend on my machine

## Resources

In English, because that is where the material is.

Not endorsements of the whole runtime: the rule is watch the first hour, then
build. The Robot repo was not learned by watching.

**Postman (P1–P2)**
- [Postman Beginner's Course — API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4) — freeCodeCamp, the main one
- [Learn Postman for API Testing (Step-by-Step)](https://www.youtube.com/watch?v=wEOLZq-7DYs) — shorter alternative
- [API Testing Using Postman — Full Course in 5 hours](https://www.youtube.com/watch?v=CGX6DRNfS-E) — reference, not a sitting

**Process and writing (P8–P10)**
- [Manual QA: Testing for Beginners — How to file a bug report](https://www.youtube.com/watch?v=7cDzjS6z5ks)
- [Manual QA: Testing for Beginners — Managing Test Cases and QA Docs](https://www.youtube.com/watch?v=tS5vq4DqJgE)
- [How to Write a Good Defect Report](https://www.youtube.com/watch?v=rTmEUiWwgLs)

**Selenium + pytest (P3–P7)**
- [PyTest Tutorial — Learn PyTest in 90 minutes](https://www.youtube.com/watch?v=UzkuOACmBpA) — start here, pytest alone
- [Pytest Selenium Python Hybrid Framework with Page Object Model](https://www.youtube.com/watch?v=8V3uP77o7kQ) — the POM part, for P4–P6
- [Selenium With Python and PyTest — Free Full Course](https://www.youtube.com/playlist?list=PL63jFO_mmwQ0u6iiEN56JsgjTLRuEa30D) — playlist, dip in as needed

**Cypress (P11–P16, later)**
- [Learn Cypress End-to-End Testing From Scratch — 2.5h](https://www.youtube.com/watch?v=AnyKTiC3P1M)
- [Testing JavaScript with Cypress — Full Course](https://www.youtube.com/watch?v=u8vMu7viCm8) — freeCodeCamp
