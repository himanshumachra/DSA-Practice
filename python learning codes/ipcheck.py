def ip(a):
    valid=set()
    invalid=set()
    for i in a:
        b= i.split(".")
        
        if len(b) !=4:
            invalid.add(i)
        else:
            t= True
            for j in b:
                
                if not j.isdigit():
                    t = False
                    invalid.add(i)
                    break 
                else:
                    t = True
                if t == True:
                    j=int(j)
                    if j>255 or j<0 :
                        invalid.add(i)
                        break
                    else:
                        valid.add(i)
                else:
                    pass
    print("valid ips",valid)
    print("invalid ips",invalid)

a=["192.168.i29.3","136.23.26.23.3","123f.12.23.52","1200.23.23.55"]
ip(a)
                
