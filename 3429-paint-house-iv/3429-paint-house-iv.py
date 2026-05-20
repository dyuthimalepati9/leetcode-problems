class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [
            [[float("inf") for k in range(3)] for j in range(3)] for i in range(n // 2)]
        for i in range(n // 2):
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue

                    dp[i][j][k] = cost[i][j] + cost[n - 1 - i][k]
                    if i != 0:
                        dp[i][j][k] += min(
                            dp[i - 1][l][m]
                            for l in range(3)
                            for m in range(3)
                            if l != m and l != j and m != k
                        )
        return min(min(v) for v in dp[n // 2 - 1])