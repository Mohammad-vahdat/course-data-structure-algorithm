"""
Valid Anagram
------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = {}

        for char in s:

            if char in mem:
                mem[char] += 1
            else:
                mem[char] = 1

        for char in t:

            if char not in mem:

                return False

            else:

                mem[char] -= 1

        return min(mem.values()) == max(mem.values()) == 0
