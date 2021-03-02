"""Bubble sort implementation"""


def bubble_sort(array: list) -> list:
    """Uses bubble sort to sort a list"""
    # Bubble sort is a O(N**2) algorithm
    # First, assume the array is not sorted
    is_sorted = False
    # Now, fix the range until the end of the array
    unsorted_until = len(array) - 1
    # repeat until it is sorted
    while not is_sorted:
        # assume it is sorted
        is_sorted = True
        # loop through the range from 0 till the last sorted index.
        for index in range(unsorted_until):
            # Check current item with the next item.
            # This is safe to do because there's always one item ahead of this
            # this is because we use unsorted_until = len(array) -1, which
            # yields the index of the last item, but we also use
            # range(unsorted_until), which gives us an iterable from 0 *till*
            # that number, but not including it.  So even in the first trial,
            # we do not reach the end of the list.
            if array[index] > array[index+1]:
                # If the item is larger than the next item, *bubble* the
                # smaller one upwards.  Another way to think of bubble sort is
                # to think of it as *sinking* the largest item to the bottom of
                # the row at each trial.
                array[index], array[index+1] = array[index+1], array[index]
                # Now that a change has been made, you know that the list was
                # unsorted
                is_sorted = False
        # Reduce the sorting view to exclude the item.
        unsorted_until -= 1
    # return the item, note that this is not really necessary since we are
    # *modifying* the original item.
    return array


def test_bubble_sort():
    """Tests bubble sort"""
    import random
    array = [random.randint(0, 10000) for _ in range(5)]
    sorted_array = sorted(array)
    bubble_sorted_array = bubble_sort(array)
    assert bubble_sorted_array == sorted_array, "Bubble sorting failed"
