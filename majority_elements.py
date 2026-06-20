class Solution(object):
    def majorityElement(self, nums):
        cur = nums[0]
        c = 1
        for i in nums[1:]:
            if i == cur:
                c+=1
            else:
                if c == 0:
                    cur = i
                else:
                    c-=1
        return cur