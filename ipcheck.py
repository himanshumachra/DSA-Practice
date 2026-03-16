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
                    pass
                if t == True:
                    j=int(j)
                    if j>255 or j<0 :
                        t=False
                        invalid.add(i)
                        break
            if t == True:
                valid.add(i)
                    
    print("valid ips",valid)
    print("invalid ips",invalid)

a=["192.168.29.3","136.23.26.23.3","123f.12.23.52","1200.23.23.55"]
ip(a)



'''
MORE SHORT AND EASY TO WRRITEN AND IN A PROPER ORDER 

def ip(a):
    valid = set()
    invalid = set()

    for i in a:
        b = i.split(".")

        if len(b) == 4 and all(j.isdigit() and 0 <= int(j) <= 255 for j in b):
            valid.add(i)
        else:
            invalid.add(i)

    print("valid ips:", valid)
    print("invalid ips:", invalid)


a = ["192.168.129.3", "136.23.26.23.3", "123f.12.23.52", "1200.23.23.55"]

ip(a)

'''


'''
###
#asked in tcs and amazon

def restore_ip(s):
    res = []

    for i in range(1,4):
        for j in range(i+1,i+4):
            for k in range(j+1,j+4):

                a = s[:i]
                b = s[i:j]
                c = s[j:k]
                d = s[k:]

                parts = [a,b,c,d]

                if all(p.isdigit() and 0 <= int(p) <= 255 and str(int(p)) == p for p in parts):
                    res.append(".".join(parts))

    return res


print(restore_ip("25525511135"))
###
'''