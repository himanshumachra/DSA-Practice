class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=set(nums)
        k=list(k)
        return k
a=Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(nums))
