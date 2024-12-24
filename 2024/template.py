from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 13
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")
    grid = list(map(list, f.read().strip().split("\n")))

width, height = len(grid)[0], len(grid)
def printgrid():
    for line in grid:
        print(line)

def inbounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def inbounds(coord: complex):
    return 0 <= coord.real < width and 0 <= coord.imag < height

pt1 = 0      
pt2 = 0

print(pt1)

print(pt2)

