class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n: int = len(nums)
        total: int = 0
        per_round: int = 0
        for i in range(n):
            total += nums[i]
            per_round += i * nums[i]
        answer: int = per_round
        for i in range(1, n):
            rotated: int = nums[n - i]
            per_round = per_round - (rotated * (n - 1)) + (total - rotated)
            answer = max(answer, per_round)
        return answer