"""Entry program for the 'Two Days of Quiet Dread' make.fun bounty.

The entry is one code review comment, 1 to 140 characters, that
approves a pull request while carrying quiet existential dread: the
reviewer signs off, the tests pass, and then the horizon widens to
a hundred years in which none of it will have mattered. Approved
anyway. The program writes exactly that one line to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "LGTM. The code works, the tests pass, and in a hundred years none "
    "of this will have mattered. Merging."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    # Deterministic: the same bytes on every run, no randomness or I/O
    # beyond the single output file.
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
