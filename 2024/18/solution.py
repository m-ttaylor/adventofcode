from bisect import bisect
from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heappop, heappush

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

dirsj = (-1j, 1 + 0j, 1j, -1 + 0j)

YEAR = 2024
DAY = 18
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

bytes = 12 if TEST else 1024

if TEST:
    width, height = 7, 7
else:
    width, height = 71, 71

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = "."

corruption = []

for i, line in enumerate(data):
    x, y = map(int, line.split(","))
    grid[x, y] = "#"
    corruption.append((x, y))

for r in range(height):
    print(" ".join(grid.get((c, r)) for c in range(width)))

goal = width-1, height-1

def bfs(bytes):
  
    queue = deque([(0, (0, 0))])
    visited = {*corruption[:bytes]}

    while queue:
        dist, (x, y) = queue.popleft()
        if (x, y) == goal:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
    
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) in grid and (nx, ny) not in visited:
                queue.append((dist+1, (nx, ny)))
                
    return 1e9

print("part 1\n", bfs(bytes))

blocking_byte = corruption[bisect(range(len(corruption)), 1e9-1, key=bfs)-1]
print("part 2\n", ",".join(map(str, blocking_byte)))

