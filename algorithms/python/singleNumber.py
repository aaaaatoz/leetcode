

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1: return nums[0]
        for i in range(0, int((len(nums) - 1)/2)):
            if nums[2*i] != nums[2*i +1]: return nums[2*i]
        return nums[len(nums)-1]



if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([1,3,5,7,9,9,5,3,1]))