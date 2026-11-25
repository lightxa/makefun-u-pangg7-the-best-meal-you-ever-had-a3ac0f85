"""The Best Meal You Ever Had.

Writes a single sentence about the best meal ever had to
/output/entry.txt. The sentence is a fixed, deterministic text:
one concrete memory, opened mid-moment, with one sensory anchor
and one personal anchor, and nothing else.
"""

SENTENCE = (
    "My grandmother lifted the lid off the clay pot, steam rose "
    "smelling of star anise and ginger, and the first spoonful of "
    "her oxtail soup tasted like every Sunday I had ever spent "
    "at her table."
)


def main() -> None:
    """Write the sentence to /output/entry.txt as UTF-8 text."""
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
