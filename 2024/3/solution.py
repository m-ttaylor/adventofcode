from collections import defaultdict, Counter
from functools import reduce


YEAR = 2024
DAY = 3
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip()

pt1 = 0
pt2 = 0

i = 0
valid_command = False
while i < len(data):

    if data[i] == "(" and i > 2 and data[i - 3 : i] == "mul":
        valid_command = True
    elif valid_command:
        a = ""
        while i < len(data) and data[i].isdigit():
            a += data[i]
            i += 1
        if i < len(data) and data[i] == ",":
            i += 1
        else:
            valid_command = False
            continue
        b = ""
        while i < len(data) and data[i].isdigit():
            b += data[i]
            i += 1
        if i < len(data) and data[i] == ")":
            i += 1
            pt1 += int(a) * int(b)
        else:
            valid_command = False
    else:
        valid_command = False

    i += 1

print(pt1)

i = 0
valid_command = False
enabled = True
while i < len(data):
    if data[i] == "(":
        if i > 1 and data[i - 2 : i] == "do":
            enabled = True
        elif i > 4 and data[i - 5 : i] == "don't":
            enabled = False
        elif i > 2 and data[i - 3 : i] == "mul":
            valid_command = True
    elif valid_command and enabled:
        a = ""
        while i < len(data) and data[i].isdigit():
            a += data[i]
            i += 1
        if i < len(data) and data[i] == ",":
            i += 1
        else:
            valid_command = False
            continue
        b = ""
        while i < len(data) and data[i].isdigit():
            b += data[i]
            i += 1
        if i < len(data) and data[i] == ")":
            i += 1
            pt2 += int(a) * int(b)
        else:
            valid_command = False
    else:
        valid_command = False

    i += 1
print(pt2)
