from functools import lru_cache
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def fn(i):
            ans = 1
            for j in range(i+1, min(len(arr), i+d+1)):
                if arr[j] >= arr[i]: break 
                ans = max(ans, 1+fn(j))
            for j in reversed(range(max(0, i-d), i)):
                if arr[j] >= arr[i]: break 
                ans = max(ans, 1+fn(j))
            return ans 
        return max(fn(i) for i in range(len(arr)))