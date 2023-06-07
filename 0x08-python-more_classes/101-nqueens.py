#!/usr/bin/python3
"""import module
"""
import sys

"""define safe
"""


def is_safe(board, row, col):
    """Check if the current position is safe for the queen
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, board, row):
    if row == n:
        """If all queens are placed, print the solution
        """
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            """Place the queen on the board
            """
            board[row] = col
            """Recursively solve the problem for the next row
            """
            solve_nqueens(n, board, row + 1)

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0] * n
    solve_nqueens(n, board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
