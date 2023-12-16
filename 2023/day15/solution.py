from collections import defaultdict
from utils import aoc


TEST = False

data = aoc.getInput(2023, 15, TEST)


def holidayHash(word: str):
    value = 0
    for c in word:
        value += ord(c)
        value *= 17
        value %= 256

    return value


total = 0
for sequence in data:
    for step in sequence.split(","):
        total += holidayHash(step)
print("part 1:", total)

boxes = [{} for _ in range(256 + 1)]
for step in data[0].split(","):
    removeOp = "-" in step
    if removeOp:
        key = step.split("-")[0]
    else:
        key, focalLength = step.split("=")

    box = holidayHash(key)
    if removeOp:
        boxes[box].pop(key, -1)
    else:
        boxes[box][key] = focalLength


power = 0
for b, box in enumerate(boxes):
    for i, (label, focalLength) in enumerate(box.items()):
        power += (1 + b) * (i + 1) * int(focalLength)

print("-" * 10)
print("part 2:", power)
