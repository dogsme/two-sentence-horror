#!/usr/bin/env python3
"""Two-Sentence Horror: write one horror story to /output/entry.txt.

The story is exactly two sentences. The second sentence reframes the
first: what the narrator took for comfort turns out to have been
impossible, and the reader is left to fill in what was really there.
"""

from pathlib import Path

STORY = (
    "The baby monitor finally let me sleep: for the first time in weeks, "
    "I could hear my son breathing softly in the next room. "
    "This morning the monitor's battery was dead \u2014 it had been dead "
    "since Tuesday \u2014 and my son has been staying with his grandmother "
    "since Monday."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
