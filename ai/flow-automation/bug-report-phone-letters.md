# Bug: `Normalize Phone Number` accepts letters and silently drops them

Written with the [`bug-report`](../../.claude/skills/bug-report/SKILL.md) skill,
from the reading in [`failing-log.md`](failing-log.md). Filed against the
finished Robot repo, and left unfixed there on purpose.

**Title:** `Normalize Phone Number` returns a valid-looking number for input
containing letters, instead of raising

**Environment:** `robot-framework-learning` at `a387fd1`,
`libraries/DataHelpers.py`, Python 3.14, Robot Framework 7.4.2, Windows 11

**Preconditions:** none - a pure function

**Steps to reproduce**

1. Call `Normalize Phone Number` with `O721 123 456` (capital letter O, not zero)

**Expected result:** a `ValueError`. Source: the keyword's docstring - "Strips
spaces, dots, dashes, brackets. Keeps a leading +. Raises on anything
implausible." Letters are not on the list of characters it strips.

**Actual result:** returns `721123456` - nine digits, which passes the length
check. The leading digit the user meant to type is gone.

**Evidence:** `ai/flow-automation/test-data/run.robot`, rows
`letters-in-the-number` (`0721 ABC 123456` → `0721123456`) and
`letter-o-for-zero` (`O721 123 456` → `721123456`). Reproduced on two runs.

**Frequency:** always

**Severity:** medium - a mistyped number is accepted as a different, valid
number, with no signal to anyone. **Priority:** low - the function is test
tooling in a finished learning repo, and no suite feeds it user input.

**Suspected cause** (a suspicion, not a finding): the regex `[^\d+]` removes
*every* character that is not a digit or a plus, which is broader than the list
in the docstring. Either the regex or the docstring is wrong; deciding which is
the owner's call.

**Ruled out:** the test data. The expected value comes from the docstring, not
from running the function.
