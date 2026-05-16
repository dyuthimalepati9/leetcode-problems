class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats) 
        h2p = collections.defaultdict(list) 
        for person in range(N):
            for hat in hats[person]:
                h2p[hat].append(person)
        if len(h2p) < N: 
            return 0
        MASK = [1 << p for p in range(N)]
        dp = [[0] * (2 ** N) for _ in range(len(h2p) + 1)]
        dp[0][0] = 1
        i, MOD = 1, 1000000007
        while h2p: 
            _, people = h2p.popitem()
            for j, n in enumerate(dp[i - 1]): 
                if not n:
                    continue
                dp[i][j] += n 
                for p in people: 
                    if not (MASK[p] & j):
                        dp[i][MASK[p] + j] += n
            i += 1
        return dp[-1][-1] % MOD