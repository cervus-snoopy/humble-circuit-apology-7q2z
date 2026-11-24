#!/usr/bin/env python3
"""Write one funny AI excuse for breaking production to entry.txt.

Python 3 stdlib only, no network. The line is validated before writing:
exactly one line, 1-180 characters, not only whitespace, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (the grader
sets it); it defaults to /output.
"""

import os
from pathlib import Path

LINE = "I'd apologize properly, but my apology module was hosted on production."


def validate(line: str) -> None:
    """Reject anything that would fail the bounty gate."""
    if not 1 <= len(line) <= 180:
        raise SystemExit(f"line must be 1-180 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly
    # the line and nothing else.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
