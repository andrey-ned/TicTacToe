X_or_O = 1
cells = [["_" for j in range(3)] for i in range(3)]


def find_error(cell):
    row = 0
    col = 0
    n_of_x = 0
    n_of_o = 0
    for i in range(3):
        if cell[i][0] == cell[i][1] == cell[i][2] != '_':
            row += 1
        elif cell[0][i] == cell[1][i] == cell[2][i] != '_':
            col += 1
        n_of_x += cell[i].count("X")
        n_of_o += cell[i].count("O")
    if row == 2 or col == 2:
        return True
    elif abs(n_of_x - n_of_o) >= 2:
        return True


def win_func(cell, winner):

    if find_error(cell):
        print_field(cells)
        print("Impossible")
        return False
    for i in range(len(winner)):
        if winner[i][0] == winner[i][1] == winner[i][2] == 'X':
            print_field(cells)
            print("X wins")
            return False

        elif winner[i][0] == winner[i][1] == winner[i][2] == 'O':
            print_field(cells)
            print("O wins")
            return False
    else:
        count_under = 0
        for i in range(3):
            count_under += cell[i].count("_")
        if count_under == 0:
            print_field(cells)
            print("Draw")
            return False
    return True


def checker(n, m, cell):
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        print("You should enter numbers!")
        return False
    else:
        if n > 3 or m > 3:
            print("Coordinates should be from 1 to 3!")
            return False
        elif cell[-m][n - 1] != '_':
            print("This cell is occupied! Choose another one!")
            return False
    return True


def print_field(field):
    print("---------")
    for i in range(3):
        print("| ", end='')
        for j in range(3):
            print(field[i][j], end=" ")
        print(" |")
    print("---------")


def step(cell, n, m):
    global X_or_O
    X_or_O += 1
    if X_or_O % 2 == 1:
        cell[-m][n - 1] = "O"
    else:
        cell[-m][n - 1] = "X"
    return cell


print_field(cells)

try:
    x, y = [int(i) for i in input("Enter the coordinates: ").split()]
    while x > 3 or y > 3:
        print("Coordinates should be from 1 to 3!")
        x, y = [int(i) for i in input("Enter the coordinates: ").split()]
    cells = step(cells, x, y)
    print_field(cells)
except ValueError:
    print("You should enter numbers!")
finally:
    x, y = [int(i) for i in input("Enter the coordinates: ").split()]
    while not checker(x, y, cells):
        x, y = [i for i in input("Enter the coordinates: ").split()]
    else:
        x = int(x)
        y = int(y)
    cells = step(cells, x, y)
    win_pos = []
    while win_func(cells, win_pos):
        print_field(cells)
        x, y = [int(i) for i in input("Enter the coordinates: ").split()]
        while not checker(x, y, cells):
            x, y = [int(i) for i in input("Enter the coordinates: ").split()]
        cells = step(cells, x, y)
        win_pos = [[cells[0][0], cells[0][1], cells[0][2]], [cells[1][0], cells[1][1], cells[1][2]],
                   [cells[2][0], cells[2][1], cells[2][2]], [cells[0][0], cells[1][0], cells[2][0]],
                   [cells[0][1], cells[1][1], cells[2][1]], [cells[0][2], cells[1][2], cells[2][2]],
                   [cells[0][0], cells[1][1], cells[2][2]], [cells[0][2], cells[1][1], cells[2][0]]]
