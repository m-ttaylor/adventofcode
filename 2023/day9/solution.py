from collections import defaultdict
from utils import aoc

"""template"""

TEST = False

data = aoc.getInput(2023, 9, TEST)


def findDiffs(seq: list[int]):
    return [seq[i] - seq[i - 1] for i in range(1, len(seq))]


def findAllDiffs(seq: list[int]):
    diffs = findDiffs(seq)
    layers = [diffs]
    while any(d != 0 for d in diffs):
        diffs = findDiffs(diffs)
        layers.append(diffs)

    return layers


def findNextVal(seq: list[int]):
    layers = [seq, *findAllDiffs(seq)]
    for i in range(len(layers) - 1, 0, -1):
        layers[i - 1].append(layers[i - 1][-1] + layers[i][-1])
    return layers[0][-1]


def findPrevVal(seq: list[int]):
    layers = [seq, *findAllDiffs(seq)]
    for i in range(len(layers) - 1, 0, -1):
        layers[i - 1] = [(layers[i - 1][0] - layers[i][0]), *layers[i - 1]]
    return layers[0][0]


def part1():
    sequences = [aoc.parseInts(line) for line in data]
    return sum(findNextVal(seq) for seq in sequences)


def part2():
    return sum(findPrevVal(seq) for seq in [aoc.parseInts(line) for line in data])


print(part1())
print(part2())
