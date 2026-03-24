class Solution:
    def isPrime(self, n):
        s=n
        div=[]
        for i in range(1,int(s**0.5)):
            if s % i == 0:
                div.append(i)
        if len(div) == 2:
            return True
        else:
            return False

a=Solution()
print(a.isPrime(7))