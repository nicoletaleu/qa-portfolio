# Learning Plan

The order below is a colleague's. He is
a working QA engineer, he read the Robot repo, and he said what he would learn
and in what order. His three additions come first; everything after them is what
this plan already had, with his cuts and corrections applied.

His reasons are kept in his words where he gave them. A plan without its
reasoning is a plan nobody can argue with later.

## Where I am

| Area | Where it stands |
|---|---|
| Framework design & maintenance | done — resources, page objects, listeners, pabot |
| API testing | done — RequestsLibrary, stub server, contracts, DB checks |
| Python | done — eight modules: two listeners, two servers, four helper libraries |
| Test isolation | done — 189 tests, none of them touching the network |
| CI | half — three run paths and a nightly job, never exercised through a pull request |
| Git beyond `commit` and `push` | missing — every commit in both repos went straight to `main` |
| AI as a working tool | missing as a written-down skill |
| Test design on paper | missing — everything so far is automation, nothing is a written test |
| A second browser stack | missing |
| Performance, containers, security | missing |

---

## 1. Prompt engineering + using AI at an advanced level

> sunt cerute extrem de mult acum

- [ ] **Skills** — reusable instructions instead of retyping context every session
- [ ] **Context** — what a model can and cannot see, why a long session degrades,
      what belongs in a prompt versus a file versus a repo
- [ ] **Constructive limitations** — where the output is confidently wrong, what
      always has to be verified, which tasks cost more to check than to do
- [ ] **Flow automation** — the repetitive parts of the job: test data, a first
      draft of test cases from an acceptance criterion, reading a failing log,
      drafting a bug report from a session
- [ ] Write down what actually worked and what did not, from real sessions

## 2. Git + GitHub — the practical side

> logic, the actual practicality of it

- [ ] **Commands** — the everyday set, and what each one really does
- [ ] **Working with multiple branches**
- [ ] **Multiple PRs** — several small pull requests rather than one large one
- [ ] **Requesting code reviews, human and non-human**, in GitHub
- [ ] Resolve a conflict on purpose, before one happens for real

Worth knowing before starting: nothing in either repo has ever been through a
branch or a pull request, and `main` is unprotected in both.

## 3. GitHub Actions — CI/CD workflows

> YML files, structure & logic

- [ ] **YML structure and logic** — triggers, jobs, steps, conditions, secrets
- [ ] **`paths:` filters** — one repo, several tools: a Postman change must not
      start another tool's workflow
- [ ] **A workflow that gates a pull request** — required checks
- [ ] **Artifacts and reports**
- [ ] **Dependency updates** — `dependabot.yml`, which pairs exactly with the
      version pinning done on the last day of the Robot repo: pinning bought
      reproducibility at the cost of upgrades no longer being free, and
      dependabot is what pays that cost back

