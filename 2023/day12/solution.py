from collections import defaultdict
from functools import cache
import itertools
from utils import aoc

TEST = False

data = aoc.getInput(2023, 12, TEST)


def countContig(line):
    contig = []
    i = 0
    ccount = 0
    while i < len(line):
        while i < len(line) and line[i] in {"#", "?"}:
            ccount += 1
            i += 1

        contig.append(ccount)
        ccount = 0
        i += 1
    return contig


print(countContig("#.##.###"))
print(countContig("???.###"))


@cache
def solve(springs: str, contig):
    if not contig:
        if "#" not in springs:
            return 1
        else:
            return 0
    if not springs:
        return 0

    ways = 0

    nextSpring = springs[0]
    nextContig = contig[0]

    def pound():
        group = springs[:nextContig]
        group = group.replace("?", "#")

        if group != nextContig * "#":
            return 0

        if len(springs) == nextContig:
            if len(contig) == 1:
                return 1
            return 0

        if springs[nextContig] in "?.":
            return solve(springs[nextContig + 1 :], contig[1:])

        return 0

    def dot():
        return solve(springs[1:], contig)

    if nextSpring == "#":
        ways = pound()
    elif nextSpring == ".":
        ways = dot()
    else:  # ?
        ways = dot() + pound()

    # print(springs, contig, "->", ways)
    return ways


print(solve("???.###", (1, 1, 3)))
print(solve(".??..??...?##.", (1, 1, 3)))

ans = 0
for line in data:
    springs, contig = line.split()
    contig = tuple(int(x) for x in contig.split(","))

    ans += solve(springs, contig)

print("part one:", ans)

ans = 0
for line in data:
    springs, contig = line.split()

    springs = "?".join([springs] * 5)
    contig = tuple([int(x) for x in contig.split(",")] * 5)

    ans += solve(springs, contig)

print("part two:", ans)


def part1():
    # print(data)
    pass


def part2():
    pass


print(part1())
print(part2())
