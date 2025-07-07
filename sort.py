class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[j]
            j+=1
        nums1[:]=sorted(nums1)
        return nums1
sol=Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,4],3))