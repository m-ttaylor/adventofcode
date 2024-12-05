from collections import defaultdict, Counter, deque
from functools import reduce, partial, cache
import sys

sys.setrecursionlimit(10_000)

YEAR = 2024
DAY = 5
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n\n")

rules = data[0].split("\n")
toprint = data[1].split("\n")

before = defaultdict(list)
outOfOrder = []
pt1 = 0

for rule in rules:
    a, b = list(map(int, rule.split("|")))
    before[b].append(a)

for i, pages in enumerate(toprint):
    print(pages)
    visited = set()
    sp = list(map(int, pages.split(",")))
    canPrint = True
    needsFirst = set()
    for page in sp:
        if page in needsFirst:
            outOfOrder.append(i)
            canPrint = False
            break
        for first in before[page]:
            needsFirst.add(first)

        visited.add(page)
    if canPrint:
        # print(f"middle of row is {sp[len(sp)//2]}")
        pt1 += sp[len(sp) // 2]


print(pt1)

pt2 = 0


@cache
def lookup(page, weight=0):
    firsts = before[page]

    if firsts:

        return max(lookup(first, weight + 1) for first in firsts)

    return weight


lookupKey = partial(lookup, weight=0)


def topSort(nodes: list):
    graph = {node: [] for node in nodes}
    indegree = {node: 0 for node in nodes}
    for a, b in [rule.split("|") for rule in rules]:
        if a in nodes and b in nodes:
            graph[a].append(b)
            indegree[b] += 1
    fixed = []
    queue = deque([node for node, deg in indegree.items() if deg == 0])
    while queue:
        current = queue.pop()
        fixed.append(current)
        for newnode in graph[current]:
            indegree[newnode] -= 1
            if indegree[newnode] == 0:
                queue.append(newnode)
    return fixed


for index in outOfOrder:
    badPages: str = toprint[index]
    fixed = topSort(badPages.split(","))
    pt2 += int(fixed[len(fixed) // 2])

print(pt2)
