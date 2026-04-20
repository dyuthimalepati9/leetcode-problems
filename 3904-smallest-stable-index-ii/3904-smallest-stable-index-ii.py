class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        rightMin = [0] * n
        rightMin[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i+1])
        leftMax = float('-inf')
        for i in range(n):
            leftMax = max(leftMax, nums[i])
            if leftMax - rightMin[i] <= k:
                return i
        return -1