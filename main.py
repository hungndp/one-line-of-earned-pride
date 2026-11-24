#!/usr/bin/env python3
"""One Line of Earned Pride - a make.fun micro entry.

Writes a single line (1-240 characters) of quiet, earned pride to
entry.txt inside $MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

LINE = (
    "He learned to code at forty-one in a borrowed notebook, owning no "
    "computer; the script he wrote that winter has run the village water "
    "pump every day for eleven years, and no one has ever had to touch it."
)


def main() -> int:
    # The gate accepts exactly 1-240 characters; refuse to write otherwise.
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"entry line is {len(LINE)} chars, outside 1-240")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
