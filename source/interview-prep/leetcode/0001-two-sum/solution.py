"""Solution for the Leetcode problem #0001 Two Sum
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Given a list of integers, find two numbers that add up to
    a given target integer."""
    values = {}
    for index, item in enumerate(nums):
        if values.get(item) is None:
            values[item] = [index]
        else:
            values[item].append(index)

    for index, item in enumerate(nums):
        matching_value = target - item
        positions = values.get(matching_value)
        if positions is not None:
            if matching_value == item:
                if len(positions) > 1:
                    return item, matching_value
            else:
                return item, matching_value

    return []
