from collections import defaultdict
from random import random, choice
import sys
from typing import DefaultDict

StyleDict = DefaultDict[str, list[str]]


def main():
    styleDict: StyleDict = defaultdict(list)
    with open(sys.argv[1], "r") as inp:
        # Fill the styledict
        for line in inp:
            cleaned = [
                word.strip() for word in remove_puncts(line.lower()).split(" ") if word
            ]
            for w1, w2 in zip(cleaned, cleaned[1:]):
                styleDict[w1].append(w2)
    # Pick a random start word that has follower words
    start = choice([k for k, v in styleDict.items() if v])
    n = 150
    print(start.capitalize() + generate(start, 150, styleDict))
    return


def generate(current: str, n: int, sd: StyleDict) -> str:
    choices = sd[current]
    if n == 0:
        return "."
    if not choices:
        return "."
    wordChoice = choice(choices)
    return " " + wordChoice + generate(wordChoice, n - 1, sd)


def remove_puncts(line: str) -> str:
    puncts = ".,!;:'\"“”()-—"
    return "".join([c if not c in puncts else " " for c in line])


if __name__ == "__main__":
    main()
