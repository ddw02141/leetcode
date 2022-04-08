from typing import List
from heapq import heappush, heappop


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key=lambda i: i.start)
        endTimes = [intervals[0].end]
        for interval in intervals[1:]:
            endTime = heappop(endTimes)
            if endTime <= interval.start:
                heappush(endTimes, interval.end)
            else:
                heappush(endTimes, endTime)
                heappush(endTimes, interval.end)

        return len(endTimes)
