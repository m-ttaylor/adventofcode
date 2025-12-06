YEAR = 2025
DAY = 5
TEST = False
file = f"{YEAR}/{DAY}/sample.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    ranges, ingredients = f.read().strip().split("\n\n")
    ranges = ranges.split("\n")
    ingredients = ingredients.split("\n")

print(ranges)
print(ingredients)

intervals = set()
ordered = []
for line in ranges:
    left, right = map(int, line.split("-"))
    intervals.add((left, right))
    ordered.append((left, right))

pt1, pt2 = 0, 0
for item in ingredients:
    item = int(item)
    fresh = any(left <= item <= right for left, right in intervals)
    pt1 += int(fresh)

current = 0
ordered.sort()
start = ordered[0][0]
for left, right in ordered:
    left = max(left, current+1)
    pt2 += max(0, right-left+1)
    current = max(current, right)

print(pt1)
print(pt2)