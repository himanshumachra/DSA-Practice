a = ["aman","raj","sudhir","ashish","anuj","akash","raman"]
with_A= []
check = ("a","A")

without_A = []
for i in a:
    if i in check:
        with_A.append(i)
    else:
        without_A.append(i)

print("names with A",with_A)
print("names without A", without_A)