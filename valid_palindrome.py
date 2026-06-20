class Solution(object):
    def isPalindrome(self, s):
         m = []
         
         for i in s:
            if 'A' <= i <= 'Z':
                m.append(chr(ord(i)+32))
            elif 'a' <= i <='z' or "0"<= i <="9":
                m.append(i)

         m = "".join(m)
         if m == m[::-1]:
            return True
         else:
            return False