"""
Valid Palindrome
-------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not self.alphanum(s[left]):
                left += 1
            while left < right and not self.alphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():

                return False
            else:

                left += 1
                right -= 1
        return True

    def alphanum(self, char):
        return (
            ord("a") <= ord(char) <= ord("z")
            or ord("A") <= ord(char) <= ord("Z")
            or ord("0") <= ord(char) <= ord("9")
        )
