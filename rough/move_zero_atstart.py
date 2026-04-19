nums = [0,1,0,3,12]
a=0
b=0
while am<len(nums)-1:
    if not nums[a] == 0:
        nums.insert(b,nums[a])
        b=b+1
    a=a+1
    print(a)

print(nums)