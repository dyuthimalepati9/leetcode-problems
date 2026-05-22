from heapq import heappush as push, heappop as pop
class Solution:
    def minSkips(self, x: List[int], speed: int, hoursBefore: int) -> int:
        
        @lru_cache(None)
        def f(i, skips):
            if skips < 0: return inf 
            if i==0:
                return x[i]
            next_time = f(i-1,skips)
            return min(f(i-1,skips-1) + x[i], x[i] + next_time + (-next_time%speed))
            
        n = len(x)
        hoursBefore *= speed

        for skips in range(0, n+1):
            ans = f(n-1,skips)
            
            if ans <= hoursBefore:
                return skips

        return -1