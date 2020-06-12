from python.arrays.productarray import Solution
import pytest


@pytest.fixture(scope="class")
def product_array_object():
    t = Solution()
    return t


def test_product_array_case1(product_array_object):
    input_list = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    actual = product_array_object.with_division(nums=input_list)
    assert actual == expected


def test_product_array_case2(product_array_object):
    input_list = [3, 2, 1]
    expected = [2, 3, 6]
    actual = product_array_object.with_division(nums=input_list)
    assert actual == expected