x=[1,6,7]
z=[5,6,7]

result=list()
a=0
b=0
while a<len(x) and b<len(z):
    if x[a]<z[b]:
        result.append(x[a])
        a=a+1
       
    elif z[b]<x[a]:
        result.append(z[b])
        b=b+1
    elif x[a] == z[b]:
        print("we have fint the position of both arrays intersection at index :",a,"in x array and index:",b,"in z array")
        break
        result.append(x[a])
        a=a+1
        b=b+1 #if you want to add only non repetive then comment the b variable 
"""if a<len(x):
    result=result+x[a:]
else:
    result=result+z[b:]"""
print(result)