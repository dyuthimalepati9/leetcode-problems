class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        g = [[]for _ in range(len(edges)+2)]
        depth, curLevel =  -1, [1] 
        for u, v in edges:
            if u > v: u, v = v, u
            g[u].append(v)
        while curLevel:
            depth +=1
            nxtLevel = list(chain(*map(lambda x: g[x], curLevel)))
            curLevel = nxtLevel
        return pow(2, depth - 1, 1_000_000_007)