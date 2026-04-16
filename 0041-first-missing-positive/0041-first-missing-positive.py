class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # The target domain is 1 to len(nums) -> That means we can use the given array as a hashmap to mark 
        # the occurances of the numbers.
        # Each index will represent that positive number. We will start with 1. (Index 0 will represent 1)
        # We don't need negative values -> Convert them into len(nums)+1 (out of range)
        # We don'y need zeros -> Convert them into len(nums)+1 (out of range)
        outOfRange = len(nums)+1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = outOfRange
            
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if index < len(nums) and nums[index] > 0:
                nums[index] *= -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1