"""
Encode and Decode Strings
---------
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        output = ""
        for char in strs:
            output += str(len(char)) + "#" + char
        return output



    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        output, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#"
                j+= 1
            length = int(str[i:j])
            output.append(str[j+1:j+1+length])
            i = j + 1 + length
        return output
