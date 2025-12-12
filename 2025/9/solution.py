from collections import Counter, defaultdict
import numpy as np
from functools import reduce
from math import prod, sqrt, dist
from itertools import combinations, pairwise
from heapq import heappush, heappop, nlargest

YEAR = 2025
DAY = 9
TEST = False

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left


file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")


def printGrid(leftbound, topbound, rightbound, botbound):
    print("".join([str(i) for i in range(max(0, leftbound - 5), rightbound + 5)]))
    for r in range(max(0, topbound - 5), botbound + 5):
        line = []
        for c in range(max(0, leftbound - 5), rightbound + 5):
            # if (c, r) in largestRectangle:
            #     line.append("O")
            if (c, r) in corners:
                line.append("#")
            elif (c, r) in outside:
                line.append("z")
            else:
                line.append(".")
        print(str(r) + "".join(line))


corners = []

for line in data:
    x, y = map(int, line.split(","))

    corners.append((x, y))
    # if prev:
    #     px, py = prev
    #     if py == y:  # horizontal movement
    #         for i in range(min(x, px), max(x, px)):
    #             corners.add((i, y))
    #     if px == x:  # vertical movement:
    #         for j in range(min(y, py) + 1, max(y, py)):
    #             corners.add((x, j))
    # prev = (x, y)


rectangles = []
pt1 = 0
for x1, y1 in corners:
    for x2, y2 in corners:
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        pt1 = max(pt1, area)
        rectangles.append(
            (area, (min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))
        )


rectangles.sort(reverse=True)

_, (x1, y1), (x2, y2) = rectangles[0]

print(pt1)

for area, (x1, y1), (x2, y2) in rectangles:
    for (ax, ay), (bx, by) in pairwise(corners + [corners[0]]):
        # print(area, (ax, ay), (bx, by))
        if ax < x2 and ay < y2 and bx > x1 and by > y1:
            break
    else:
        print(area)
        break


# red = list(map(eval, open("in.txt")))


def area(x, y, u, v):
    return (u - x + 1) * (v - y + 1)


pairs, lines = [
    sorted(
        ((min(a, c), min(b, d), max(a, c), max(b, d)) for (a, b), (c, d) in pair),
        key=lambda p: area(*p),
        reverse=True,
    )
    for pair in (combinations(corners, 2), pairwise(corners + [corners[0]]))
]

print("p1:", area(*pairs[0]))

for x, y, u, v in pairs:
    for p, q, r, s in lines:
        if p < u and q < v and r > x and s > y:
            break

    else:
        print("p2:", area(x, y, u, v))
        break
# printGrid(leftbound, topbound, rightbound, botbound)
