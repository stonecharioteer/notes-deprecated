"""Program to find the factorial of a number"""


def factorial(n: int) -> int:
    """Function to find the factorial of a number"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    """Test for the factorial function"""
    import math
    for number in range(500):
        assert factorial(number) == math.factorial(
            number), "Could not calculate the factorial of {}".format(number)
