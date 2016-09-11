"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 2.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

class Solution(object):
    def powerof2(self, number):
        if number == 2:
            return True
        elif number % 2 != 0:
            return False
        else:
            return self.powerof2(int(number/2))