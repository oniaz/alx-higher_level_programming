#!/usr/bin/python3
""" task 12 """


def pascal_triangle(n):
    """Generates Pascal's Triangle.

        Args:
            n (int): Number of rows.

        Returns:
            list: A list of lists of integers representing Pascal’s triangle,
                where each inner list is a row in the triangle.
    """
    if n < 1:
        return []
    triangle = []
    for r in range(n):
        row = []
        for b in range(r + 1):
            if (b == 0) or (b == r):
                row.append(1)
            else:
                x = triangle[r - 1][b - 1] + triangle[r - 1][b]
                row.append(x)
        triangle.append(row)
    return triangle
