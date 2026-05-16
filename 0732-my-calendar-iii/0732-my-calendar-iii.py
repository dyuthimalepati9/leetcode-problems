class MyCalendarThree:
    def __init__(self):
        self.delta = collections.Counter()
        self.max_k = 0
    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] += 1
        self.delta[endTime] -= 1
        curr = 0
        for t in sorted(self.delta):
            curr += self.delta[t]
            if curr > self.max_k:
                self.max_k = curr
        return self.max_k