from collections import defaultdict
from utils import aoc
from utils.aoc import dirs
import sys

sys.setrecursionlimit(10000)

data = aoc.getInput(2023, 23, False)
graph = [list(l) for l in data]

n, m = len(graph), len(graph[0])
start = 0, 1
stop = n - 1, m - 2


def adj(pos, part=2):
    px, py = pos
    adjs = list(dirs)
    if part == 1 and graph[px][py] in "^>v<":
        adjs = {"^": [(-1, 0)], ">": [(0, 1)], "v": [(1, 0)], "<": [(0, -1)]}[
            graph[px][py]
        ]
    for dx, dy in adjs:
        nx, ny = px + dx, py + dy
        if nx in range(n) and ny in range(m) and graph[nx][ny] != "#":
            yield (nx, ny)


longest = 0


def dfs(cur, path, pathset):
    global best
    if cur == (n - 1, m - 2):
        best = max(best, len(path))
    for a in adj(cur, part=1):
        if a not in pathset:
            path.append(a)
            pathset.add(a)
            dfs(a, path, pathset)
            pathset.remove(a)
            path.pop(-1)


best = 0

dfs((0, 1), [], set())
print("part 1", best)


v = set()
gd = defaultdict(list)

for i in range(n):
    for j in range(m):
        if graph[i][j] != "#":
            neighbors = len(list(adj((i, j))))
            if neighbors > 2:
                v.add((i, j))

v.add(start)
v.add(stop)

for x, y in v:
    q = []
    q.append((x, y))
    visited = {(x, y)}
    dist = 0

    while q:
        nq = []
        dist += 1
        for c in q:
            for a in adj(c):
                if a not in visited:
                    if a in v:
                        gd[x, y].append((dist, a))
                        visited.add(a)
                    else:
                        visited.add(a)
                        nq.append(a)
        q = nq


best = 0


def dfs2(cur, pathset, totaldist):
    global best
    if cur == stop:
        best = max(best, totaldist)
    for da, a in gd[cur]:
        if a not in pathset:
            pathset.add(a)
            dfs2(a, pathset, totaldist + da)
            pathset.remove(a)


dfs2((0, 1), set(), 0)
print("part 2", best)
