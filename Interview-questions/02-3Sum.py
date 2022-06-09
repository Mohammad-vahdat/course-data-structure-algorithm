"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        z, p, n = [], [], []

        for num in nums:
            if num == 0:
                z.append(num)
            if num > 0:
                p.append(num)
            if num < 0:
                n.append(num)

        N, P = set(n), set(p)

        if len(z) >= 3:
            res.add((0, 0, 0))

        if len(z) > 0:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
