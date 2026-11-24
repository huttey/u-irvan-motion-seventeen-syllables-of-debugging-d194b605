"""One haiku about debugging — writes it to /output/entry.txt."""

import os
import re


def _syllables(word: str) -> int:
    """Vowel-group count; exact for every word in this haiku."""
    return len(re.findall(r"[aeiou]+", word.lower()))


HAIKU = (
    "cursor blinks at three\n"
    "the log says nothing new yet\n"
    "and the bug was me\n"
)


def main() -> None:
    text = HAIKU
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    lines = text.strip().splitlines()
    assert len(lines) == 3, "entry must be exactly 3 lines"
    counts = [sum(_syllables(w) for w in line.split()) for line in lines]
    assert counts == [5, 7, 5], "entry must be 5-7-5 syllables"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
