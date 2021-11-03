class MyCalendar:

    def __init__(self):
        self.intervals = list()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.intervals:
            if (s < end and start < e) or (start < e and s < end):
                return False
        self.intervals.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)