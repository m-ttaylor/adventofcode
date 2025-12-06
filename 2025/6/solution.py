import numpy as np
from functools import reduce
from math import prod
import itertools

YEAR = 2025
DAY = 6
TEST = False

file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = np.array([line.split() for line in f.read().strip().split("\n")])

pt1, pt2 = 0, 0
for i in range(data.shape[1]):
    col = data[:, i]
    op = col[-1]
    if op == "+":
        result = sum(map(int, col[:len(col)-1]))
    elif op == "*":
        result = prod(map(int, col[:len(col)-1]))
    pt1 += result
    
print(pt1)

with open(file) as f:
    data = [list(line) for line in  f.read().split("\n")]
width = len(data[0])
data[-1].extend(" "*(width-len(data[-1])))
data = np.array(data)

chunk = []
start = True
for c in range(width):
    col = data[:, c]
    if start:
        op = col[-1]
        col = col[:len(col)-1]
        start = False
    isGapCol =  all(x == " " for x in col)
    if not isGapCol:
        chunk.append(int("".join(col)))
    if c == width-1 or isGapCol:
        if op == "+":
            pt2 += sum(chunk)
        elif op == "*":
            pt2 += prod(chunk)
        chunk = []
        start = True

print(pt2)