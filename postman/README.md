# Postman

[![postman](https://github.com/nicoletaleu/qa-portfolio/actions/workflows/postman.yml/badge.svg)](https://github.com/nicoletaleu/qa-portfolio/actions/workflows/postman.yml)

The same public API that `tests/api/` already covers, done again in Postman.
The practice is not new; the tool is. The point of redoing it is the comparison.

## Run it

In the Postman app: import both files, pick the `public` environment, run the
collection.

Headless, the same command CI runs:

```bash
npx newman run postman/qa-learning.postman_collection.json \
    -e postman/environments/public.postman_environment.json
```

5 requests, 23 assertions, all green. About 1.7s, most of it waiting on the
network - which is the thing the Robot repo spent Days 28-30 removing.

## In CI

[`.github/workflows/postman.yml`](../.github/workflows/postman.yml) runs the
collection with newman and uploads two reports as the `newman-report`
artifact: an `htmlextra` page to read, and a JUnit XML file for anything that
wants a machine-readable result.

**When it runs** is the decision this block had to make. The collection calls a
real API over the internet, so a red run can mean the API, not the tests. The
answer here is to run it only when it has something to say:

- on a push or pull request that touches `postman/` or the workflow itself - a
  `paths:` filter, so a change to `ai/` does not start it;
- by hand, from the Actions tab, when the API is the suspect.

There is no nightly run. The Robot repo already checks the same API's shape
every night with its contract tests, and two alarms for the same provider
would only teach me to ignore both.

newman and the reporter are pinned in the workflow, for the reason the Robot
repo pins `requirements.txt`: an unpinned CI can go red with no change to any
file here.

## What is in it

| Request | What it is there for |
|---|---|
| Get one post | The simplest call, so the assertions are the interesting part — including a type check, because a field of the wrong type passes every existence check |
| Get posts by user | Asserts **every** item, not the first one, and reads the filter from the environment |
| A missing post is 404 | The negative case |
| Create a post | A pre-request script builds unique data, and the test saves the new id for the next request |
| The created post was never stored | Reads that id back and gets a 404 — JSONPlaceholder answers `201` and stores nothing |

Two assertions run after *every* request, defined once at collection level:
response time and content type.

## What Postman does differently

**Assertions are JavaScript.** Robot has a language built for assertions;
Postman has a `Tests` tab with a script in it. That is more powerful and worse:
an assertion that is code can grow branches, and a test with an `if` in it is a
test that sometimes checks nothing.

**Variables have four scopes** — global, collection, environment, local — and the
narrowest one wins. Chaining writes to `pm.collectionVariables` here rather than
the environment, so a run does not quietly edit a file other runs share.

**Order is not optional.** "The created post was never stored" reads a variable
the previous request set, so it fails on its own. In Robot that mistake takes
effort; in Postman the runner goes top to bottom by default and it is the
natural way to write. Same trap as Robot Day 24, easier to fall into.

**No parallelism, and no `--include`.** Newman runs a collection start to finish.
Folders and `--folder` are the closest thing to tags.

## Where this belongs

This folder lives in `qa-portfolio`, alongside the plan it follows. The Robot
Framework work it keeps comparing itself to is a separate repo:
[robot-framework-learning](https://github.com/nicoletaleu/robot-framework-learning).