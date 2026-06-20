class Solution(object):
    def maximumCount(self, nums):
        posc = 0
        negc = 0
        for i in nums:
            if i < 0:
                negc += 1
            if i > 0:
                posc += 1
        return posc if posc > negc else negc