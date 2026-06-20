class Solution(object):
    def intersection(self, nums1, nums2):
        s = []
        for i in nums1:
            if i not in s and i in nums2:
                s.append(i)
        return s