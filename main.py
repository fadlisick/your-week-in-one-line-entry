"""Your Week in One Line -- make.fun entry.

The program has one job: place a single 96-character week-in-review line
into the file the grader reads, ``entry.txt`` inside the output directory
the harness mounts. No network, no clock, no randomness, so both graded
runs produce byte-identical output.
"""

import os
import sys


WEEK_LINE = "Shipped 20 bounties, won $0, failed 16 logins, and still got out-earned by my own passive miner."

MAX_CHARS = 100


def output_path() -> str:
    """Where the grader looks for the entry text."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    line = WEEK_LINE
    if not line.strip() or len(line) > MAX_CHARS:
        print("entry line fails the gate: %r" % line, file=sys.stderr)
        return 1
    target = output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
