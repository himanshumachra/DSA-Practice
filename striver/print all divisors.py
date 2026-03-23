class Solution:
    def divisors(self, n):
        div=[]
        for i in range(1,n+1):
            if n % i == 0:
                div.append(i)
        div.sort()
        return div 
a=Solution()
print(a.divisors(6))