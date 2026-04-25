nums = [0,1,0,3,12]
a=0
for i in range(len(nums)):
    if not nums[i] == 0:
        nums[i],nums[a]=nums[a],nums[i]
        a=a+1
print(nums)