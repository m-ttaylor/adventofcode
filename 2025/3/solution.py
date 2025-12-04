from bisect import bisect
from collections import defaultdict, Counter, deque
from itertools import combinations
from functools import reduce
from heapq import heappop, heappush, nlargest
import re

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

dirsj = (-1j, 1 + 0j, 1j, -1 + 0j)

YEAR = 2025
DAY = 3
TEST = False
file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

pt1 = 0
pt2 = 0

for bank in data:
    largest = 0
    for a, b in combinations(map(int, bank), 2):
        largest = max(largest, a*10+b)
    pt1 += largest

    largest = 0
    for left in range(len(bank)-12):
        largest = max(largest, int(left))

    largest = max(l+k*10+j*100+i*1000+h*10_000+g*100_000+f*1_000_000+e*10_000_000+d*100_000_000+c*1_000_000_000+b*10_000_000_000+a*100_000_000_000 for a, b, c, d, e, f, g, h, i, j, k, l in combinations(map(int, bank), 12))
    pt2 += largest
    # line = [(val, i) for i, val in enumerate(map(int, bank))]
    # a, ai = max(line)
    # if ai == len(line)-1:
    #     a, ai = max(line[:len(line)-1])
    # b, bi = max(line[ai+1:])

    # print(f"{a}{b}")
    # pt1 += a*10+b
    
    # largest = nlargest(2, ((val, i) for i, val in enumerate(map(int, bank))))
    # a = largest[0][0] if largest[0][1] < largest[1][1] else largest[1][0]
    # b = largest[1][0] if largest[1][1] > largest[0][1] else largest[0][0]
    # print(f"{a}{b}")
    # pt1 += a*10+b
    # pt1 += sum(nlargest(2, map(int, bank)))

            
print(pt1)
print(pt2)