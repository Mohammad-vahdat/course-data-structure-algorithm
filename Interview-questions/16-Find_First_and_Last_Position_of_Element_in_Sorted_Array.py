"""
Find First and Last Position of Element in Sorted Array
----------------------------

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]

    # LeftBias = [True/False], if False, res is rightBiased
    def binSearch(self, nums, target, leftBias):

        left, right = 0, len(nums) - 1

        i = -1

        while left <= right:

            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i
