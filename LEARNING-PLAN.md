# Learning Plan

Rewritten after a review from a colleague,
a working QA engineer who read the Robot repo and said what he would change. The
order below is his; the reasons are kept where he gave them, because a plan
whose reasoning is missing is a plan nobody can argue with later.

**The `P1, P2, …` numbers are gone.** They were reordered twice in a week and
had stopped meaning anything — the second reorder needed a line explaining that
the numbers were not an order, which is the point at which numbering is costing
more than it pays. Blocks are named, and the order is top to bottom.

## What changed in this rewrite

| Change | Why |
|---|---|
| **AI as a working tool** added, first | "cerute extrem de mult acum" |
| **Git + GitHub** added, second | Practical branch/PR/review work. Everything in both repos so far went straight to `main` |
| **GitHub Actions** raised to third | Already half-built in the Robot repo; the gap is the PR-shaped half |
| **Selenium removed entirely** | "depășit tare, old". The reviewer used it, hit a ceiling, moved to Cypress and Playwright |
| **Playwright + Cypress** replace it | And Playwright is not a new tool here — see the block |
| **Postman right-sized** | Kept, with his caveat: fun, good in interviews, and he has never used it in a real-life scenario |
| **Cybersecurity → nice-to-have, shallow on purpose** | Fun and well paid, very hard to get into, expensive certifications. Worth having as breadth, not worth maxing |
| **Networking dropped** | His read: interesting shallow, boring deep, low ceiling and a lot of low-level work |

## Where I am

| Area | Where it stands |
|---|---|
| Framework design & maintenance | done — resources, page objects, listeners, pabot |
| API testing | done — RequestsLibrary, stub server, contracts, DB checks |
| Python | done — eight modules: two listeners, two servers, four helper libraries |
| Test isolation | done — 189 tests, none of them touching the network |
| CI | **half** — three run paths and a nightly job, but never exercised through a pull request |
| Git beyond `commit` + `push` | **missing** — no branch I made, no PR I opened, no review I gave |
| AI as a working tool | **missing** as a written-down skill |
| Test design on paper | **missing** — everything so far is automation, nothing is a written test |
| A second browser stack | **missing** — though less missing than it looks |
| Performance, containers, security | missing |

---

## 1. AI as a working tool

First because it is what the market is asking for right now, and because it
compounds: every block below gets faster if this one is real.

Not "how to ask a chatbot things". The parts that hold up under work:

- [ ] **Context** — what a model can and cannot see, why a long session degrades,
      what to put in a prompt versus a file versus a repo
- [ ] **Skills and instructions** — reusable setup instead of retyping. A
      `CLAUDE.md`, a project instruction file, a saved prompt that encodes how I
      want work done
- [ ] **Constructive limitations** — the useful half. Where output is confidently
      wrong, what has to be verified, which tasks are worth delegating and which
      cost more to check than to do
- [ ] **Flow automation** — the repetitive parts of the job: generating test data,
      first-draft test cases from an acceptance criterion, reading a failing
      log, drafting a bug report from a session
- [ ] **Write it up.** The deliverable is a document in this repo, not a feeling.
      What worked, what produced confident nonsense, what I now always check

## 2. Git and GitHub, for real

The honest gap. Thirty days of Robot and every single commit went straight to
`main`. No branch, no pull request, no review — which means the part of the
workflow every team actually runs on is the part with zero practice behind it.

The material is already there and waiting: **The reviewer has an open pull request on
the Robot repo** — `improve_overall`, 9 files, +267 lines. Reviewing it is the
first exercise, not a chore to clear.

- [ ] **Branches** — create, switch, rebase vs merge, what a fast-forward is and
      when it is a lie
- [ ] **Pull requests** — open one for a real change. Several small ones beat one
      large one, and finding that out by living with a large one is the lesson
- [ ] **Review the open PR properly.** It is a good exercise precisely because it
      is not all correct — see the notes below
- [ ] **Request reviews, human and non-human** — and read what the automated ones
      get wrong, which is the more useful half
- [ ] **Branch protection on `main`** — neither repo has it. Currently nothing
      stops a push straight to main, including mine
- [ ] Resolve conflicts on purpose, at least once, before one happens for real

### Notes for reviewing that PR

Written down because "review a PR" is advice and this is practice.

`dependabot.yml` is the strongest thing in it, and it pairs exactly with the
dependency pinning done on the last day of the Robot repo: pinning bought
reproducibility at the cost of upgrades no longer being free, and dependabot is
the thing that pays that cost back by opening a PR per bump.

`scripts/run_gitleaks.py` scans for committed secrets. That is the cybersecurity
block's "minimal addition", already written and already in the repo.

`on-pr.yml` is where the review gets interesting, and it should **not** be merged
as-is:

- it runs on `pull_request` and so does the existing `tests.yml` — the suite
  would run twice per PR
- it has no `rfbrowser init`, so every web test would fail on a clean runner
- it runs all of `tests/`, where the existing PR path deliberately runs
  `--include smoke` for fast feedback
- it pins Python 3.11; the existing workflow uses 3.12
- no pabot, no listeners, no `--skiponfailure quarantine`

None of that makes the PR bad. It makes it a real pull request, which is the
only kind worth practising on. There is also a genuine design disagreement in
it — he splits CI into one file per trigger, the Robot README argues for one
file with three steps because *the thing a workflow most needs to be is readable
at a glance*. That disagreement is worth having in the PR comments rather than
silently resolving by merging or closing.

