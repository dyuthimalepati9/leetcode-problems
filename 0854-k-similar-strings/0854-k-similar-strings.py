class Solution:
    from collections import deque
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        def neighbors(s):
            s = list(s)
            i = 0
            while s[i] == s2[i]:
                i += 1
            res = []
            swap_matches_one = []
            swap_matches_both = -1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    if s[i] == s2[j]:
                        swap_matches_both = j
                        break
                    else:
                        swap_matches_one.append(j)
            if swap_matches_both != -1:
                j = swap_matches_both
                s[i], s[j] = s[j], s[i]
                res.append("".join(s))
                s[i], s[j] = s[j], s[i]
                return res
            else:
                for j in swap_matches_one:
                    s[i], s[j] = s[j], s[i]
                    res.append("".join(s))
                    s[i], s[j] = s[j], s[i]
                return res
        queue = deque([(s1, 0)])
        visited = set([s1])
        while queue:
            curr, steps = queue.popleft()
            if curr == s2:
                return steps
            for nxt in neighbors(curr):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))   