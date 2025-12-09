import numpy as np
from functools import reduce
from math import prod, sqrt, dist
import itertools
from heapq import heappush, heappop, nlargest

YEAR = 2025
DAY = 8
TEST = True

file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"


def eucDist(x1, y1, z1, x2, y2, z2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


with open(file) as f:
    data = f.read().strip().split("\n")

jboxes = []
heap = []
for line in data:
    x, y, z = map(int, line.split(","))
    jboxes.append((x, y, z))

# print(jboxes))
seen = set()
for p1 in jboxes:
    for p2 in jboxes:
        if p1 != p2 and (st := tuple(sorted((p1, p2)))) not in seen:
            heappush(heap, (dist(p1, p2), p1, p2))
            seen.add(st)

# print(heap)
connections = 0
target = 10 if TEST else 1000
circuits = {}
foo = set()
# foo.upd

while connections < target and heap:
    d, p1, p2 = heappop(heap)
    print(f"creating connection between {p1} and {p2}")
    updatedCircuit = False
    # if d in circuits:
    #     circuits[d].add(p1)
    #     circuits[d].add(p2)
    # else:
    for k in circuits:
        if p1 in circuits[k] and p2 in circuits[k]:
            continue
        if p1 in circuits[k]:
            circuits[k].add(p2)
            updatedCircuit = True
            break
        if p2 in circuits[k]:
            circuits[k].add(p1)
            updatedCircuit = True
            break
    if not updatedCircuit:
        circuits[p1] = {p1, p2}
    connections += 1
    print(len(circuits))
print()
print(connections)
print()
# print(heap)

print(circuits)
print(len(circuits.values()))
print(len(circuits))

threeLargestCircuits = nlargest(3, (len(circuit) for circuit in circuits.values()))
print(threeLargestCircuits)
print(prod(threeLargestCircuits))

# # start = data[0].index("S")

# pt1, pt2 = 0, 0


# print(pt1)
# print(pt2)
# # print(prod, )
