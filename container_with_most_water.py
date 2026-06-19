class Solution(object):
    def maxArea(self, height):
        m = 0
        i = 0
        j = len(height)-1
        while(i < j):
            w = j - i
            h = min(height[i],height[j])
            m = max(m,h * w)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m
        
        