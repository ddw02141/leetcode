from typing import List
from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        answer = list()
        window = sorted(nums[:k - 1])
        for i in range(len(nums) - k + 1):
            # len(nums) - k ~ len(nums) - 1: -1 +k + 1  = k
            insort(window, nums[i + k - 1])
            median = (window[(k - 1) // 2] + window[k // 2]) / 2
            answer.append(median)
            window.pop(bisect_left(window, nums[i]))

        return answer
