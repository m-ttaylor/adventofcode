def getInput(year, day, test=False):
    input = []
    with open(f"{year}/inputs/day-{day}{'-test' if test else ''}.txt", "r") as f:
        input = f.read().strip().split("\n")

    return input


def isDigit(char: str):
    if len(char) > 1:
        raise Exception("please only check one character at a time")
    try:
        int(char)
    except Exception:
        return False
    else:
        return True
    # return char in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
