class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(l, r):
            if l>=r:
                return 0
            mid=(l+r)//2
            count=sort(l,mid)+sort(mid+1,r)
            end=mid+1
            for left in nums[l:mid+1]:
                while end<=r and left>2*nums[end]:
                    end+=1
                count+=end-(mid+1)
            nums[l:r+1]=sorted(nums[l:r+1])
            return count
        return sort(0,len(nums)-1)