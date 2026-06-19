class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    start = j+1
                    end = len(nums)-1
                    while(start < end):
                        if nums[i] + nums[j] + nums[start] + nums[end] == target and [nums[i],nums[j],nums[start],nums[end]] not in ans:
                            ans.append([nums[i],nums[j],nums[start],nums[end]])
                            start += 1
                            end -= 1
                        elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                            start += 1
                        else:
                            end -= 1
        return ans