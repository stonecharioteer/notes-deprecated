"""Use recursion to write a function that accepts an array of numbers and returns a new
array containing just the even numbers"""


def get_even_numbers(input_array):
    """Return a list of even numbers in the given input array"""
    result = []
    if len(input_array) == 1:
        if input_array[0] % 2 == 0:
            return [input_array[0]]
        else:
            return []
    else:
        if input_array[0] % 2 == 0:
            result.append(input_array[0])
        result.extend(get_even_numbers(input_array[1:]))
    return result


def test_get_even_numbers():
    """Test get_even_numbers"""
    import random
    random_list = [random.randint(0, 1000)
                   for _ in range(random.randint(100, 1000))]
    evens = [x for x in random_list if (x % 2 == 0)]
    print(len(random_list))
    assert get_even_numbers(random_list) == evens, "Unable to get even numbers"
