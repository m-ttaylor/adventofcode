import functools
from utils import aoc

TEST = False

data = aoc.getInput(2023, 2, TEST)


def part1():
    bag = {"red": 12, "green": 13, "blue": 14}

    total = 0
    for game in data:
        id, reveals = game.split(":")
        possible = True
        for reveal in reveals.split(";"):
            possible &= all(
                int(amount) <= bag[color]
                for amount, color in map(
                    lambda cube: cube.strip().split(" "), reveal.strip().split(",")
                )
            )

        if possible:
            total += int(id.split(" ")[1])

    return total


def part2():
    total = 0
    for game in data:
        mins = {"red": 0, "green": 0, "blue": 0}
        __, reveals = game.split(":")
        for reveal in reveals.split(";"):
            for cubes in reveal.strip().split(","):
                amount, color = cubes.strip().split(" ")
                mins[color] = max(mins[color], int(amount))

        power = functools.reduce(lambda x, y: x * y, mins.values())
        total += power

    return total


print(all(i > 0 for i in [1, 2, 3, 4]))
print(part1())  # 3099
print(part2())  # 72970
