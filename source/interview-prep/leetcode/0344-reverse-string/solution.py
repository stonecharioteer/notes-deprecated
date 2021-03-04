"""Solution for Leetcode problem #344 Reverse String
https://leetcode.com/problems/reverse-string/
"""


def reverse_string(inp_str: list[str]) -> list[str]:
    """Returns a reversed list of chars
    """

    mid = len(inp_str) // 2
    for index in range(mid):
        counterpart = -1 - index
        inp_str[index], inp_str[counterpart] = (
            inp_str[counterpart], inp_str[index]
        )
    return inp_str


def test_reverse_string():
    input_strings = [
        "hello",
        "avengers assemble",
        "there is no cake",
        "hodl"
    ]
    for input_string in input_strings:
        str_list = list(input_string)
        rev_string = list(reversed(str_list))
        assert reverse_string(
            str_list) == rev_string, "Unable to reverse `{}`".format(input_string)
