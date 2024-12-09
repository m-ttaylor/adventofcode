from collections import defaultdict, Counter, deque
from copy import deepcopy
from functools import reduce


YEAR = 2024
DAY = 9
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip()

expanded = []
for i, c in enumerate(data):
    if i % 2 == 0:
        expanded.append([str(i // 2)] * int(c))
        # files.append(str(i // 2) * int(c))
    else:
        expanded.append(["."] * int(c))
        # empty.append("." * int(c))

if "." not in expanded[-1]:
    expanded.append([])

backup = deepcopy(expanded)

if TEST:
    print("".join(x for block in expanded for x in block))
    print(expanded)

else:
    print("".join(x for block in expanded for x in block)[:200])
    print(expanded[200:])
    print("...")
    print(expanded[-200:])


print()

left, right = 1, len(expanded) - 1
if right % 2 != 0:
    right -= 1

while left < right:
    file = expanded[right]
    space = expanded[left]
    spaceToFill = min(len(space), len(file))
    leftoverSpace = max(len(space) - spaceToFill, 0)
    leftoverFile = max(len(file) - spaceToFill, 0)
    expanded[left - 1].extend(spaceToFill * [file[0]])
    expanded[left] = leftoverSpace * ["."]
    expanded[right] = [file[0]] * leftoverFile
    expanded[right + 1].extend(["."] * (len(file) - leftoverFile))

    if not leftoverSpace:
        left += 2
    if not leftoverFile:
        right -= 2


print("compacted:")
if TEST:
    # print("".join(expanded))
    # print("".join(x for block in expanded for x in block))
    print(expanded)
else:
    print(expanded[:200])
#     print("".join(expanded)[:200])

pt1 = 0

index = 0
for whatever in expanded:
    if whatever:
        for c in whatever:
            if c.isdigit():
                pt1 += index * int(c)
            else:
                break
            index += 1

print(pt1)

pt2 = 0

expanded = backup
right = len(expanded) - 1
if right % 2 != 0:
    right -= 1
while right > 0:
    file = expanded[right]

    if file and all(c != "." for c in file):
        for left in range(1, right, 1):
            if all(c == "." for c in expanded[left]):
                space = expanded[left]
                diff = len(space) - len(file)
                if diff >= 0:

                    expanded[left] = [file[0]] * len(file)
                    expanded.insert(left + 1, ["."] * diff)
                    right += 1
                    expanded[right] = ["."] * len(file)
                    break
    # print("".join(x for block in expanded for x in block))
    right -= 1


index = 0
for whatever in expanded:
    if whatever:
        for c in whatever:
            if c.isdigit():
                pt2 += index * int(c)
            index += 1

print("pt2 compacted:")
if TEST:
    print("".join(x for block in expanded for x in block))
else:
    print(expanded[:200])

print(pt2)
