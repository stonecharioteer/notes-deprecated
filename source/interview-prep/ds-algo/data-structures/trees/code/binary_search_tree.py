"""Binary Search Tree Implementation in Python"""


class BSTException(Exception):
    """This exception is raised when a particular facet or requirement
    of a BST is not satisfied."""


class BinarySearchTreeNode:
    """A Single node of a Binary Search Tree"""

    def __init__(self, value, left=None, right=None):
        self.value = value
        if left is not None:
            if left > self.value:
                raise BSTException(
                    "The left value should be lesser than the current value.")
        self.left = left
        if right is not None:
            if right < self.value:
                raise BSTException(
                    "The right value should be greater than the current value.")
        self.right = right

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


def construct_binary_search_tree(*args):
    """Given a list of integers, this can construct a BST and returns the root
    node."""
    if len(args) == 0:
        return
    elif len(args) > 0:
        root_node = BinarySearchTreeNode(args[0])
        if len(args) > 1:
            for value in args:
                insert_into_bst(value, root_node)
        return root_node


def search_bst(search_value, node):
    """Finds a value in a BST given a node

    To find a node in a BST, remember:

    1. Each node has a maximum of 2 children (a left and a right).
    2. The left side of a node has values lesser than the node.
    3. The right side of a node has values greater than the node.
    """
    if node is None or node.value == search_value:
        return node
    elif search_value < node:
        return search_bst(search_value, node.left)
    else:
        return search_bst(search_value, node.right)


def insert_into_bst(value, node):
    """Inserts a value into a Binary Search Tree
    1. If the value to be inserted is less than the current node, it belongs on
    the left.
    2. If the value to be inserted is greater than the current node, it belongs
    on the right.

    Remember, all nodes have only a maximum of 2 children: a left child and a
    right child.
    """
    if value < node:
        if node.left is None:
            node.left = BinarySearchTreeNode(value)
        else:
            insert_into_bst(value, node.left)
    elif value > node:
        if node.right is None:
            node.right = BinarySearchTreeNode(value)
        else:
            insert_into_bst(value, node.right)


def delete_from_bst(value, node):
    """Deletes a value from a BST
    When deleting remember the following:

    1. If the node being deleted has no children, then simply delete it.
    2. If the node being deleted has one child, delete the node and plug the
    child into the spot where the deleted node was.
    3. When deleting a node with two children, replace the deleted node with
    the successor node. The successor node is the child node whose value is
    the least of all values that are greater than the deleted node.
    4. To find the successor node: visit the right child of the deleted value,
    and then keep on visiting the left child of each subsequent child until
    there are no more left children. The bottom value is the successor node.
    5. If the successor node has a right child, after plugging the successor
    node into the spot of the deleted node, take the former right child of the
    successor node and turn it into the left child of the former parent of the
    successor node.
    """
    if node is None:
        return None
    elif value < node:
        node.left = delete_from_bst(value, node.left)
        return node
    elif value > node:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.right = lift_node_in_bst(node.right, node)
            return node


def lift_node_in_bst(node, node_to_delete):
    """If the current node of this function has a left child, recursively call
    this function to continue down the left subtree to find the successor node.
    """
    if node.left is not None:
        node.left = lift_node_in_bst(node.left, node_to_delete)
        return node
    else:
        node_to_delete.value = node.value
        return node.right


def traverse_bst_and_run_function(node, function, mode="in-order"):
    """Traverses a bst and runs a function on each value.
    The modes are 'in-order', 'pre-order', 'post-order'
    TODO: Try to implement *returning* the values accrued
    by these function calls.
    """

    if node is None:
        return
    if mode == "in-order":
        traverse_bst_and_run_function(node.left, function)
        function(node)
        traverse_bst_and_run_function(node.right, function)
    elif mode == "pre-order":
        function(node)
        traverse_bst_and_run_function(node.left, function)
        traverse_bst_and_run_function(node.right, function)
    elif mode == "post-order":
        traverse_bst_and_run_function(node.left, function)
        traverse_bst_and_run_function(node.right, function)
        function(node)
