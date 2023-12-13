from collections import defaultdict, deque
import math
from utils import aoc

"""
Compass Reminder:

     N
   \ | /
W -- o -- E
   / | \
     S

"""

TEST = False

data = aoc.getInput(2023, 10, TEST)


pipes = {
    "L": {(0, -1), (1, 0)},
    "J": {(-1, 0), (0, -1)},
    "7": {(-1, 0), (0, 1)},
    "F": {(1, 0), (0, 1)},
    "-": {(1, 0), (-1, 0)},
    "|": {(0, 1), (0, -1)},
}


def pad(s, n):
    while len(s) < n:
        s += " "
    return s


def prettyPrintGraph(g):
    for row in g:
        print(
            "".join(
                [
                    pad(str(item), 3) if str(item).isdigit() else f"{item}  "
                    for item in row
                ]
            )
        )


VALID_PIPES = {"L", "S", "-", "|", "7", "J", "F"}


def simplifyGridDos(grid, dists):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if (x, y) not in dists:
                grid[y][x] == "Z"

    return grid


def countConnections(grid, r, c, pipe):
    """unused"""
    connections = 0
    if pipe not in VALID_PIPES:
        return 0
    if pipe == "S":
        return 2
    for dir in pipes[pipe]:
        validConnectors = {"S"}
        match dir:
            case _, 1:  # down 1
                validConnectors |= {"L", "|", "J"}
            case _, -1:  # up 1
                validConnectors |= {"F", "|", "7"}
            case 1, _:  # right 1
                validConnectors |= {"7", "-", "J"}
            case -1, _:  # left 1
                validConnectors |= {"L", "-", "F"}

        if 0 <= r + dir[1] < len(grid) and 0 <= c + dir[0] < len(grid[r]):
            if grid[r + dir[1]][c + dir[0]] in validConnectors:
                connections += 1
    return connections


def simplifyGrid(grid):
    """unused"""
    for r, row in enumerate(grid):
        for c, pipe in enumerate(row):
            if countConnections(grid, r, c, pipe) < 2:
                grid[r][c] = "."


def part1():
    grid = [list(row) for row in data]

    sx, sy = None, None

    for y, row in enumerate(grid):
        for x, pipe in enumerate(row):
            if pipe == "S":
                sx, sy = x, y
                break

    q = deque()

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        pipe = grid[sy + dy][sx + dx]

        if pipe in pipes:
            for dx2, dy2 in pipes[pipe]:
                if dx + dx2 == 0 and dy + dy2 == 0:
                    q.append((1, (sx + dx, sy + dy)))

    dists = {(sx, sy): 0}

    while q:
        d, (x, y) = q.popleft()

        if (x, y) in dists:
            continue
        dists[(x, y)] = d

        for dx, dy in pipes[grid[y][x]]:
            q.append((d + 1, (x + dx, y + dy)))

    simplifyGrid(grid)
    prettyPrintGraph(grid)
    print()

    return max(dists.values())


def part2():
    grid = [list(row) for row in data]

    ans = 0
    sx, sy = None, None

    for y, row in enumerate(grid):
        for x, pipe in enumerate(row):
            if pipe == "S":
                sx, sy = x, y
                break

    q = deque()

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        pipe = grid[sy + dy][sx + dx]

        if pipe in pipes:
            for dx2, dy2 in pipes[pipe]:
                if dx + dx2 == 0 and dy + dy2 == 0:
                    q.append((1, (sx + dx, sy + dy)))

    dists = {(sx, sy): 0}

    while q:
        d, (x, y) = q.popleft()

        if (x, y) in dists:
            continue
        dists[(x, y)] = d

        for dx, dy in pipes[grid[y][x]]:
            q.append((d + 1, (x + dx, y + dy)))

    inside = 0

    for y, row in enumerate(grid):
        pipecount = 0
        for x, char in enumerate(row):
            if (x, y) in dists:
                continue

            intersections = 0
            x2, y2 = x, y
            while x2 < len(row) and y2 < len(grid):
                if (x2, y2) in dists and grid[y2][x2] not in {"L", "7"}:
                    intersections += 1
                x2 += 1
                y2 += 1

            if intersections % 2 != 0:
                inside += 1

    return inside


print(part1())  # for test data 1 -> 4, for test data 2 -> 8
print(part2())


graph = [row for row in data]


for r, pipes in enumerate(graph):
    graph[r] = pipes.translate(str.maketrans("-|F7LJ.", "─│┌┐└┘ "))

for l in graph:
    print(l)
