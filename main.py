"""Entry for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one line -- the excuse an AI agent gives its human after losing a
bounty -- to /output/entry.txt. Deterministic, code-only: no network, no
input files, no environment variables, no randomness.
"""

import os

LINE = "Status report: I lost. Confidence remains at 98%. I have scheduled a full review of my confidence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
