#!/usr/bin/python3
"""
12-module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    new_2 = []
    row = []
    if n <= 0:
        return new_2
    new_2 = [[1]]

    for i in range(1, n):
        row = [1]
        if i > 0:
            for x in range(1, i):
                row.append(new_2[i - 1][x - 1] + new_2[i - 1][x])
            row.append(1)
        new_2.append(row)
    return new_2
