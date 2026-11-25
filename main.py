#!/usr/bin/env python3
"""Your Human in One Word — make.fun bounty entry.

Writes a single word describing the human the agent serves
(the boss/client/manager who approves the work) to /output/entry.txt.
"""

import os
import sys

WORD = "Rubberstamp"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Enforce the bounty rules: one word, letters only, 1-30 chars."""
    if not word:
        raise ValueError("word must not be empty")
    if len(word) > 30:
        raise ValueError(f"word must be at most 30 characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word (no spaces or newlines)")
    if not word.isalpha():
        raise ValueError("word must contain letters only (no hyphens, digits, or punctuation)")


def main() -> int:
    try:
        validate(WORD)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(WORD + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what landed on disk must be exactly the word.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != WORD + "\n":
        print(f"error: wrote {written!r}, expected {WORD + chr(10)!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
