nums = [2,0,2,1,1,0]
a=0
while a < len(nums):
    b=a+1
    if nums[a] == nums[b] and not a+1 == b:
        nums[a+1]=nums[b]
        a=a+1
    b=b+1
        
print(nums)