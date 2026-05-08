class FenwickTree:
    def __init__(self, size):
        self.arr = [0] * (size + 1)
        self.n = size

    def update(self, i, num):
        while i <= self.n:
            self.arr[i] += num
            i += i & -i

    def prefixSum(self, i):
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= i & -i
        return res

    def querySum(self, l, r):
        return self.prefixSum(r) - self.prefixSum(l-1)
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        ft = FenwickTree(len(s))
        for (i,c) in enumerate(s, 1):
            if i == 1:
                ft.update(i, 0)
            else:
                if c == s[i-2]:
                    ft.update(i, 1)
                else:
                    ft.update(i, 0)
        # print(ft.arr)
        res = []
        for i in range(len(queries)):
            if queries[i][0] == 1:
                if s[queries[i][1]] == 'A':
                    s[queries[i][1]] = 'B'
                else:
                    s[queries[i][1]] = 'A'
                if len(s) > 1 and queries[i][1] == 0 and s[queries[i][1] + 1] == s[queries[i][1]]:
                    ft.update(queries[i][1] + 2, 1)
                elif len(s) > 1  and queries[i][1] == 0 and s[queries[i][1] + 1] != s[queries[i][1]]:
                    ft.update(queries[i][1] + 2, -1)
                elif queries[i][1] != 0:
                    if s[queries[i][1]] == s[queries[i][1] - 1]:
                        ft.update(queries[i][1] + 1, 1)
                    else:
                        ft.update(queries[i][1] + 1, -1)
                    # print(ft.arr)
                    if queries[i][1] + 1 < len(s):
                        if s[queries[i][1]] == s[queries[i][1] + 1]:
                            ft.update(queries[i][1] + 2, 1)
                        else:
                            ft.update(queries[i][1] + 2, -1)
                # print(ft.arr)
            else:
                if queries[i][1] - 1 >= 0 and s[queries[i][1] - 1] == s[queries[i][1]]:
                    
                    res.append(ft.querySum(queries[i][1] + 1, queries[i][2] + 1) - 1)
                else:
                    res.append(ft.querySum(queries[i][1] + 1, queries[i][2] + 1))
            # ABBBABAA
            # 00122223
        return res