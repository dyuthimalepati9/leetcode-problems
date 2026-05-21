import numpy as np
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        rows = np.arange(1, m + 1)
        while low < high:
            mid = (low + high) // 2
            count = np.sum(np.minimum(n, mid // rows))
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return int(low)          