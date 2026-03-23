# spiral in array
a= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
sro=0
ero=len(a)
scol=0
ecol=len(a[0])

while sro<ero and scol<ecol:

    for i in range(scol,ecol):
        print(a[scol][i],end=" ")
    sro+=1

    for j in range(sro,ero):
        print(a[j][ecol-1],end=" ")
    ecol-=1

    if scol<ecol:
        for k in range(ecol-1,scol-1,-1):
            print(a[ero-1][k],end=" ")
        ero-=1
    if sro<ero:
        for l in range(ero-1,sro-1,-1):
            print(a[l][scol],end=" ")
        scol+=1
