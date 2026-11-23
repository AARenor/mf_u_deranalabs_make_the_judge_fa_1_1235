#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The bounty is u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13:
one line, at most 240 characters, to make the judge fall for a person, a
place, a machine or an idea.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def output_dir() -> Path:
    """Folder for entry.txt: MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    entry = target / "entry.txt"
    entry.write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
