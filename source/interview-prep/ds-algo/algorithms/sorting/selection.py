"""Selection Sort"""


def selection_sort(array: list) -> list:
    """Selection Sort"""
    for index in range(len(array)):
        minimum_number_index = index
        for index_2 in range(index+1, len(array)):
            if array[index_2] < array[minimum_number_index]:
                minimum_number_index = index_2
        if minimum_number_index != index:
            array[index], array[minimum_number_index] = array[minimum_number_index], array[index]
    return array


def test_selection_sort():
    """Tests selection sort"""
    import random
    array = [random.randint(0, 10000) for _ in range(5)]
    sorted_array = sorted(array)
    bubble_sorted_array = selection_sort(array)
    assert bubble_sorted_array == sorted_array, "Selection sorting failed"
