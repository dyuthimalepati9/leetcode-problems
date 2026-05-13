from collections import Counter

class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        freq = Counter()
        for r in responses:
            freq.update(set(r))
        maxCnt = max(freq.values())
        return min([w for w, c in freq.items() if c == maxCnt])