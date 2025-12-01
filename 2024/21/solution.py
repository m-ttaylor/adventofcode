from collections import defaultdict, Counter, deque
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 21
TEST = True

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"


npad = ["789", "456", "123", " 0A"]
dpad = [" ^A", "<v>"]



with open(file) as f:
    codes = f.read().strip().split("\n")

print(codes)

ndists = [[1e9 for c in range(len(npad[0]))] for r in range(len(npad))]
ddists = [[1e9 for c in range(len(dpad[0]))] for r in range(len(dpad))]



def type(start, stop, path, pad):
    # for c in sequence
    
    dists = [[1e9 for _c in range(len(pad[0])+1)] for _r in range(len(pad)+1)]
    print(dists)
    r, c = start
    # queue = deque([(start, [start])])
    queue = [(0, start)]

    while queue:
        # (r, c), path = queue.popleft()
        cost, (r, c) = heappop(queue)

        if (r, c) == stop:
            return path
        
        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            nr, nc = r+dr, c+dc
            d = dists[nr][nc]
            if 0 <= nr < len(pad) and 0 <= nc < len(pad[0]):
                # type((nr, nc), stop, (*path, (nr, nc)), pad)
                # queue.append(
                #     ((nr, nc), path+[(nr, nc)])
                #     )
                dists[nr][nc] = cost + d
                heappush(queue, (cost + d, (nr, nc)))

    return 1e9

print(type((3, 2), (0, 0), [], npad))


# width, height = len(grid)[0], len(grid)
# def printgrid():
#     for line in grid:
#         print(line)

def inbounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def inbounds(coord: complex):
    return 0 <= coord.real < width and 0 <= coord.imag < height

pt1 = 0      
pt2 = 0

print(pt1)

print(pt2)

