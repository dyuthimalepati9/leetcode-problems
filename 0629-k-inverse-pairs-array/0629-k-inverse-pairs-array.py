class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp, mod = [1]+[0] * k, 1_000_000_007
        
        for i in range(n):
            tmp, sm = [], 0

            for j in range(k + 1):
                sm+= dp[j]
                if j-i >= 1: sm-= dp[j-i-1]
                sm%= mod
                tmp.append(sm)

            dp = tmp

            
        return dp[k]