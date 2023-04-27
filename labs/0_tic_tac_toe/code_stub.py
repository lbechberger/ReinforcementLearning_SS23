

game_state = ["_" for i in range(0, 9)]


def print_board():
    print(game_state[0:3])
    print(game_state[3:6])
    print(game_state[6:9])


def update_board(position, symbol, move_by_user):
    # Task: Check, if the position is valid (0-8), if not: print error message
    #   (only if move was made by user, i.e., move_by_user == True) and return False
    # Task: Check, if the position is empty, if not: print error message
    #   (only if move was made by user, i.e., move_by_user == True) and return False
    game_state[position] = symbol
    return True


def game_finished():
    # Task: Write logic to decide if game is finished (return "True" if game is finished, "False" otherwise)
    # and print the result from the human player's perspective ("win", "loose", "draw").
    return False


if __name__ == "__main__":
    print("Welcome to TicTacToe!")
    print("You can put your 'x' at the following positions:")
    print('[0,1,2]\n[3,4,5]\n[6,7,8]')

    print("Current board:")
    print_board()
    while not game_finished():
        i = int(input("Where do you want to put your 'x'? (0-8) "))
        if update_board(i, "x", True):
            # Task: implement helper function opponents_move(), which is called here, and which simulates
            # the oppontent's move. Hint: you can combine randint() with update_board()
            print_board()
