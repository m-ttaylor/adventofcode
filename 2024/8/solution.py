from collections import defaultdict, Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, permutations
from math import gcd, sqrt


YEAR = 2024
DAY = 8
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

grid = [list(line) for line in data]
# print(grid)

rows, cols = len(grid), len(grid[0])


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def inbounds(pos):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


antennae = defaultdict(list)
antinodes = set()
pt2antinodes = set()

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val != ".":
            antennae[val].append((r, c))

for val in antennae:
    print("combinations of key", val)
    print(list(combinations(antennae[val], 2)))

    combs = combinations(antennae[val], 2)
    for (r1, c1), (r2, c2) in combs:

        yoffset = r2 - r1
        xoffset = c2 - c1

        slope = Fraction(yoffset, xoffset)

        a = r2 - (yoffset * 2), c2 - (xoffset * 2)
        b = r1 + (yoffset * 2), c1 + (xoffset * 2)

        if inbounds(a):
            antinodes.add(a)
        if inbounds(b):
            antinodes.add(b)

        a = r1, c1

        while inbounds(a):
            pt2antinodes.add(a)
            a = a[0] - slope.numerator, a[1] - slope.denominator

        b = r2, c2
        while inbounds(b):
            pt2antinodes.add(b)
            b = b[0] + slope.numerator, b[1] + slope.denominator


# for row in grid:
#     print(" ".join(row))

print("pt1", len(antinodes))

print("pt2", len(pt2antinodes))
