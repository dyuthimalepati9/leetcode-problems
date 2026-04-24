class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        answer = []
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            trimmed.sort(key=lambda x: (x[0], x[1]))
            answer.append(trimmed[k-1][1])
        return answer
 