from collections import defaultdict, Counter
from enum import Enum
from functools import reduce
from heapq import heappop, heappush

YEAR = 2024
DAY = 16
TEST = False

file = f"{YEAR}/{DAY}/test2.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

grid = {}

width, height = len(data[0]), len(data)

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c != "#":
            grid[x, y] = c
        if c == "S":
            start = x, y
        if c == "E":
            end = x, y

def printgrid():
    for y in range(height):
        print("".join(grid.get((x, y), "#") if (x, y) != start else "S" for x in range(width)))

def inbounds(pos):
    x, y = pos
    return 0 <= x < width and 0 <= y < height

if TEST:
    printgrid()

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
    dist = defaultdict(lambda: 1e9)
    best = 1e9
    heap = [(0, E, start, [start])]
    visited = []
    while heap:
        cost, facing, (ux, uy), path = heappop(heap)
        if cost > dist[(ux, uy), facing]:
            continue
        dist[(ux, uy), facing] = cost
    
        if (ux, uy) == end and cost <= best:
            visited.extend(path)
            best = cost
     
        for v, d, in (((ux+dx, uy+dy), (dx, dy)) for (dx, dy) in (N, E, S, W)):
            c = 1
            findex, dindex = dirs.index(facing), dirs.index(d)
            if  abs(dindex-findex) == 1 or abs(dindex-findex) == 3:
                c += 1000
            elif abs(dindex-findex) == 2:
                c += 2000
            if v not in grid:
                continue

            heappush(heap, (cost+c, d, v, [*path, (ux, uy)]))
    
    return best, path, visited


pt1, path, visited = dijkstra(start, end)

if TEST or True:
    printgrid()
    print(len(path))

print("pt1", pt1)
print("pt2", len(set(visited))+1)

