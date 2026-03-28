a="ahghgasdasdsah"

def fun(a):
    k=set()
    for j in a:
        if not j in k:
            k.add(j)
    print(len(k))
    
    
fun(a)