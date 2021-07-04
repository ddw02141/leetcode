class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i, (prev, cur) in enumerate(zip(intervals, intervals[1:])):
            prevStart, prevEnd = prev
            curStart, curEnd = cur
            if prevEnd >= curStart:
                intervals[i] = None
                intervals[i+1] = [min(prevStart, curStart), max(prevEnd, curEnd)]
        return [interval for interval in intervals if interval]
