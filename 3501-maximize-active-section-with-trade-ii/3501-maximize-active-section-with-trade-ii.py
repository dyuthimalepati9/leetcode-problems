from bisect import bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # Maximal zero runs: (start, end) inclusive.
        segs = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                segs.append((i, j - 1))
                i = j
            else:
                i += 1
        k = len(segs)
        starts = [a for a, _ in segs]

        # ---- Case 1: fully-contained adjacent pairs, answered offline ----
        # candidate: A = Zi.start, D = Zi+1.end, val = len(Zi)+len(Zi+1)
        # query: max val with A >= l and D <= r
        cands = []
        for idx in range(k - 1):
            A = segs[idx][0]
            D = segs[idx + 1][1]
            val = (segs[idx][1] - segs[idx][0] + 1) + (segs[idx + 1][1] - segs[idx + 1][0] + 1)
            cands.append((A, D, val))
        cands.sort(key=lambda c: c[0], reverse=True)          # by A desc

        q = len(queries)
        order = sorted(range(q), key=lambda t: queries[t][0], reverse=True)  # l desc

        fen = [0] * (n + 1)                                   # Fenwick prefix-max over D

        def update(pos, val):
            x = pos + 1
            while x <= n:
                if val > fen[x]:
                    fen[x] = val
                x += x & (-x)

        def pref_max(pos):
            res, x = 0, pos + 1
            while x > 0:
                if fen[x] > res:
                    res = fen[x]
                x -= x & (-x)
            return res

        case1 = [0] * q
        ci, m = 0, len(cands)
        for qi in order:
            l = queries[qi][0]
            while ci < m and cands[ci][0] >= l:              # A >= l
                update(cands[ci][1], cands[ci][2])
                ci += 1
            case1[qi] = pref_max(queries[qi][1])             # D <= r

        # ---- Combine with boundary-clipped pairs ----
        def seg_containing(p):
            idx = bisect_right(starts, p) - 1
            if idx >= 0 and segs[idx][0] <= p <= segs[idx][1]:
                return idx
            return -1

        ans = [0] * q
        for qi in range(q):
            l, r = queries[qi]
            best = case1[qi]

            # left-clipped pair: run containing l (l strictly inside) + right neighbor
            if s[l] == '0':
                jl = seg_containing(l)
                if jl != -1 and l > segs[jl][0] and jl + 1 < k:
                    C = segs[jl + 1][0]
                    if r >= C:                               # pair valid
                        left_len = segs[jl][1] - l + 1
                        right_len = min(segs[jl + 1][1], r) - C + 1
                        best = max(best, left_len + right_len)

            # right-clipped pair: run containing r (r strictly inside) + left neighbor
            if s[r] == '0':
                jr = seg_containing(r)
                if jr != -1 and r < segs[jr][1] and jr - 1 >= 0:
                    B = segs[jr - 1][1]
                    if l <= B:                               # pair valid
                        right_len = r - segs[jr][0] + 1
                        left_len = B - max(segs[jr - 1][0], l) + 1
                        best = max(best, left_len + right_len)

            ans[qi] = total_ones + best
        return ans