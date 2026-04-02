def nor(a):
    n=[]
    for j in a:
        x=0
        for i in a:
            if i == j:
                x=x+1   
            if x%2 == 0:
                n.append(j)
    if len(n)==0:
        print("all numberss are in pair")
    else:
        print("the non pair number is = ",n)

nor([4,4])