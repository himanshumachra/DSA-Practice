l1=[15,4,8,5,51,651,84,64,321,2]
l2=[4,5,6,351,849,87,5,84]
l1.sort()
l2.sort()
newl=[]
a=0
b=0
while a < len(l1) and b<len(l2):
    if l1[a]<=l2[b]:  
        newl.append(l1[a])
        a=a+1
    elif l1[a]>=l2[b]:
        newl.append(l2[b])
        b=b+1
while a < len(l1):
    newl.append(l1[a])
    a=a+1
while b< len(l2):
    newl.append(l2[b])
    b=b+1

print(newl)
# to check all elements are got properly mearged 
if len(l1)+len(l2) == len(newl):
    print(True)
else:
    print(False)