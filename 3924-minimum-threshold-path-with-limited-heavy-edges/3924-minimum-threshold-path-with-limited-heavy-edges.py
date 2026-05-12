from collections import deque

class Solution:
    def minimumThreshold(self, n, edges, source, target, k):
        
        def can(T):
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                cost = 1 if w > T else 0
                graph[u].append((v, cost))
                graph[v].append((u, cost))

            INF = 10**9
            dist = [INF] * n
            dist[source] = 0

            dq = deque([source])

            while dq:
                node = dq.popleft()

                for nei, cost in graph[node]:
                    nd = dist[node] + cost
                    if nd < dist[nei]:
                        dist[nei] = nd
                        if cost == 0:
                            dq.appendleft(nei)
                        else:
                            dq.append(nei)

            return dist[target] <= k

        # collect max weight for binary search
        max_w = max((w for _, _, w in edges), default=0)

        l, r = 0, max_w
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if can(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans