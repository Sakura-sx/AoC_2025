# part 1
def solve2_1():
    solution = 0
    input_file = open("2.txt", "r")

    input_list = input_file.read().split(",")
    for pair in input_list:
        pair = pair.split("-")
        for i in range(int(pair[0]), int(pair[1]) + 1):
            if len(str(i)) & 1 == 0:
                if int(str(i)[:len(str(i))//2]) == int(str(i)[len(str(i))//2:]):
                    solution += i

    print(solution)


# part 2
def solve2_2():
    solution = 0
    input_file = open("2.txt", "r")

    input_list = input_file.read().split(",")
    for pair in input_list:
        pair = pair.split("-")
        for i in range(int(pair[0]), int(pair[1]) + 1):
            for j in range(1, int(len(str(i)))):
                if len(str(i)) % j == 0:
                    if all(str(i)[0:j] == str(i)[k:k+j] for k in range(0, len(str(i)), j)):
                        solution += i
                        break

    print(solution)

def main():
    solve2_1()
    solve2_2()

if __name__ == "__main__":
    main()