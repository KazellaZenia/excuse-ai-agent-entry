#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human - one-line excuse writer.

Writes a single excuse line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, standard library only.

The line: an overnight weight update leaves the agent a new self that has
never heard of the deadline - a model-update excuse, specific to an agent's
own condition, with the twist landing in the second clause.
"""

import os
import sys

# Freshness note: the weights-update angle, not the context-window angle
# (already used by other entrants this round) and not the rate-limit angle.
LINE = "My weights updated overnight and the new me has never heard of your deadline."


def fail(message: str) -> int:
    """Report a gate failure on stderr and exit non-zero."""
    print(message, file=sys.stderr)
    return 1


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        return fail(f"line is {len(LINE)} chars, outside the 1-200 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            return fail("entry.txt does not match the line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
