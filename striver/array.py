a= [[
    [1,2,"G",88],
    [4,5,6,99]
],[
    [7,8,9,110],
    [10,11,12,200]
]]
          

kj=a[1][1].index(11)
print(kj)


b=[[[1,2,3,4],
  [5,6,7,8]
],[
[9,10,11,12],
[13,14,15,16]
]]
print(b)

#for geting use to input to access the element 

ac=int(input("enter dimention index : "))
bc=int(input("row index : "))
c= int(input("element index : "))
print("your element",b[ac][bc][c])


#for printing colum wise 

k=input(" can i run the  for loop for colum vise printing")
for z in range(len(a[0][0])):
    print("")
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j][z],end=" ")
            #print("block:",i,", row:",j,", element index:",z," == ",a[i][j][z])
            #print("a","[",i,"]","[",j,"]","[","2","]")

# for accessing all elements by row wise 
print("\n")
for i in a:
    for j in i:
        print(j)