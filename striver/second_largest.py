class Solution:
    def secondLargestElement(self, nums):
        k=max(nums)
        b=list(set(nums))
        b.remove(k)
        k=max(b)
        return k
a=Solution()
nums=([8, 8, 7, 6, 5])
a.secondLargestElement(nums)