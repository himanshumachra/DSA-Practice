class Soultion:
    def factorial(self,n):
        if n == 0:
            return 1
        return n *self.factorial(n-1)
a=Soultion()
print(a.factorial(6))