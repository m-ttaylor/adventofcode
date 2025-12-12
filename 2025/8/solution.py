from collections import Counter, defaultdict
import numpy as np
from functools import reduce
from math import prod, sqrt, dist
import itertools
from heapq import heappush, heappop, nlargest

YEAR = 2025
DAY = 8
TEST = False

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


for i, p1 in enumerate(jboxes):
    for j, p2 in enumerate(jboxes):
        if (d := dist(p1, p2)) > 0:
            heappush(heap, (d, i, j))
            # heappush(heap, (dist(p1, p2), p1, p2))
            # seen.add(st)

circuits = {i: i for i in range(len(jboxes))}
# print(heap)
connections = 0
target = 10 if TEST else 1000
# circuits = {i: i for i in range(len(data))}


def find(x):
    if x == circuits[x]:
        return x
    circuits[x] = find(circuits[x])
    return circuits[x]


def merge(x, y):
    circuits[find(x)] = find(y)


# foo = set()
# foo.upd

while heap:
    d, p1, p2 = heappop(heap)
    if find(p1) != find(p2):
        connections += 1
        # if connections == len(data)-1:
        merge(p1, p2)
    if connections == target:
        break

conns = Counter()
for x in range(len(jboxes)):
    conns[find(x)] += 1

threeLargestCircuits = nlargest(3, (x for x in conns.values()))
print(threeLargestCircuits)
print(prod(threeLargestCircuits))


# print(f"creating connection between {p1} and {p2}")
# updatedCircuit = False
# # if d in circuits:
# #     circuits[d].add(p1)
# #     circuits[d].add(p2)
# # else:
# for k in circuits:
#     if p1 in circuits[k] and p2 in circuits[k]:
#         continue
#     if p1 in circuits[k]:
#         circuits[k].add(p2)
#         updatedCircuit = True
#         break
#     if p2 in circuits[k]:
#         circuits[k].add(p1)
#         updatedCircuit = True
#         break
# if not updatedCircuit:
#     circuits[p1] = {p1, p2}
# connections += 1
# print(len(circuits))
# print()
# print(connections)
# print()
# # print(heap)

# print(circuits)
# print(len(circuits.values()))
# print(len(circuits))


# # start = data[0].index("S")

# pt1, pt2 = 0, 0


# print(pt1)
# print(pt2)
# # print(prod, )
