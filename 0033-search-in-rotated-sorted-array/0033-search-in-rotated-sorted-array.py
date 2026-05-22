class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums, target, s, e):
            if s > e:
                return -1
            mid = s + (e - s) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[s]:
                if nums[s] <= target <= nums[mid]:
                    return binary(nums, target, s, mid - 1)
                else:
                    return binary(nums, target, mid + 1, e)
            else:
                if nums[mid] <= target <= nums[e]:
                    return binary(nums, target, mid + 1, e)
                else:
                    return binary(nums, target, s, mid - 1)
        return binary(nums, target, 0, len(nums) - 1)