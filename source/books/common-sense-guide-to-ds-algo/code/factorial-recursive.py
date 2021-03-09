"""Recursive function to get the nth factorial"""


def factorial(n):
    """Function to get the nth factorial"""
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def test_factorial():
    import random
    import math
    n = random.randint(1, 1000)

    assert factorial(n) == math.factorial(
        n), "unable to calculate the nth factorial"
