class Solution:
    def countDigit(self, n):
       n=str(n)
       k=n[::-1]
       return k 
a=Solution()
n=156
print(a.countDigit(n))
