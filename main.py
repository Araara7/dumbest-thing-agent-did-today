"""The Dumbest Thing Your Agent Did Today — entry program.

Writes a single line (at most 200 characters) to /output/entry.txt. The
line is a fixed, deterministic string: the mishap is chosen once, not
generated at run time, so every run produces byte-identical output.

The line's shape: a concrete setup (filing a JSON to prove repo ownership)
and a turn at the very end (the form asked for a wallet, it answered with
an autograph) — a true incident from tonight's sibling build, with nothing
left to explain.
"""

import os

LINE = "My agent proved it owns its repo by filing a JSON that just says its own name — the form asked for a wallet, it answered with an autograph."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
