#!/usr/bin/python3
"""import module
"""


import sys

"""define safe
"""


def is_safe(board, row, col):
    """Check if a queen can be placed at the given position without attacking any other queens

    Check the current row on the left side"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    """Check the upper diagonal on the left side
    """
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """Check the lower diagonal on the left side
    """
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    """Base case: All queens are placed
    """
    if col >= N:
        solutions.append([i[:] for i in board])
        return

    """Recursive backtracking to find a solution
    """
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, col + 1)
            board[row][col] = 0


def print_solutions():
    """Print the solutions in the required format
    """
    for solution in solutions:
        print([[row, col] for col, row in enumerate(solution)])


"""Main program
"""
if __name__ == "__main__":
    """Check the number of arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """Get the value of N from the command-line argument
    """
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """Check the value of N
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Initialize an empty board
    """
    board = [[0 for _ in range(N)] for _ in range(N)]

    """List to store the solutions
    """
    solutions = []

    """Solve the N-Queens problem
    """
    solve_n_queens(board, 0)

    """Print the solutions
    """
    print_solutions()