The worked example the reviewer pointed at is his own pull request on the Robot repo:
[`robot-framework-learning` PR #1](https://github.com/nicoletalucia/robot-framework-learning/pull/1/files)
— 9 files, split workflows per trigger, `dependabot.yml`, a Robot linter and a
`gitleaks` secret scan. Read it as the example he meant it to be; reviewing and
merging it is block 2's work, not this one's.

## 4. Postman + Newman (+ htmlextra)

> mi s-a părut extrem de fun, dar doar m-am jucat pentru mine cu treaba asta…
> m-a ajutat prin interviuri… dar nu am folosit niciodată în real-life-scenario

Kept, and kept in proportion. Learn it, be able to demo it, do not build an
identity on it.

- [x] A collection over a public API: environments, variables, assertions in the
      Tests tab, pre-request scripts → [`postman/`](postman/)
- [ ] **newman** in GitHub Actions
- [ ] **htmlextra** — a readable HTML report as a CI artifact

## 5. Test design on paper

Everything built so far answers *does this work*. Nothing yet answers **what
should be tested, and why that and not something else**.

- [ ] A test plan for one application: scope, risk, entry and exit criteria
- [ ] Formal test cases, and one genuinely good bug report — steps, expected,
      actual, severity
- [ ] A traceability matrix, and a smoke/regression tag strategy written down
      (the Robot repo enforces one in code without ever having written one out)

## 6. Newer frameworks: Playwright, Cypress, +/- Puppeteer

**Selenium is out.** The reviewer's call, and his own history behind it: he liked it,
felt it plateau, and moved to Cypress and Playwright. There is no reason to
learn a tool in the state he left it in.

One thing worth knowing before starting: **Playwright is cheaper than it looks.**
Robot's Browser library *is* Playwright underneath, so the auto-waiting, the
selector engine, `>>>` for frames and the promise-based dialog handling are all
concepts already used for thirty days. What changes is the dialect.

- [ ] **The JavaScript that is actually needed first** — `const`/`let`, arrow
      functions, promises and `async`, npm
- [ ] **Playwright** — locators, fixtures, `expect`, trace viewer
- [ ] Port three web tests from the Robot repo and write up what moved and what
      did not
- [ ] **Cypress** — commands, assertions, `cy.intercept()` and fixtures (stubbing
      again, the same idea as the Robot stub server), custom commands, CI with
      video and screenshots
- [ ] **+/- Puppeteer** — a browser automation library rather than a test
      framework. Worth knowing it exists

## 7. Cybersecurity — nice to have, not mandatory

> greu tare de ajuns pe post de Pentester or similar (nevoie de pile); nu merită
> super-aprofundat, maxat pe skill-ul ăsta, însă e fain ca minimă adiție pentru
> că noi suntem jack-of-all-trades

Extremely fun and engaging, well paid, and very hard to get into — expensive
certifications, and the pipeline targets students. Shallow on purpose.

- [ ] OWASP Top 10, at a reading level
- [ ] Secret scanning — `gitleaks`, already written in that PR
- [ ] An OWASP ZAP baseline scan against a demo application
- [ ] (Already started: the path-traversal test written on Day 29)

## 8. The rest

- [ ] **k6** — a first load test, thresholds, a report
- [ ] **Docker** — the suites running somewhere that is not my laptop

**Networking is not in this plan.** The reviewer's read: interesting at the surface,
boring deep, and it plateaus in both knowledge and salary, with a lot of
low-level work.

## Housekeeping

Not learning, but he raised both and both are real.

- [ ] **The GitHub profile is empty** — no photo, no details, no public repos.
      His point, from experience: people do find you that way and write to you
- [ ] **Decide what goes public, and when.** Both repos are private today

## How to use this plan

> recomand să experimentezi, să vezi ce-ți place, să vezi dacă se caută în piață,
> și să forjezi în acea parte (skills, frameworks, knowledge)

A starting order, not a commitment. A block that turns out to be dull, or dead
in the market, is a block to cut — and cutting it is a result.

## Resources

In English, because that is where the material is. The rule is watch the first
hour, then build.

**Postman**
- [Postman Beginner's Course — API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4)
  — freeCodeCamp. The reviewer learned Postman from this exact one: *GOD-tier*
- [Learn Postman for API Testing (Step-by-Step)](https://www.youtube.com/watch?v=wEOLZq-7DYs) — shorter alternative

**Process and writing**
- [Manual QA: How to file a bug report](https://www.youtube.com/watch?v=7cDzjS6z5ks)
- [Manual QA: Managing Test Cases and QA Docs](https://www.youtube.com/watch?v=tS5vq4DqJgE)
- [How to Write a Good Defect Report](https://www.youtube.com/watch?v=rTmEUiWwgLs)

**Cypress**
- [Learn Cypress End-to-End Testing From Scratch — 2.5h](https://www.youtube.com/watch?v=AnyKTiC3P1M)
- [Testing JavaScript with Cypress — Full Course](https://www.youtube.com/watch?v=u8vMu7viCm8) — freeCodeCamp

**AI, Git and Playwright** — not filled in yet. Left empty rather than padded
with links nobody has watched.
