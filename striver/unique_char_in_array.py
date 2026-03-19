a=["ahghgasdasdsah","sdfsdfsdfsfs","himanshu","#kfkd"]

#Write a Python program to:

#Find all characters that appear exactly once across the entire array (i.e., globally non-repeating).

#Return a list of these characters.

#Also, print the total count of these characters.


def fun(a):
    unq=dict()
    for i in a:
        for j in i:
            if not j in unq:
                unq[j]=1
            elif j in unq:
                unq[j]+=1

    print("the list of unique char are :",unq.keys())        
    print("the list of unique char with there frequency",unq)
    print("the total count of the characters",len(unq))
    
fun(a)