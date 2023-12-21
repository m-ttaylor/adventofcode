from collections import defaultdict
import itertools
from utils import aoc


TEST = False

data = aoc.getInputRaw(2023, 19, TEST)


def processRule(part, rule):
    if type(rule) == str:
        return rule
    else:  # a comparison
        key, cmp, val, dest = rule
        match cmp:
            case ">":
                if int(part[key]) > val:
                    return dest
            case "<":
                if int(part[key]) < val:
                    return dest
        return False


def processWorkflow(part, key: str, i: int):
    # try rule 1 on the part, store result
    # if result leads us somewhere, keep calling process workflow on that new destination
    # otherwise, go to next rule

    rules = workflows[key]
    if not rules or i >= len(rules):
        return

    rule = rules[i]
    result = processRule(part, rule)

    if result:
        if result == "R":
            return
        if result == "A":
            accepted.append(part)
            return True

        return processWorkflow(part, result, 0)

    return processWorkflow(part, key, i + 1)


workflows = {}
accepted = []

workflowData, partRatingsData = data.split("\n\n")
for line in workflowData.splitlines():
    key, rest = line.split("{")
    workflow = []
    for rule in rest.split(","):
        comparison = None
        if rule.find("<") != -1:
            comparison = "<"
        elif rule.find(">") != -1:
            comparison = ">"

        if comparison:
            part, rest = rule.split(comparison)
            val, dest = rest.split(":")
            workflow.append((part, comparison, int(val), dest.replace("}", "")))

        else:
            workflow.append(rule.replace("}", ""))
    workflows[key] = workflow

parts = []
for line in partRatingsData.splitlines():
    line = line.replace("{", "").replace("}", "")
    ratings = dict(tuple(m.split("=")) for m in line.split(","))
    parts.append(ratings)
    processWorkflow(ratings, "in", 0)


print(len(accepted))
print("-" * 20)
print(sum(int(value) for part in accepted for value in part.values()))


def both(ch, gt, val, ranges):
    ch = "xmas".index(ch)
    rtn = []
    for inter in ranges:
        inter = list(inter)
        low, high = inter[ch]
        if gt:
            low = max(low, val + 1)
        else:
            high = min(high, val - 1)
        if low > high:
            continue
        inter[ch] = (low, high)
        rtn.append(inter)
    return rtn


def rangesInner(work: list[str]):
    it = work[0]

    if it == "R":
        return []
    if it == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]

    if type(it) == str:
        return rangesOuter(it)

    ch, gt, val, dest = it
    gt = ">" in gt

    valInverted = val + 1 if gt else val - 1
    compTrue = both(ch, gt, val, rangesInner([dest]))
    compFalse = both(ch, not gt, valInverted, rangesInner(work[1:]))
    return compTrue + compFalse


def rangesOuter(work):
    return rangesInner(workflows[work])


count = 0
for inter in rangesOuter("in"):
    v = 1
    for low, high in inter:
        v *= high - low + 1
    count += v

print(count)
