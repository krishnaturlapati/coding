"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Reference:
LeetCode #283 https://leetcode.com/problems/move-zeroes/
"""

from typing import List


class Solution(object):
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # initialize pointer
        ptr = 0

        # swap out all non zeros
        for num in nums:
            if num != 0:
                nums[ptr] = num
                ptr += 1

        # loop through nums starting with ptr index, everything north of ptr index will be zeros
        for x in range(ptr, len(nums)):
            nums[x] = 0
        return nums
