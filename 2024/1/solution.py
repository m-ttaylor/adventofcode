from collections import defaultdict, Counter
from functools import reduce
from utils import aoc

YEAR = 2024
DAY = 1
TEST = False

file = f"{YEAR}/{DAY}/" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

list1, list2 = [], []
for line in data:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))
list1.sort()
list2.sort()

ans = sum(abs(left - right) for left, right in zip(list1, list2))
print(ans)

counts = Counter(list2)
ans = 0
for num in list1:
    ans += num * counts[num]

print(ans)
