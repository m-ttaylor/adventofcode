from collections import defaultdict
from utils import aoc


TEST = False

data = aoc.getInput(2023, 6, TEST)

times = []
distances = []

print(data[0].split(":")[1].strip())
times = [int(t) for t in data[0].split(":")[1].strip().split()]
distances = [int(d) for d in data[1].split(":")[1].strip().split()]

print(times)
print(distances)


def part1():
    product = 1
    for i, time in enumerate(times):
        waysToWin = 0
        for hold in range(1, time):
            canTravel = hold * (time - hold)
            if canTravel > distances[i]:
                waysToWin += 1
        product *= waysToWin

    return product


def part2():
    time = int("".join(str(t) for t in times))
    distance = int("".join(str(d) for d in distances))

    left, right = None, None
    for hold in range(1, time):
        canTravel = hold * (time - hold)
        if canTravel > distance:
            left = hold
            break
    for hold in range(time, 0, -1):
        canTravel = hold * (time - hold)
        if canTravel > distance:
            right = hold
            break
    return right - left + 1


print(part1())
print(part2())
