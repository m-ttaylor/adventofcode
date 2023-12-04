from collections import deque
import math
from utils import aoc
from utils.aoc import parseInts

TEST = False

data = aoc.getInput(2023, 4, TEST)


def part1():
    total = 0
    for card in data:
        game, numbers = card.split(":")
        winningNumbers, myNumbers = numbers.split("|")
        winningNumbers = set(parseInts(winningNumbers))
        myNumbers = set(parseInts(myNumbers))
        score = 1 / 2
        for number in myNumbers:
            if number in winningNumbers:
                score *= 2

        total += math.floor(score)

    return total


def part2():
    total = 0
    copies = deque()
    games = {}
    for card in data:
        total += 1
        game, numbers = card.split(":")
        game = int(parseInts(game)[0])
        winningNumbers, myNumbers = numbers.split("|")
        winningNumbers = set(parseInts(winningNumbers))
        myNumbers = set(parseInts(myNumbers))
        matches = games.get(game, 0)
        if not matches:
            for number in myNumbers:
                if number in winningNumbers:
                    matches += 1
            games[game] = matches

        for i in range(matches):
            copies.append(game + i + 1)

    while copies:
        total += 1
        copy = copies.popleft()
        matches = games[copy]
        for i in range(matches):
            copies.append(copy + i + 1)

    return total


print(part1())
print(part2())
