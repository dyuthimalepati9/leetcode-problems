class Solution:
    def integerReplacement(self, n: int) -> int:
        numOps = 0
        while n > 1:
            if n&1 == 0:
                n >>= 1
            elif n&0b11 == 0b11 and n != 0b11:
                n += 1
            else:
                n -= 1

            numOps += 1
        
        return numOps