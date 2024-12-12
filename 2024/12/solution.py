from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 12
TEST = True

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    grid = list(map(list, f.read().strip().split("\n")))

def printgrid():
    for line in grid:
        print(line)

def inbounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def findPerimeter(i, j, region: set, sides, area):
    
    neighbors = [
        (i+dr, j+dc) for dr, dc in fourDirs 
        if inbounds(i+dr, j+dc) 
        and grid[i+dr][j+dc] == grid[i][j]
    ]

    for dr, dc in fourDirs:
        if not inbounds(i+dr, j+dc) or (i+dr, j+dc) not in neighbors:
            perimeter.add(((i, j), (i+dr, j+dc)))
    
    region.add((i, j))
    sides += 4 - len(neighbors)
    neighbors = filter(lambda n: n not in region, neighbors)
    
    for nr, nc in neighbors:
        sides, area, region = findPerimeter(nr, nc, region, sides, area+1)

    return sides, area, region

pt1 = 0      
pt2 = 0

regions = []
perimeters: list[set] = []
for i, r in enumerate(grid):
    for j, plant in enumerate(r):

        if all((i, j) not in region for region in regions):
            perimeter = set()
            price = findPerimeter(i, j, set(), 0, 1)
            
            pt1 += price[0]*price[1]
            regions.append(price[2])
            perimeters.append(perimeter)
            edges = set()
            for (ar, ac), (br, bc) in perimeter:
                keep = True
                for dr, dc in ((0, 1), (1, 0)):
                    na = ar+dr, ac+dc
                    nb = br+dr, bc+dc
                    if (na, nb) in perimeter:
                        keep = False
                if keep:
                    edges.add(((ar, ac),  (br, bc)))

            if TEST: 
                print("pt1:", grid[i][j], "region has a price", price)
                print(len(perimeter))
                print(f"pt2: {plant} region has a price {len(edges), price[1]}")
                print("-"*25)
            pt2 += len(edges) * price[1]

print(pt1)

print(pt2)

