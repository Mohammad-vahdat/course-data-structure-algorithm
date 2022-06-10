"""
Reverse Integer
--------
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

"""


class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        res = str(x)[::-1]

        while "0" == res[0]:
            res = res[1:]

        if res[-1] == "-":
            res = "-" + res[:-1]

        if int(res) > 2**31 - 1 or int(res) < -(2**31):
            return 0

        return int(res)
