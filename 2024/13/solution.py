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


# def findPath(pos, a, b, prize, cost):
#     x, y = pos
#     ax, ay = a
#     bx, by = b
#     px, py = prize
#     print(pos)
#     qax, rax = divmod(px, ax)
#     qbx, rbx = divmod(px, bx)
#     qay, ray = divmod(py, ax)
#     qby, rby = divmod(py, by)
#     # if (rax % bx != 0 and ray % by != 0) or (rbx % ax != 0 and rby % ay != 0):
#     #     return 500
#     if pos == prize:
#         return cost

#     if x > px or y > py:
#         return 500
    
#     return min(findPath((px+ax, py+ay), a, b, prize, cost+A), findPath((px+bx, py+by), a, b, prize, cost+B))

pt1 = 0

for claw in claws:

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

    # x, y = 0, 0
    print(f"{slope_a=} {slope_b=}")
    intersects = False
    cost = 0
    for x in range(ax, px, ax):
        # if (x, y) == prize:
        #     intersects = True
        #     break
        cost += A
        # print("looping", x)
        y = slope_a * x
        # print(cost, x, y)

        slope_between_point_and_prize = -(py-y) / (px-x)
        # print(f"{slope_between_point_and_prize=}")
        if (py-y) / (px-x) == slope_b:

            x2 = px - x

            if x2//bx == x2/bx:
                print("which means cost is:", (x/ax)*A + (x2)/bx*B)
                pt1 += (x/ax)*A + (x2)/bx*B
            more_x = -(px-x) / bx - x
            # print(more_x)
            # if more_x == floor(more_x):
            #     print("foo foo foo foo", A*x+B*more_x)
            # intersects = x, y == prize
            # intersects = (x, y) == prize
            print("A hit! a intersects with b", x, y)
        
            cost2 = 0
            for x2 in range(0, px, bx):
                # if x2 > x:
                cost2 += B
                y = slope_b*x2
                if (x2, y) == prize:
                    print("A hit!", x, y)
                    intersects = True
                    break

    if intersects:
        print(f"final {x=} {x2=}")
        print("costs", (x/ax)*A + (x2-x)/bx*B )
        print("costs2", cost+cost2)
        pt1 += cost+cost2

    else:
        print("no solution")
        # print("cost to get the prize", findPath((0, 0), (ax, ay), (bx, by), (px, py), 0))
    print("-"*25)
    
# pt1 = 0      
pt2 = 0

print("pt1", pt1)

print(pt2)

