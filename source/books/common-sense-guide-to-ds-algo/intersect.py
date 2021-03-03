"""Algorithm to determine the intersection of two arrays"""


def intersect_arrays(arr_1: list, arr_2: list) -> list:
    """Returns the intersection of two arrays"""
    from collections import OrderedDict
    arr_1_hash = OrderedDict()
    for item in arr_1:
        arr_1_hash[item] = arr_1_hash.get(item, 0) + 1

    arr_2_hash = OrderedDict()
    for item in arr_2:
        arr_2_hash[item] = arr_2_hash.get(item, 0) + 1

    intersection = []
    for key in arr_1_hash:
        count_1 = arr_1_hash[key]
        count_2 = arr_2_hash.get(key, 0)
        # include items that are in arr_1, and arr_2
        occurs_in_both = min(count_1, count_2)
        intersection.extend([key]*occurs_in_both)
    return intersection


def test_intersect_arrays():
    """Tests that the above algorithm works"""
    assert intersect_arrays([1, 2, 3], [2]) == [2]
    assert intersect_arrays([1, 1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert intersect_arrays([2, 1, 3], [1, 2, 2, 3]) == [2, 1, 3]
