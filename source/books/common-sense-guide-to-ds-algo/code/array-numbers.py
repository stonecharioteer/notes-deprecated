"""For an array containing both numbers and other arrays, write a recursive funciton that prints out all the numbers, and just the numbers"""


def print_nums(arr):
    for item in arr:
        if isinstance(item, int):
            print(int)
        else:
            print_nums(item)
