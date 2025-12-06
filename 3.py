# part 1
def solve3_1():
    solution = 0

    with open("3.txt") as f:
        for line in f:
            digits = [int(d) for d in line.strip()]
            best = 0
            
            for i, d1 in enumerate(digits):
                for d2 in digits[i+1:]:
                    best = max(best, d1*10 + d2)
            
            solution += int(best)

    print(solution)


# part 2
def solve3_2():
    def best_k(digits, k):
        stack = []
        remove = len(digits) - k

        for d in digits:
            while stack and remove > 0 and stack[-1] < d:
                stack.pop()
                remove -= 1
            stack.append(d)

        return stack[:k]


    solution = 0

    with open("3.txt") as f:
        for line in f:
            digits = list(map(int, line.strip()))
            best = best_k(digits, 12)
            solution += int("".join(map(str, best)))

    print(solution)


def main():
    solve3_1()
    solve3_2()

if __name__ == "__main__":
    main()