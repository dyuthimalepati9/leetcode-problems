from collections import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        
        grid = [[0]*m for _ in range(n)]
        dist = [[float('inf')]*m for _ in range(n)]
        
        q = deque()
        
        for r, c, color in sources:
            grid[r][c] = color
            dist[r][c] = 0
            q.append((r, c))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    
                    # If reached first time
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        grid[nr][nc] = grid[r][c]
                        q.append((nr, nc))
                    
                    elif dist[nr][nc] == dist[r][c] + 1:
                        grid[nr][nc] = max(grid[nr][nc], grid[r][c])
        
        return grid
        