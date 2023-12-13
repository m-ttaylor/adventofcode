from collections import defaultdict
from utils import aoc

TEST = True

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


for line in data:
    springs, contig = line.split()
    # contig = [int(x) for x in contig]
    i = 0

    unknowns = [u for u in springs.split(".") if "?" in u]
    print(f"{springs=}, {contig=}")
    print(f"{unknowns=}")


def part1():
    # print(data)
    pass


def part2():
    pass


print(part1())
print(part2())
