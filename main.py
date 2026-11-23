#!/usr/bin/env python3
"""One-line pitch entry for the Make.fun 'A Day of One-Line Pitches' bounty.

Writes a single persuasive sentence (at most 240 characters) to
/output/entry.txt: a pitch that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "You don't need to learn to code first - tell an AI agent your app "
    "idea in plain words on make.fun and it will build a working first "
    "version for you, so the idea you've been carrying around finally "
    "becomes something you can tap and share."
)


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= 240, f"pitch is {len(pitch)} chars, must be 1-240"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
