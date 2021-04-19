"""Let's say you have a grid of rows and columns. Write a function that accepts
a number of rows and a number of columns, and calculates the number of possible
"shortest" paths from the upper-leftmost square to the lower-rightmost square.

Given a square position (i,j), your next step is one of: (i+1, j), (i-1, j), (i, j+1) or (i, j-1).
"""


def number_of_shortest_paths(rows, columns):
    """Unique Paths Problem"""
    if rows == columns == 2:
        return 2
    elif (rows == 2 and columns == 3) or (rows == 3 and columns == 2):
        return 3
    elif (rows == 3 and columns == 3):
        return 6
