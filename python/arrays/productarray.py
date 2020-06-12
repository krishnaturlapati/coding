"""

Given an array of int, return new array such that each element at index i of the new array is the
product of all other numbers of the original array
Example:

Input: [1,2,3,4,5]
Output: [120, 60, 40, 30, 24]

Input: [3, 2, 1]
Output: [2, 3, 6]


Reference:
DCP 1
"""

from typing import List
from functools import reduce


class Solution(object):

    def with_division(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: return List[int].
        """
        # multiply all items in array using reduce func
        product_of_list = reduce(lambda a, b: a*b, nums)
        # loop through nums and divide each element with product
        return [int(product_of_list/i) for i in nums]

    def with_out_division(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: return List[int].
        """
        pass
