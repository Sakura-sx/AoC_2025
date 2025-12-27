# part 1
def solve11_1():
    with open("11.txt", "r") as file:
        data = file.readlines()

    follow_map = {}
    for line in data:
        follow_map[line.split(":")[0].strip()] = line.split(":")[1].strip().split(" ")

    visited = set()
    global paths
    paths = 0

    def dfs(node, visited, target):
        if node in visited:
            return
        if node == target:
            global paths
            paths += 1
            return
        visited.add(node)
        for follow in follow_map[node]:
            dfs(follow, visited, target)
        visited.remove(node)

    dfs("you", visited, "out")
    print(paths)

# part 2
def solve11_2():
    import sys
    sys.setrecursionlimit(1000000)

    with open("11.txt", "r") as file:
        data = file.readlines()

    follow_map = {}
    for line in data:
        parts = line.strip().split(":")
        follow_map[parts[0].strip()] = [x for x in parts[1].strip().split(" ") if x]

    memo = {}

    def get_paths(node, target):
        if node == target:
            return 1
        if node in memo:
            return memo[node]
        
        total = 0
        if node in follow_map:
            for follow in follow_map[node]:
                total += get_paths(follow, target)
                
        memo[node] = total
        return total

    memo = {}
    paths_1 = get_paths("svr", "fft")
    memo = {}
    paths_2 = get_paths("fft", "dac")
    memo = {}
    paths_3 = get_paths("dac", "out")

    print(paths_1 * paths_2 * paths_3)


def main():
    solve11_1()
    solve11_2()

if __name__ == "__main__":
    main()