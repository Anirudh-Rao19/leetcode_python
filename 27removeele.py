from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
k = sol.removeElement(nums, val)

print("k =", k)
print("Modified nums =", nums[:k])