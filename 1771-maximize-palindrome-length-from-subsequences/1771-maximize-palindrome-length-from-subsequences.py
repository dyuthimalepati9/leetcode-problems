class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        word = word1 + word2
        dp = [[0] * (n + m) for _ in range(n + m)]
        
        for i in range(n + m - 1, -1,-1):
            for j in range(i, n + m):
                if i == j: dp[i][j] = 1
                elif word[i] == word[j]: dp[i][j] = 2 + dp[i + 1][j - 1]
                else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])        
        ans = 0
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]: ans = max(ans, dp[i][n + j])
        return ans