TEST = False

data = []
inputFile = "2023/inputs/"
inputFile += "1test2.txt" if TEST else "day1.txt"
with open(inputFile, "r") as f:
    for line in f.readlines():
        data.append(line.strip())

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total = 0
for line in data:
    word = ""
    first, last = None, None

    for c in line:
        word += c
        for number in numbers.keys():
            if number in word:
                numberWord = numbers[number]
                if first == None:
                    first = numberWord

        if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if first == None:
                first = int(c)

    word = ""
    for c in reversed(line):
        word = c + word
        for number in numbers.keys():
            if number in word:
                numberWord = numbers[number]
                if last == None:
                    last = numberWord
        if c in [str(i) for i in range(10)]:
            if last == None:
                last = int(c)

    if TEST:
        print(f"{first}{last}")
    total += int(f"{first}{last}")


print("-" * 20)
print(total)
