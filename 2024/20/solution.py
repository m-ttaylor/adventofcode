from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 20
TEST = False

def neighbors(pos: complex):
    yield pos+1
    yield pos-1
    yield pos+1j
    yield pos-1j

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")
    # grid = list(map(list, f.read().strip().split("\n")))

grid = {}
start, end = None, None
# for row in data:
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c != "#":
            grid[x + y*1j] = c
            if c == "S":
                start = x + y*1j
            if c == "E":
                end = x + y*1j

print(grid)

width, height = len(data[0]), len(data)
def printgrid():
    # for line in grid:
    #     print(line)
    for y in range(height):
        print(" ".join("#" if x + y*1j not in grid else grid[x + y*1j] for x in range(width)))

def inbounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def inbounds(coord: complex):
    return 0 <= coord.real < width and 0 <= coord.imag < height

printgrid()

from_start = {start: 0}
queue = deque([start])

while queue:
    pos = queue.popleft()
    for npos in neighbors(pos):
         if npos in grid and npos not in from_start:
             from_start[npos] = from_start[pos]+1
             queue.append(npos)


from_end = {end: 0}
queue = deque([end])
while queue:
    pos = queue.popleft()
    for npos in neighbors(pos):
         if npos in grid and npos not in from_end:
             from_end[npos] = from_end[pos]+1
             queue.append(npos)


def mdist(a: complex, b: complex):
    return abs(a.real-b.real) + abs(a.imag-b.imag)
pt1 = 0
for pos in grid:
    for npos in neighbors(pos):
        for nnpos in neighbors(npos):
            odist, ndist = from_end.get(pos, 1e9), from_end.get(nnpos, 1e9)+2

            print(odist, ndist)
            if odist - ndist >= 100:
                pt1 += 1


pt2 = 0
for pos in grid:
    for opos in grid:
        if pos != opos and (d:= mdist(pos, opos)) <= 20:
            nd = from_end.get(opos, 1e9) + d
            if from_end.get(pos, 1e9) - nd >= 100:
                pt2 += 1

print(from_start)

print(pt1)
print(pt2)

