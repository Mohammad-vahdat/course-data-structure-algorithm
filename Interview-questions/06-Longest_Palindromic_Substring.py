"""
Longest Palindromic Substring
---------------------
Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        longest = 0

        for middle in range(len(s)):

            ### odd length
            left_, right_ = middle, middle
            while left_ >= 0 and right_ < len(s) and s[left_] == s[right_]:
                if right_ - left_ + 1 > longest:
                    res = s[left_ : right_ + 1]
                    longest = right_ - left_ + 1

                left_ -= 1
                right_ += 1

            ### even length
            left_, right_ = middle, middle + 1
            while left_ >= 0 and right_ < len(s) and s[left_] == s[right_]:
                if right_ - left_ + 1 > longest:
                    res = s[left_ : right_ + 1]
                    longest = right_ - left_ + 1

                left_ -= 1
                right_ += 1

        return res
