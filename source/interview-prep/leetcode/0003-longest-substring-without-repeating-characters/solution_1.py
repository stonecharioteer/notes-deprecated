"""Solution for the Leetcode Problem #0003 Longest Substring without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    """Given an input string `s`, return the length of the longest substring without repeating characters"""
    lengths = []

    previous_string = []
    for character in s:
        if character not in previous_string:
            previous_string.append(character)
        else:
            lengths.append(len(previous_string))
            previous_string = previous_string[previous_string.index(
                character)+1:]+[character]

    lengths.append(len(previous_string))

    return max(lengths) if len(lengths) > 0 else len(s)
