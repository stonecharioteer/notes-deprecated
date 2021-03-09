"""Recursive function to double every item in an array"""


def double_array(array, index=0):
    """Doubles every item in an array"""
    array[index] *= 2
    index += 1
    if index < len(array):
        double_array(array, index)


def test_double_array():
    import random
    input_array = [random.random() for _ in range(random.randint(0, 1000))]
    doubled_array = [x*2 for x in input_array]
    double_array(input_array)
    assert input_array == doubled_array, "Unable to double array"
