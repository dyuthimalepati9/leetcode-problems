class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 0: return []
        
        # Precompute the maximum values coming from the right
        # suffix_max[i] will store the max value from index i+1 to n-1
        suffix_max = [0] * n
        current_max = -float('inf')
        for i in range(n - 1, -1, -1):
            suffix_max[i] = current_max
            current_max = max(current_max, nums[i])
            
        result = []
        left_max = -float('inf')
        
        for i in range(n):
            # Condition 1: Strictly greater than everything to the left
            is_left_valid = nums[i] > left_max
            
            # Condition 2: Strictly greater than everything to the right
            is_right_valid = nums[i] > suffix_max[i]
            
            # If either condition is met, the element is valid
            if is_left_valid or is_right_valid:
                result.append(nums[i])
            
            # Update left_max for the next iteration
            left_max = max(left_max, nums[i])
            
        return result