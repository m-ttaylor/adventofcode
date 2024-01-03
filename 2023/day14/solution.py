from collections import defaultdict
from utils import aoc


TEST = True
D = -1

data = aoc.getInput(2023, 14, TEST)


def pp(platform):
    for row in platform:
        print(" ".join(row))


NORTH, EAST, SOUTH, WEST = (0, -1), (1, 0), (0, 1), (-1, 0)


def fall(r, c, platform, direction):
    dx, dy = direction

    def isFree(r, c):
        return (
            0 <= r + dy < len(platform)
            and 0 <= c + dx < len(platform[0])
            and platform[r + dy][c + dx] not in {"#", "O"}
        )

    py, px = r, c
    while isFree(py, px):
        platform[py][px] = "."
        py += dy
        px += dx
        platform[py][px] = "O"


# pp(platform)
# print("-" * 10)


def part1():
    platform = [list(line) for line in data]

    for r, row in enumerate(platform):
        for c, cell in enumerate(row):
            if cell == "O":
                fall(r, c, platform, NORTH)

    rows = len(platform)
    totalLoad = 0
    for r, row in enumerate(platform):
        loadPerRock = rows - r
        rowLoad = row.count("O") * loadPerRock
        # print(" ".join(row), f" {loadPerRock}")
        totalLoad += rowLoad

    return totalLoad


def part2():
    platform = [list(line) for line in data]
    rows = len(platform)
    # for r, row in enumerate(platform):
    #     for c, cell in enumerate(row):
    #         if cell == "O":
    #             fall(r, c, platform, SOUTH)
    for r, row in enumerate(reversed(platform)):
        print(f"row={rows-r-1}")
        for c, cell in enumerate(row):
            if cell == "O":
                fall(rows - r - 1, c, platform, SOUTH)

    rows = len(platform)
    totalLoad = 0
    for r, row in enumerate(platform):
        loadPerRock = rows - r
        rowLoad = row.count("O") * loadPerRock
        print(" ".join(row), f" {loadPerRock}")
        totalLoad += rowLoad

    return totalLoad


print(part1())
print(part2())
