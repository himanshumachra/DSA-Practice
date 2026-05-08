A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(A[0:5])
print("  ")
print("  ")


#print in range
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(9 in A[0:8])
print("  ")
print("------------------------------------------ ")


#check not in the list
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(65 not in A[0:7])
print("  ")
print("------------------------------------------ ")


#print the lisyt without declaring the both start and end range
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(type(A[:]))
print("  ")
print("------------------------------------------ ")


#print the list by execiding the end rqange
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print("this is the list actual length = ",end= '' )
print(len(A[0:115]))
print("  ")
print("------------------------------------------ ")

#print negative index
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(A[-3])
print("  ")
print("------------------------------------------ ")


#print the length of the list
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(len(A[0:5]))
print("  ")
print("------------------------------------------ ")


#check the type od varible a is?
A=[ 1,2,3,3,3,3,65,9,] 
print(type(A))
print("  ")
print("------------------------------------------ ")


#print from range 0 to 5
A= list([ 1,2,3,3,3,3,65,9,'HII'])
print(A[0:5])
print("  ")
print("------------------------------------------ ")


#print only the selsted inedx list
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print(A[5],A[8],A[7],A[6])
print("  ")
print("  ")


#print the negative index
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print((A[::-1]))
print("  ")
print("------------------------------------------ ")

#print the negative index 
A=[ 1,2,3,3,3,3,65,9,'HII']
b=(len(A)) 
print((A[-4:-1]))
print("this is the len of A =", b)
print("  ")
print("------------------------------------------ ")

#change the element 
A=[ 1,2,3,3,3,3,65,9,'HII'] 
A[4]= "hi"
print(A)
print("  ")
print("------------------------------------------ ")

#change the element in the range 
A=[ 1,2,3,3,3,3,65,9,'HII'] 
A[3:5]= "hi",'by',78888888
print(A)
print("  ")
print("------------------------------------------ ")

#change the element in the range same element for all range
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print ("this bitchy list len is =",len(A),"  ")
A[3:100]= ["hii"]
print("   ",A)
print ("after the replacement the list length === ",len(A))
print("  ")
print("------------------------------------------ ")


#to insert a new element in the list  means adding a new element 
A=[1,2,3,3,3,3,65,9,'HII'] 
print("length of a list before the insertion = ",len(A))
A.insert(2,'bay')#at index 2 add a new element as an bay and it increse the list lenght also
print(A)
print ('length of list after the insertion = ',len(A))
print("  ")
print("------------------------------------------ ")


#to add elemnts at just last 
A=[ 1,2,3,3,3,3,65,9,'HII'] 
print("  ")
print("------------------------------------------ ")