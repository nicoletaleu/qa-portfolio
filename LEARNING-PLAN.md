# Learning Plan

My plan for what to learn after Robot Framework, and in what order.

The list and its order come from a working QA engineer who read the Robot repo
and told me what he would learn in my place. I have kept his conclusions and
dropped his name: the advice came in a private message, and it is not mine to
publish.

An earlier version mixed his list with blocks from my own first plan — test
design on paper, k6, Docker — and in doing so moved Postman ahead of
Playwright, against his order. Those blocks are gone. If one of them earns its
way back, it comes back as a decision written down here, not as something left
over.

## Where I am

| Area | Where it stands |
|---|---|
| Framework design, API testing, Python, test isolation | done — the Robot repo, 189 tests, none of them touching the network |
| AI as a working tool | in progress — block 1 |
| Git beyond `commit` and `push` | started — three pull requests of my own, but most work still goes straight to `main` |
| CI | half — three run paths and a nightly job in the Robot repo, running on pull requests too; no required checks yet |
| A modern browser stack | missing — Robot's Browser library is Playwright underneath, but never used directly |
| Postman | done — a collection, run by newman in CI with an htmlextra report |
| Security | one test — the path-traversal check from the Robot repo |

---

## 1. Prompt engineering + using AI at an advanced level

In demand right now, and it compounds: every block below goes faster once this
one is real.

Work lives in [`ai/`](ai/).

- [x] **Skills** — reusable instructions instead of retyping context every
      session: `CLAUDE.md` for what is always true, `.claude/skills/bug-report/`
      for what is only sometimes needed
- [x] **Context** — what belongs in a prompt versus a file versus a repo, and
      why a long session degrades. Written up in [`ai/`](ai/)
- [ ] **Constructive limitations** — started. A running record of real
      failures, with the rule each one produced. Stays open: this is a record,
      not a task that finishes
- [x] **Flow automation** — the repetitive parts of the job: test data, a first
      draft of test cases from an acceptance criterion, reading a failing log,
      bug reports. A skill for each, each used once on real material →
      [`ai/flow-automation/`](ai/flow-automation/)

## 2. Git + GitHub — the practical side

The logic of it, and the actual practicality: not what a commit is, but what a
working day with branches and reviews in it looks like.

- [ ] **Commands** — the everyday set, and what each one really does. Started on
      what came up rather than on a list: `fetch`, `merge-base`, `cherry-pick`,
      `branch`, `remote prune`, `ls-remote`, `merge-tree` to test a merge
      without doing it
- [x] **Working with multiple branches** — four branches across the two repos,
      one of them rebuilt from scratch after a mangled commit message
- [x] **Multiple PRs** — three of my own, two in `qa-portfolio` and one in the
      Robot repo, plus the eight dependabot opened
- [ ] **Requesting code reviews, human and non-human**, in GitHub
- [ ] Resolve a conflict on purpose, before one happens for real

When this block started, nothing in either repo had been through a branch or a
pull request. `main` is still unprotected in both. From this block on, nothing
goes straight to `main`.

**Where this stands.** The two items still open are the two that need another
person or a deliberate setup:

- **Reviews.** A colleague opened a pull request on the Robot repo, and I wrote
  a full review of it. It found real things: the branch was cut before the repo
  had any CI, so merging it would have added a second workflow that goes red on
  every pull request. The review was never posted. Its three usable ideas were
  taken into a pull request of my own instead. The original pull request stays
  in a private copy of the repo, because it is his work, not mine to publish.
- **A conflict on purpose.** A real one sits in that pull request, in
  `.gitignore`. It has not been resolved, because resolving it means touching
  somebody else's branch. It needs a setup of my own.

What did get exercised, and was not planned: reviewing eight dependency updates
and noticing that a green pull request is weak evidence here, because a pull
request runs the smoke set only. All eight were re-run against the whole suite
before merging.

## 3. GitHub Actions — CI/CD workflows

YML files, their structure and their logic.

- [ ] **YML structure and logic** — triggers, jobs, steps, conditions, secrets
- [ ] **`paths:` filters** — one repo, several tools: a Postman change must not
      start another tool's workflow
- [ ] **A workflow that gates a pull request** — required checks
- [ ] **Artifacts and reports**
- [ ] **Dependency updates** — `dependabot.yml`, which pays back the cost of the
      version pinning done at the end of the Robot repo: pinning bought
      reproducibility, and upgrades stopped being free

The worked example is the Robot repo's own
[`tests.yml`](https://github.com/nicoletaleu/robot-framework-learning/blob/main/.github/workflows/tests.yml):
the smoke set on pull requests, a dry run of every suite, a `gitleaks` secret
scan, and `dependabot.yml` next to it. The colleague's review also proposed
splitting it into one workflow per trigger. That idea is not taken yet.

## 4. Newer frameworks: Playwright, Cypress, +/- Puppeteer

**Selenium is out entirely** — on the advice of someone who used it for years,
watched it plateau and fall behind, and moved to Cypress and Playwright.

**Playwright is cheaper than it looks.** Robot's Browser library *is* Playwright
underneath, so auto-waiting, the selector engine and the dialog handling are
concepts already used for thirty days. What changes is the language.

- [ ] **The JavaScript that is actually needed** — `const`/`let`, arrow
      functions, promises and `async`, npm
- [ ] **Playwright** — locators, fixtures, `expect`, trace viewer
- [ ] Port three web tests from the Robot repo and write up what moved and what
      did not
- [ ] **Cypress** — commands, assertions, `cy.intercept()` and fixtures, custom
      commands, CI with video and screenshots
- [ ] **+/- Puppeteer** — a browser automation library rather than a test
      framework. Worth knowing it exists and what it is for

## 5. Postman + Newman (+ htmlextra)

Kept in proportion, and the reason is worth recording: it is genuinely fun and
it helps in interviews, but a job that is mostly API testing can hold you back.
Learn it,
be able to demo it, do not build an identity on it.

- [x] A collection over a public API: environments, variables, assertions in the
      Tests tab, pre-request scripts → [`postman/`](postman/)
- [x] **newman** from the command line and in GitHub Actions →
      [`postman.yml`](.github/workflows/postman.yml)
- [x] **htmlextra** — a readable HTML report, uploaded as a CI artifact

## 6. Cybersecurity — nice to have, not mandatory

Extremely fun and engaging, well paid, and very hard to get into: expensive
certifications, entry through connections, and a pipeline aimed at students.
Not worth maxing out. Worth a minimal addition, because QA is a
jack-of-all-trades role. Shallow on purpose.

- [ ] OWASP Top 10, at a reading level
- [ ] Secret scanning — `gitleaks`, already running in the Robot repo's CI
- [ ] (Already started: the path-traversal test in the Robot repo)

---

## Not in this plan

**Selenium** — plateaued and fell behind. See block 4.

**Networking** — interesting at the surface, boring deep, and it plateaus in
both knowledge and salary, with a lot of low-level work.

## Housekeeping

Not learning, but real.

- [ ] **The GitHub profile is empty** — no photo, no details, no public repos.
      Worth fixing: people do find you that way and write to you
- [x] **Decide what goes public, and when.** Both repos are public

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

**Cypress**
- [Learn Cypress End-to-End Testing From Scratch — 2.5h](https://www.youtube.com/watch?v=AnyKTiC3P1M)
- [Testing JavaScript with Cypress — Full Course](https://www.youtube.com/watch?v=u8vMu7viCm8) — freeCodeCamp

**AI, Git, Actions, Playwright** — not filled in yet. Left empty rather than
padded with links nobody has watched.
