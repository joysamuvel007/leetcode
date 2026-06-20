class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s1 = {}
        t1 = {}
        for i,j in zip(s,t):
            if i in s1:
                s1[i] += 1
            else:
                s1[i] = 1
            if j in t1:
                t1[j] += 1
            else:
                t1[j] = 1
        return s1==t1