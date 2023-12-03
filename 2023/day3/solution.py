from collections import defaultdict
from utils import aoc

TEST = False

data = aoc.getInput(2023, 3, TEST)


def isDigit(char: str):
    if len(char) > 1:
        raise Exception("please only check one character at a time")
    return char in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}


rows = len(data)


def adjacentToSymbol(r: int, c: int, sizeOfNumber: int) -> bool | str:
    # check up
    if 0 <= (checkRow := r - 1) < rows:
        for i in range(c - sizeOfNumber, c + 2):
            if 0 <= i < len(data[checkRow]):
                adj = data[checkRow][i]
                if not isDigit(adj) and adj != ".":
                    if TEST:
                        print(f"found a row-1 adjacency at {checkRow}, {i}: {adj}")
                    return adj, (checkRow, i)

    # check row of:
    for i in [c - sizeOfNumber, c + 1]:
        if 0 <= i < len(data[r]):
            adj = data[r][i]
            if not isDigit(adj) and adj != ".":
                if TEST:
                    print(f"found a row adjacency at {r}, {i}: {adj}")
                return adj, (r, i)

    # check row below:
    if 0 <= (checkRow := r + 1) < rows:
        for i in range(c - sizeOfNumber, c + 2):
            if 0 <= i < len(data[checkRow]):
                adj = data[checkRow][i]
                if not isDigit(adj) and adj != ".":
                    if TEST:
                        print(f"found a row+1 adjacency at {checkRow}, {i}: {adj}")
                    return adj, (checkRow, i)

    return False


# def calculateGearRatio(r: int, c: int, numbers: defaultdict):
#     adjacentNumbers = []
#     # check up
#     if 0 <= (checkRow := r - 1) < rows:
#         for i in range(c - 1, c + 2):
#             if 0 <= i < len(data[checkRow]):

#                 adj = data[checkRow][i]
#                 if numbers[(checkRow, i)]
#                 if isDigit(adj):
#                     # number = []
#                     # while
#                     # if not isDigit(adj) and adj != ".":
#                     if TEST:
#                         print(f"found a row-1 adjacency at {checkRow}, {i}: {adj}")
#                     return True

#     # check row of:
#     for i in [c - 1, c + 1]:
#         if 0 <= i < len(data[r]):
#             adj = data[r][i]
#             if not isDigit(adj) and adj != ".":
#                 if TEST:
#                     print(f"found a row adjacency at {r}, {i}: {adj}")
#                 return True

#     # check row below:
#     if 0 <= (checkRow := r + 1) < rows:
#         for i in range(c - sizeOfNumber, c + 2):
#             if 0 <= i < len(data[checkRow]):
#                 adj = data[checkRow][i]
#                 if not isDigit(adj) and adj != ".":
#                     if TEST:
#                         print(f"found a row+1 adjacency at {checkRow}, {i}: {adj}")
#                     return True

#     return False


def part1():
    total = 0
    for r in range(rows):
        number = ""
        for i, c in enumerate(data[r]):
            if isDigit(c):
                number += c
                if i + 1 >= len(data[r]) or not (isDigit(data[r][i + 1])):
                    asInt = int(number)
                    if TEST:
                        print(f"checking number {asInt}")
                    sizeOfNumber = len(number)
                    number = ""
                    if adjacentToSymbol(r, i, sizeOfNumber):
                        if TEST:
                            print(f"adding {asInt} to total")
                        total += asInt
    return total


def part2():
    stars = defaultdict(list)
    total = 0
    for r in range(rows):
        number = ""
        for i, c in enumerate(data[r]):
            if isDigit(c):
                number += c
                if i + 1 >= len(data[r]) or not (isDigit(data[r][i + 1])):
                    asInt = int(number)
                    sizeOfNumber = len(number)
                    number = ""
                    if adj := adjacentToSymbol(r, i, sizeOfNumber):
                        if adj[0] == "*":
                            if TEST:
                                print(f"adding {asInt} to stars")
                            stars[adj[1]].append(asInt)
    for star in stars:
        if len(stars[star]) == 2:
            gearRatio = stars[star][0] * stars[star][1]
            total += gearRatio

    return total


print(part1())
print(part2())
