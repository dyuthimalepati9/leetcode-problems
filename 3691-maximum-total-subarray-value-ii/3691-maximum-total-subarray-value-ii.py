from math import log2
from sortedcontainers import SortedList
class SparseTable:
    def __init__(self, a):
        self.n = len(a)
        max_log = self.n.bit_length()
        self.mn = [[0] * max_log for _ in range(self.n)]
        self.mx = [[0] * max_log for _ in range(self.n)]
        self.log_val = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_val[i] = self.log_val[i // 2] + 1
        for i in range(self.n):
            self.mn[i][0] = a[i]
            self.mx[i][0] = a[i]
        j = 1
        while (1 << j) <= self.n:
            for i in range(self.n - (1 << j) + 1):
                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + (1 << (j - 1))][j - 1]
                )
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + (1 << (j - 1))][j - 1]
                )
            j += 1
    def query_min(self, l, r):
        j = self.log_val[r - l + 1]
        return min(
            self.mn[l][j],
            self.mn[r - (1 << j) + 1][j]
        )
    def query_max(self, l, r):
        j = self.log_val[r - l + 1]
        return max(
            self.mx[l][j],
            self.mx[r - (1 << j) + 1][j]
        )
class Solution:
    def maxTotalValue(self, a, k):
        n = len(a)
        st = SparseTable(a)
        s = SortedList()
        for i in range(n):
            diff = st.query_max(0, i) - st.query_min(0, i)
            s.add((diff, 0, i))
        ans = 0
        while k:
            x, l, r = s.pop()  
            ans += x
            if l + 1 <= r:
                diff = (
                    st.query_max(l + 1, r)
                    - st.query_min(l + 1, r)
                )
                s.add((diff, l + 1, r))
            k -= 1
        return ans