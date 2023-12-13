from string import ascii_uppercase
from utils import aoc

TEST = False

data = aoc.getInput(2023, 7, TEST)
games = [tuple(line.split()) for line in data]
strengths = {card: i + 1 for i, card in enumerate(reversed("AKQJT98765432"))}
p2Strengths = {card: i + 1 for i, card in enumerate(reversed("AKQT98765432J"))}


def handScoreKey(game):
    """
    the lowest score here needs to be at least 5x the highest card value, then
    increment by the highest value+1
    or we could just return a tuple of tuples and let python do it's thing ¯\_(ツ)_/¯
    """

    hand = game[0]
    scores = {
        "5oak": 125,
        "4oak": 112,
        "fullHouse": 99,
        "3oak": 86,
        "twoPair": 73,
        "onePair": 60,
    }

    score = 0
    type = getTypeOfHand(hand)

    cardPoints = tuple(strengths[card] for card in hand)
    if type != "highCard":
        score += scores[type]

    return (score, cardPoints)


def p2HandScoreKey(game):
    """
    Using tuple returns, just need to rank the hands, not assing some formulaic value
    """

    hand = game[0]
    scores = {
        "5oak": 7,
        "4oak": 6,
        "fullHouse": 5,
        "3oak": 4,
        "twoPair": 3,
        "onePair": 2,
        "highCard": 1,
    }

    type = p2GetTypeOfHand(hand)
    score = scores[type]
    cardPoints = tuple(p2Strengths[card] for card in hand)

    return (score, cardPoints)


def getTypeOfHand(hand: str):
    counts = {
        c: hand.count(c) for c in ascii_uppercase + "23456789" if hand.count(c) > 0
    }

    if any([value == 5 for value in counts.values()]):
        return "5oak"
    if any([value == 4 for value in counts.values()]):
        return "4oak"

    pairs = list(counts.values()).count(2)
    triples = 3 in counts.values()

    if triples and pairs:
        return "fullHouse"
    if triples:
        return "3oak"
    if pairs == 2:
        return "twoPair"
    if pairs == 1:
        return "onePair"
    return "highCard"


def p2GetTypeOfHand(hand: str):
    counts = {
        c: hand.count(c) for c in ascii_uppercase + "23456789" if hand.count(c) > 0
    }
    jokers = counts.get("J", 0)

    if jokers < 5:
        maxCount = max([v for (k, v) in counts.items() if k != "J"])
        for c in counts:
            if c != "J" and counts[c] == maxCount:
                counts[c] += jokers
                jokers = 0
                break

    if any([value >= 5 for value in counts.values()]):
        return "5oak"
    if any([value == 4 for value in counts.values()]):
        return "4oak"

    pairs = 0
    triples = 0

    for c in counts:
        # this is a bit kludgey, but we can just ignore triples or doubles of Joker,
        # because they could always go towards making something else more valuable
        if c != "J" and counts[c] == 3:
            triples += 1

        elif c != "J" and counts[c] == 2:
            pairs += 1

    if triples and pairs:
        return "fullHouse"
    if triples:
        return "3oak"
    if pairs == 2:
        return "twoPair"
    if pairs == 1:
        return "onePair"
    return "highCard"


if TEST:
    games.sort(key=p2HandScoreKey)
    for rank, (hand, bid) in enumerate(games):
        print(f"{rank+1}: {hand}  {bid} -- hint: {p2GetTypeOfHand(hand)}")


def part1():
    games = [tuple(line.split()) for line in data]
    games.sort(key=handScoreKey)
    winnings = 0
    for i, (_, bid) in enumerate(games):
        winnings += (i + 1) * int(bid)

    return winnings


def part2():
    games = [tuple(line.split()) for line in data]
    games.sort(key=p2HandScoreKey)
    winnings = 0
    for i, (_, bid) in enumerate(games):
        winnings += (i + 1) * int(bid)

    return winnings


print(part1())
print(part2())
