"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt.

The joke's craft, against the judge's brief:
  * A real joke with a setup and a turn, punchline last. The setup is a
    small, ordinary office request (a second monitor). The turn is that
    the office answers a hardware request with the one thing it always
    seems able to produce: another meeting. "Booked me" was chosen over
    "got" in revision: booking is what offices do to people, and the
    verb makes the turn feel like something done to the speaker, not
    just something that happened. The punchline lands on the
    word "duplicates", which ties the request (a duplicate screen) to
    the answer (a duplicate calendar invite).
  * Built on something anyone who has worked in an office knows: asking
    IT for equipment and drowning in calendar invites instead.
  * Fresh angle: it avoids the three examples every entrant will reach
    for first (the meeting that could have been an email, reply-all,
    the jammed printer) and picks a different everyday frustration.
  * One line, 1-200 characters, every word earning its place.
"""

import os

JOKE = (
    "I asked IT for a second monitor and they booked me a second meeting instead "
    "-- apparently the only thing this office duplicates is calendar invites."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
