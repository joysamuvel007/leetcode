class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(2,len(nums)):
            if nums[i]!=nums[j]:
                i+=2
                nums[i] = nums[j]
        return i+1