import random

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def create_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def game_over():
    count = 0
    for i, j, k in win_combination:
        if board[i] == board[j] == board[k] == 'O':
            print("Congratulation!! Player 1 won")
            return True
        if board[i] == board[j] == board[k] == 'X':
            print("Congratulation!! Player 2 won")
            return True



def game():
    game_end = False
    while not game_end:
        create_board()
        game_end = game_over()
        if game_end is True:
            break
        print("first player turn")
        player1()
        create_board()
        game_end = game_over()
        print(game_end)
        if game_end is True:
            break
        print("second player turn")
        player2()


def player1():
    get_position = position()
    if board[get_position] == 'X' or board[get_position] == 'O':
        print("\n please assign new position")
        player2()
    else:
        board[get_position] = 'O'


def position():
    while True:
        get_pos = int(input("enter your position"))
        if get_pos in board:
            return get_pos
        else:
            print("please enter number between 1 to 9 ")


def player2():
    get_position = position()
    # get_position = str(get_position)
    if board[get_position] == 'X' or board[get_position] == 'O':
        print("\n please assign new position")
        player2()
    else:
        board[get_position] = 'X'


if __name__ == "__main__":
    game()
