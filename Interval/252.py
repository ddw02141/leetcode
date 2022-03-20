from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        # True
        # s1 e1 s2 e2
        # False
        # s1 s2 e2 e1
        # s1 s2 e1 e2
        intervals.sort(key=lambda i: i.start)
        for s1e1, s2e2 in zip(intervals, intervals[1:]):
            # print(s1e1.start, s1e1.end)
            # print(s2e2.start, s2e2.end)
            if s1e1.end > s2e2.start:
                return False

        return True
