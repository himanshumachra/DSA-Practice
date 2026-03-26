a = ["aman","raj","sudhir","ashish","anuj","akash","raman"]
with_A= []
without_A = []
for i in a:
    if "a"in i[0] or "A" in i[0]:
        with_A.append(i)
    else:
        without_A.append(i)

print("names with A",with_A)
print("names without A", without_A)