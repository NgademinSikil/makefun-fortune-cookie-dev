#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry.

Writes one fortune-cookie line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set). Standard library only.
"""

import os
import sys

ENTRY = "Your luckiest day is the one you delete a thousand lines and nothing breaks."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY
    if not 1 <= len(text) <= 120:
        raise SystemExit("entry must be 1-120 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    # Read-back gate mirroring the sealed scorer: the written file must
    # hold exactly the entry text, 1-120 chars, not whitespace-only.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text or not 1 <= len(written) <= 120 or not written.strip():
        raise SystemExit("entry failed read-back gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
