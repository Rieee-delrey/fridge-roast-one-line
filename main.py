#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge to /output/entry.txt,
then validates the bytes on disk and reads them back to confirm
they match exactly what was written.
"""

import os

LINE = "My fridge emailed me that the milk expired, then offered a $4.99 monthly plan to remind me I never drink it anyway."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Validate the line before writing: 1-200 chars, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read back and verify: exact bytes, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != LINE.encode("utf-8"):
        raise ValueError("read-back bytes do not match the line")
    if data.endswith(b"\n"):
        raise ValueError("entry must not end with a newline")


if __name__ == "__main__":
    main()
