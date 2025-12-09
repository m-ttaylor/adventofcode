import numpy as np
from functools import reduce
from math import prod
import itertools

YEAR = 2025
DAY = 7
TEST = False

file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"


def prettyPrint(data):
    for line in data:
        print(" ".join(line))
    print()


with open(file) as f:
    data = [list(line) for line in f.read().strip().split("\n")]

start = data[0].index("S")

pt1, pt2 = 0, 0

lazers = [0] * len(data[0])
lazers[data[0].index("S")] = 1

for i in range(1, len(data)):

    newLazers = [0] * len(data[i])

    for j, c in enumerate(data[i]):

        if data[i - 1][j] in ("S", "|"):
            if data[i][j] == ".":
                data[i][j] = "|"
            elif data[i][j] == "^":
                pt1 += 1

                if 0 <= j - 1 and data[i][j - 1] == ".":
                    data[i][j - 1] = "|"

                if j + 1 < len(data[i]) and data[i][j + 1] == ".":
                    data[i][j + 1] = "|"

    if "^" in data[i]:
        newLazers = [0] * len(data[i])
        for j, c in enumerate(data[i]):
            if c == "^":
                newLazers[j - 1] += lazers[j]
                newLazers[j + 1] += lazers[j]
            else:
                newLazers[j] += lazers[j]

        print(newLazers)
        lazers = newLazers

    prettyPrint(data)

print(pt1)
print(sum(lazers))
