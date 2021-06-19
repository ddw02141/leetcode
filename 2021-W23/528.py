# https://leetcode.com/problems/random-pick-with-weight/

from bisect import bisect_left
from random import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.accumulated = list()
        for weight in w:
            if not self.accumulated:
                self.accumulated.append(weight)
            else:
                self.accumulated.append(self.accumulated[-1] + weight)

    def pickIndex(self) -> int:
        r = random.uniform(0, self.accumulated[-1])
        return bisect_left(self.accumulated, r)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
