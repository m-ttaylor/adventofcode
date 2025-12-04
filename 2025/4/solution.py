from bisect import bisect
from collections import defaultdict, Counter, deque
from itertools import combinations
from functools import reduce
from heapq import heappop, heappush, nlargest
import re
from typing import List

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left
dirs8 = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
dirsj = (-1j, 1 + 0j, 1j, -1 + 0j)

YEAR = 2025
DAY = 4
TEST = False
file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

pt1 = 0
pt2 = 0

graph = {}
grid = [["." for i in range(len(data[0]))] for j in range(len(data))]
for y, line in enumerate(data):
    for x, val in enumerate(line):
        if val == "@":
            graph[(x, y)] = 1
            grid[y][x] = "@"

for line in grid:
    print("".join(line))
print()

def countAdj(x, y):
    adj = 0
    for dx, dy in dirs8:
        if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid[0]) and grid[y+dy][x+dx] == "@":
            adj += 1
    return adj

def buildQueue(queue: List):
    moves = 0

    for x, y in graph:

        if graph[(x, y)] and (c := countAdj(x, y)) < 4:
            moves += 1
            grid[y][x] = "X"
            queue.append((x, y))

    return moves

queue = []
pt1 += buildQueue(queue)
pt2 += pt1

# 8665

while queue:
    while queue:
        x, y = queue.pop()
        grid[y][x] = "."
        graph[(x, y)] = 0
    pt2 += buildQueue(queue)

for line in grid:
    print("".join(line))

print()

for line in grid:
    print("".join(line))

print(pt1)
print(pt2)