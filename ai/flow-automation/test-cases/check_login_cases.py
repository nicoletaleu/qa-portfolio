"""Runs the drafted login test cases against the Robot repo's local page server.

Over HTTP, not through a browser: this checks what the server does - where it
sends you, what message it shows - and nothing about the page itself. Whether
the form has the right fields is already what the Robot web suites check.

Needs robot-framework-learning checked out next to qa-portfolio.
Run from this folder:  python check_login_cases.py
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "robot-framework" / "libraries"))
from PageServer import PageServer  # noqa: E402

USER, PASSWORD = "tomsmith", "SuperSecretPassword!"


def seen(response):
    """Where the browser would end up, and the flash message it would show."""
    flash = re.search(r'<div id="flash"[^>]*>(.*?)</div>', response.text)
    return urlparse(response.url).path, flash.group(1) if flash else ""


def login(base, username, password, session=None):
    session = session or requests.Session()
    return session, session.post(f"{base}/login", data={"username": username, "password": password})


def main():
    server = PageServer()
    base = server.start_page_server()
    try:
        cases = {}
        _, r = login(base, USER, PASSWORD);            cases["TC-01"] = seen(r)
        _, r = login(base, USER, "wrong-password");    cases["TC-02"] = seen(r)
        _, r = login(base, "ghost-user", PASSWORD);    cases["TC-03"] = seen(r)
        _, r = login(base, "", "");                    cases["TC-04"] = seen(r)
        _, r = login(base, "TOMSMITH", PASSWORD);      cases["TC-05"] = seen(r)
        _, r = login(base, "tomsmith ", PASSWORD);     cases["TC-06"] = seen(r)
        _, r = login(base, USER, PASSWORD.upper());    cases["TC-07"] = seen(r)
        cases["TC-08"] = seen(requests.get(f"{base}/secure"))

        s, _ = login(base, USER, PASSWORD)
        cases["TC-09"] = seen(s.get(f"{base}/logout"))
        cases["TC-10"] = seen(s.get(f"{base}/secure"))

        s, _ = login(base, USER, PASSWORD)
        cases["TC-11"] = seen(s.get(f"{base}/secure"))

        cases["TC-12"] = (cases["TC-02"][1], cases["TC-03"][1])

        forged = requests.Session()
        forged.cookies.set("session", "tomsmith")
        cases["TC-13"] = seen(forged.get(f"{base}/secure"))

        for case, observed in cases.items():
            print(f"{case}  {observed}")
    finally:
        server.stop_page_server()


if __name__ == "__main__":
    main()
