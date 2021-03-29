"""Solution for the Leetcode Problem #0392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
"""


def is_subsequence(input_string: str, sequence: str) -> bool:
    """Checks if a given sequence is a subsequence of an input string"""
    # For this solution, iterate through the input string
    # while maintaining a cursor into the sequence string.
    # Keep checking the sequence string for matches,
    # and only go to the next value in the sequence when
    # there *is* a match.
    # this ensures that although we are looping through 2 inputs, we only
    # loop through each once overall.
    # Thus, the time complexity is just O(n) while the space complexity is O(1)
    index_sequence = 0
    for character in input_string:
        if len(sequence) > index_sequence:
            if sequence[index_sequence] == character:
                index_sequence += 1
        if len(sequence) == index_sequence:
            return True
    return len(sequence) == index_sequence
