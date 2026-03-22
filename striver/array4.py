"""#print the sum of allelements
a=["e",1,2,3,4,5,6,7,8,9,10]
c=0
print(type(a[0]))
for i in range(len(a)):
    if type(a[i]) == int:
        b=a[i]
        c=c+b
print(c)
"""
#linear search
a= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
c=-1
for i in range(len(a)):
    b=len(a)-1
    c=c+1
    for j in range(len(a[i])):
        print(a[b][c],end=" ")
        b=b-1
    print()
