"""
Longest Common Prefix
--------
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for char_index in range(len(strs[0])):
            for s in strs:
                if char_index == len(s) or s[char_index] != strs[0][char_index]:
                    return res
            res += strs[0][char_index]
        return res
