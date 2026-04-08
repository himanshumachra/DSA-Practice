l1=[15,4,8,5,51,651,84,64,321,2]
l2=[4,5,6,351,849,87,5,84]
l1.sort()
l2.sort()
a=0
b=0
while a<len(l1) and b< len(l2):
    print(l1[:])
    if l1[a]<l2[b]:
        l1.(a+1,l2[b])
        b=b+1
        
    elif l1[a]>l2[b]:
        l1(a,l2[b])
        a=a+1
if len(l1)<len(l2):
    while b<len(l2):
        l1.append(l2[b])
        b=b+1
print(l1[:])
