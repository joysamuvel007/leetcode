class Solution(object):
    def maxSubArray(self, nums):
        max = nums[0]
        curr = 0
        for i in nums:
            if curr < 0:
                curr = 0
            curr+=i
            if curr > max:
                max = curr
        return max