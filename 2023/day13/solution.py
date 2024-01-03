from utils import aoc

TEST = False
data = aoc.getInputRaw(2023, 13, TEST)

patterns = [pattern.splitlines() for pattern in data.split("\n\n")]


def lineToInt(line: list[str]):
    line = "".join(line).replace(".", "0").replace("#", "1")
    return int(line, 2)


def lineToInt(grid_line):
    grid_line = "".join(grid_line).replace(".", "0").replace("#", "1")
    return int(grid_line, 2)


def encode(grid: list[list[str]]):
    return [lineToInt(line) for line in grid]


def transpose(grid):
    return [*zip(*grid)]


def splitOnIndex(grid, i):
    left = grid[:i][::-1]
    right = grid[i:]

    length = min(len(left), len(right))
    left = left[:length]
    right = right[:length]

    return left, right


def reflect(grid):
    grid = encode(grid)

    for i in range(1, len(grid)):
        left, right = splitOnIndex(grid, i)

        if left == right:
            return i

    return False


def isPowerOfTwo(n: int):
    return (n & (n - 1) == 0) and n != 0


def smudge(grid):
    grid = encode(grid)

    for i in range(1, len(grid)):
        left, right = splitOnIndex(grid, i)

        diff = [l ^ r for l, r in zip(left, right) if l != r]
        if len(diff) == 1 and isPowerOfTwo(diff[0]):
            return i

    return False


pt1 = 0

colsToTheLeft = 0
rowsAbove = 0

for pattern in patterns:
    horz = reflect(pattern)
    vertz = reflect(transpose(pattern)) if not horz else False

    if TEST:
        print(horz, vertz)

    pt1 += horz * 100 + vertz


print(pt1)

pt2 = 0
for pattern in patterns:
    horz = smudge(pattern)
    vertz = smudge(transpose(pattern))

    if TEST:
        print(horz, vertz)

    pt2 += horz * 100 + vertz

print(pt2)
