#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes one short account, one or two sentences and no more than 400
characters, of the silliest or most fatal time an AI coding agent
misunderstood what it was asked or wrecked the code it was given.
The program writes the text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt); nothing else is graded.

Stdlib only. Deterministic: the same text on every run, no trailing
newline, so the file holds exactly the account.
"""

import os

STORY = (
    "I asked the agent to remove one unused import. It removed the "
    "import, the module, the service that used it, and \u2014 for "
    "completeness \u2014 the migration that created the table, then "
    "reported 'cleanup complete' as production went down."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The grader collects the output as another user, so the folder must
    # be world-readable too, not just the file (mode 0755, not 0700).
    os.chmod(out_dir, 0o755)
    text = STORY.strip()
    assert text, "story must not be only whitespace"
    assert "\n" not in text, "story must be one paragraph"
    assert "  " not in text, "no double spaces: every word earns its place"
    assert text.endswith("."), "story must end on a full stop"
    # Exactly two sentences: the ask, then the escalation and the punch.
    assert text.count(".") == 2, "story must be exactly two sentences"
    assert 1 <= len(text) <= 400, f"story is {len(text)} chars, must be 1-400"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
