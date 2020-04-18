# BY : Mohamed Ashraf Gaber.
# This is a Sudoku Solver by Python.
# It can solve any valid Sudoku board.

# This is the board that the project will solve it.
# You can change the board if you need to solve another board.
# All zeros are the empty places.
board = [
    [0, 4, 3, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 6, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 4, 1, 0, 0],
    [9, 0, 1, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 7, 2, 6, 0, 0, 0],
    [0, 0, 8, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 7, 2, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 5, 0, 6, 0],
]


# The play function will contain the functions we will use.
def play():
    # First print the board without any solution
    print('Before :- ')
    draw_board(board)

    # Second solve the board
    solve(board)

    # Third print the board after solving it
    print('\nAfter :-')
    draw_board(board)


# The draw board function will print the board in the terminal.
def draw_board(game):
    for i in range(len(game)):
        # After three rows, print a new horizontal line
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')

        for j in range(len(game[0])):
            # After three columns, print a new vertical line
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            # If we reach the end of the row, print last number and a new line
            if j == 8:
                print(game[i][j])

            # Else print the number and a space between it and the following number
            else:
                print(game[i][j], end=' ')


# The solve function will solve the board.
def solve(game):
    # Try to get a new empty place
    get = get_empty(game)

    # If there isn't an empty place, return True and it is solved
    if not get:
        return True

    # If not, get the position of the new place in (row, col)
    row, col = get

    # Try every number from 1 to 10 to get a valid number
    for i in range(1, 10):
        # if the number is valid, replace the zero to this number
        if is_valid(game, i, (row, col)):
            game[row][col] = i

            # Try to continue solving after replacing last number.
            # If it works, it will return True and it's solved
            if solve(game):
                return True

            # Else set it to zero
            game[row][col] = 0

    return False


# The find empty will return the position of the first empty place in the board.
# But if there isn't an empty place, it will return None.
def get_empty(game):
    # Loop for every single place.
    # If the place is empty, return the position for this place.
    for i in range(len(game)):
        for j in range(len(game[0])):
            if game[i][j] == 0:
                return (i, j)  # i for row. j for column


# The valid function will check if the number
# in this position in this board is valid or not.
def is_valid(game, num, pos):
    # First, checking in row
    for i in range(len(game)):
        if game[pos[0]][i] == num and i != pos[1]:
            return False

    # Second, checking in column
    for i in range(len(game[0])):
        if game[i][pos[1]] == num and i != pos[0]:
            return False

    # Third, checking in box
    box_x = pos[1] // 3  # The x position for the box
    box_y = pos[0] // 3  # The y position for the box

    # Loop for the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if game[i][j] == num and (i, j) != pos:
                return False

    return True  # Return True if the number is valid


play()
