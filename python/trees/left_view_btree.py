from typing import List


class Node(object):
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LeftViewOfTree(object):
    max_level = 0

    def left_view(self, root: Node, level: int, result: List) -> None:
        if root is None:
            return None

        if self.max_level < level:
            result.append(root.data)
            self.max_level = level

        self.left_view(root.left, level + 1, result)
        self.left_view(root.right, level + 1, result)

