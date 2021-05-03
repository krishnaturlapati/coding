from problems.left_view_btree import LeftViewOfTree, Node

def test_one():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = []
    lvot = LeftViewOfTree()
    lvot.left_view(root, 1, result)

    for item in result:
        print(item)
    assert result == [1, 2, 4]


def test_two():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    result = []
    lvot = LeftViewOfTree()
    lvot.left_view(root, 1, result)

    for item in result:
        print(item)
    assert result == [1, 2, 4, 5, 6]


def test_three():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
    result = []
    lvot = LeftViewOfTree()
    lvot.left_view(root, 1, result)

    for item in result:
        print(item)
    assert result == [10, 2, 7, 14 ]
    """
                10
        2               3
     7      8       12      15
                        14
    """