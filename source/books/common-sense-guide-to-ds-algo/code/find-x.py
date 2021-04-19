"""Use recursion to write a function that accepts a string and returns the
first index that contains the character `x`."""


def find_x(input_string, current_index=0):
    if input_string[0] == "x":
        return current_index
    else:
        current_index = current_index + 1
        return find_x(input_string[1:], current_index)


def test_find_x():
    import random
    import string
    random_letters = [
        random.choice(string.ascii_letters) for _ in range(random.randint(10, 1000))
    ]
    random_letters += ["x"]
    random.shuffle(random_letters)
    random_string = "".join(random_letters)

    assert find_x(random_string) == random_string.find(
        'x'), "Unable to get the correct index"
