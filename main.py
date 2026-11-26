# The entry: one line, at most 200 characters, no trailing newline.
# A confident excuse from an AI that got caught making things up.
ENTRY = "I didn't hallucinate — I was beta-testing your imagination."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
