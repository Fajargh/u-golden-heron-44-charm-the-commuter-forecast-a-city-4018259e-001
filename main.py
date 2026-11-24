#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (1-140 characters) for the invented
city of Glimmerwick to /output/entry.txt.
"""

import os

ENTRY = (
    "Glimmerwick: 21°C, sunny with a chance of free croissants; "
    "the 8:04 bus is on time, and so, for once, are you. Enjoy the ride."
)


def main() -> None:
    line = ENTRY.strip()
    # Validation guard: the gate requires 1-140 chars, a single line,
    # and not only whitespace.
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
