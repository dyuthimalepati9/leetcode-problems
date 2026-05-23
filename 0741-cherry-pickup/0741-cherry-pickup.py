class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        bad = float('-inf')
        @functools.cache
        def dfs(k: int, r1: int, r2: int):
            if r1 < 0 or r2 < 0 or r1 > r2:
                return bad
            c1 = k-r1
            c2 = k-r2
            if c1 < 0 or c2 < 0:
                return bad
            if k == 0:
                return grid[0][0] 
            if grid[r1][c1] < 0 or grid[r2][c2] < 0:
                return bad
            prev = max(
                dfs(k-1, r1, r2),
                dfs(k-1, r1-1, r2),
                dfs(k-1, r1, r2-1),
                dfs(k-1, r1-1, r2-1)
            )
            if r1 == r2:
                return prev + grid[r1][c1]
            else:
                return prev + grid[r1][c1] + grid[r2][c2]
        N = len(grid)
        return max(dfs(2*N-2, N-1, N-1), 0)  