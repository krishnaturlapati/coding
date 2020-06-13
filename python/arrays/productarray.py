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
        # begin prd
        bp = 1
        # end prd
        ep = 1
        # final ans list
        ans = []

        for i in range(len(nums)):

            # begin loop, j is begin ptr
            for j in range(i):
                bp *= nums[j]

            # end loop, k is end ptr
            for k in range(i+1, len(nums)):
                ep *= nums[k]

            ans.append(bp * ep)
            ep = 1
            bp = 1
        return ans


t = Solution()
t.with_out_division(nums=[1,2,3,4,5])