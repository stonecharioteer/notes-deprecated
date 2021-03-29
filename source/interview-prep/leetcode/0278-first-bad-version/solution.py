"""Solution for the Leetcode problem #0278 First Bad Version
https://leetcode.com/problems/first-bad-version/

"""


def isBadVersion(version) -> bool:
    import random
    return random.choice([True, False])


def first_bad_version(n):
    """Given a function whose calls are to be limited, identify the first bad version"""
    start = 1
    end = n
    last_bad = None
    while start <= end:
        mid_point = (start + end) // 2
        if isBadVersion(mid_point):
            last_bad = mid_point
            end = mid_point - 1
        else:
            start = mid_point + 1

    return last_bad
