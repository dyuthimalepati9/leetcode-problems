class Solution:
    def numberOfEdgesAdded(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        parity = [0] * n
        def find(x):
            if parent[x] != x:
                px = parent[x]
                parent[x] = find(px)
                parity[x] ^= parity[px]
            return parent[x]
        def union(u, v, w):
            ru, rv = find(u), find(v)
            if ru == rv:
                return (parity[u] ^ parity[v] ^ w) == 0
            parent[ru] = rv
            parity[ru] = parity[u] ^ parity[v] ^ w
            return True
        res = 0
        for u, v, w in edges:
            if union(u, v, w):
                res += 1
        return res
        