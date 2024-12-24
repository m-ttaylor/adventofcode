from collections import defaultdict, Counter, deque
from functools import cache, reduce
from heapq import heappop, heappush

YEAR = 2024
DAY = 19
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

towels = data[0].split(", ")
designs = data[2:]

@cache
def canDesign(design: str):
    if design == "":
        return True
    return sum(
        canDesign(design.removeprefix(towel)) for towel in towels if design.startswith(towel)
    )

pt1 = 0
pt2 = 0
for design in designs:
    foo = canDesign(design)
    pt1 += 1 if foo else 0
    pt2 += foo

print(pt1)
print(pt2)