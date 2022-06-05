from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = deque()
        answer = list()
        for i, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                answer.append(nums[d[0]])

        return answer
