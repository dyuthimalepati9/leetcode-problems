class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        taboo = {(1, 3), (1, 5), (2, 5), (3, 1), (3, 5), (5, 1), (5, 2), (5, 3)}
        dp = [[1] * 6 for _ in range(6)]
        for i in range(6):
            dp[i][i] = 0
        for i, j in taboo:
            dp[i][j] = 0
        sub_totals = [sum(dp[i]) for i in range(6)]
        MOD = 10**9 + 7
        for k in range(2, n):
            new_dp = [[0] * 6 for _ in range(6)]
            for i in range(6):
                for j in range(6):
                    if i == j or (i, j) in taboo:
                        continue
                    new_dp[i][j] = sub_totals[j] - dp[j][i]
            dp = new_dp
            sub_totals = [sum(dp[i]) % MOD for i in range(6)]
        return sum(sub_totals) % MOD