from math import gcd

class Solution:
    def gcdSum(self, nums):
        n = len(nums)

        prefix = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        prefix.sort()

        ans = 0
        l, r = 0, n - 1

        while l < r:
            ans += gcd(prefix[l], prefix[r])
            l += 1
            r -= 1

        return ans