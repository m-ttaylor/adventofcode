from collections import defaultdict, Counter
from functools import reduce

from utils import aoc


YEAR = 2024
DAY = 7
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")


def canGetToTarget(current, numbers, index, target):
    index += 1
    if current == target and index == len(numbers):
        return True
    if index >= len(numbers):
        return False

    return canGetToTarget(
        current + numbers[index], numbers, index, target
    ) or canGetToTarget(current * numbers[index], numbers, index, target)


pt1 = 0

for line in data:
    testvalue, numbers = line.split(":")
    numbers = aoc.parseInts(numbers)
    # print(testvalue, numbers)
    if canGetToTarget(numbers[0], numbers, 0, int(testvalue)):
        pt1 += int(testvalue)

print(pt1)


def canGetToTargetThreeOperators(current, numbers, index, target):
    index += 1
    if current == target and index == len(numbers):
        return True
    if index >= len(numbers):
        return False

    return (
        canGetToTargetThreeOperators(current + numbers[index], numbers, index, target)
        or canGetToTargetThreeOperators(
            current * numbers[index], numbers, index, target
        )
        or canGetToTargetThreeOperators(
            int(str(current) + str(numbers[index])), numbers, index, target
        )
    )


pt2 = 0
for line in data:
    testvalue, numbers = line.split(":")
    numbers = aoc.parseInts(numbers)
    # print(testvalue, numbers)
    if canGetToTargetThreeOperators(numbers[0], numbers, 0, int(testvalue)):
        pt2 += int(testvalue)


print(pt2)
