x = [-6, -1, 0, 1, 1, 1, 1, 1, 2, 3, 5, 8]
z=[0, 1, 1, 1, 1, 2, 3, 4, 5, 5, 6, 8, 9, 9, 516, 651, 987]
a=0
b=0
ress=[]
while x[a] < x[len(x)-1]:
    if x[a]<z[b]:
        ress.append(x[a])
        a=a+1
    elif x[a]>z[b]:
        ress.append(z[b])
        b=b+1
    elif x[a] == z[b]:
        ress.append(x[a])
        a=a+1
        b=b+1
if b < len(z):
    ress.append(z[b:])
