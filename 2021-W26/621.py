# https://leetcode.com/problems/task-scheduler/
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (n+1) * (M - 1) + Mct)
