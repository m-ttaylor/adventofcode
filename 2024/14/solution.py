from collections import defaultdict, Counter
from functools import reduce
from utils import aoc

YEAR = 2024
DAY = 14
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

robots = {}
velocities = {}
grid = {}

for i, line in enumerate(data):
    parts = line.split()
    x, y = map(int, parts[0].split("=")[1].split(","))
    vx, vy = map(int, parts[1].split("=")[1].split(","))
    robots[i] = [x, y]
    velocities[i] = vx, vy

if TEST:
    width, height = 11, 7
else:
    width, height = 101, 103

def printgrid(grid):
    for y in range(height):
        row = [str(grid.get((x, y), 0)) if grid.get((x, y), 0) != 0 else "." for x in range(width)]
        print("".join(row))

def calculateSafety():
    z1, z2, z3, z4 = 0, 0, 0, 0
    for x in range(width // 2):
        for y in range(height // 2):
            z1 += grid.get((x, y), 0)
        for y in range(height//2 + 1, height):
            z2 += grid.get((x, y), 0)
    
    for x in range(width//2+1, width):
        for y in range(height // 2):
            z3 += grid.get((x, y), 0)
        for y in range(height//2 + 1, height):
            z4 += grid.get((x, y), 0)
    return z1*z2*z3*z4

def updateGrid():
    grid.clear()
    for r, (x, y) in robots.items():
        grid[(x, y)] = grid.get((x, y), 0)+1

minVariance = float('inf')
pt2 = float('inf')
treegrid = None
for part2 in (False, True):
    updateGrid()
    for i in range(8_000 if part2 else 100):
        for j in robots:
            x, y = robots[j]
            vx, vy = velocities[j]
            nx, ny = robots[j] = (x+vx)%width, (y+vy)%height
        
        if part2:
            updateGrid()
            x_coords, y_coords = zip(*grid.keys())
            x_mean = sum(x_coords) / len(x_coords)
            y_mean = sum(y_coords) / len(y_coords)
            x_variance = sum([(x-x_mean)**2 for x in x_coords]) / len(x_coords)
            y_variance = sum([(y-y_mean)**2 for y in y_coords]) / len(y_coords)
            variance = (x_variance+y_variance)/2

            if variance < minVariance:
                minVariance = variance
                pt2 = i
                treegrid = grid.copy()

        else:
            updateGrid()
            
    if not part2:
        printgrid(grid)
        print("part1", calculateSafety())

printgrid(treegrid)
print("part2", pt2+101) # account for pt 1 iterating through 100 times already and starting at zero