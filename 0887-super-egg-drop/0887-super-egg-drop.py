class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1)]
        drops = 0
        while dp[drops][k] < n:
            drops += 1
            dp.append([0] * (k + 1))
            for i in range(1, k+1):
                dp[drops][i] = 1 + dp[drops-1][i] + dp[drops-1][i-1]
        return drops