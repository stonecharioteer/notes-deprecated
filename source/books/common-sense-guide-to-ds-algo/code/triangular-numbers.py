"""There is a numerical sequence known as Triangular Numbers. The pattern
begins as `1, 3, 5, 10, 15, 21`, and continues onward with the Nth number in
the pattern, which is N plus the previous number. For example, the 7th number
in the sequence is 28, since it's 7 (which is N) plus 21 (the previous number
in the sequence). Write a function that accepts the number for N and
returns the correct number from the series. That is, if the function was passed
the number 7, the function would return 28."""


import pytest


def triangular_number(n):
    """Return the nth triangular number"""
    defined_values = [1, 3, 5, 10, 15, 21]
    if 1 <= n <= 6:
        return defined_values[n-1]
    else:
        return n + triangular_number(n-1)


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (2, 3),
    (3, 5),
    (4, 10),
    (5, 15),
    (6, 21),
    (7, 28),
    (8, 36),
    (9, 45)
])
def test_triangular_number(test_input, expected):
    """Test triangular numbers"""
    assert triangular_number(test_input) == expected, (
        f"Triangular number value for {test_input} should have been {expected}"
    )
