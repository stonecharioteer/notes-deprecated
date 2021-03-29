"""Solution for the Leetcode problem #0771 Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/
"""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """Given a string of jewels and a string of stones,
    count the number of stones that are jewels"""

    jewels_hashmap = {}

    for jewel in jewels:
        jewels_hashmap[jewel] = 1
    jewels_count = 0
    for stone in stones:
        jewels_count += jewels_hashmap.get(stone, 0)
    return jewels_count
