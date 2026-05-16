from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Map each valid number from 2 to 30 to its prime bitmask
        # If a number is divisible by a square, its mask remains 0
        num_to_mask = {}
        for i in range(2, 31):
            mask = 0
            is_valid = True
            for idx, p in enumerate(primes):
                if i % (p * p) == 0:
                    is_valid = False
                    break
                if i % p == 0:
                    mask |= (1 << idx)
            if is_valid and mask > 0:
                num_to_mask[i] = mask

        # Count frequencies of each number in the input
        counts = Counter(nums)
        
        # dp[mask] stores the number of valid subsets formed so far
        # There are 10 primes, so 2^10 = 1024 possible masks
        dp = [0] * 1024
        dp[0] = 1  # Base case: 1 way to make an empty subset
        
        # Iterate through each valid candidate number available in the input
        for num in num_to_mask:
            if counts[num] == 0:
                continue
                
            num_mask = num_to_mask[num]
            freq = counts[num]
            
            # Update DP table backwards to avoid using the same element multiple times
            for mask in range(1023, -1, -1):
                if (mask & num_mask) == 0:
                    dp[mask | num_mask] = (dp[mask | num_mask] + dp[mask] * freq) % MOD
                    
        # Sum up all valid combinations (excluding the empty subset mask 0)
        ans = sum(dp[1:]) % MOD
        
        # Handle the contribution of 1s: each '1' doubles the number of valid subsets
        if counts[1] > 0:
            ans = (ans * pow(2, counts[1], MOD)) % MOD
            
        return ans