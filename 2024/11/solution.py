from collections import defaultdict, Counter
from functools import cache, reduce
from heapq import heappop, heappush
from math import floor, log10

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 11
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    stones = list(map(int, f.read().strip().split(" ")))
        
print(stones)

# my dumbass modified the original input so pt 2 was using the simulated output of pt1...
pt1 = []

for step in range(25):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(s:= str(stone))%2 == 0:
            newStones.extend([int(s[:len(s)//2]), int(s[len(s)//2:])])
        else:
            newStones.append(stone * 2024)
    stones = newStones
print(len(stones))


@cache
def simulate(stone: int, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return simulate(1, steps-1)
    if len(s := str(stone))%2 == 0:
        return simulate(int(s[:len(s)//2]), steps-1) + simulate(int(s[len(s)//2:]), steps-1)

    return simulate(stone*2024, steps-1)

with open(file) as f:
    stones = list(map(int, f.read().strip().split(" ")))
print("part2", sum(simulate(stone, 75) for stone in stones))
