"""Bubble sort implementation"""


def bubble_sort(array: list) -> list:
    """Uses bubble sort to sort a list"""
    # Bubble sort is a O(N**2) algorithm
    is_sorted = False
    unsorted_until = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for index in range(unsorted_until):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                is_sorted = False
        unsorted_until -= 1
    return array


def test_bubble_sort():
    """Tests bubble sort"""
    import random
    array = [random.randint(0, 10000) for _ in range(5)]
    sorted_array = sorted(array)
    bubble_sorted_array = bubble_sort(array)

    assert bubble_sorted_array == sorted_array, "Bubble sorting failed"
