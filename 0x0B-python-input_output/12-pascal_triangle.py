#!/usr/bin/python3
"""module pascal
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n: Number of rows in the Pascal's triangle.

    Returns:
        A list of lists containing the values of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
