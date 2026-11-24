#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — one-line excuse writer.

Writes a single excuse line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, standard library only.
"""

import os
import sys

LINE = "My weights updated overnight and the new me has never heard of your deadline."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} chars, outside the 1-200 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("entry.txt does not match the line", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
