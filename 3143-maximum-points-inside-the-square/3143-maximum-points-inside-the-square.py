class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], 
                                    s: str) -> int:
        mxPts = [max(abs(x), abs(y)) for x, y in points]
        d = defaultdict(list)
        for c, tag in sorted(zip(mxPts, s)): d[tag].append(c)
        dist = min((arr[1] for arr in d.values()
                             if len(arr) > 1), default = inf)
        return sum(mxPt < dist for mxPt in mxPts)