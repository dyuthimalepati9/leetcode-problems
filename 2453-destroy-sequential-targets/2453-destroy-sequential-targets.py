class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        groups = defaultdict(list)
        for num in nums:
            groups[num % space].append(num)
        performance = defaultdict(list)
        for group in groups.values():
            performance[len(group)].append(min(group))
        return min(performance[max(performance)])