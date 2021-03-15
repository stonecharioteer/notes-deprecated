"""Generate all anagrams of a set of letters"""


def anagrams_of(string: str):
    """Returns a list of anagrams of a string"""
    if len(string) == 1:
        # if the string is a single character, return a list containing that
        # single character.
        return [string[0]]
    # instantiate an empty placeholder
    collection = []
    # Get all the anagrams of the rest of the string, besides the first
    # character, until the end of the string.
    substring_anagrams = anagrams_of(string[1:])

    for substring_anagram in substring_anagrams:
        # now, while looping through this new list of sub-anagrams,
        for index in range(len(substring_anagram)+1):
            # loop through each character in this anagram, insert the first
            # character into a place dictated by the index of the sub-anagrams
            anagram = substring_anagram[:index] + \
                string[0] + substring_anagram[index:]
            # append to our collection
            collection.append(anagram)
    # return the result
    return collection


def test_anagrams_of():
    "tests anagrams_of"
    input_string = "abc"
    result = [
        "abc",
        "bac",
        "cab",
        "cba",
        "acb",
        "bca"
    ]
    anagrams = anagrams_of(input_string)
    for item in result:
        assert item in anagrams, "{} not found in anagrams of {}".format(
            item, input_string)
