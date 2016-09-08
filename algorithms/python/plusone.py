"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Subscribe to see which companies asked this question
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [9]:
            return [1, 0]
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1]+1]
        else:
            return self.plusOne(digits[:-1]) + [0]

if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([1]))
