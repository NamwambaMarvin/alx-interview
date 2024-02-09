#!/usr/bin/python3
"""
Pascals triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists containing
    pascal triangle sequence
    """
    mainList = []
    if n < 0:
        return mainList
    mainList = [[1]]
    if n == 1:
        return mainList

    for row in range(1, n):
        toleft = -1  # Left
        toright = 0  # Right
        innerList = []
        for column in range(row + 1):
            integer = 0
            if toleft > -1:
                integer += mainList[row - 1][toleft]
            if toright < row:
                integer += mainList[row - 1][toright]
            toright += 1
            toleft += 1
            innerList.append(integer)
        mainList.append(innerList)
    return mainList
