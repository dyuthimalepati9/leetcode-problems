class ExamRoom:
    def __init__(self, n):
        self.n = n 
        self.seats = []
    def seat(self):
        if not self.seats:
            pos = 0 
        else:
            pos, dist = 0, self.seats[0]
            for i in range(1,len(self.seats)):
                if (self.seats[i] - self.seats[i-1])//2 > dist:
                    dist = (self.seats[i] - self.seats[i-1])//2
                    pos = (self.seats[i-1] + self.seats[i])//2 
            if self.n-1-self.seats[-1] > dist:
                pos = self.n-1
                dist = self.n-1-self.seats[-1]
        bisect.insort(self.seats, pos)   
        return pos
    def leave(self, p):
        self.seats.remove(p)