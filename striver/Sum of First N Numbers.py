class Solution:
    def NnumbersSum(self,n):
        if n==0:
            return 1
        
        return n * self.NnumbersSum(n-1)
a=Solution()
print(a.NnumbersSum(5))

