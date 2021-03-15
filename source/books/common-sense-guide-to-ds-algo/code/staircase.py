"""Let’s say we have a staircase of N steps, and a person has the ability to climb
one, two, or three steps at a time. How many different possible “paths” can
someone take to reach the top? Write a function that will calculate this for N
steps.
"""


def number_of_paths(n):
    """Solves the staircase problem"""
    if n < 0:
        return 0
    elif n in (0, 1):
        return 1
    else:
        return (
            number_of_paths(n-1) + number_of_paths(n-2) + number_of_paths(n-3)
        )
