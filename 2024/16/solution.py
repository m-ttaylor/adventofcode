from collections import defaultdict, Counter
from enum import Enum
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 16
TEST = True

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

grid = {}

width, height = len(data[0]), len(data)

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "#":
            # grid[x + y*1j] = "#"
            grid[x, y] = "#"
        if c == "S":
            start = x, y
            # start = x + y*1j
        if c == "E":
            # end = x + y*1j
            end = x, y

# def printgrid():
#     for line in grid:
#         print(line)
def printgrid():
    for y in range(height):
        # print("".join(grid.get(r+c*1j, ".")  for c in range(width)))
        print("".join(grid.get((x, y), ".") if (x, y) != start else "S" for x in range(width)))

def inbounds(pos):
    x, y = pos
    return 0 <= x < width and 0 <= y < height

# def inbounds(coord: complex):
#     return 0 <= coord.real < width and 0 <= coord.imag < height

printgrid()

# dirs = {"N": - 1j, "E": 1 + 0j, "S": 0 + 1j, "W": -1 + 0j}
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)

drunes = {
    N: "^",
    E: ">",
    S:  "v",
    W: "<"
}

def dijkstra(start: tuple[int, int], end: tuple[int, int]):
    heap = [(0, E, start)]
    visited = set()
    path = []
    while heap:
        cost, facing, (ux, uy) = heappop(heap)
        if (ux, uy) in visited:
            continue
        path.append((drunes[facing], (ux, uy)))
        visited.add((ux, uy))
        if (ux, uy )== end:
            return cost, path
        for v, d, in (((ux+dx, uy+dy), (dx, dy)) for (dx, dy) in (N, E, S, W)):
            c = max(abs(dirs.index(facing) - dirs.index(d))*1000, 1)
            print(c)
            if not inbounds(v) or v in visited or grid.get(v) == "#":
                continue

            heappush(heap, (cost+c, d, v))
                
    return -1, path



pt1, path = dijkstra(start, end)
for (rune, (x, y)) in path:
    grid[x, y] = rune
printgrid()
pt2 = 0

print("pt1", pt1)

print(pt2)

