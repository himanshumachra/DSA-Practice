class Solution:
    def printNumbers(self, n):
        if n == 0:
            return
        print(n)
        self.printNumbers(n-1)
a=Solution()
a.printNumbers(10)