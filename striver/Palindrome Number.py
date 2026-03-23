class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        p=str()
        for i in x:
            p=i+p
        if x == p:
            return True
        else:
            return False
a=Solution()
x=1212
print(a.isPalindrome(x))