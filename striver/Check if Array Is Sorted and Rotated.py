class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        for i in range(len(nums)-1) :
            if not nums[i] < nums[i+1] :
                k=k+1
        if k == 2:
            return True 
        else:
            return False 
        

a=Solution()
nums = [3,4,5,1,2]
print(a.check(nums))