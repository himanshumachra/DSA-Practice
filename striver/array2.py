b= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
k=len(b)-1
a=set()

for i in range(len(b)):
    
    a.add(b[i][k])
    #a.add(b[i][i])
    k = k -1

print(a)


"""
k=(len(a))-1
d= a.copy()
ad= a.copy()
print(k)


for i in range(len(a)):
    print("daigonal",a[i][i])
    d[i].pop(i)
    ad[i].pop(k)
    k=k-1
    
print(d)
print(ad)
"""