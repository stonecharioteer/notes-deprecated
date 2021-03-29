"""Solution for the Leetcode Problem #1295
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""


def numbers_with_even_number_of_digits(nums: list[int]) -> int:
    """Given an array `nums` of integers, return how many
    of them contain an even number of digits"""
    evens = 0
    for number in nums:
        # check if the given number has even number of digits
        divides = 0
        # the quicker, pythonically speaking, method is to convert the number
        # to a string and use its length.
        while number != 0:
            number = number // 10
            divides += 1
        if divides % 2 == 0:
            evens += 1

    return evens
