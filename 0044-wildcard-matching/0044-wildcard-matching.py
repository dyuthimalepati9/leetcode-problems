class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[-1]*(n+1)for _ in range(m+1)]
        def find(i,j,s,p,dp):
            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0:
                return False
            if i < 0 and j >= 0:
                for k in range(j + 1):
                    if p[k] != "*":
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = find(i-1,j-1,s,p,dp)
            elif p[j]=='*':
                dp[i][j] = find(i-1,j,s,p,dp) or find(i,j-1,s,p,dp)
            else:
                dp[i][j]= False
            return dp[i][j]
        return find(m-1,n-1,s,p,dp) 