import random

game_state = ["_" for i in range(0, 9)]


def print_board():
    print(game_state[0:3])
    print(game_state[3:6])
    print(game_state[6:9])


def update_board(position, symbol, move_by_user):
    if position < 0 or position > 8:
        if move_by_user:
            print("Invalid position. Choose number between 0 and 8!")
        return False
    current_symbol = game_state[position]
    if current_symbol != "_":
        if move_by_user:
            print(f"Position already occupied with '{current_symbol}'. Choose another one!")
        return False

    game_state[position] = symbol
    return True


def game_finished():
    g = game_state

    # horizontal rows
    for i in [0, 3, 6]:
        if g[i] == g[i + 1] == g[i + 2] != "_":
            print(f"Player {g[i]} wins!")
            return True

    # vertical rows
    for i in [0, 1, 2]:
        if g[i] == g[i + 3] == g[i + 6] != "_":
            print(f"Player {g[i]} wins!")
            return True

    # diagonal 1
    if g[0] == g[4] == g[8] != "_":
        print(f"Player {g[0]} wins!")
        return True
    # diagonal 2
    if g[2] == g[4] == g[6] != "_":
        print(f"Player {g[2]} wins!")
        return True

    if "_" not in g:
        print(f"Draw!")
        return True

    return False


def opponents_move():
    if "_" not in game_state:
        # board already full, don't do anything
        return

    success = False
    while not success:
        r = random.randint(0, 8)
        success = update_board(r, 'o', False)


if __name__ == "__main__":
    print("Welcome to TicTacToe!")
    print("You can put your x at the following positions:")
    print('[0,1,2]\n[3,4,5]\n[6,7,8]')

    print("Current board:")
    print_board()
    while not game_finished():
        i = int(input("Where do you want to put your 'x'? (0-8) "))
        if update_board(i, "x", True):
            opponents_move()
            print_board()
