# Gomoku Constants
BOARD_LENGTH = 15
WINNING_LENGTH = 5

# Game Functionalities
cross_turn = True
play_count = 0

# Board
board = []

for i in range(BOARD_LENGTH):
    board.append([])

for i in board:
    for j in range(BOARD_LENGTH):
        i.append(" ")


# Printing Board
def printing_board() -> None:
    """
    Prints the board
    """
    for row in board:
        print(row)


# Checking If Position is a Valid Position on the Board
def is_on_board(x: int, y:int) -> bool:
    """ Checks if the position is on the board 
    :param x: An `int` for position x in the board.
    :param y: An `int` for position y in the board.
    :return: The `bool` answer to whether or not
        the position is on the board
    """
    if x in range(BOARD_LENGTH) and y in range(BOARD_LENGTH):
        return True
    return False


# Player Input
def get_int(prompt: str) -> int:
    """
    Gets an integer from the player

    :param prompt: The request displayed in the console
    :return: The `int` given by the player
    """
    while True:
        integer = input(prompt)
        if integer.isnumeric():
            return int(integer)
        else:
            print("Please enter an Integer")


# Player Move Functionality
player_turn = True
turn_count = 0


def choose_pos(x: int, player_y: int) -> None:
    """
    Lets the player/computer choose a postition on
    the board.
    
    :param x: An `int` for position x in the board.
    :param y: An `int` for position y in the board. 
    """
    global turn_count, player_turn
    y = (BOARD_LENGTH - 1) - player_y

    if is_on_board(x, y):
        if board[y][x] == " ":
            if player_turn:
                board[y][x] = "X"
                player_turn = False
            else:
                board[y][x] = "O"
                player_turn = True
            turn_count += 1
        else:
            print(f"Positions x: {x} and y: {player_y} are occupied by {board[y][x]}")
    else:
        print(f"Positions x: {x} and y: {player_y} are not on the board")


# Resets the Game
def reset():
    global turn_count

    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            board[i][j] = " "

    player_turn = True
    turn_count = 0


# Finding Consecutives
def consecutive(item: str or int, items: list or tuple) -> int:
    """
    Finds the highest consecutive of something in a list
    :param item: The item to find the highest consecutive of.
    :param items: The items to look through to find the
        highest consecutive.
    :return: The highest consecutive of item in items.
    """
    high_consec = 0
    consec = 0
    for num in items:
        if num == item:
            consec += 1
            if consec > high_consec:
                high_consec = consec
        else:
            count = 0
    return high_consec


# Checking Win or Loss
def checking(moved: str, x: int, player_y: int) -> None or str:
    """
    Checks if the previous move was a winning move
    
    :param x: An `int` for position x in the board.
    :param y: An `int` for position y in the board.
    :return: If the previous move was a winning move
        or caused a draw, a string with the appropriate
        message will be returned. Otherwise nothing
        will be returned.
    """
    y = (BOARD_LENGTH - 1) - player_y

    cl_row = [None] * (WINNING_LENGTH * 2 - 1)
    cl_col = cl_row 
    cl_pdia = cl_row
    cl_ndia = cl_row

    # Starting Positions  
    starting_x = x - (WINNING_LENGTH - 1)
    starting_y = y + (WINNING_LENGTH - 1)
    
    # Row, Column and Diagonals
    for change in range(WINNING_LENGTH * 2 - 1):
        # Row
        if is_on_board(starting_x + change, y):
            cl_row[change] = board[y][starting_x + change]
        # Column
        if is_on_board(x, starting_y - change):
            cl_col[change] = board[starting_y - change][x]
        # Positive Diagonal
        if is_on_board(starting_x + change, starting_y - change):
            cl_pdia[change] = board[starting_y - change][starting_x + change]
        
        # Negative Diagonal        
        starting_x = x + (WINNING_LENGTH - 1)
        starting_y = y + (WINNING_LENGTH - 1)

        if is_on_board(starting_x - change, starting_y - change):
            cl_ndia[change] = board[starting_y - change][starting_x - change]

    if consecutive(moved, cl_row) >= WINNING_LENGTH:
        return f"{moved} Won!"
    
    if consecutive(moved, cl_col) >= WINNING_LENGTH:
        return f"{moved} Won!"
    
    if consecutive(moved, cl_pdia) >= WINNING_LENGTH:
        return f"{moved} Won!"
    
    if consecutive(moved, cl_ndia) >= WINNING_LENGTH:
        return f"{moved} Won!"
    
    # Draw
    if turn_count == (BOARD_LENGTH ** 2):
        return "Draw!"


# Running the Game
def main():
    """
    The Game Itself
    """
    play = True
    while play:
        while True:
            printing_board()

            move_x = get_int("x: ") 
            move_y = get_int("y: ")
            choose_pos(move_x, move_y)

            outcome = checking("X", move_x, move_y)
            if outcome is not None:
                printing_board()
                print(outcome)
                break

            printing_board()

            move_x = get_int("x: ") 
            move_y = get_int("y: ")
            choose_pos(move_x, move_y)

            outcome = checking("O", move_x, move_y)
            if outcome is not None:
                printing_board()
                print(outcome)
                break

        still_play = input("Play Again? (y/n): ")
        if still_play.casefold() in "y or n":
            if still_play.casefold() == "n":
                break
        reset()


if __name__ == "__main__":
    main()

