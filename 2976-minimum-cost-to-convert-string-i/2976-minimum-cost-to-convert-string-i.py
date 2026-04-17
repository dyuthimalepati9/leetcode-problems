class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        ALPHABET = 26

        dist = [[INF] * ALPHABET for _ in range(ALPHABET)]
        for i in range(ALPHABET):
            dist[i][i] = 0
            
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        for k in range(ALPHABET):
            for i in range(ALPHABET):
                if dist[i][k] == INF:
                    continue
                for j in range(ALPHABET):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]

        return total_cost   