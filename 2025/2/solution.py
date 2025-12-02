from bisect import bisect
from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heappop, heappush
import re

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

dirsj = (-1j, 1 + 0j, 1j, -1 + 0j)

YEAR = 2025
DAY = 2
TEST = False
file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split(",")

pt1 = 0
pt2 = 0

for line in data:
    left, right = map(int, line.split("-"))
    for id in range(left, right+1):
        strid = str(id)
        mid = len(strid)//2
        if strid[:mid] == strid[mid:]:
            pt1 += id
        if re.match(r'^(\d+)\1$', strid):
            pt1 += id
        if re.match(r'(\d+)\1+$', strid):
            pt2 += id

            


  
print(pt1)
print(pt2)