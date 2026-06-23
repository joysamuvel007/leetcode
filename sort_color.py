class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            m = i
            for j in range(i + 1,len(nums)):
                if nums[m] > nums[j]:
                    m = j
            nums[i],nums[m] = nums[m],nums[i]