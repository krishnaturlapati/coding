from python.arrays.movezeros import Solution
import pytest


@pytest.fixture(scope="class")
def move_zero_object():
    t = Solution()
    return t


def test_move_zeroes_case1(move_zero_object):
    input_list = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    actual = move_zero_object.moveZeroes(nums=input_list)
    assert actual == expected


def test_move_zeroes_case2(move_zero_object):
    input_list = [0, 1, 0]
    expected = [1, 0, 0]
    actual = move_zero_object.moveZeroes(nums=input_list)
    assert actual == expected


def test_move_zeroes_case3(move_zero_object):
    input_list = [0, 0, 1]
    expected = [1, 0, 0]
    actual = move_zero_object.moveZeroes(nums=input_list)
    assert actual == expected


def test_move_zeroes_case4(move_zero_object):
    input_list = [0]
    expected = [0]
    actual = move_zero_object.moveZeroes(nums=input_list)
    assert actual == expected