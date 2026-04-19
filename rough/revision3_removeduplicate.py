x = [-6,-3,-1,0,1,1,1,1,1,2,5,8]
z=[9,0,6,5,2,3,4,1,1,1,1,8,9,516,987,651,5]
result=[]
a=0
b=0
while x[a] < x[len(x)-1]:
    print(a)
    if not x[a] in result:
        result.append(x[a])
    a=a+1
    if  z[b] < z[len(z)-1]:
    if not z[b] in result:
        result.append(z[b])
    b=b+1
print(result)