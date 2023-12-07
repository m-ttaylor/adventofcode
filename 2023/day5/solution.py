from collections import defaultdict
import math
from utils import aoc

TEST = False

data = []

# only seeds has the title on the same line as the data, need to parse differently
file = f"2023/inputs/day-5{'-test' if TEST else ''}.txt"
with open(file, "r") as f:
    data = f.read().split("\n\n")


def notQuiteMap(currentMap, seed):
    for dest, source, r in currentMap:
        if source <= seed < source + r:
            return dest + (seed - source)
    return seed


def inverseNotQuiteMap(currentMap, seed):
    for dest, source, r in currentMap:
        if dest <= seed < dest + r:
            return source + (seed - dest)
    return seed


def seedToLocation(seed):
    soil = notQuiteMap(seedToSoil, seed)
    fertilizer = notQuiteMap(soilToFertilizer, soil)
    water = notQuiteMap(fertilizerToWater, fertilizer)
    light = notQuiteMap(waterToLight, water)
    temperature = notQuiteMap(lightToTemperature, light)
    humidity = notQuiteMap(temperatureToHumidity, temperature)
    location = notQuiteMap(humidityToLocation, humidity)
    return location


seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

seeds = []
maps = []

for chunk in data:
    category, rest = chunk.split(":")
    category = category.strip()
    currentMap = None
    if category == "seeds":
        for seed in [int(x) for x in rest.strip().split(" ")]:
            seeds.append(seed)
        seeds.sort()

    else:
        match category:
            case "seed-to-soil map":
                currentMap = seedToSoil
            case "soil-to-fertilizer map":
                currentMap = soilToFertilizer
            case "fertilizer-to-water map":
                currentMap = fertilizerToWater
            case "water-to-light map":
                currentMap = waterToLight
            case "light-to-temperature map":
                currentMap = lightToTemperature
            case "temperature-to-humidity map":
                currentMap = temperatureToHumidity
            case "humidity-to-location map":
                currentMap = humidityToLocation

        if currentMap is not None:
            for entry in rest.strip().split("\n"):
                destStart, sourceStart, rangeLen = [
                    int(x) for x in entry.strip().split(" ")
                ]
                currentMap.append((destStart, sourceStart, rangeLen))


def part1():
    return min(seedToLocation(s) for s in seeds)


def part2():
    """
    this is just shamelessly from https://github.com/mitchardee/advent2023/blob/main/05/05-2.py
    with some very minor changes
    """

    def reverseMap(interval):
        for currMap in reversed(maps):
            d = [m for m in currMap if m[0] <= interval[0] < m[0] + m[2]]
            s = [m for m in currMap if interval[0] < m[0] < interval[0] + interval[1]]

            if d:
                i1 = d[0][1] + interval[0] - d[0][0]
                interval = (i1, min(d[0][1] + d[0][2], i1 + interval[1]) - i1)
            elif s:
                interval = (interval[0], s[0][0] - interval[0])
        return interval

    def overlap(i1, i2):
        return 0 < i2[0] - i1[0] < i1[1] or 0 < i1[0] - i2[0] < i2[1]

    data = []

    # only seeds has the title on the same line as the data, need to parse differently
    file = f"2023/inputs/day-5{'-test' if TEST else ''}.txt"
    with open(file, "r") as f:
        data = f.read().split("\n\n")

    seeds = [int(x) for x in data[0].split(":")[1].split()]
    seedIntervals = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = []
    for chunk in data[1:]:
        # each 'line' will represent one chunk of maps
        cat, mappingLines = map(str.strip, chunk.split(":"))

        newMap = []
        for line in mappingLines.split("\n"):
            d, s, r = [int(x) for x in line.split()]
            newMap.append((d, s, r))
        maps.append(newMap)

    interval = (0, math.inf)
    while True:
        reverseMapped = reverseMap(interval)
        # l = [s for s in seedIntervals if overlap(reverseMapped, interval)]
        l = list(
            filter(lambda interval: overlap(reverseMapped, interval), seedIntervals)
        )

        if l:
            return interval[0]
        else:
            interval = (interval[0] + reverseMapped[1], math.inf)

    return -1


print(part1())
print(part2())
