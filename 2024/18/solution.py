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

# grid = [["." for x in range(width)] for y in range(height)]
grid = {}
for x in range(width):
    for y in range(height):
        # grid[i + j*1j] = "."
        grid[x, y] = "."
        # grid[y][x] = "."

corruption = []

for i, line in enumerate(data):
    x, y = map(int, line.split(","))
    # print((x, y))
    grid[x, y] = "#"
    # grid[y][x] = "#"
    # grid[x + y*1j] = "#"
    corruption.append((x, y))
    # corruption.append(x + y*1j)
    # if i == bytes:
    #     break

# print(grid)
# for row in grid:
#     print(" ".join(row))
for r in range(height):
    print(" ".join(grid.get((c, r)) for c in range(width)))
# print(corruption)
# for r in range(height+1):
#     print(" ".join(["#" if c + r*1j in corruption[:bytes] else "." for c in range(width+1)]))

# print(grid)
# goal = width + height*1j
goal = width-1, height-1

# print("corruption", corruption)
def bfs(bytes):
    # visited = {*corruption[:bytes]}
    # queue = [(0, (0j))]
    queue = deque([(0, (0, 0))])
    # visited = set()
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
            # if (nx, ny) in grid and grid[nx, ny] != "#":
            # if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] != "#":
            if (nx, ny) in grid and (nx, ny) not in visited:
                queue.append((dist+1, (nx, ny)))
                # visited.add((nx, ny))
    return 1e9

print(bfs(bytes))

for i in range(len(corruption)):
    if bfs(i) == 1e9:
        print(",".join(map(str, corruption[i-1])))
        break

