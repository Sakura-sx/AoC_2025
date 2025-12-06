# part 1
def solve6_1():
    solution = 0
    grid: list[list[any]] = []

    with open("6.txt") as f:
        file = f.readlines()
    for i in range(len((" ".join((file[0]).split())).split())): grid.append([None] * len(file))

    for i, line in enumerate(file):
        for j, cell in enumerate(" ".join(line.split()).split()):
            if cell != "*" and cell != "+":
                grid[j][i] = int(cell)
            elif cell == "*":
                grid[j][i] = "*"
            elif cell == "+":
                grid[j][i] = "+"
                
    for i in grid:
        if i[-1] == "+":
            solution += sum(i[:-1])
        elif i[-1] == "*":
            last = 1
            for j in i[:-1]:
                last *= j
            solution += last

    print(solution)

# part 2
def solve6_2():
    solution = 0
    grid = []
    with open("6.txt") as f:
        file = f.readlines()

    for line in file:
        l = []
        for i in line[:-1]:
            l.append(i)
        grid.append(l)

    for i in grid:
        i.reverse()

    numbers: list[int | None] = []
    last: int = 1
    x = 0
    for i, s in enumerate(grid[-1]):
        numbers.append(None)
        
        if s == " ":
            for n in range(len(grid) - 1):
                if grid[n][i] != " ":
                    if numbers[i-x] is not None:
                        numbers[i-x] = int(f"{str(numbers[i-x])}{str(grid[n][i])}")
                    else:
                        numbers[i-x] = int(grid[n][i])
        elif s == "+":
            for n in range(len(grid) - 1):
                if grid[n][i] != " ":
                    if numbers[i-x] is not None:
                        numbers[i-x] = int(f"{str(numbers[i-x])}{str(grid[n][i])}")
                    else:
                        numbers[i-x] = int(grid[n][i])
            solution += sum(int(n) for n in numbers if n is not None)
            numbers = [None]
            x = i
        elif s == "*":
            for n in range(len(grid) - 1):
                if grid[n][i] != " ":
                    if numbers[i-x] is not None:
                        numbers[i-x] = int(f"{str(numbers[i-x])}{str(grid[n][i])}")
                    else:
                        numbers[i-x] = int(grid[n][i])
            for n in numbers:
                if n is not None: 
                    last *= n
            solution += last
            last = 1
            numbers = [None]
            x = i

    print(solution)

def main():
    solve6_1()
    solve6_2()

if __name__ == "__main__":
    main()