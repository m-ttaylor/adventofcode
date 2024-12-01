from collections import defaultdict
from functools import reduce
from utils import aoc

with open("2024/1/input") as f:
    data = f.read().strip().split("\n")


def part1():
    list1, list2 = [], []
    for line in data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    list1.sort()
    list2.sort()

    return reduce(lambda tot, i: tot + (abs(list2[i] - list1[i])), range(len(list1)), 0)


def part2():
    counts = defaultdict(int)
    list1 = []
    for line in data:
        counts[int(line.split()[1])] += 1
        list1.append(int(line.split()[0]))

    return reduce(lambda tot, x: tot + x * counts[x], list1, 0)


print(part1())
print(part2())
