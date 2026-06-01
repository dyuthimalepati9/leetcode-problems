class Solution:
    def minimumOperations(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[0 for i in range(10)] for j in range(m)]
        for i in range(n):
            for j in range(m):
                dp[j][grid[i][j]] += 1 
        @lru_cache(None)
        def function(col,prev):
            if col == m:
                return 0 
            min_val = float("inf")
            for i in range(10):
                if i != prev:
                    count = n-dp[col][i]
                    min_val = min(min_val,count+function(col+1,i))
            return min_val 
        return function(0,-1)