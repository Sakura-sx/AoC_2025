# part 1
def solve5_1():
    solution = 0
    ranges = set()

    with open("5.txt") as f:
        for line in f:
            if "-" in line:
                a, b = line.strip().split("-")
                ranges.add(range(int(a), int(b)))
            else:
                if line.strip() != "":
                    if any(int(line.strip()) in r for r in ranges):
                        solution += 1

    print(solution)

# part 2
def solve5_2():
    ranges = set()

    with open("5.txt") as f:
        for line in f:
            if "-" in line:
                a, b = line.strip().split("-")
                ranges.add((int(a), int(b)))

    ranges = sorted((min(a,b), max(a,b)) for a,b in ranges)

    merged = []
    s, e = ranges[0]

    for start, end in ranges[1:]:
        if start <= e + 1:
            e = max(e, end)
        else:
            merged.append((s, e))
            s, e = start, end

    merged.append((s, e))
    solution = sum(end - start + 1 for start, end in merged)

    print(solution)

def main():
    solve5_1()
    solve5_2()

if __name__ == "__main__":
    main()