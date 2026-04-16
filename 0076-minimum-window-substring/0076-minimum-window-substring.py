class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        count = 0  # Count of t in s
        HashMap = Counter(t)
        min_len = float("inf")
        start_idx = -1
        m = len(s)
        n = len(t)
        while l < m and r < m:
            if count < n:
                if s[r] in HashMap:
                    if HashMap[s[r]] > 0:
                        count += 1
                    HashMap[s[r]] -= 1
                else:
                    HashMap[s[r]] = -1
            while count == n:
                length = r - l+1
                if length < min_len:
                    min_len = length
                    start_idx = l
                HashMap[s[l]] += 1
                if HashMap[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        return s[start_idx : start_idx + min_len] if start_idx > -1 else ""