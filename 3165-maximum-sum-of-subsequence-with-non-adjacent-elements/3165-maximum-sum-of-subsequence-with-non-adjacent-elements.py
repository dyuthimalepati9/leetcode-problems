from typing import List
class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        NEG = -10**18
        size = 1
        while size < n:
            size <<= 1
        seg = [(0,0,NEG,NEG)] * (2*size)
        def leaf_matrix(x):
            return (0,0,x,NEG)
        for i in range(n):
            seg[size + i] = leaf_matrix(nums[i])
        for i in range(size - 1, 0, -1):
            L = seg[2*i]
            R = seg[2*i+1]
            a00,a01,a10,a11 = R
            b00,b01,b10,b11 = L
            c00 = a00 + b00 if a00 + b00 >= a01 + b10 else a01 + b10
            c01 = a00 + b01 if a00 + b01 >= a01 + b11 else a01 + b11
            c10 = a10 + b00 if a10 + b00 >= a11 + b10 else a11 + b10
            c11 = a10 + b01 if a10 + b01 >= a11 + b11 else a11 + b11
            seg[i] = (c00,c01,c10,c11)
        mod = 10**9 + 7
        total = 0
        for pos, x in queries:
            idx = size + pos
            seg[idx] = leaf_matrix(x)
            idx //= 2
            while idx >= 1:
                L = seg[2*idx]
                R = seg[2*idx+1]
                a00,a01,a10,a11 = R
                b00,b01,b10,b11 = L
                c00 = a00 + b00 if a00 + b00 >= a01 + b10 else a01 + b10
                c01 = a00 + b01 if a00 + b01 >= a01 + b11 else a01 + b11
                c10 = a10 + b00 if a10 + b00 >= a11 + b10 else a11 + b10
                c11 = a10 + b01 if a10 + b01 >= a11 + b11 else a11 + b11
                seg[idx] = (c00,c01,c10,c11)
                idx //= 2
            root = seg[1]
            res = root[0] if root[0] >= root[2] else root[2]
            total = (total + res) % mod
            nums[pos] = x
        return total    