from collections import defaultdict, Counter
from functools import cache, reduce


YEAR = 2024
DAY = 6
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")


grid = [list(line) for line in data]
rows, cols = len(grid), len(grid[0])


def inbounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


pt1 = 0
guard = None

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val in ("^", ">", "<", "v"):
            guard = r + c * 1j
            break

visited = set()
d = -1 + 0j
pos = guard
visited.add(pos)

while inbounds(pos.real, pos.imag):

    gr, gc = int(pos.real), int(pos.imag)
    newguard = pos + d
    nr, nc = map(int, (newguard.real, newguard.imag))
    if TEST:
        grid[gr][gc] = "X"

    if inbounds(newguard.real, newguard.imag) and grid[nr][nc] == "#":
        d *= -1j
    else:
        pos = newguard
        visited.add(pos)


print(len(visited) - 1)


@cache
def turningWouldCycle(r, c):

    pos = guard
    d = -1 + 0j
    path = set()

    while inbounds(pos.real, pos.imag):
        if (pos, d) in path:
            return True

        path.add((pos, d))
        newpos = pos + d
        nr, nc = map(int, (newpos.real, newpos.imag))

        if inbounds(newpos.real, newpos.imag) and grid[nr][nc] == "#":
            d *= -1j
        else:
            pos = newpos

    return False


pt2 = 0

for r, row in enumerate(grid):
    for c, val in enumerate(row):

        if grid[r][c] == "." and (r + c * 1j) in visited:
            grid[r][c] = "#"
        else:
            continue

        if turningWouldCycle(r, c):
            pt2 += 1

        grid[r][c] = "."

print(pt2)
