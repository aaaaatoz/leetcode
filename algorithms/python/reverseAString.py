#!/usr/bin/python

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseStringOne(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join((x for x in reversed(s)))

if __name__ == "__main__":
    a = Solution()
    print(a.reverseStringOne("sadjfoiejflkdfjs"))
