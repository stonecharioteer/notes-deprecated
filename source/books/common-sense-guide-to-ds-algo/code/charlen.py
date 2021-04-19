"""Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings.
"""


def charlen(input_array):
    """Takes an array of strings and returns the total number of characters"""

    if len(input_array) == 1:
        return len(input_array[0])
    else:
        return len(input_array[0]) + charlen(input_array[1:])
