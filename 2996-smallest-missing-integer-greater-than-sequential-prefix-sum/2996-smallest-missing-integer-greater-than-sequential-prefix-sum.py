class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        idx = 1
        while idx < n and nums[idx] == nums[idx-1] + 1:
            idx += 1
        x = sum(nums[:idx])
        nums = set(nums)
        while x in nums:
            x += 1
        return x