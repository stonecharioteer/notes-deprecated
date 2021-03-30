"""Solution for Leetcode #0004 - Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


def median_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    """Return a median of two sorted arrays in O(log(m+n))
    """
    # Note: Please read the explanation / watch the linked video
    # *before* trying to understand this.
    if len(nums1) < len(nums2):
        smaller_array = nums1
        larger_array = nums2
    else:
        smaller_array = nums2
        larger_array = nums1

    # perform binary search on the smaller array.
    start = 0
    end = len(smaller_array) - 1

    found_partition = False
    counter = 0
    while not found_partition:
        counter += 1
        partition_smaller_array = (end + start) // 2

        partition_larger_array = (
            len(smaller_array) + len(larger_array) + 1
        ) // 2 - partition_smaller_array

        left_smaller = smaller_array[:partition_smaller_array]
        left_larger = larger_array[:partition_larger_array]
        right_smaller = smaller_array[partition_smaller_array:]
        right_larger = larger_array[partition_larger_array:]

        max_left_smaller = left_smaller[-1] if len(
            left_smaller) > 0 else -float('inf')
        min_right_larger = right_larger[0] if len(
            right_larger) > 0 else float('inf')
        max_left_larger = left_larger[-1] if len(
            left_larger) > 0 else -float("inf")
        min_right_smaller = right_smaller[0] if len(
            right_smaller) > 0 else float("inf")

        if max_left_smaller <= min_right_larger and max_left_larger <= min_right_smaller:
            found_partition = True
        elif max_left_smaller > min_right_larger:
            end -= 1
        else:
            start += 1

            # now the median will be in the last four digits:
    total_length = len(smaller_array) + len(larger_array)

    if total_length % 2 == 0:  # this is even
        median = (max(max_left_smaller, max_left_larger
                      ) + min(min_right_larger, min_right_smaller))/2
    else:
        median = max(max_left_smaller, max_left_larger)

    return median


def test_base():
    import random
    import statistics

    list_1 = [random.randint(0, 100)
              for _ in range(random.randint(10**5, 10**6))]
    list_2 = [random.randint(0, 100)
              for _ in range(random.randint(10**5, 10**6))]

    list_1.sort()
    list_2.sort()

    calculated_median = median_two_sorted_arrays(list_1, list_2)

    merged_list = sorted(list_1 + list_2)

    median = statistics.median(merged_list)
    assert calculated_median == median, f"Returned value {calculated_median=} is wrong! {median=}"


def test_edgecase():
    list_1 = [1, 3]
    list_2 = [2]

    calculated_median = median_two_sorted_arrays(list_1, list_2)
    median = 2
    assert calculated_median == median, f"Returned value {calculated_median=} is wrong! {median=}"
