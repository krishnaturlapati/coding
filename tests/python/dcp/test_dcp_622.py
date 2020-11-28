from python.dcp.dcp_622 import *


def test_get_deepest_node_given_only_root_node():
    root = Node(12)
    assert get_deepest_node(root) == 12


def test_get_deepest_node_given_a_simple_balaced_tree():
    root = Node(12)
    root.insert(6)
    root.insert(14)
    assert get_deepest_node(root) == 6


def test_get_deepest_node_case_given_a_left_skewed_tree():
    root = Node(12)
    root.insert(6)
    root.insert(4)
    root.insert(3)
    root.insert(2)
    root.insert(-1)
    root.insert(-15)
    assert get_deepest_node(root) == -15


def test_get_deepest_node_case_given_a_right_skewed_tree():
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)
    root.insert(7)
    root.insert(8)
    root.insert(9)
    assert get_deepest_node(root) == 9
