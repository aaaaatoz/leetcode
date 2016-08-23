#!/usr/bin/python

#time ex

class Solution(object):
    #simple and straight forward but timedout
    def firstUniqCharOne(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1 : return i
        return -1

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unUniqueChars = []
        uniqueChars = []
        # 遍历这个字符串
        # 取出一个数, 看是否已经重复过,如果是,那么下一个
        # 如果还没有, 那么我们把他放到唯一列表里,如果已经有了,那把唯一列表的元素删除, 放入不唯一列表,判断不唯一列表为26,返回-1
        # 遍历完成, 返回唯一列表的第一个元素.
        for char in s:
            if char in unUniqueChars:
                continue
            elif char in uniqueChars:
                uniqueChars.remove(char)
                unUniqueChars.append(char)
                if len(unUniqueChars) == 26:
                    return -1
            else:
                uniqueChars.append(char)
        if len(uniqueChars) == 0:
            return -1
        else
            return s.index(uniqueChars[0])


if __name__ == "__main__":
    a = Solution()
    print(a.firstUniqChar("leetcode"))
    print(a.firstUniqChar("loveleetcode"))