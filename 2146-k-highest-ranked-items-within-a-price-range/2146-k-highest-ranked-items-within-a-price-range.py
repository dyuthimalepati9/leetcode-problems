from collections import deque
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        def in_range(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != 0
        R, C = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(C)] for _ in range(R)]
        queue = deque()
        queue.append((0, start))
        dist[start[0]][start[1]] = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            curr_dist, (i, j) = queue.popleft()
            for move_i, move_j in moves:
                new_i, new_j = i + move_i, j + move_j
                if in_range(new_i, new_j) and dist[new_i][new_j] == math.inf:
                    dist[new_i][new_j] = curr_dist + 1
                    queue.append((curr_dist + 1, (new_i, new_j)))
        data = []
        for i in range(R):
            for j in range(C):
                if pricing[0] <= grid[i][j] <= pricing[1] and dist[i][j] != math.inf:
                    data.append((dist[i][j], grid[i][j], i, j))
        return [[i, j] for (_, _, i, j) in sorted(data)[:k]]