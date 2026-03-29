def freq(a):
    b=a
    frq=dict()
    for i in a:
        if i in frq:
            frq[i]+=1
        else:
            frq[i]=1
    print(frq)
a=[1,12,3165,44,3,44,21,32,65,5,32,321,3221,321,31,32,32,1,21,54,4,4,5,63,2,585,5,54]
freq(a)