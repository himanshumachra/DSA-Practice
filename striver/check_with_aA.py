a = ["Aman","raj","sudhir","ashish","anuj","akash","raman"]
with_A= []

without_A = []
for i in a:
    i=i.lower()

    if i[0] == "a" :
        with_A.append(i)
    else:
        without_A.append(i)

print("names with A",with_A)
print("names without A", without_A)