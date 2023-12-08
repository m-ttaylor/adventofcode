from collections import defaultdict
import math
from utils import aoc


TEST = False

data = aoc.getInput(2023, 8, TEST)


def part1():
    sequence = data[0]
    n = len(sequence)

    nodes = {}

    for line in data[2:]:
        origin, pair = [part.strip() for part in line.split("=")]
        left, right = [
            part.strip() for part in pair.replace("(", "").replace(")", "").split(",")
        ]
        nodes[origin] = (left, right)

    steps = 0

    loc = "AAA"
    while loc != "ZZZ":
        match sequence[steps % n]:
            case "L":
                loc = nodes[loc][0]
            case "R":
                loc = nodes[loc][1]
        steps += 1

    return steps


def part2():
    sequence = data[0]
    n = len(sequence)

    nodes = {}
    locs: list[str] = []

    for line in data[2:]:
        origin, pair = [part.strip() for part in line.split("=")]
        left, right = [
            part.strip() for part in pair.replace("(", "").replace(")", "").split(",")
        ]

        if origin.endswith("A"):
            locs.append(origin)

        nodes[origin] = (left, right)

    def findCycleLength(loc: str):
        steps = 0
        while not loc.endswith("Z"):
            match sequence[steps % n]:
                case "L":
                    loc = nodes[loc][0]
                case "R":
                    loc = nodes[loc][1]
            steps += 1

        hitsOnZ = 1
        cycle = 0
        target = loc
        while hitsOnZ < 2:
            match sequence[steps % n]:
                case "L":
                    loc = nodes[loc][0]
                case "R":
                    loc = nodes[loc][1]
            steps += 1
            cycle += 1
            if loc == target:
                hitsOnZ += 1

        return cycle

    cycleLengths = [findCycleLength(loc) for loc in locs]
    print(cycleLengths)

    return math.lcm(*cycleLengths)


print(part1())
print(part2())
