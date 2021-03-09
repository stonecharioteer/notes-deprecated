"""Recursive solution to reverse a string"""


def reverse_string(input_string):
    """Reverse string"""
    if len(input_string) > 1:
        return input_string[-1] + reverse_string(input_string[:-1])
    else:
        return input_string[0]


def test_reverse_string():
    sample_strings = [
        "hello world",
        "peter piper picked a pack of pickled peppers"
        "the cake is a lie",
        "once upon a time"
    ]
    for st in sample_strings:
        assert reverse_string(st) == "".join(reversed(st))
