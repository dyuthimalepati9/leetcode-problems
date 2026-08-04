class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 1):
            for val in range(nums[i] + 1, nums[i + 1]):
                result.append(val)
        
        return result