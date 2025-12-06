# part 1
def solve1_1():
    password = 0
    file = open("1.txt", "r")
    dial = 50
    for line in file:
        if line.startswith("R"):
            dial += int(line[1:])
        elif line.startswith("L"):
            dial -= int(line[1:])
        if dial % 100 == 0:
            password += 1
    print(password)

# part 2
def solve1_2():
    import math

    password = 0
    file = open("1.txt", "r")
    dial = 50

    for line in file:
        dial = dial % 100
        if line.startswith("R"):
            password += math.floor((dial + int(line[1:])) / 100)
            dial += int(line[1:])
        elif line.startswith("L"):
            if dial == 0: password -= 1
            if dial - int(line[1:]) < 0:
                password += (math.floor(abs(dial - int(line[1:])) / 100))
            if dial - int(line[1:]) <= 0:
                password += 1
            dial -= int(line[1:])
    print(password)

def main():
    solve1_1()
    solve1_2()

if __name__ == "__main__":
    main()