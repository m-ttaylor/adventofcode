from collections import defaultdict, Counter
from functools import reduce
from re import finditer, findall
from typing import Iterator

"""
answers should be:
182619815
80747545
"""

YEAR = 2024
DAY = 3
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip()

pt1 = 0
pt2 = 0

for match in finditer("mul\({1}(\d+),(\d+)\){1}", data):
    pt1 += reduce(lambda a, b: a * b, (map(int, match.groups())), 1)

donts = [dont.span() for dont in finditer(r"don't\(\){1}.+do\(\){1}", data)]
# dos = [do.span() for do in finditer("do\(\){1}", data)]
last_dont = data.rfind("don't()")
if last_dont > donts[-1][0]:
    donts.append((data.rfind("don't()"), len(data)))

current_interval = 0
last_index = 0
for match in finditer("mul\({1}(\d+),(\d+)\){1}", data):
    if last_index > donts[current_interval][1]:
        current_interval += 1
    start, stop = match.span()
    # if (
    #     current_interval < len(donts)
    #     and start >= donts[current_interval][0]
    #     and stop <= donts[current_interval][1]
    # ):
    if any(start >= left and stop <= right for left, right in donts):
        print(
            f"{match.groups()} {start}, {stop} is inside {donts[current_interval]}, skipping"
        )
        continue
    pt2 += reduce(lambda a, b: a * b, map(int, match.groups()), 1)

#     print(match.groups())
# matches = finditer("mul\({1}(\d+),(\d+)\){1}", data)
# does = finditer("do\(\){1}", data)

print(donts)
# print(dos)

# print(findall("mul\({1}\d\d\){1}", data))
# i = 0
# valid_command = False
# while i < len(data):

#     if data[i] == "(" and i > 2 and data[i - 3 : i] == "mul":
#         valid_command = True
#     elif valid_command:
#         a = ""
#         while i < len(data) and data[i].isdigit():
#             a += data[i]
#             i += 1
#         if i < len(data) and data[i] == ",":
#             i += 1
#         else:
#             valid_command = False
#             continue
#         b = ""
#         while i < len(data) and data[i].isdigit():
#             b += data[i]
#             i += 1
#         if i < len(data) and data[i] == ")":
#             i += 1
#             pt1 += int(a) * int(b)
#         else:
#             valid_command = False
#     else:
#         valid_command = False

#     i += 1

print(pt1)

# i = 0
# valid_command = False
# enabled = True
# while i < len(data):
#     if data[i] == "(":
#         if i > 1 and data[i - 2 : i] == "do":
#             enabled = True
#         elif i > 4 and data[i - 5 : i] == "don't":
#             enabled = False
#         elif i > 2 and data[i - 3 : i] == "mul":
#             valid_command = True
#     elif valid_command and enabled:
#         a = ""
#         while i < len(data) and data[i].isdigit():
#             a += data[i]
#             i += 1
#         if i < len(data) and data[i] == ",":
#             i += 1
#         else:
#             valid_command = False
#             continue
#         b = ""
#         while i < len(data) and data[i].isdigit():
#             b += data[i]
#             i += 1
#         if i < len(data) and data[i] == ")":
#             i += 1
#             pt2 += int(a) * int(b)
#         else:
#             valid_command = False
#     else:
#         valid_command = False

#     i += 1
print(pt2)
