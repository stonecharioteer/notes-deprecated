"""Solution for the Leetcode Problem #0003 Longest Substring without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    """Given an input string `s`, return the length of the longest substring
    without repeating characters"""

    start = max_length = 0
    used_characters = {}

    for index, character in enumerate(s):
        if used_characters.get(character) is not None and start <= used_characters[character]:
            start = used_characters[character] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used_characters[character] = index

    return max_length
