x="1221"
a = 0
b=len(x)-1
palindrom = True
while a< b :
    if x[a]==x[b]:
        palindrom=True
    else:
        palindrom=False
    a=a+1
    b=b-1
print(palindrom)