"""Algorithm to detect whether 2 words are an Anagram or not"""


def is_anagram(word_1: str, word_2: str) -> bool:
    """Checks whether 2 words is an anagram or not"""
    word_1_dict = {}
    for letter in word_1:
        word_1_dict[letter] = word_1_dict.get(letter, 0) + 1

    word_2_dict = {}
    for letter in word_2:
        word_2_dict[letter] = word_2_dict.get(letter, 0) + 1

    return word_1_dict == word_2_dict


def test_anagram():
    """Checks the anagram function"""
    assert is_anagram("mood", "doom")
    assert is_anagram("rot", "tor")
    assert is_anagram("something", "nothing") is False
