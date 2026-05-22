class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @lru_cache(None)
        def dfs(target):
            if not target: return 0
            tCtr, res = Counter(target), inf
            mn = min(tuple(tCtr), key= lambda x: tCtr[x] )
            for sCtr in sCtrs: 
                if sCtr[mn] == 0: continue 
                nxt = dfs(''.join((tCtr-sCtr).elements()))
                if nxt != -1: res = min(res, 1 + nxt)
            return -1 if res == inf else res
        sCtrs = list(filter(lambda s: bool(set(s)
                 & set(target)), map(Counter, stickers)))
        return dfs(target) 