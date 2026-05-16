import numpy as np

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # find prime factors of each unique number in `nums`
        nums_set = set(nums)
        fact = {
            n: set([p for p in PRIMES if n % p == 0]) 
            for n in iter(nums_set)
        }

        # coprime[m, n] = True if `gcd(m, n) = 1`, otherwise False.
        coprime = np.zeros((51, 51), dtype=bool)
        for m in iter(nums_set):
            for n in iter(nums_set):
                coprime[m, n] = coprime[n, m] = \
                    bool(fact[m].intersection(fact[n]) == set())

        # store edges in a more convenient adjacency list format
        adj_list = {u: [] for u in range(len(nums))}
        for u, v in edges:
            adj_list[u] += [v]
            adj_list[v] += [u]

        # nearest[u][m] = nearest node `v` to `u` along the path 
        # from `0` s.t. 
        #   `gcd(m, nums[v]) = 1`   for all m = 1,...,50
        nearest = {0: np.full(51, -1, dtype=int)}

        # ans[u] = nearest node `v` to `u` along the path from `0` s.t. 
        #   `gcd(nums[u], nums[v]) = 1`
        ans = np.full(len(nums), -1, dtype=int)

        q = deque([0])
        while len(q) > 0:
            u = q.popleft()
            nearest_new = nearest[u].copy()

            # mask that indicates which numbers are coprime to `nums[u]`
            coprime_mask = coprime[nums[u]]

            # vectorized update
            nearest_new[coprime_mask] = u

            # iterate through children of `u`
            for v in adj_list[u]:
                if v not in adj_list:
                    continue
                nearest[v] = nearest_new
                ans[v] = nearest_new[nums[v]]
                q += [v]
                
            # mark visited
            adj_list.pop(u) 

            # `nearest[u]` is no longer needed; release from memory
            nearest.pop(u)

        return ans.tolist()
                        