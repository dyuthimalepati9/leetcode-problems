class Solution:
    def orderlyQueue(self, s: str, k: int) -> str: 
        if k > 1:
            return "".join(sorted(list(s)))
        n = len(s)
        minS = s
        for i in range(1, n):
            rot = s[i:] + s[:i]
            minS = min(minS,rot)
        return minS