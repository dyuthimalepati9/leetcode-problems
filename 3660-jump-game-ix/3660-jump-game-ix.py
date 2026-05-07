from typing import List
from itertools import accumulate

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = list(accumulate(nums, max))
        nums_rev = nums[::-1]
        suff = list(accumulate(nums_rev, min))[::-1]
        ans = pref[:]
        for i in range(n - 2, -1, -1):
            if pref[i] > suff[i + 1]:
                ans[i] = ans[i + 1]
                
        return ans