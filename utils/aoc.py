def getInput(year, day, test=False):
    input = []
    with open(f"{year}/inputs/day-{day}{'-test' if test else ''}.txt", "r") as f:
        input = f.read().strip().split("\n")

    return input
