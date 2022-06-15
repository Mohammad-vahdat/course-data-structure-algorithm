"""
Climbing Stairs
-----------
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    #     def __init__(self):
    #         self.mem = {}

    #     def climbStairs(self, n: int) -> int:

    #         if n in [0,1]: return 1
    #         if n in self.mem:
    #             return self.mem[n]

    #         else:
    #             self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

    #         return self.mem[n]
    mem = {}

    def climbStairs(self, n: int) -> int:
        if n in [0, 1]:
            return 1
        if n in Solution.mem:
            return Solution.mem[n]

        else:
            Solution.mem[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return Solution.mem[n]
