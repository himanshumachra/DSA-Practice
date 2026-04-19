x = [-6,-3,-1,0,1, 2, 5]
t=2
a=0
while a < len(x)-2:
    b=a+1
    c=len(x)-1
    while b<c:
        sum = x[a]+x[b]+x[c]
        if t==sum:
            print("these are the 3 numbers ",x[a],",",x[b],",",x[c],"to get the target value :",t)
            break
        elif sum<t:
            b=b+1
        else:
            c=c-1
    a=a+1