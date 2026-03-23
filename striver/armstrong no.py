class Solution:
    def armno(self,  n):
        s=str(n)
        p=len(s)
        k=0
        for i in range(len(s)):
            k=k+int(s[i]) ** p
        if k == n:
            print("armstrong no")
        else:
            print("not armstrong no")
         

a=Solution()
a.armno(153)
