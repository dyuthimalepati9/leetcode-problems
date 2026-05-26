from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.intervals = SortedList()

    def addRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and right >= self.intervals[k][0]: 
            right = max(right, self.intervals[k][1])
            self.intervals.pop(k)
        if k and self.intervals[k-1][1] >= left: 
            left = min(left, self.intervals[k-1][0])
            right = max(right, self.intervals[k-1][1])
            self.intervals.pop(k-1)
        self.intervals.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        k = self.intervals.bisect_left([left, right])
        return k and self.intervals[k-1][0] <= left < right <= self.intervals[k-1][1] or k < len(self.intervals) and self.intervals[k][0] <= left < right <= self.intervals[k][1] 

    def removeRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and self.intervals[k][0] <= right: 
            if right < self.intervals[k][1]: 
                self.intervals[k][0] = right 
                break 
            else: self.intervals.pop(k)
        if k and left < self.intervals[k-1][1]: 
            if right < self.intervals[k-1][1]: self.intervals.add([right, self.intervals[k-1][1]])
            self.intervals[k-1][1] = left 