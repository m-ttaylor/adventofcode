from collections import defaultdict
import math
from utils import aoc
import heapq

TEST = False

data = aoc.getInput(2023, 17, TEST)

data = [[int(x) for x in line] for line in data]

print(data)

NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)
dirs = {NORTH, SOUTH, EAST, WEST}


def opposite(dir):
    match dir:
        case -1, 0:
            return SOUTH
        case 0, 1:
            return WEST
        case 1, 0:
            return NORTH
        case 0, -1:
            return EAST
        case _, _:
            return (0, 0)


pathGraph = [row.copy() for row in data]
symbolMap = {NORTH: "^", EAST: ">", SOUTH: "v", WEST: "<"}

rows = len(data)
cols = len(data[0])


def finalDijkstra(start, end, least, sameDirLimit):
    queue = [(0, start, (0, 0))]
    visited = set()

    while queue:
        heatloss, (x, y), (pdx, pdy) = heapq.heappop(queue)
        if (x, y) == end:
            return heatloss
        if ((x, y), (pdx, pdy)) in visited:
            continue
        visited.add(((x, y), (pdx, pdy)))
        for dx, dy in dirs - {(pdx, pdy), (-pdx, -pdy)}:
            nx, ny, newHeat = x, y, heatloss
            for i in range(1, sameDirLimit + 1):
                nx, ny = nx + dx, ny + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    newHeat += data[ny][nx]
                    if i >= least:
                        heapq.heappush(queue, (newHeat, (nx, ny), (dx, dy)))
    return -1


def cDijkstra(graph: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    dists = [[math.inf] * cols for r in range(rows)]
    heap = [(0, start, (0, 0))]  # heap of weight, position, previous dir
    visited = set()
    prevDir = (0, 0)
    prevPrevDir = (0, 0)
    sameDir = 0
    predecessors = [[None for c in range(cols)] for r in range(rows)]
    while heap:
        cost, (py, px), prevDir = heapq.heappop(heap)

        if (py, px) in visited:
            continue
        visited.add((py, px))

        if (py, px) == end:
            path = []
            while (py, px) != start:
                path.append((py, px))
                (ny, nx), (dy, dx) = predecessors[py][px]
                pathGraph[py][px] = symbolMap.get((py - ny, px - nx), "!")
                py, px = ny, nx
            path.append(start)
            path.reverse()
            pathGraph[end[0]][end[1]] = "𝕏"
            return dists[end[0]][end[1]], path

        print(f"DEBUG {prevDir=}")
        # symbol = symbolMap.get(prevDir, "!")
        # pathGraph[py][px] = symbol

        sameDir = sameDir + 1 if prevDir == prevPrevDir else 0
        print(f"running samedir count = {sameDir}")
        prevPrevDir = prevDir

        neighbors = dirs - set(opposite(prevDir))
        print(neighbors)
        if sameDir >= 3:
            print(
                f"moved the same direction 3 times in a row, removing it from options"
            )
            neighbors -= {prevDir}
            sameDir = 0

        for dy, dx in neighbors:
            ny, nx = ((py + dy), (px + dx))
            if 0 <= ny < rows and 0 <= nx < cols:
                # print(graph[ny][nx])
                nextCost = graph[ny][nx] + cost
                # if graph[ny][nx] not in visited and dists[ny][nx] > nextCost:
                if nextCost < dists[ny][nx]:
                    heapq.heappush(heap, (nextCost, (ny, nx), (dy, dx)))
                    dists[ny][nx] = nextCost
                    predecessors[ny][nx] = (py, px), (dy, dx)
    return math.inf, []


def dijkstra(graph: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    """plain ol' dijkstra, not for this problem"""
    heap = [(0, start)]
    visited = set()
    while heap:
        cost, (py, px) = heapq.heappop(heap)
        if (py, px) in visited:
            continue
        visited.add((py, px))
        if (py, px) == end:
            return cost
        neighbors = dirs
        for dy, dx in neighbors:
            v = ((py + dy), (px + dx))
            if v[0] < 0 or v[0] >= len(data) or v[1] < 0 or v[1] >= len(data[0]):
                continue
            print(v)
            # for v in graph[py][px]:
            if v in visited:
                continue
            nextCost = cost + graph[v[0]][v[1]]
            heapq.heappush(heap, (nextCost, v))
    return -1


print(finalDijkstra((0, 0), (rows - 1, cols - 1), 1, 3))
print(finalDijkstra((0, 0), (rows - 1, cols - 1), 4, 10))
