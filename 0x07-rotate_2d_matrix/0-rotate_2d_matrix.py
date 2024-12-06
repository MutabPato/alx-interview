#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwisw in-place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.

    Returns:
        None: the matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
