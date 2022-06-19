"""
Top K Frequent Elements
-------
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mem = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:

            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1

        for n, c in mem.items():
            freq[c].append(n)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)

                if len(output) == k:
                    return output


# BucketSort
# time:O(n)
