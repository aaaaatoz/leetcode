"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

class Solution(object):
    def powerofN(self, number, power):
        assert(power >= 2)
        if number < power:
            return False
        elif number == power:
            return True
        elif number % power != 0:
            return False
        else:
            return self.powerofN(int(number/power), power)


if __name__ == "__main__":
    a = Solution()
    print(a.powerofN(2,2))