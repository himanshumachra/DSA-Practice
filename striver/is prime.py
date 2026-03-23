class Solution:
    def isPrime(self, n):
        s=n
        div=[]
        for i in range(1,s+1):
            if s % i == 0:
                div.append(i)
        if len(div) == 2:
            return True
        else:
            return False

a=Solution()
print(a.isPrime(8))