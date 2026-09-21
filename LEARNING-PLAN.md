# Learning Plan

My plan for what to learn after Robot Framework, and in what order.

The order was reworked after a working QA engineer read the Robot repo and told
me what he would change. I have kept his conclusions and dropped his name: the
advice came in a private message, and it is not mine to publish. The reasoning
is written out below, because a plan without its reasoning is a plan I cannot
argue with in six months.

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

In demand right now, and it compounds: every block below goes faster once this
one is real.

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

The logic of it, and the actual practicality: not what a commit is, but what a
working day with branches and reviews in it looks like.

- [ ] **Commands** — the everyday set, and what each one really does
- [ ] **Working with multiple branches**
- [ ] **Multiple PRs** — several small pull requests rather than one large one
- [ ] **Requesting code reviews, human and non-human**, in GitHub
- [ ] Resolve a conflict on purpose, before one happens for real

Worth knowing before starting: nothing in either repo has ever been through a
branch or a pull request, and `main` is unprotected in both.

## 3. GitHub Actions — CI/CD workflows

YML files, their structure and their logic.

- [ ] **YML structure and logic** — triggers, jobs, steps, conditions, secrets
- [ ] **`paths:` filters** — one repo, several tools: a Postman change must not
      start another tool's workflow
- [ ] **A workflow that gates a pull request** — required checks
- [ ] **Artifacts and reports**
- [ ] **Dependency updates** — `dependabot.yml`, which pairs exactly with the
      version pinning done on the last day of the Robot repo: pinning bought
      reproducibility at the cost of upgrades no longer being free, and
      dependabot is what pays that cost back

There is a worked example already waiting: the open pull request on the Robot
repo — 9 files, workflows split one per trigger, `dependabot.yml`, a Robot
linter and a `gitleaks` secret scan. Read it as an example here; reviewing and
merging it is block 2's work, not this one's.

## 4. Postman + Newman (+ htmlextra)

Kept in proportion, on a warning worth recording: it is genuinely fun, it helps
in interviews — and the person who told me so has never once used it in a
real-life scenario. Learn it, be able to demo it, do not build an
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

**Selenium is out** — on the recommendation of someone who used it for years,
watched it plateau, and moved to Cypress and Playwright. No reason to learn a
tool in the state he left it in.

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

Extremely fun and engaging, well paid, and very hard to get into: getting a
pentester role takes connections, the certifications are expensive, and the
pipeline targets students. Not worth maxing out. Worth having because QA is a
jack-of-all-trades role. Shallow on purpose.

- [ ] OWASP Top 10, at a reading level
- [ ] Secret scanning — `gitleaks`, already written in that open PR
- [ ] An OWASP ZAP baseline scan against a demo application
- [ ] (Already started: the path-traversal test written on Day 29)

## 8. The rest

- [ ] **k6** — a first load test, thresholds, a report
- [ ] **Docker** — the suites running somewhere that is not my laptop

**Networking is not in this plan.** Interesting at the surface, boring deep,
and it plateaus in both knowledge and salary, with a lot of low-level work.

## Housekeeping

Not learning, but all three are real.

- [ ] **The GitHub profile is empty** — no photo, no details, no public repos.
      Worth fixing: people do find you that way and write to you
- [ ] **Decide what goes public, and when.** Both repos are private today

## How to use this plan

Experiment, see what I enjoy, check whether the market is asking for it, and
then forge in that direction — skills, frameworks, knowledge.

A starting order, not a commitment. A block that turns out to be dull, or dead
in the market, is a block to cut — and cutting it is a result.

## Resources

In English, because that is where the material is. The rule is watch the first
hour, then build.

**Postman**
- [Postman Beginner's Course — API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4)
  — freeCodeCamp. Recommended by someone who learned Postman from this exact
  one, in the strongest terms
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
