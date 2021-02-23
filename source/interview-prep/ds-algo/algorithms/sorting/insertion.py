
def insertion_sort(inp_list):
    """Insertion Sort
    O(n**2) sorting algorithm.
    This algorithm will assume that the left portion is sorted.
    At the beginning, the first item in the list is assumed to be sorted.
    Then, the first item of the unsorted portion is *inserted* into this
    sorted sublist at the right position.
    When this is done, the items in the sublist that are greater
    than this item are shifted to the right.
    """
    for index in range(1, len(inp_list)):
        key = inp_list[index]
        position = index

        while position > 0 and inp_list[position-1] > key:
            # shift greater items to the left
            inp_list[position] = inp_list[position-1]
            position -= 1

        inp_list[position] = key
    return inp_list


def binary_insertion_sort(inp_list):
    """Binary Insertion Sort.
    This is a modification of selection sort, wherein
    instead of comparing *all* items in the sorted list to the
    key value, we find the best place to put it.
    However, since the insertion will mandate the shifting of the numbers anyway,
    this will still take O(n**2).
    """
