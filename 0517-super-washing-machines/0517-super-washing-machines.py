class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        target = sum(machines) // len(machines)  
        if target * len(machines) != sum(machines):
            return -1
        last_shift = 0
        res = 0
        for i in range(len(machines)):
            shift = last_shift + machines[i] - target
            if last_shift < 0 < shift:
                res = max(res, (shift - last_shift))
            else:
                res = max(res, abs(shift))
            last_shift = shift
        return res