class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2*limit + 2)
        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            if a > b:
                a, b = b, a
            delta[a+b] -= 1
            delta[a+b+1] += 1
            delta[a+1] -= 1
            delta[b+limit+1] += 1
        min_delta = 0
        curr_delta = 0
        for t in range(2, 2*limit+1):
            curr_delta += delta[t]
            if curr_delta < min_delta:
                min_delta = curr_delta
        return n+min_delta