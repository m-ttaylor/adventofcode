from collections import defaultdict, Counter
from functools import reduce


YEAR = 2024
DAY = 2
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

pt1 = 0
pt2 = 0


def reportIsSafe(levels):
    inc, dec = False, False
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if abs(diff) > 3 or abs(diff) < 1:
            return False

        if i == 1:
            if diff < 0:
                dec = True
            else:
                inc = True
        else:
            if (inc and diff < 0) or (dec and diff > 0):
                inc, dec = False, False
                return False
    return True


for report in data:
    levels = list(map(int, report.split()))
    unsafe = False
    inc, dec = False, False
    if reportIsSafe(levels):
        pt1 += 1

for report in data:
    levels = list(map(int, report.split()))
    if any(reportIsSafe(levels[:i] + levels[i + 1 :]) for i in range(len(levels))):
        pt2 += 1

print("part1", pt1)
print("part2", pt2)
