class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=0,0
        res=0
        n1,n2=len(nums1),len(nums2)
        while i<n1 and j<n2:
            if nums2[j]>=nums1[i]:
                res=max(res,j-i)
                j+=1
            else:
                i+=1
        return res