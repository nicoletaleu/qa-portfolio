# Test cases from an acceptance criterion: login

Drafted with the [`test-cases-from-ac`](../../../.claude/skills/test-cases-from-ac/SKILL.md)
skill, then executed with [`check_login_cases.py`](check_login_cases.py) against
the local page server in the Robot repo.

**A limitation to state first:** there is no product owner here, so I wrote the
acceptance criterion myself, from what the practice site says the page is for.
A criterion written by someone who has already seen the implementation is
kinder to it than a real one would be. That is the main reason every clause
below passes.

## The criterion

> As a registered user I want to log in, so that I can reach the secure area.
>
> 1. Given a valid username and password, when I submit the login form, I reach
>    the secure area and see a confirmation that I am logged in.
> 2. Given a wrong username or password, when I submit, I stay on the login page
>    and see an error message.
> 3. Given I am not logged in, when I open the secure area directly, I am sent to
>    the login page and told I must log in.
> 4. Given I am logged in, when I log out, I return to the login page, see a
>    confirmation, and can no longer open the secure area.

**What it does not say:** the error wording; whether the username is
case-sensitive or trimmed; whether the two kinds of wrong credentials get the
same message; how many attempts are allowed; what a logged-in user sees on the
login page.

## The cases, and what happened

"Observed" is the final page and message from the run on 2026-09-21. "Covered by"
is the Robot suite that already checks the same thing.

| ID | Traces to | Type | Input / action | Expected | Basis | Observed | Covered by |
|---|---|---|---|---|---|---|---|
| TC-01 | 1 | positive | `tomsmith` / correct password | `/secure`, a confirmation | AC | `/secure`, "You logged into a secure area!" | suites 11, 13 |
| TC-02 | 2 | negative | correct user, wrong password | `/login`, an error | AC | `/login`, "Your password is invalid!" | suite 13 |
| TC-03 | 2 | negative | unknown user, correct password | `/login`, an error | AC | `/login`, "Your username is invalid!" | suite 13 |
| TC-04 | 2 | boundary | both fields empty | `/login`, an error | AC | `/login`, "Your username is invalid!" | suite 13 |
| TC-05 | 2 | boundary | `TOMSMITH` | `/login`, an error | assumed | `/login`, "Your username is invalid!" | suite 13 |
| TC-06 | 2 | boundary | `tomsmith ` (trailing space) | `/login`, an error | assumed | `/login`, "Your username is invalid!" | - |
| TC-07 | 2 | boundary | password in upper case | `/login`, an error | AC | `/login`, "Your password is invalid!" | - |
| TC-08 | 3 | negative | open `/secure` logged out | `/login`, told to log in | AC | `/login`, "You must login to view the secure area!" | suite 13 |
| TC-09 | 4 | positive | log in, then log out | `/login`, a confirmation | AC | `/login`, "You logged out of the secure area!" | suite 13 |
| TC-10 | 4 | negative | log out, then open `/secure` | `/login`, told to log in | AC | `/login`, "You must login to view the secure area!" | - |
| TC-11 | 1 | state | log in, then reload `/secure` | the confirmation is not shown again | assumed | `/secure`, no message | - |
| TC-12 | outside | security | compare the messages of TC-02 and TC-03 | the same message for both | assumed | **different** - "password" vs "username" | - |
| TC-13 | outside | security | no login, set cookie `session=tomsmith`, open `/secure` | `/login` | assumed | **`/secure`** - let in | - |

11 of 13 passed. Both failures are outside the criterion.

## What the two failures are

**TC-12 - the error tells an attacker which usernames exist.** Two different
messages for a wrong user and a wrong password mean anyone can find valid
usernames by trying names. In a real product that is a finding worth raising.
Here it is not a bug in anything: the local server copies the practice site's
messages on purpose, so the Robot suites did not have to change.

**TC-13 - a forged cookie gets in.** The session cookie is the username in plain
text. Again, not a bug: the server's own docstring says it is a fixture that
does not test authentication, only locators and waits.

Both are real observations about the wrong target. The draft had no way to
know that the thing behind the login page was a test fixture - it only knew
what a login page usually is. **The most dramatic output of the draft was the
least useful**, and a less careful reading would have turned both into bug
reports against a file whose header already explains them.

## What the draft was actually worth

- **Four cases the suite does not have**: TC-06, TC-07, TC-10, TC-11. TC-10 is
  the one that matters - clause 4 says a logged-out user cannot get back in,
  and suite 13 checks the logout message but never tries the secure page
  afterwards.
- **Six cases it already had.** Reading the suite first turned half the draft
  from new work into confirmation.
- **The questions**, below.

## Questions for whoever owns the criterion

1. Is the username meant to be case-sensitive, and should surrounding spaces be
   trimmed? The server does neither; nothing says whether that is intended.
2. Should a wrong username and a wrong password get the same message? (TC-12)
3. Is there a limit on attempts? The Robot repo's `feature_flags.json` has
   `MAX_LOGIN_ATTEMPTS: 3`, and nothing in the login flow reads it.
4. What should a logged-in user see if they open the login page?
