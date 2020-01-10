from pprint import pprint

n = 4

board = [[0] * n for i in range(n)]


def place_queens(board, len_board):
    for i in range(n):
        for j in range(n):
            val = queen_present(i, j)
            print(val)
            if not val:
                board[i][j] = 1
            print(board)
            # exit(1)
    pass


def queen_present(i, j):
    for k in range(n):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(n):
        for l in range(n):
            if (k + l) == i + j or (k - l) == i - j:
                if board[k][l] == 1:
                    return True

    return False


def NQueen(n):
    if n == 0:
        return True
    for i in range(0, n):
        for j in range(0, n):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not (queen_present(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                # recursion
                # wether we can put the next queen with this arrangment or not
                if NQueen(n - 1):
                    return True
                board[i][j] = 0


def main():
    n = 4  # int(input("Enter the number"))

    # board = [[0] * n for i in range(4)]

    pprint(board)
    NQueen(n)
    for i in range(n):
        for j in range(n):
            place_queens(board, len(board))


if __name__ == '__main__':
    main()
