"""Solution for the Leetcode problem #0002 Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Adds the numbers in a linked list and returns the sum as another linked
    list."""
    iteration = 0
    while l1 and l2:
        sum_numbers = (l1.val + l2.val) * 10**iteration
        iteration += 1
        l1 = l1.next
        l2 = l2.next

    new_list = None
    cursor = None

    while sum_numbers != 0:
        pos = sum_numbers % 10
        sum_numbers = sum_numbers // 10

        if cursor is None:
            new_list = ListNode(val=pos)
            cursor = new_list
        else:
            cursor.next = ListNode(val=pos)
            cursor = cursor.next
    return new_list
