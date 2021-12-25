
from random import randint

board = []

# print("Hello!!")
# print("Welcome to BattleShip")

size = input("Enter board size: ")

size = int(size)

for i in range(0, size):
    board.append(["O"] * size)


def print_board(board):
    for i in board:
        print(" ".join(i))


# print_board(board)


def place_ship(board):
    x_var = randint(0, size - 1)
    y_var = randint(0, size - 1)
    print(x_var, y_var)
    board[x_var][y_var] = "X"
    # print_board(board)


place_ship(board)
