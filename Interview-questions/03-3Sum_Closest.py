"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        import numpy as np

        nums = sorted(nums)

        closest_sum, closest_dist = np.inf, np.inf

        for index in range(len(nums) - 2):

            left_ = index + 1
            right_ = len(nums) - 1

            while left_ < right_:

                new_sum = nums[index] + nums[right_] + nums[left_]

                if abs(target - new_sum) < abs(closest_dist):

                    closest_sum = new_sum
                    closest_dist = target - new_sum

                if new_sum == target:

                    return target

                elif new_sum > target:

                    right_ -= 1
                else:

                    left_ += 1
        return closest_sum
