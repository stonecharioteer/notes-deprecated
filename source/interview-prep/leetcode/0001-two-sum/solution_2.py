"""Solution for the Leetcode problem #0001 Two Sum
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Given a list of integers, find two numbers that add up to
    a given target integer
    While this solution does have an n.logn Time complexity, it
    has an O(1) space complexity and is a better solution
    when we have memory constraints.
    """

    # sort the array
    array.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        l_val = nums[left]
        r_val = nums[right]
        if l_val + r_val == target:
            return [l_val, r_val]
        elif l_val + r_val > target:
            right -= 1
        elif l_val + r_val < target:
            l_val += 1

    return []
