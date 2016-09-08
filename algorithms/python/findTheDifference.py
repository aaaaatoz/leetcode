class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sDict = {letter: s.count(letter) for letter in set(s)}
        tDict = {letter: t.count(letter) for letter in set(t)}
        for letter in tDict:
            if letter not in sDict or sDict[letter] != tDict[letter]: return letter


if __name__ == "__main__":
    a = Solution()
    print(a.findTheDifference("wsxcderfv","wsxedcrfvs"))