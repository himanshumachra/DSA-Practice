x=[1,5,6,4,8,96,32,5,6,45,8,96,55,554,87,894,213,354,98732.5,754,254,8515,54,5687,877,23,10,9,7487]
x.sort()
a=0
b=len(x)-1
target=60

while a<b:
    if x[a]+x[b] == target:
        print("we fount the two numbers there addition matches the target =",x[a],"+",x[b])
        break
    elif x[a]+x[b] < target:
        a=a+1
        
    elif x[a]+x[b] > target:
        b=b-1
        