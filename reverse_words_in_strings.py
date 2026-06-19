class Solution(object):
    def reverseWords(self, s):
        m = ""
        s = s.split()
        for i in range(len(s)-1,0,-1):
            if s[i] != " ":
                m += s[i] + " "
        m += s[0]
        return m