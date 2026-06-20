class Solution(object):
    def isPalindrome(self, x):
        giv = x
        if giv<0:
            return False
        m=0
        while(x!=0):
             m=(m*10)+(x%10)
             x=x//10
        if m==giv:
            return True
        else:
            return False
             