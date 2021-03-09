"""Recursive algorithm to count x in a string"""


def count_x(input_string):
    """Counts the occurrence of x in a string"""
    if len(input_string) == 1:
        return 1 if input_string[0] == "x" else 0
    elif len(input_string) > 1:
        return (1 if input_string[0] == "x" else 0) + count_x(input_string[1:])
    else:
        return 0


def test_count_x():
    """tests that the counting function works"""
    input_strings = [
        "x",
        "",
        "lmzxcvuljwsdf;laxlvjsdflweo asdflkxc;lvslweropupas xlx;lkvj;ljweorijxlj ;xlxx;lkj;lxx ",
        "something that doesn't have it"
    ]
    for string in input_strings:
        assert count_x(string) == string.count("x")
