class Solution:
    def selectionSort(self, nums):
        nums.sort(reverse=False)
        return nums
a=Solution()
nums = [5, 4, 4, 1, 1]
print(a.selectionSort(nums))