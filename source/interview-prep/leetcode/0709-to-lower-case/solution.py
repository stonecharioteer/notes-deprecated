"""Solution for the Leetcode problem #0709 - To Lower Case
https://leetcode.com/problems/to-lower-case/
"""


def to_lower_case(s: str) -> str:
    """Converts a string to lowercase"""
    s = [character for character in s]
    for index, character in s:
        s[index] = chr(ord(character) - (ord('A') - ord('a'))) \
            if ord('A') <= ord(character) <= ord('Z') else character

    return "".join(s)
