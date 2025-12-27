# part 1
def solve10_1():
    from collections import deque

    with open("10.txt", "r") as f:
        file = f.readlines()

    solution = 0

    for line in file:
        buttons = []
        for i in line.split(" "):
            if i.startswith("["):
                lights = ""
                for light in i[1:-1]:
                    if light == ".":
                        lights += "0"
                    elif light == "#":
                        lights += "1"
            elif i.startswith("("):
                button = ""
                for j in range(len(lights)):
                    if j in list(map(int, i[1:-1].split(","))):
                        button += "1"
                    else:
                        button += "0"
                buttons.append(button)
            elif i.startswith("{"):
                continue

        queue = deque([(frozenset(), '0' * len(lights))])
        visited = {frozenset()}

        found = False
        while queue and not found:
            used_buttons, current_state = queue.popleft()
            
            if current_state == lights:
                solution += len(used_buttons)
                found = True
                break
            
            for i in range(len(buttons)):
                if i not in used_buttons:
                    new_state = ''.join('1' if a != b else '0' for a, b in zip(current_state, buttons[i]))
                    new_used = frozenset(used_buttons | {i})
                    
                    if new_used not in visited:
                        visited.add(new_used)
                        queue.append((new_used, new_state))

    print(solution)


# part 2
def solve10_2():
    print("I wasn't able to solve this one :(")