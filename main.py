#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — one Wi-Fi network name.

The entry is a single fixed Wi-Fi network name, written for make.fun
u-xvader-tell-a-whole-story-in-32-characters-f86dd978: one name of at
most 32 characters that lands a joke and implies a whole story. A
breakup told in one breath — she left, took the cat, and left the
router behind. This program writes that name to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The name is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "SheLeftTheRouterTookTheCat"


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the name against the gate, then write it out."""
    if not 1 <= len(LINE) <= 32:
        return abort(f"name is {len(LINE)} characters, the gate allows 1-32")
    if not LINE.strip():
        return abort("name is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
