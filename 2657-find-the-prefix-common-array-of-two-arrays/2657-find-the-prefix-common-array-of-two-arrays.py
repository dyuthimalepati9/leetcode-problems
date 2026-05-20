class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)

        seen = [0] * (n + 1)

        common = 0
        ans = []

        for i in range(n):

            seen[A[i]] += 1
            if seen[A[i]] == 2:
                common += 1

            seen[B[i]] += 1
            if seen[B[i]] == 2:
                common += 1

            ans.append(common)

        return ans