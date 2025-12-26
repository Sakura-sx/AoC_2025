# part 1
def solve7_1():
    solution = 0

    with open("7.txt", "r") as f:
        file = f.readlines()

    beampositions = [False for _ in range(len(file[0]))]
    newbeampositions = [False for _ in range(len(file[0]))]
    for i in range(len(file[0])):
        if file[0][i] == "S":
            beampositions[i] = True

    for line in file[1:]:
        for i in range(len(line)):
            if beampositions[i]:
                if line[i] == ".":
                    newbeampositions[i] = True
                elif line[i] == "^":
                    newbeampositions[i-1] = True
                    newbeampositions[i+1] = True
                    solution += 1
        beampositions = newbeampositions.copy()
        newbeampositions = [False for _ in range(len(file[0]))]

    print(solution)




# part 2
def solve7_2():
    with open("7.txt", "r") as f:
        file = f.readlines()

    beampositions = [False for _ in range(len(file[0]))]
    newbeampositions = [False for _ in range(len(file[0]))]

    goodsplits = [[False for _ in range(len(file[0]))] for _ in range(len(file[1:]))]
    for i in range(len(file[0])):
        if file[0][i] == "S":
            beampositions[i] = True

    for line in file[1:]:
        for i in range(len(line)):
            if beampositions[i]:
                if line[i] == ".":
                    newbeampositions[i] = True
                elif line[i] == "^":
                    newbeampositions[i-1] = True
                    newbeampositions[i+1] = True
                    goodsplits[file.index(line)][i] = True
        beampositions = newbeampositions.copy()
        newbeampositions = [False for _ in range(len(file[0]))]

    goodsplits = goodsplits[::-1]

    splitcount = [[0 for _ in range(len(file[0]))] for _ in range(len(file[1:]))]

    for i in range(len(file[0])):
        if goodsplits[0][i]:
            splitcount[0][i] = 2
        else:
            splitcount[0][i] = 1

    for h, line in enumerate(goodsplits):
        if h == 0:
            continue
        for i in range(len(line)):
            if line[i]:
                for side in range(-1, 2, 2):
                    for j in range(h-1, -1, -1):
                        if splitcount[j][i+side] > 0:
                            splitcount[h][i] += splitcount[j][i+side]
                            break

    print(max(max(line) for line in splitcount))


def main():
    solve7_1()
    solve7_2()

if __name__ == "__main__":
    main()