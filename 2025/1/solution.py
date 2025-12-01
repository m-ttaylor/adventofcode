from bisect import bisect
from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heappop, heappush

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

dirsj = (-1j, 1 + 0j, 1j, -1 + 0j)

YEAR = 2025
DAY = 1
TEST = False
file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

pt1 = 0
pt2 = 0

pos = 50
for line in data:
    d, dist = line[0], int(line[1:])
    for i in range(dist):
        match d:
            case 'L':
                pos = (pos-1)%100
            
            case 'R':
                pos = (pos+1)%100
        if pos == 0:
            pt2 += 1

    if pos == 0:
        pt1 += 1
  
print(pt1)
print(pt2)