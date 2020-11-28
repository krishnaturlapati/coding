"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


class Node:
    """ Binary tree implementation """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            # root already present check if the given data is less than current value
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            # root not found, create one
            self.data = data


def get_deepest_node(root):
    # case1: root node doesnt have children
    if root.left is None and root.right is None:
        return root.data
