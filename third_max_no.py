class Solution(object):
    def thirdMax(self, nums):
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        for i in range(len(nums)):
            if nums[i] == first_max or nums[i] == second_max or nums[i] == third_max:
                continue
            if nums[i] > first_max:
                first_max,second_max,third_max = nums[i],first_max,second_max
            elif nums[i] > second_max:
                second_max,third_max = nums[i],second_max
            elif third_max < nums[i]:
                third_max = nums[i]
        return third_max if third_max != float('-inf') else first_max