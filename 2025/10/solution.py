from collections import Counter, defaultdict
import numpy as np
from functools import cache, reduce
from math import prod, sqrt, dist
from itertools import combinations, pairwise
from heapq import heappush, heappop, nlargest
import re

YEAR = 2025
DAY = 10
TEST = False

file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

lights = []
goals = []
wirings = []
rest = []
for line in data:
    chunks = line.split()
    goal = 0
    for i, c in enumerate(chunks[0][1:-1]):
        if c == "#":
            goal |= 1 << i
    # print("goal", goal, bin(goal))
    buttons = []
    for chunk in chunks[1:-1]:
        mask = 0
        for c in chunk[1:-1].split(","):
            mask |= 1 << int(c)
        buttons.append(mask)
        # print("button", mask, bin(mask))

    rest = chunks[-1][1:-1]

    goals.append(goal)
    wirings.append(buttons)


def bfs(goal, buttons):
    visited = set()
    state = 0
    queue = [(state, 0)]
    steps = 0
    while queue:
        state, steps = queue.pop(0)
        for button in buttons:
            newState = state ^ button
            if newState == goal:
                return steps + 1
            if newState not in visited:
                queue.append((newState, steps + 1))
                visited.add(newState)


pt1, pt2 = 0, 0
for row in range(len(data)):
    buttons = wirings[row]
    goal = goals[row]
    steps = bfs(goal, buttons)
    print(steps)
    pt1 += steps


print("pt1", pt1)
print("pt2", pt2)
