from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 15
TEST = False

file = f"{YEAR}/{DAY}/test2.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n\n")
    griddata = data[0].split("\n")
    commands = "".join(data[1].split("\n"))

if TEST:
    print(griddata)
    print(commands)

robot = None
rows = len(griddata)
cols = len(griddata[0])
grid: dict[complex, str] = {}

for r, row in enumerate(griddata):
    for c, col in enumerate(row):
        grid[r+c*1j] = col
        if col == "@":
            robot = r+c*1j

def printgrid():
    for r in range(rows):
        print("".join(grid.get(r+c*1j, ".") if r+c*1j != robot else "@" for c in range(cols)))

vectors = {
    "^": -1 + 0j,
    ">": 0 + 1j,
    "v": 1 + 0j,
    "<": 0 - 1j
}

if TEST:
    printgrid()
    print()


for move in commands:
    v = vectors[move]
    next_robot = robot+v

    if next_robot in grid and grid[next_robot] != "#":
        if grid[next_robot] == ".":
            grid[robot] = "."
            robot = next_robot
        elif grid[next_robot] == "O":
            # shoot vector until a wall and confirm at least one open space
            ahead = next_robot
            while grid.get(ahead) == "O":
                ahead += v
            
            if grid[ahead] != "#" and grid[ahead] != "O" and ahead != next_robot:
                if TEST: print(f"  and there is space to push because {ahead} {grid[ahead]} is open")
                grid[robot] = "."
                grid[ahead] = "O"
                robot = next_robot
        if TEST: printgrid()

    
pt1 = 0
for pos in grid.keys():
    if grid[pos] == "O":
        pt1 += int(pos.real)*100 + int(pos.imag)

print("part 1", pt1)

##############
# end part 1 #
##############

def canPush(pos: complex, v: complex):
    pos += v
    if grid[pos] == "#":
        return False
    if grid[pos] == ".":
        return True
    if v.imag == 0:
        if grid[pos] == "]":
            return canPush(pos, v) and canPush(pos-1j, v)
        elif grid[pos] == "[":
            return canPush(pos, v) and canPush(pos+1j, v)
    elif v.imag == -1:
        if grid[pos] == "]":
            return canPush(pos-1j, v)
    elif v.imag == 1:
        if grid[pos] == "[":
            return canPush(pos+1j, v)
        
def push(pos: complex, v: complex):
    newPos = pos+v
    if grid[newPos] == ".":
        grid[pos], grid[newPos] = grid[newPos], grid[pos]
    elif v.imag == 0: # vector is vertical
        if grid[newPos] == "]":
            # push above/down and to its left
            push(newPos, v)
            push(newPos-1j, v)
        elif grid[newPos] == "[":
            # push above/down and to its right
            push(newPos, v)
            push(newPos+1j, v)
        grid[pos], grid[newPos] = grid[newPos], grid[pos]
    elif v.imag == -1: # left
        if grid[newPos] == "]":
            push(newPos-1j, v)
            grid[newPos-1j], grid[newPos], grid[newPos-v] = grid[newPos], grid[newPos-v], grid[newPos-1j]
    elif v.imag == 1: #right
        if grid[newPos] == "[":
            push(newPos+1j, v)
            grid[newPos+1j], grid[newPos], grid[newPos-v] = grid[newPos], grid[newPos-v], grid[newPos+1j]

robot = None
rows = len(griddata)
cols = len(griddata[0]*2)
grid.clear()

for r, row in enumerate(griddata):
    for c, col in enumerate(row):
        match(col):
            case "#":
                grid[r+(c*2)*1j] = "#"
                grid[r+(c*2+1)*1j] = "#"
            case "O":
                grid[r+(c*2)*1j] = "["
                grid[r+(c*2+1)*1j] = "]"
            case ".":
                grid[r+(c*2)*1j] = "."
                grid[r+(c*2+1)*1j] = "."
            case "@":
                grid[r+(c*2)*1j] = "@"
                grid[r+(c*2+1)*1j] = "."
                robot = r+(c*2)*1j


printgrid()

for move in commands:
    v = vectors[move]
    
    if canPush(robot, v):
        push(robot, v)
        robot = robot+v
    
        if TEST: printgrid()

pt2 = 0

for pos in grid.keys():
    if grid[pos] == "[":
        pt2 += int(pos.real)*100 + int(pos.imag)

print("part 2", pt2)

