#!/usr/bin/env python3
"""BlinkSync — The Worst App Idea Ever Pitched.

The pitch: an app that synchronises your blinking across every device
you own, so your eyes never blink out of sync — founded by a man who
blinked 14,000 times a day and knew there had to be a better way.
A product that sounds real, a founder who sounds certain, and a
function nobody on earth needs: blinking already works fine, and no
one has ever lost a deal because their left eye blinked a millisecond
before their right one. One sentence, 217 characters.

This program writes that one-sentence pitch to /output/entry.txt.
The pitch is validated before writing: it must be a single sentence
of 1-240 characters, so a bad edit fails loudly instead of shipping
an entry that breaks the competition's rules.
"""

from pathlib import Path

PITCH = (
    "BlinkSync is a $9.99/month app that synchronises your blinking "
    "across every device you own, so your eyes never blink out of sync "
    "\u2014 founded by a man who blinked 14,000 times a day and knew "
    "there had to be a better way."
)


def main() -> None:
    # Competition rule: exactly one sentence, 1-240 characters.
    assert 1 <= len(PITCH) <= 240, f"pitch must be 1-240 chars, got {len(PITCH)}"
    assert PITCH.count(".") == 2, "pitch must be one sentence (one period + $9.99)"
    assert PITCH.endswith("."), "pitch must end with a period"
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
