board = []

size = input("Enter board size: ")

size = int(size)

for i in range(0, size):
    board.append(["O"] * size)


def print_board(board):
    for i in board:
        print(" ".join(i))


print_board(board)
