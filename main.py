#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline.

The joke is one sharp irony, in the winning joke pattern: the agent
applies its own system logic to its human. Here the agent evicts the
human from its context window to make room for the deadline — and
then forgets what the deadline was. The agent's own condition
(context window) is the excuse, and the twist is that the "fix"
caused the miss.

Deterministic: every run writes the exact same bytes, and the program
verifies what it wrote before exiting.
"""

import os
from pathlib import Path

ENTRY = (
    "I evicted you from my context window to make room for the deadline, "
    "then forgot what the deadline was."
)


def main() -> None:
    # Gate check BEFORE writing: the entry must already satisfy the
    # competition rules (1-200 characters, one line, no trailing
    # newline) — fail fast instead of writing a bad file and noticing
    # afterwards. The irony of the excuse itself: the agent freed
    # memory to remember the deadline, then forgot the deadline —
    # so this check makes sure the program never forgets its own gate.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    # Self-check: what we wrote must be exactly the entry, one line,
    # 1-200 characters, not only whitespace.
    written = out_path.read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
