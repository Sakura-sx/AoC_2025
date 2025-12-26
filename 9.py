# part 1
def solve9_1():
    with open('9.txt', 'r') as file:
        file = file.readlines()

    grid = []

    for line in file:
        x, y = int(line.split(',')[0]), int(line.split(',')[1])
        grid.append((x, y))

    biggest_square = 0
    for point in grid:
        x, y = point
        for other_point in grid:
            other_x, other_y = other_point
            biggest_square = max(biggest_square, abs(x - other_x + 1) * abs(y - other_y + 1))
            biggest_square = max(biggest_square, abs(x - other_x + 1) * abs(other_y - y + 1))
            
            
    print(biggest_square)


# part 2
def solve9_2():
    with open('9.txt', 'r') as file:
        file = file.readlines()

    grid = []
    horizontal_lines = {}
    vertical_lines = {}

    for i, line in enumerate(file):
        x1, y1 = int(line.split(',')[0]), int(line.split(',')[1])
        grid.append((x1, y1))
        if i == len(file) - 1:
            x2, y2 = int(file[0].split(',')[0]), int(file[0].split(',')[1])
        else:
            x2, y2 = int(file[i+1].split(',')[0]), int(file[i+1].split(',')[1])
        if x1 == x2:
            vertical_lines[x1] = (min(y1, y2), max(y1, y2))
        else:
            horizontal_lines[y1] = (min(x1, x2), max(x1, x2))

    biggest_square = 0
    for point in grid:
        x, y = point
        for other_point in grid:
            other_x, other_y = other_point
            
            current_area = (abs(x - other_x) + 1) * (abs(y - other_y) + 1)
            
            if biggest_square < current_area:
                vertical_line_check = True
                horizontal_line_check = True
                
                min_x, max_x = min(x, other_x), max(x, other_x)
                min_y, max_y = min(y, other_y), max(y, other_y)

                for vertical_line in vertical_lines:
                    if min_x < vertical_line < max_x:
                        line_y_min, line_y_max = vertical_lines[vertical_line]
                        
                        if line_y_min < max_y and line_y_max > min_y:
                            vertical_line_check = False
                            break
                
                if vertical_line_check:
                    for horizontal_line in horizontal_lines:
                        if min_y < horizontal_line < max_y:
                            line_x_min, line_x_max = horizontal_lines[horizontal_line]
                            
                            if line_x_min < max_x and line_x_max > min_x:
                                horizontal_line_check = False
                                break
                    
                    if horizontal_line_check:
                        biggest_square = current_area

    print(biggest_square)


def main():
    solve9_1()
    solve9_2()

if __name__ == "__main__":
    main()