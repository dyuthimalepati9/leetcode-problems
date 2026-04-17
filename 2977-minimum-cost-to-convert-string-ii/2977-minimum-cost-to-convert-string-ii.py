class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        costs = {}
        for u, v, w in zip(original, changed, cost):
            graph[u].append((v, w))

        def compute_costs(source):
            if source in costs:
                return costs[source]
            heap, memo = [(0, source)], {source: 0}
            while heap:
                dist, u = heapq.heappop(heap)
                if dist > memo[u]:
                    continue
                for v, w in graph[u]:
                    next_w = dist + w
                    if v not in memo or memo[v] > next_w:
                        memo[v] = next_w
                        heapq.heappush(heap, (next_w, v))
            costs[source] = memo
            return memo

        n = len(source)
        swap_lengths = sorted(set(len(s) for s in original))
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for l in range(n):
            if dp[l] == float('inf'):
                continue
            if source[l] == target[l]:
                dp[l + 1] = min(dp[l + 1], dp[l])
            for length in swap_lengths:
                r = l + length
                if r > n:
                    break
                s = source[l:r]
                t = target[l:r]
                if s in graph:
                    dists = compute_costs(s)
                    if t in dists:
                        dp[r] = min(dp[r], dp[l] + dists[t])
        return -1 if dp[-1] == float('inf') else dp[-1]