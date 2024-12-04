from collections import defaultdict, Counter
from functools import reduce


YEAR = 2024
DAY = 4
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

eightDirs = (
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (1, 1),
    (-1, -1),
)

pt1 = 0
pt2 = 0


w, h = len(data[0]), len(data)
# hits = [["." for _ in range(w)] for __ in range(h)]
visited = set()
for y, row in enumerate(data):
    for x, c in enumerate(row):

        if c == "X":
            start, stop = None, None
            for dy, dx in eightDirs:
                start = (y, x)
                word = [data[y][x]]
                ny, nx = y, x
                for _ in range(3):
                    ny += dy
                    nx += dx
                    if ny >= h or ny < 0 or nx >= w or nx < 0:
                        break
                    word.append(data[ny][nx])

                if "".join(word) in ("XMAS", "SAMX"):
                    stop = (ny, nx)
                    if (start, stop) not in visited:
                        # for i, char in enumerate(reversed(word)):
                        #     hits[ny - i * dy][nx - i * dx] = char
                        pt1 += 1
                        visited.add((start, stop))

# for row in hits:
#     print(" ".join(row))
print(pt1)

# hits = [["." for _ in range(w)] for __ in range(h)]
visited = set()
for y, row in enumerate(data):
    for x, c in enumerate(row):

        if 0 < y < h - 1 and 0 < x < w - 1:
            if c == "A":

                upleft, upright = data[y - 1][x - 1], data[y - 1][x + 1]
                downleft, downright = data[y + 1][x - 1], data[y + 1][x + 1]
                # center = data[y][x]
                # shape = [["."] * 3 for _ in range(3)]
                # shape[0][0] = upleft
                # shape[0][2] = upright
                # shape[1][1] = center
                # shape[2][0] = downleft
                # shape[2][2] = downright
                # for row in shape:
                #     print(" ".join(row))

                masmas = (
                    upleft == "M"
                    and upright == "S"
                    and downleft == "M"
                    and downright == "S"
                )
                samsam = (
                    upleft == "S"
                    and upright == "M"
                    and downleft == "S"
                    and downright == "M"
                )
                sammas = (
                    upleft == "S"
                    and upright == "S"
                    and downleft == "M"
                    and downright == "M"
                )
                massam = (
                    upleft == "M"
                    and upright == "M"
                    and downleft == "S"
                    and downright == "S"
                )
                if masmas or samsam or sammas or massam:
                    pt2 += 1


# for row in hits:
#     print(" ".join(row))

print(pt2)
