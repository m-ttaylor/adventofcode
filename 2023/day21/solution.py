from collections import deque
from utils import aoc
from utils.aoc import dirs


TEST = False

data = aoc.getInput(2023, 21, TEST)

height = len(data)
width = len(data[0])
sx, sy = width // 2, height // 2

# print(data)


def walk(target):
    queue = deque()

    queue.append((sx, sy, 0))
    stopPoints = set()
    visited = set()

    while queue:
        x, y, steps = queue.popleft()
        if (x, y, steps) in visited:
            continue
        visited.add((x, y, steps))

        if steps % 131 == 65:
            done.append(len(stopPoints))
        if steps == target:
            stopPoints.add((x, y))
        else:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx % 131 < width
                    and 0 <= ny % 131 < height
                    and data[ny % 131][nx % 131] != "#"
                ):
                    queue.append((nx, ny, steps + 1))

    return len(stopPoints)


# print(walk(6))
done = []
print(walk(64))

# goal = 26501365

# n = height


# def f(n):
#     a0 = 3906
#     a1 = 34896
#     a2 = 96784

#     b0 = a0
#     b1 = a1 - a0
#     b2 = a2 - a1
#     return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)

# print(f(goal // n))
done = []
walk(3 * 131)

n = 26501365 // 131
f = lambda n, a, b, c: a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
print(f(n, *done))

# G = {i + j * 1j: c for i, r in enumerate(data) for j, c in enumerate(r) if c in ".S"}

# done = []
# todo = {x for x in G if G[x] == "S"}
# cmod = lambda x: complex(x.real % 131, x.imag % 131)

# for s in range(3 * 131):
#     if s == 64:
#         print(len(todo))
#     if s % 131 == 65:
#         done.append(len(todo))

#     todo = {p + d for d in {1, -1, 1j, -1j} for p in todo if cmod(p + d) in G}

# f = lambda n, a, b, c: a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
# print(f(26501365 // 131, *done))


# 612941134797232


# print(1j + 1)
# foo = 1j + 1
# foo += 1
# print(foo.real)
# print(foo.imag)
