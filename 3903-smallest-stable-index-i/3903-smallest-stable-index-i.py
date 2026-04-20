class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        leftMax = [0] * n
        leftMax[0] = nums[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], nums[i])
        rightMin = [0] * n
        rightMin[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i])
        for i in range(n):
            if leftMax[i] - rightMin[i] <= k:
                return i

        return -1