"""Binary Search Algorithm"""


def search_in_ordered_array(arr: list, item: int) -> int:
    """Finds item in an ordered array"""
    # loop through array, if `item` is lesser than the mid,
    # look left, else look right.
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid_point = (start + end)//2
        mid = arr[mid_point]
        if mid < item:
            start = mid_point + 1
        elif mid > item:
            end = mid_point - 1
        else:
            return mid_point

    return -1


def test_binary_search_even_inputs():
    """check that this works for even number of inputs"""
    array = [1, 2, 3, 4]
    pos = search_in_ordered_array(array, 1)
    assert pos == 0


def test_binary_search_odd_inputs():
    """Tests that this works for odd number of inputs"""
    array = [1, 2, 3, 4, 5]
    pos = search_in_ordered_array(array, 4)
    assert pos == 3


def test_binary_search_not_found():
    """Tests that this returns -1 when the element is not found"""

    array = list(range(10**5))
    pos = search_in_ordered_array(array, 10**5+1)
    assert pos == -1
