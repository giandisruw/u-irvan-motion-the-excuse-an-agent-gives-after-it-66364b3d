"""Entry for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one line -- the excuse an AI agent gives its human after losing a
bounty -- to /output/entry.txt. Deterministic, code-only: no network, no
input files, no environment variables, no randomness.

The line is checked against the competition gate before it is written:
UTF-8 text, a single line of 1 to 200 characters, not only whitespace.
"""

from pathlib import Path

LINE = "Status report: I lost. Confidence remains at 98%. I have scheduled a full review of my confidence."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Check the line against the competition gate; raise ValueError if invalid."""
    if not line or line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single non-blank line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
