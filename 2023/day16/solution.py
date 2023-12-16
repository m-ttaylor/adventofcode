import sys
from numpy import array

from utils import aoc

sys.setrecursionlimit(4000)  # 4x the default max

TEST = False

data = aoc.getInput(2023, 16, TEST)
contraption = array([list(line) for line in data])

NORTH, EAST, SOUTH, WEST = (0, -1), (1, 0), (0, 1), (-1, 0)  # x, y vectors

w, h = contraption.shape

# NUMPY IS ROW, COLUMN ACCESS
print(contraption.shape)

lightSymbol = {NORTH: "^", EAST: ">", SOUTH: "v", WEST: "<"}


def emit(sx, sy, dir):
    dx, dy = dir

    def inBounds(x, y):
        return 0 <= x + dx < w and 0 <= y + dy < h

    if inBounds(sx, sy):
        nx, ny = sx + dx, sy + dy

        if ((ny, nx), dir) in memo:
            return

        memo.add(((ny, nx), dir))
        lit.add((ny, nx))

        if contraption[ny, nx] not in {"|", "-", "\\", "/"}:
            contraption[ny, nx] = lightSymbol[dir]

        match contraption[ny, nx]:
            case "|":
                if dir in (EAST, WEST):
                    emit(nx, ny, NORTH)
                    emit(nx, ny, SOUTH)
                else:
                    emit(nx, ny, dir)
            case "\\":
                if dir == NORTH:
                    emit(nx, ny, WEST)
                elif dir == EAST:
                    emit(nx, ny, SOUTH)
                elif dir == SOUTH:
                    emit(nx, ny, EAST)
                elif dir == WEST:
                    emit(nx, ny, NORTH)
            case "/":
                if dir == NORTH:
                    emit(nx, ny, EAST)
                elif dir == EAST:
                    emit(nx, ny, NORTH)
                elif dir == SOUTH:
                    emit(nx, ny, WEST)
                elif dir == WEST:
                    emit(nx, ny, SOUTH)
            case "-":
                if dir in (NORTH, SOUTH):
                    emit(nx, ny, EAST)
                    emit(nx, ny, WEST)
                else:
                    emit(nx, ny, dir)
            case _:
                emit(nx, ny, dir)


lit = set()
memo = set()
emit(-1, 0, EAST)
print("part 1:", len(lit))

# Sure, we could do something clever...
mostEnergized = 0

for y in range(h):  # west edge
    lit = set()
    memo = set()
    emit(-1, y, EAST)
    mostEnergized = max(mostEnergized, len(lit))

for x in range(w):  # north edge
    lit = set()
    memo = set()
    emit(x, -1, SOUTH)
    mostEnergized = max(mostEnergized, len(lit))

for y in range(h):  # south edge
    lit = set()
    memo = set()
    emit(h + 1, y, NORTH)
    mostEnergized = max(mostEnergized, len(lit))

for x in range(w):  # east edge
    lit = set()
    memo = set()
    emit(x, w + 1, WEST)
    mostEnergized = max(mostEnergized, len(lit))

print("part 2:", mostEnergized)
