class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans, n = 0, len(cost)
        cost.sort(reverse = True)
        ind = 0
        while ind < n:
            if ind + 1 < n:
                ans += cost[ind] + cost[ind + 1]
            else:
                ans += cost[ind]
            ind += 3
        return ans