from collections import defaultdict
from utils import aoc
import numpy as np

data = aoc.getInput(2023, 22, False)

coords = []

bricks = []
for line in data:
    # print(line)
    a, b = line.split("~")
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]
    print(a, b)
    bricks.append((a, b))


bricks.sort(key=lambda b: b[0][2])


def droppedBrick(tallest, brick):
    ba, bb = brick
    peak = max(
        tallest[x, y] for x in range(ba[0], bb[0] + 1) for y in range(ba[1], bb[1] + 1)
    )
    dz = max(ba[2] - peak - 1, 0)
    return ((ba[0], ba[1], ba[2] - dz), (bb[0], bb[1], bb[2] - dz))


def drop(tower):
    tallest = defaultdict(int)
    newTower = []
    falls = 0
    for ba, bb in tower:
        nba, nbb = droppedBrick(tallest, (ba, bb))
        if nba[2] != ba[2]:
            falls += 1
        newTower.append((nba, nbb))
        for x in range(ba[0], bb[0] + 1):
            for y in range(ba[1], bb[1] + 1):
                tallest[x, y] = nbb[2]

    return falls, newTower


_, dropped = drop(bricks)
p1, p2 = 0, 0
for i in range(len(dropped)):
    removed = dropped[:i] + dropped[i + 1 :]
    falls, _ = drop(removed)
    if not falls:
        p1 += 1
    else:
        p2 += falls

print("-" * 20)
print(p1)
print(p2)
print("-" * 20)


def isSolid(bricks, x, y, z):
    if z == 0:
        return True
    # return (x, y, z) in bricks
    for ax, ay, az, bx, by, bz in bricks:
        if x in range(ax, bx + 1) and y in range(ay, by + 1) and z in range(az, bz + 1):
            return True

        # for ix in range(brick[0][0], brick[1][0]+1):
        #     for iy in range(brick[0][1], brick[1][1]+1):


n = len(bricks)

highest = defaultdict(lambda: (0, -1))
bad = set()
graph = [[] for i in range(n)]
for i, brick in enumerate(bricks):
    maxHeight = -1
    occupied = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if highest[x, y][0] + 1 > maxHeight:
                occupied = {highest[x, y][1]}
            elif highest[x, y][0] + 1 == maxHeight:
                occupied.add(highest[x, y][1])

    for x in occupied:
        if x != -1:
            graph[x].append(i)
    if len(occupied) == 1:
        bad.add(occupied.pop())

    fall = brick[0][2] - maxHeight
    if fall > 0:
        brick[0][2] -= fall
        brick[1][2] -= fall

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            highest[x, y] = (brick[1][2], i)


def count(i, graph):
    indeg = [0 for _ in range(n)]

    for j in range(n):
        for k in graph[j]:
            indeg[k] += 1
    queue = [i]
    count = -1
    while queue:
        count += 1
        x = queue.pop()
        for k in graph[x]:
            indeg[k] -= 1
            if indeg[k] == 0:
                queue.append(k)

    return count


print(len(bricks) - len(bad) + 1)
print("-" * 20)
print(sum(count(x, graph) for x in range(n)))

# read in blocks
# sort by z ascending, so we settle the lowest first
# count collisions in a dict?

# if bricks have a higher z, it's the second
