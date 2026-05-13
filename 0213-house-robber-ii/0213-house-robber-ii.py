class Solution:
    def rob(self, nums):
        def solve(arr):
            n = len(arr)
            dp = [[0, 0] for _ in range(n)]
            dp[0][0] = 0
            dp[0][1] = arr[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = arr[i] + dp[i-1][0]
            return max(dp[n-1][0], dp[n-1][1])
        n = len(nums)
        if n == 1:
            return nums[0]
        case1 = solve(nums[:-1])
        case2 = solve(nums[1:])
        return max(case1, case2)
    