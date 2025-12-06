# part 1
def solve4_1():
    solution = 0

    with open("4.txt") as f:
        rolls = [list(map(bool, map(lambda x: x == '@', line.strip()))) for line in f]
        for i, row in enumerate(rolls):
            for j, roll in enumerate(row):
                if roll:
                    window = [rolls[k][l]for k in range(max(0, i-1), min(len(rolls), i+2)) for l in range(max(0, j-1), min(len(rolls), j+2))]
                    if sum(window) < 5:
                        solution += 1


    print(solution)

# part 2
def solve4_2():
    solution = 0

    with open("4.txt") as f:
        rolls = [list(map(bool, map(lambda x: x == '@', line.strip()))) for line in f]
        while True:
            newrolls = [[False]*len(rolls[0]) for _ in range(len(rolls))]
            changed = False
            
            for i, row in enumerate(rolls):
                for j, roll in enumerate(row):
                    if roll:
                        window = [rolls[k][l]for k in range(max(0, i-1), min(len(rolls), i+2)) for l in range(max(0, j-1), min(len(rolls[0]), j+2))]
                        if sum(window) < 5:
                            solution += 1
                            changed = True
                        else:
                            newrolls[i][j] = True
                    else:
                        newrolls[i][j] = False
            if not changed:
                break
            rolls = newrolls
    print(solution)


def main():
    solve4_1()
    solve4_2()

if __name__ == "__main__":
    main()