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


def parseInts(string: str):
    "find and return all ints in string separated by spaces or commas"
    values = []
    for chunk in string.strip().replace(",", " ").split(" "):
        value: int = None
        try:
            value = int(chunk)
        except ValueError:
            pass
        else:
            values.append(value)

    return values
