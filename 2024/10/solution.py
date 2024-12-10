from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush


YEAR = 2024
DAY = 10
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

grid = [list(map(int, line)) for line in data]
rows, cols = len(grid), len(grid[0])
print(grid)

starts = []
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 0:
            starts.append((r, c))


pt1 = 0


def findTrail(pos, trailheads):
    heap = [pos]
    visited = {pos}

    while heap:
        pr, pc = heap.pop()

        for nr, nc in (
            (pr + dr, pc + dc)
            for (dr, dc) in ((0, 1), (1, 0), (0, -1), (-1, 0))
            if 0 <= pr + dr < rows and 0 <= pc + dc < cols
        ):
            if (nr, nc) not in visited:
                if grid[nr][nc] == grid[pr][pc] + 1:
                    if grid[nr][nc] == 9:
                        trailheads += 1
                    heap.append((nr, nc))
                    visited.add((nr, nc))

    return trailheads


def findDistinct(pos, path):
    pr, pc = pos
    if grid[pr][pc] == 9:
        paths.add(path)

    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = pr + dr, pc + dc
        if (
            0 <= pr + dr < rows
            and 0 <= pc + dc < cols
            and (nr, nc) not in path
            and grid[nr][nc] == grid[pr][pc] + 1
        ):

            findDistinct((nr, nc), (*path, (nr, nc)))


for start in starts:
    pt1 += findTrail(start, 0)


print(pt1)

pt2 = 0

for start in starts:
    paths = set()
    findDistinct(start, ())
    pt2 += len(paths)

print(pt2)
