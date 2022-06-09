"""

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = set()
        nums = sorted(nums)

        for index in range(len(nums) - 3):

            for index2 in range(index + 1, len(nums) - 2):

                left = index2 + 1
                right = len(nums) - 1

                while left < right:

                    sum_now = nums[index] + nums[index2] + nums[left] + nums[right]

                    if sum_now == target:

                        res.add((nums[index], nums[index2], nums[left], nums[right]))
                        left += 1
                    elif sum_now > target:

                        right -= 1
                    else:
                        left += 1

        return res
