class Solution(object):
    def reverseOnlyLetters(self, s):
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z'):
                i += 1
            elif not ('a' <= s[j] <= 'z' or 'A' <= s[j] <= 'Z'):
                j -= 1
            else:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
        return ''.join(s)