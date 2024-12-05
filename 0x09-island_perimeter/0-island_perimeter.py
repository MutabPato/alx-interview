#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in the grid.

    Args:
        grid (list of list of int): 2D list where 1 represents land
        and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for a land cell
                perimeter += 4

                # Check if there is adjacent land on each side
                if i > 0 and grid[i - 1][j] == 1:  # Above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
