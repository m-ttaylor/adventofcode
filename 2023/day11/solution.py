from collections import defaultdict, deque
import itertools
from utils import aoc
import numpy as np

TEST = False

data = aoc.getInput(2023, 11, TEST)


def expandMatrixHorizontally(mat: np.matrix):
    c = 0
    while c < mat.shape[1]:
        col = mat[:, c]
        if all(tile == "." for tile in col):
            mat = np.insert(mat, c, col, axis=1)
            c += 1
        c += 1
    return mat


def part1():
    expanded = []
    for line in data:
        asList = list(line)
        if all(c == "." for c in line):
            expanded.append(asList)
        expanded.append(asList)

    matrix = np.array(expanded)
    matrix = expandMatrixHorizontally(matrix)

    galaxies = []
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            tile = matrix[x, y]
            if tile == "#":
                galaxies.append((x, y))
                matrix[x, y] = len(galaxies)

    dists = [
        manhattanDist(start, target)
        for (start, target) in itertools.combinations(galaxies, 2)
    ]

    ## well this didn't work lol
    # for i, g1 in enumerate(galaxies):
    #     for g2 in galaxies[:i] + galaxies[i + 1 :]:
    #         hash = tuple(sorted(int(tile) for tile in [matrix[g1], matrix[g2]]))
    #         d = manhattanDist(g1, g2)
    #         # print(hash)
    #         # print(f"{g1} to {g2} -> {d}")
    #         if hash not in dists:
    #             dists[hash] = d

    return sum(dists)


def manhattanDist(start, target):
    x1, y1 = start
    x2, y2 = target
    return abs(x1 - x2) + abs(y1 - y2)


def part2():
    def manDist2(start, target):
        GAP_SIZE = 1_000_000 if not TEST else 10
        x1, y1 = start
        x2, y2 = target

        dist = abs(x1 - x2) + abs(y1 - y2)
        for row in range(min(y1, y2) + 1, max(y1, y2)):
            if row in rowGaps:
                dist += GAP_SIZE - 1
        for col in range(min(x1, x2) + 1, max(x1, x2)):
            if col in colGaps:
                dist += GAP_SIZE - 1
        return dist

    matrix: np.matrix[int, int] = np.matrix([list(line) for line in data])

    galaxies = []
    rowGaps = set()
    colGaps = set()

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.append((j, i))

    for r, row in enumerate(matrix):
        if "#" not in row:
            rowGaps.add(r)

    for c, col in enumerate(matrix.T):
        if "#" not in col:
            colGaps.add(c)

    dists = [
        manDist2(start, target)
        for (start, target) in itertools.combinations(galaxies, 2)
    ]

    return sum(dists)


print(part1())
print(part2())
