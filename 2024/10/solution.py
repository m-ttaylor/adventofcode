from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 10
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

grid = [list(map(int, line)) for line in data]
rows, cols = len(grid), len(grid[0])


def inBounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


starts = []
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 0:
            starts.append((r, c))


def findTrail(pos, trailheads):
    heap = [pos]
    visited = {pos}

    while heap:
        pr, pc = heap.pop()

        for nr, nc in ((pr + dr, pc + dc) for (dr, dc) in fourDirs if inBounds(pr + dr, pc + dc)):
            if (nr, nc) not in visited:
                if grid[nr][nc] == grid[pr][pc] + 1:
                    if grid[nr][nc] == 9:
                        trailheads += 1
                    heap.append((nr, nc))
                    visited.add((nr, nc))

    return trailheads


def findDistinct(pos, path, height):
    pr, pc = pos

    if (pr, pc) not in path and inBounds(pr, pc) and grid[pr][pc] == height:
        if grid[pr][pc] == 9:
            return 1

        return sum(
            findDistinct((pr + dr, pc + dc), (*path, pos), height + 1)
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0))
        )
    return 0


pt1 = 0

for start in starts:
    pt1 += findTrail(start, 0)

print(pt1)

pt2 = 0

for start in starts:
    pt2 += findDistinct(start, (), 0)

print(pt2)
