class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=len(nums)-2
        for i in range(len(nums)):
            if nums.index(nums[i]) == nums.index(nums[k]):
                break
            else:
                if nums[i] == 0:
                    nums.pop(nums.index(nums[i]))
                    nums.append(0)
                    k=k-1
        print(nums)
a=Solution()
nums = [0,1,0]
a.moveZeroes(nums)