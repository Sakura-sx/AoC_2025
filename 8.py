# part 1

with open("8.txt", "r") as f:
    file = f.readlines()

points: dict[int, list[int]] = []

for i, line in enumerate(file):
    points.append((i, list(map(int, line.split(",")))))

distances: list[tuple[int, int, int]] = []

# find closest pairs
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = (points[i][1][0] - points[j][1][0])**2 + (points[i][1][1] - points[j][1][1])**2 + (points[i][1][2] - points[j][1][2])**2
        distances.append((i, j, distance))
        distances.append((j, i, distance))

distances.sort(key=lambda x: x[2])
n = 0

connections: list[set[int]] = []

for i in range(1000):
    for j in range((i*2), len(distances)):
        if not any(distances[j][0] in connection for connection in connections) and not any(distances[j][1] in connection for connection in connections):
            connections.append(set([distances[j][0], distances[j][1]]))
            break
        elif any(distances[j][0] in connection for connection in connections) and not any(distances[j][1] in connection for connection in connections):
            connections[connections.index(next(connection for connection in connections if distances[j][0] in connection))].add(distances[j][1])
            break
        elif not any(distances[j][0] in connection for connection in connections) and any(distances[j][1] in connection for connection in connections):
            connections[connections.index(next(connection for connection in connections if distances[j][1] in connection))].add(distances[j][0])
            break
        else:
            if connections.index(next(connection for connection in connections if distances[j][0] in connection)) == connections.index(next(connection for connection in connections if distances[j][1] in connection)):
                break
            else:
                aaa = next(connection for connection in connections if distances[j][0] in connection)
                bbb = next(connection for connection in connections if distances[j][1] in connection)
                connections[connections.index(aaa)].update(connections[connections.index(bbb)])
                connections.pop(connections.index(bbb))
                break

connections.sort(key=lambda x: len(x))
# print(len(connections[-1]) * len(connections[-2]) * len(connections[-3]))

# part 2

with open("8.txt", "r") as f:
    file = f.readlines()

points: dict[int, list[int]] = []

for i, line in enumerate(file):
    points.append((i, list(map(int, line.split(",")))))

distances: list[tuple[int, int, int]] = []

# find closest pairs
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = (points[i][1][0] - points[j][1][0])**2 + (points[i][1][1] - points[j][1][1])**2 + (points[i][1][2] - points[j][1][2])**2
        distances.append((i, j, distance))
        distances.append((j, i, distance))

distances.sort(key=lambda x: x[2])
i = 0

connections: list[set[int]] = []

lastconnection = []

while True:
    try: 
        if len(connections[0]) == 1000:
            break
    except IndexError:
        pass
    for j in range((i*2), len(distances)):
        lastconnection = [distances[j][0], distances[j][1]]
        if not any(distances[j][0] in connection for connection in connections) and not any(distances[j][1] in connection for connection in connections):
            connections.append(set([distances[j][0], distances[j][1]]))
            break
        elif any(distances[j][0] in connection for connection in connections) and not any(distances[j][1] in connection for connection in connections):
            connections[connections.index(next(connection for connection in connections if distances[j][0] in connection))].add(distances[j][1])
            break
        elif not any(distances[j][0] in connection for connection in connections) and any(distances[j][1] in connection for connection in connections):
            connections[connections.index(next(connection for connection in connections if distances[j][1] in connection))].add(distances[j][0])
            break
        else:
            if connections.index(next(connection for connection in connections if distances[j][0] in connection)) == connections.index(next(connection for connection in connections if distances[j][1] in connection)):
                break
            else:
                aaa = next(connection for connection in connections if distances[j][0] in connection)
                bbb = next(connection for connection in connections if distances[j][1] in connection)
                connections[connections.index(aaa)].update(connections[connections.index(bbb)])
                connections.pop(connections.index(bbb))
                break
    i += 1

print(int(file[lastconnection[0]].split(",")[0])*int(file[lastconnection[1]].split(",")[0]))