class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        
        i = 0
        for color in range(3):
            for _ in range(counts[color]):
                nums[i] = color
                i += 1