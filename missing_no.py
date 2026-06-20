class Solution(object):
    def missingNumber(self, nums):
        sum = 0
        for i in nums:
            sum += i
        m = len(nums)*(len(nums)+1)//2
        return m-sum
