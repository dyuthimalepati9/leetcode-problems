class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # Get the 7 path positions (indices 0-15 in the 16-digit string)
        positions = []
        row, col = 0, 0
        positions.append(row * 4 + col)
        for d in directions:
            if d == 'D': row += 1
            else: col += 1
            positions.append(row * 4 + col)
        pos_set = set(positions)
        
        def count_up_to(n: int) -> int:
            s = str(n).zfill(16)
            digits = [int(c) for c in s]
            
            from functools import lru_cache
            
            @lru_cache(maxsize=None)
            def dp(pos, tight, last_path_val):
                """
                pos: current index in 16-digit string
                tight: still bounded by n's digits
                last_path_val: last digit on the path so far (start with 0)
                """
                if pos == 16:
                    return 1
                
                limit = digits[pos] if tight else 9
                total = 0
                
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    if pos in pos_set:
                        if d >= last_path_val:
                            total += dp(pos + 1, new_tight, d)
                        # else skip: would violate non-decreasing
                    else:
                        total += dp(pos + 1, new_tight, last_path_val)
                
                return total
            
            result = dp(0, True, 0)
            dp.cache_clear()
            return result
        
        return count_up_to(r) - count_up_to(l - 1)   