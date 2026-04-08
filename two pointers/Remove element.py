arr = [3, 2, 2, 3]
val = 3
a = 0
for b in range(len(arr)): 
    if arr[b] != val:
        arr[a] = arr[b]
        a += 14
        
print(arr[:a])  