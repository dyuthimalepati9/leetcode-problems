from collections import deque

class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10 ** 9 + 7
        if m == 1: 
            return (3 * pow(2, n - 1, MOD)) % MOD
        elif m == 2: 
            return (2 * pow(3, n, MOD)) % MOD
        elif m == 3:
            ans = deque([12, 54])
            if n <= 2: return ans[n-1]
            for _ in range(2, n):
                v = (5 * ans[-1] - 2 * ans[-2]) % MOD
                ans.append(v)
                ans.popleft()
            return ans[-1]
        elif m == 4:
            ans = deque([24, 162, 1122])
            if n <= 3: return ans[n-1]
            for _ in range(3, n):
                v = (9 * ans[-1] - 15 * ans[-2] + 6 * ans[-3]) % MOD
                ans.append(v)
                ans.popleft()
            return ans[-1]
        else:
            ans = deque([48, 486, 5118, 54450, 580986])
            if n <= 5: return ans[n-1]
            for _ in range(5, n):
                v = (16 * ans[-1] - 65 * ans[-2] + 92 * ans[-3] - 48 * ans[-4] + 8 * ans[-5]) % MOD
                ans.append(v)
                ans.popleft()
            return ans[-1]