#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if nums[0]>target:
                return 0
            elif nums[-1]<target:
                return len(nums)
            else:
                i=1
                while nums[i]<target:
                    i+=1
                return i 
sol=Solution()
print(sol.searchInsert([1,2,3,4,5],5))
print(sol.searchInsert([1,2,4,5],3))
print(sol.searchInsert([2,3,4,5],1))
print(sol.searchInsert([1,2,3,4,5],6))