"""Recursive solution to array sum"""


def array_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + array_sum(arr[1:])


def test_array_sum():
    import random
    input_array = [random.randint(0, 1000)
                   for _ in range(random.randint(1, 1000))]
    assert array_sum(input_array) == sum(input_array)
