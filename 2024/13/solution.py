from collections import defaultdict, Counter
from fractions import Fraction
from functools import reduce
from heapq import heappop, heappush
from math import floor

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 13
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    claws = [claw.split("\n") for claw in f.read().strip().split("\n\n")]


print(claws)

A = 3
B = 1

pt1 = 0

print("part 1...")
for c, claw in enumerate(claws):

    a, b, prize = claw
    ax, ay = [int(coord.strip()[2:]) for coord in a.split(":")[1].split(",")]
    bx, by = [int(coord.strip()[2:]) for coord in b.split(":")[1].split(",")]
    px, py = [int(coord.strip()[2:]) for coord in prize.split(": ")[1].split(",")]

    slope_a = ay/ax
    slope_b = by/bx

    if TEST:
        print("a", ax, ay)
        print("b", bx, by)
        print("prize is at", px, py)

    print(f"claw {c+1}: {slope_a=} {slope_b=}")
    intersects = False
    cost = 0
    y = 0
    for x in range(0, px, ax):
        if intersects:
            break
        cost += A

        if x == px and y == py:
            pt1 += (x/ax) * A
            break
        elif x > px or y > py or x == px or y == py:
            break
        elif (py-y) / (px-x) == slope_b:

            x2 = px - x

            if x2 % bx == 0:
                intersects = True
                price = (x/ax)*A + (x2)/bx*B
                if TEST:
                    print("A hit! a intersects with b", x, y)
                    print("which means cost is:", price)
                pt1 += int(price)
        
        y += ay

    print("-"*25)
    
pt2 = 0

print("part 2...")
for c, claw in enumerate(claws):

    a, b, prize = claw
    ax, ay = [int(coord.strip()[2:]) for coord in a.split(":")[1].split(",")]
    bx, by = [int(coord.strip()[2:]) for coord in b.split(":")[1].split(",")]
    px, py = [int(coord.strip()[2:]) for coord in prize.split(": ")[1].split(",")]
    
    px += 10_000_000_000_000
    py += 10_000_000_000_000

    b_presses = (px*ay-py*ax)//(ay*bx-by*ax)
    a_presses = (px*by-py*bx)//(by*ax-bx*ay)

    print(f"claw {c+1}: {px, py} {a_presses=} {b_presses=}")

    if ax*a_presses + bx*b_presses == px and ay*a_presses + by*b_presses == py:
        print("hit")
        pt2 += A*a_presses + B*b_presses

    print("-"*25)
  
print("pt1", pt1)

print("pt2", pt2)

