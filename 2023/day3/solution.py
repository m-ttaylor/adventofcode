from collections import defaultdict
import math
from utils import aoc

TEST = False

data = aoc.getInput(2023, 3, TEST)
rows = len(data)


def adjacentToSymbol(r: int, c: int, sizeOfNumber: int):
    # check up and down
    for dir in (-1, 1):
        if 0 <= (checkRow := r + dir) < rows:
            for i in range(c - sizeOfNumber, c + 2):
                if 0 <= i < len(data[checkRow]):
                    adj = data[checkRow][i]
                    if not adj.isdigit() and adj != ".":
                        if TEST:
                            print(
                                f"found a row+{dir} adjacency at {checkRow}, {i}: {adj}"
                            )
                        return adj, (checkRow, i)

    # check row of:
    for i in [c - sizeOfNumber, c + 1]:
        if 0 <= i < len(data[r]):
            adj = data[r][i]
            if not adj.isdigit() and adj != ".":
                if TEST:
                    print(f"found a row adjacency at {r}, {i}: {adj}")
                return adj, (r, i)

    return False, (-1, -1)


def part1():
    total = 0
    for r in range(rows):
        number = ""
        for c, char in enumerate(data[r]):
            if char.isdigit():
                number += char
                if c + 1 >= len(data[r]) or not data[r][c + 1].isdigit():
                    asInt = int(number)
                    if TEST:
                        print(f"checking number {asInt}")
                    sizeOfNumber = len(number)
                    number = ""
                    if adjacentToSymbol(r, c, sizeOfNumber):
                        if TEST:
                            print(f"adding {asInt} to total")
                        total += asInt
    return total


def part2():
    gears = defaultdict(list)

    for r in range(rows):
        number = ""
        for c, char in enumerate(data[r]):
            if char.isdigit():
                number += char
                if c + 1 >= len(data[r]) or not data[r][c + 1].isdigit():
                    asInt = int(number)
                    width = len(number)
                    number = ""
                    symbol, coords = adjacentToSymbol(r, c, width)
                    if symbol == "*":
                        if TEST:
                            print(f"adding {asInt} to gears")
                        gears[coords].append(asInt)

    total = sum(math.prod(gears[gear]) for gear in gears if len(gears[gear]) == 2)
    return total


print(part1())
print(part2())
