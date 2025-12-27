# part 1
def solve12_1():
    solution = 0

    with open("12.txt", "r") as file:
        data = file.readlines()

    size = {}

    for i in range(6):
        size[i] = 0
        for line in data[i*5+1:(i+1)*5-1]:
            for char in line:
                if char == "#":
                    size[i] += 1

    for line in data[30:]:
        line = line.strip()
        area = int(line.split(":")[0].split("x")[0].strip()) * int(line.split(":")[0].split("x")[1].strip())
        gift_area = 0
        for i in range(6):
            gift_area += size[i] * int(line.split(":")[1].strip().split(" ")[i].strip())
        if gift_area <= area:
            solution += 1
    print(solution)

# part 2
def solve12_2():
    print("I have not completed this one yet :c")