class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 10**9
        ans = 0
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while (start < end):
                cur = nums[i] + nums[start] + nums[end]
                abs = target - cur
                if abs < 0:
                    abs *= -1
                if closest > abs:
                    closest = abs
                    ans = cur
                if cur == target:
                    return cur
                elif cur < target:
                    start += 1
                else:
                    end -= 1
        return ans
                    