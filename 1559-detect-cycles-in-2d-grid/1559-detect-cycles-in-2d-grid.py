class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis = {}
        def dfs(i, j, prev, ref):
            vis[(i, j)] = True
            for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i+k[0]
                new_j = j+k[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                if prev == (new_i, new_j) or grid[new_i][new_j] != ref:
                    continue
                if (new_i, new_j) in vis or not dfs(new_i, new_j, (i, j), ref):
                    return False
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in vis:
                    continue
                if not dfs(i, j, None, grid[i][j]):
                    return True
        return False
        
                