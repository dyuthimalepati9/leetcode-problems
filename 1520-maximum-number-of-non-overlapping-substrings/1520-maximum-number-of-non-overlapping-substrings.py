class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        firstSeen = [-1]*26
        lastSeen = [-1]*26
        for i, val in enumerate(s):
            index = ord(val) - ord('a')
            if firstSeen[index] == -1:
                firstSeen[index] = i
            lastSeen[index] = i
        intervals = []
        for i in range(26):
            if firstSeen[i] == -1:
                continue
            leftBoundary = firstSeen[i]
            rightBoundary = lastSeen[i]
            left = right = leftBoundary
            while left > leftBoundary or right < rightBoundary:
                if left > leftBoundary:
                    left -= 1
                if right < rightBoundary:
                    right +=1
                leftChar = ord(s[left]) - ord('a')
                rightChar = ord(s[right]) - ord('a')
                leftBoundary = min(leftBoundary, firstSeen[leftChar], firstSeen[rightChar])
                rightBoundary = max(rightBoundary, lastSeen[leftChar], lastSeen[rightChar])
            intervals.append([leftBoundary, rightBoundary])
        intervals = sorted(intervals)
        @lru_cache(None)
        def dp(i):
            if i == len(intervals):
                return [0, []]
            skipLength, skipArr = dp(i + 1)
            start, end = intervals[i]
            nxtLength, nxtArray = dp(bisect_right(intervals, [end, inf]))
            takeLength = nxtLength + end - start + 1
            takeArr = [intervals[i]] + nxtArray
            if len(takeArr) > len(skipArr):
                return [takeLength, takeArr]
            elif len(takeArr) == len(skipArr):
                if takeLength < skipLength:
                    return [takeLength, takeArr]
            return [skipLength, skipArr]
        length, arr = dp(0)
        ans = []
        for start, end in arr:
            ans.append(s[start: end + 1])
        return ans