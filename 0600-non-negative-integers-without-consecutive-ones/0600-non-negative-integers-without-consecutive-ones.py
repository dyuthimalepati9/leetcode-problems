class Solution:
  def findIntegers(self, n: int) -> int:
    digits = [int(c) for c in bin(n)[2:]] 
    @lru_cache(None)
    def dp(pos: int, is_tight: bool, prev_one: bool) -> int:
      if pos == len(digits):
        return 1
      res = 0
      limit = digits[pos] if is_tight else 1
      for d in range(limit + 1):
        if d == 1 and prev_one:
          continue
        is_tight_ = is_tight & (d == limit)
        res += dp(pos + 1, is_tight_, d == 1)
      return res
    return dp(0, True, False) 