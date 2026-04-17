class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n+1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [0] * (n + 1)         
        tin = [0] * (n + 1)         
        tout = [0] * (n + 1)         
        parent = [0] * (n + 1)
        current_weight = [0] * (n + 1)
        timer = 1   
        def dfs(u, par, d):
            nonlocal timer
            dist[u] = d
            tin[u] = timer
            timer += 1
            parent[u] = par
            for v, w in graph[u]:
                if v == par:
                    continue
                current_weight[v] = w
                dfs(v, u, d + w)
            tout[u] = timer - 1
        dfs(1, 0, 0)
        bit = [0] * (n + 2)
        def bit_update(i, diff):
            while i <= n:
                bit[i] += diff
                i += i & -i
        def bit_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        def range_update(l, r, diff):
            bit_update(l, diff)
            bit_update(r + 1, -diff)
        result_list = []
        for query in queries:
            if query[0] == 2:
                x = query[1]
                current_distance = dist[x] + bit_sum(tin[x])
                result_list.append(current_distance)
            else:
                _, u, v, new_weight = query
                child = u if parent[u] == v else v
                diff = new_weight - current_weight[child]
                current_weight[child] = new_weight
                range_update(tin[child], tout[child], diff)
        return result_list