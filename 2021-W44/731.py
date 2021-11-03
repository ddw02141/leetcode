:class MyCalendarTwo:

    def __init__(self):
        self.intervals = list()

    def book(self, start: int, end: int) -> bool:
        curStart = start
        curEnd = end
        overlappingCount = 0
        self.intervals.sort()
        for s, e in self.intervals:
            if s < curEnd and curStart < e:
                if curStart <= s:
                    # curStart, s, e, curEnd
                    if e <= curEnd:
                        curStart = e
                    # curStart, s, curEnd, e
                    else:
                        overlappingCount += 1
                        if overlappingCount == 2:
                            return False
                elif s < curStart:
                    # s, curStart, curEnd, e
                    if curEnd <= e:
                        overlappingCount += 1
                        if overlappingCount == 2:
                            return False
                    # s, curStart, e, curEnd
                    else:
                        curStart = e
        self.intervals.append((start, end))
        return True


if __name__ == "__main__":
    myCalendarTwo = MyCalendarTwo()
    print(myCalendarTwo.book(10, 20))  # return True
    print(myCalendarTwo.book(50, 60))  # return True
    print(myCalendarTwo.book(10, 40))  # return True
    print(myCalendarTwo.book(5, 15))  # return False
    print(myCalendarTwo.book(5, 10))  # return True
    print(myCalendarTwo.book(25, 55))  # return True
