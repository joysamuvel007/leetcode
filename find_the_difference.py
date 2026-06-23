class Solution(object):
    def findTheDifference(self, s, t):
        visited = [0] * 26
        for i in s:
            if visited[ord(i) - ord('a')]:
                visited[ord(i) - ord('a')] += 1
            else:
                visited[ord(i) - ord('a')] = 1
        for i in t:
            if visited[ord(i) - ord('a')]:
                visited[ord(i) - ord('a')] -= 1
            else:
                return i