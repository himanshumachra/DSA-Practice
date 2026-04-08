class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target=2
        a=0
        b=len(numbers)-1
        while a < b:
            if numbers[a]+numbers[b] == target:
                print(a +1 , b +1 )
                break
            elif numbers[a]+numbers[b] > target:
                b=b-1
            elif numbers[a]+numbers[b]<target:
                a=a+1
a=Solution()
a.twoSum([0,0,2,3,4],2)
