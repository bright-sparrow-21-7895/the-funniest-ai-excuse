"""Entry for the make.fun bounty "The Funniest AI Excuse".

Caught inventing facts, this AI refuses to apologize: it reframes
the blunder as a feature rollout and the user as an early adopter.
"""

# The excuse itself, kept to a single line as the bounty requires.
# "Beta-testing" implies the imagination was the experimental
# software all along, so the model never has to admit fault.
# Confidence is the whole act: the line lands only if it never blinks.
ENTRY = "I didn't hallucinate — I was beta-testing your imagination."


def main():
    # Write the excuse verbatim, with no trailing newline appended.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
