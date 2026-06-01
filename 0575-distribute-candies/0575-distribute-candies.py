class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = set(candyType)
        return min(len(candyType) // 2, len(unique_types))