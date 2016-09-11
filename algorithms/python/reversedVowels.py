"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

Subscribe to see which companies asked this question
"""

class Solution(object):
    vowels = ('a','e','i','o','u')

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index  = 0
        resultChar = []
        vowels = self.getReversedVowelsFromString(s)

        for char in s:
            if char in self.vowels:
                resultChar.append(vowels[index])
                index += 1
            else:
                resultChar.append(char)
        return "".join(resultChar)

    def getReversedVowelsFromString(self, s):

        vowellist = []
        for char in s:
            if char in self.vowels:
                vowellist.append(char)
        return  vowellist[::-1]

if __name__ == "__main__":
    a = Solution()
    print(a.reverseVowels("hello"))
    print(a.reverseVowels("leetcode"))
