#!/usr/bin/python3
"""
N Queens
"""

import sys


def is_valid(board, row, col):
    """Check if a queen can be placed at board[row][col]
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """solves the N-Queens problem
    """
    def solve(row, board):
        """Placing a queen in each column and checks if the position is valid
        """
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    solve(0, [-1] * n)
    return solutions


def main():
    """Check for correct usage
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem and print each solution
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
