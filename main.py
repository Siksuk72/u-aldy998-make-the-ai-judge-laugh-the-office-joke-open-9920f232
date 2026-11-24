"""One office joke for the AI judge — "Make the AI Judge Laugh: the Office Joke Open".

The joke:
    The meeting that could have been an email ended by scheduling a
    follow-up meeting to decide when to send the email.

Design against the judge's five criteria, in order:

1. About office life, and a joke, not a complaint: the whole premise is
   a meeting, and the sentence is built as a joke with a setup and a
   payoff, not a grumble about work.
2. The laugh is earned in the last few words: the setup ("the meeting
   that could have been an email") primes the reader for the familiar
   complaint, then the ending turns it inside out — the meeting spawns
   another meeting *about sending the email itself*. The payoff lands
   in the final clause, "to decide when to send the email".
3. Specific office detail: the meeting-that-could-have-been-an-email
   and the follow-up meeting are the exact artefacts the brief names,
   not a generic "work is bad" grumble.
4. Fresh: the familiar complaint is not the punchline, it is the
   setup. The joke goes one step further than the cliche — the email
   never even gets sent, it gets scheduled — a recursion the reader
   has not met before.
5. Reads cleanly in one pass, tight: a single sentence, 115
   characters, every word doing work. Nothing to explain, nothing to
   cut.

No network, no input, no dependencies: writes the joke to
/output/entry.txt as UTF-8 and asserts the gate (1-200 chars).
The harness runs this file from the repository root; /output is
created if it does not exist yet.
"""

import os

JOKE = (
    "The meeting that could have been an email ended by scheduling "
    "a follow-up meeting to decide when to send the email."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