## 3. GitHub Actions and CI/CD

Third because it is already half-done and the missing half is the half block 2
unlocks.

- [ ] **YML structure and logic** — triggers, jobs, steps, `needs`, conditions,
      matrices, secrets
- [ ] **`paths:` filters** — one repo, several tools: a Postman change must not
      start a pytest workflow
- [ ] **A workflow that gates a PR** — required checks, so the review is enforced
      rather than optional
- [ ] **Artifacts and reports** — already done in the Robot repo; redo it here
      for newman with `htmlextra`
- [ ] **Caching** — also already done (Playwright browsers keyed on a pinned
      `requirements.txt`) and worth being able to explain rather than copy

## 4. Postman + Newman + htmlextra

Kept, and kept in proportion. The reviewer's verdict is worth recording verbatim
because it is the kind of thing nobody tells you: *extrem de fun, m-a ajutat prin
interviuri, dar nu am folosit niciodată într-un real-life scenario.* Learn it,
be able to demo it, do not build an identity on it.

- [x] A collection over a public API: environments, variables, assertions in the
      Tests tab, pre-request scripts → [`postman/`](postman/)
- [ ] **newman in GitHub Actions**, with a `paths:` filter
- [ ] **htmlextra** — a readable HTML report as a CI artifact
- [ ] One honest paragraph on where a GUI client beats a code client and where it
      does not

## 5. Test design on paper

The block that changes how I think rather than what I can operate. Thirty days
and 189 tests answer *does this work*. None of them answer **what should be
tested, and why that and not something else** — and no further framework is
going to start answering it.

Kept high on purpose. Last in a list means first to be dropped.

- [ ] A test plan for one application: scope, risk, entry and exit criteria
- [ ] Formal test cases, and one genuinely good bug report — steps, expected,
      actual, severity
- [ ] A traceability matrix, and a smoke/regression tag strategy written down
      (the Robot repo enforces one in code without ever having written one out)

## 6. Playwright and Cypress

Selenium is not here. The reviewer used it, felt it plateau, and moved on; there is
no reason to learn a tool in the state he left it in.

**Playwright is cheaper than it looks.** Robot's Browser library *is* Playwright
underneath — the auto-waiting, the selector engine, `>>>` for frames,
`Promise To` / `Wait For` for dialogs are all Playwright concepts already used
for thirty days. What changes is the dialect, not the model.

- [ ] **Playwright** in TypeScript: locators, fixtures, `expect`, trace viewer
- [ ] Port three web tests from the Robot repo and write up what moved and what
      did not — the write-up is the deliverable
- [ ] **JavaScript that is actually needed first**: `const`/`let`, arrow
      functions, promises and `async`, npm
- [ ] **Cypress**: commands, assertions, `cy.intercept()` and fixtures (stubbing
      again — the same idea as the Robot stub server), custom commands, CI with
      video and screenshots
- [ ] +/- **Puppeteer**, if there is time. Browser automation rather than a test
      framework, and worth knowing exists

## 7. Nice to have

- [ ] **Cybersecurity, deliberately shallow.** Fun, well paid, and very hard to
      get into — expensive certifications, and the pipeline targets students.
      Not worth maxing out. Worth having because QA is a jack-of-all-trades role:
      OWASP Top 10, a ZAP baseline scan, secret scanning (already started by that
      PR), and the path-traversal test already written on Day 29
- [ ] **k6** — a first load test, thresholds, a report
- [ ] **Docker** — the suites running somewhere that is not my laptop

## Housekeeping

Not learning, but the reviewer raised both and both are real.

- [ ] **The GitHub profile is empty** — no photo, no details, no public repos.
      His point, from experience: people do find you that way and write to you.
      Nothing here is public yet, so there is nothing to find
- [ ] **Decide what goes public, and when.** Both repos are private today

## How to use this plan

The reviewer's closing advice, and the most useful line in the whole review:

> experimentează, vezi ce-ți place, vezi dacă se caută în piață, și forjează în
> partea aia.

The plan is a starting order, not a commitment. A block that turns out to be
dull or dead in the market is a block to cut, and cutting it is a result, not a
failure.

## Resources

In English, because that is where the material is. The rule is watch the first
hour, then build — the Robot repo was not learned by watching.

**Postman**
- [Postman Beginner's Course — API Testing](https://www.youtube.com/watch?v=VywxIQ2ZXw4)
  — freeCodeCamp. The reviewer learned from this exact one and calls it GOD-tier
- [Learn Postman for API Testing (Step-by-Step)](https://www.youtube.com/watch?v=wEOLZq-7DYs) — shorter alternative

**Process and writing**
- [Manual QA: How to file a bug report](https://www.youtube.com/watch?v=7cDzjS6z5ks)
- [Manual QA: Managing Test Cases and QA Docs](https://www.youtube.com/watch?v=tS5vq4DqJgE)
- [How to Write a Good Defect Report](https://www.youtube.com/watch?v=rTmEUiWwgLs)

**Cypress**
- [Learn Cypress End-to-End Testing From Scratch — 2.5h](https://www.youtube.com/watch?v=AnyKTiC3P1M)
- [Testing JavaScript with Cypress — Full Course](https://www.youtube.com/watch?v=u8vMu7viCm8) — freeCodeCamp

**Playwright and Git** — not filled in yet. Left empty rather than padded with
links nobody has watched.
