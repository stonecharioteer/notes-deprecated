"""Solution for the Leetcode Problem #0485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""


def find_max_consecutive_ones(nums: list[int]) -> 1:
    """Given a binary array, find the maximum number of consecutive 1s in this array"""
    ones = []
    count = 0
    for item in nums:
        if item == 1:
            count += 1
        else:
            if count > 0:
                ones.append(count)
            count = 0
    return max(ones)
