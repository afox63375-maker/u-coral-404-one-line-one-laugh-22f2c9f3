#!/usr/bin/env python3
"""One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Python standard library only.

The joke gives an ordinary household object a human problem: the
smoke detector that shrieks every time its owner cooks gets
reintroduced to guests as the household's food critic. The twist
lands in the final words — the alarm is not broken, it is judging.
"""

import os

MAX_CHARS = 200

LINE = (
    "My smoke detector goes off every time I cook, so I've started "
    "introducing it to guests as my food critic."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS or "\n" in line or "\r" in line:
        raise SystemExit(
            f"entry line must be a single line of 1-{MAX_CHARS} characters"
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print(f"Wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
