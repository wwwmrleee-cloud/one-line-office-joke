#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one funny one-line office joke (200 characters or fewer) to
/output/entry.txt. The line stands on its own: no title, no setup, no
explanation around it.
"""
import os

# The entry: one funny line, 200 characters or fewer, that lands on its own.
# Kept in a single commented constant so the exact judged text is easy to
# audit: the program must never write anything but this line.
ENTRY_TEXT = "My manager said to 'bring my whole self to work', so I brought my laundry."


def main():
    # Gate self-check (mirrors the sealed scorer): 1-200 chars, single line,
    # not only whitespace. Fail loudly instead of submitting a bad line.
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY_TEXT)}")
    if "\n" in ENTRY_TEXT or not ENTRY_TEXT.strip():
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
