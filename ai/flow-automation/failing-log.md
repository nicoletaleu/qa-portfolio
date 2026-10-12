# Reading a failing log

The [`failing-log`](../../.claude/skills/failing-log/SKILL.md) skill applied to
a real red run: the first run of [`test-data/run.robot`](test-data/run.robot)
on 2026-09-21, which pushed generated test data through two functions in the
Robot repo's `DataHelpers.py`.

## What exactly failed

2 tests ran, 2 failed. Behind them, 6 rows out of 28 disagreed with their
expected value.

The console showed the phone failures well - every row named, with its input
and output - and the age failure badly:

```
Every Age Row Gives Its Expected Result                               | FAIL |
Expected error '*' did not occur.
```

No row name, no value. The console could not say which of twelve rows failed.
`output.xml` could: the innermost step was `Run Keyword And Expect Error` inside
the loop iteration for `born-in-the-future`, and calling the function directly
with those dates returned **-4**.

The console also printed one phone row as `'??????????'`. That was the Windows
console failing to encode Arabic-Indic digits, not the data - `output.xml` has
the real characters. **The console is a summary, and it is lossy.**

## What kind of failure each one is

| Row | Source | Kind | Why |
|---|---|---|---|
| `born-in-the-future` - returns -4 | assumed | unclear rule | the docstring says "age in whole years" and says nothing about a birthdate after the reference date |
| `letters-in-the-number` - `0721 ABC 123456` accepted as `0721123456` | spec | product | the docstring lists what gets stripped - spaces, dots, dashes, brackets - and letters are not on it. The code strips every non-digit |
| `letter-o-for-zero` - `O721 123 456` accepted as `721123456` | spec | product, **same bug** | same line of code. Worse effect: a capital O typed for a zero silently loses a digit and still passes the length check |
| `extension` - `... ext 12` accepted as `072112345612` | assumed | unclear rule | same mechanism; whether extensions are allowed is not written anywhere |
| `double-plus` - `++40...` accepted as `+40...` | assumed | unclear rule | "keeps a leading +" does not say what happens to two |
| `non-latin-digits` - accepted unchanged | assumed | unclear rule | Python's `\d` matches every Unicode digit. Worth knowing: suite 17's own check, `^\+?\d{9,15}$`, would accept them too |

Plus one failure that belongs to the **test**: the age check's message. It was
written with `Run Keyword And Expect Error`, which cannot carry a custom message,
inside a loop where the only useful information is which row. Fixed by checking
the status explicitly, as the phone check already did. The second run's console
says `born-in-the-future (assumed): expected an error, got -4`.

Nothing landed in the "data was wrong" pile this time - but a row that passes
has only agreed with the code, not been confirmed. `leap-born-feb-28` is
`assumed` and passed: the code and I happened to pick the same convention.

## What to check next

1. The letters bug has a spec behind it, so it gets a report →
   [`bug-report-phone-letters.md`](bug-report-phone-letters.md). One report,
   not two: `letters-in-the-number` and `letter-o-for-zero` are the same line.
2. The four `assumed` rows become questions, not reports. The Robot repo is
   finished, so they are recorded here rather than fixed there.
