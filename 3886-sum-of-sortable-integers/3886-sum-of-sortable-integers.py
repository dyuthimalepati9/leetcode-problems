class Solution:
    def check(self, nums, k):
        n = len(nums)
        prev_max = 0
        for i in range(0, n, k):
            if nums[i] < prev_max:
                return False
            maxx = nums[i]  
            point = False   
            for j in range(i + 1, i + k):
                if nums[j] < prev_max:
                    return False
                if nums[j - 1] > nums[j]:
                    if point:
                        return False
                    point = True
                maxx = max(maxx, nums[j])
            if point:
                if nums[i] < nums[i + k - 1]:
                    return False
            prev_max = maxx
        return True
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k == 0 and self.check(nums, k):
                ans += k
        return ans