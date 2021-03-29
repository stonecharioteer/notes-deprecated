"""Solution for the Leetcode problem #0020 Valid Parenthesis
https://leetcode.com/problems/valid-parenthesis/
"""


def is_valid(s: str) -> bool:
    from collections import deque
    string_stack = deque()
    for character in s:
        if character in ["[", "{", "("]:
            string_stack.append(character)
        elif character in ["]", "}", ")"]:
            if len(string_stack) == 0:
                return False
            last = string_stack.pop()
            if character == "[":
                if last != "]":
                    return False
            elif character == "{":
                if last != "}":
                    return False
            elif character == ")":
                if last != "(":
                    return False

    return True
