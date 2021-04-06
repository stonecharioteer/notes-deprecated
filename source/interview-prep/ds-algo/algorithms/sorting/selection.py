"""Selection Sort"""


def selection_sort(array: list) -> list:
    """Selection Sort"""
    # first, loop through the entire array
    for index in range(len(array)):
        # let's assume the *current* position
        # occupies the ith-smallest value (as in, the value is where it needs
        # to be.) This current position is marked as `minimum_number_index`
        minimum_number_index = index
        # loop through the next items in the array
        for index_2 in range(index+1, len(array)):
            # if the item at this index_2 is lesser than the item
            # in the `minimum_number_index` position, then *select*
            # this index as the `minimum_number_index`
            if array[index_2] < array[minimum_number_index]:
                minimum_number_index = index_2
        # if the `index` is not equal to the `minimum_value_index`,
        # this means our assumption was wrong,
        # and that we *selected* the appropriate value.
        if minimum_number_index != index:
            # Swap these values.
            array[index], array[minimum_number_index] = (
                array[minimum_number_index], array[index]
            )
    return array


def test_selection_sort():
    """Tests selection sort"""
    import random
    array = [random.randint(0, 10000) for _ in range(5)]
    sorted_array = sorted(array)
    bubble_sorted_array = selection_sort(array)
    assert bubble_sorted_array == sorted_array, "Selection sorting failed"
