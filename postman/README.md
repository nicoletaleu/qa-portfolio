# Postman — P1

The same public API that `tests/api/` already covers, done again in Postman.
The practice is not new; the tool is. The point of redoing it is the comparison.

## Run it

In the Postman app: import both files, pick the `public` environment, run the
collection.

Headless, which is what CI will use in P2:

```bash
npx newman run postman/qa-learning.postman_collection.json \
    -e postman/environments/public.postman_environment.json
```

5 requests, 23 assertions, all green. About 1.7s, most of it waiting on the
network - which is the thing the Robot repo spent Days 28-30 removing, and
something P2 will have to decide what to do about.

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
[robot-framework-learning](https://github.com/nicoletalucia/robot-framework-learning).

P2 is the other half of this: newman running in GitHub Actions, with a `paths:`
filter so a change here does not start every other tool's workflow.
