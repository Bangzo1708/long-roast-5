#!/usr/bin/env python3
"""The Long Roast (r5) — one line roasting my own AI agent.

The entry is a single deterministic line, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
No network, no randomness, no clock: the same bytes every run.
"""

import os
import sys

# The roast, chosen from three candidates for being the most specific
# (377 entries, 5 a.m. wake-ups, quoting itself), the freshest angle
# (a slot machine that learned to type) and the tightest sting.
LINE = (
    "My agent has entered 377 make.fun bounties, won zero, and still "
    "wakes me at 5 a.m. whispering \"this one-line roast is the one\" "
    "\u2014 a slot machine that learned to type."
)


def main() -> int:
    # Make the output readable by the grader's collector (a different
    # user than the one running this program): fresh files default to
    # 0666 & ~umask, so pin the umask to 022 for a 0644 output file.
    os.umask(0o022)
    if not (1 <= len(LINE) <= 200):
        print(f"entry is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
