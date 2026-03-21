a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

for i in range(len(a)):
    j=len(a)-1
    for k in range(len(a[i])):
        print(a[j][i],end=" ")
        j=j-1
        
    print("\n")


#sum of all indexes
k=0
for z in range(len(a)):
    for q in range(len(a)):
        k=k+(a[z][q])
print("sum of array is :",k)
        


#printthe daigonals of a matrix
pp=len(a[0])-1
for p in range(len(a)):
    print("daigonals of this matrix:",a[p][p])
    print('anti daigonals:',a[p][pp])
    pp=pp-1