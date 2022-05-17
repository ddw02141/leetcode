from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        2
        2 6
        2 (6 4)
        2 (6 4) 8
        2 (6 4) 8 15
        2 (6 4 8 15 9)
        2 (6 4 8 15 9 10)
        """
        n = len(nums)
        l, r = n, 0
        prev = nums[0]
        for i in range(1, n):
            if nums[i] < prev:
                r = i
            else:
                prev = nums[i]
        prev = nums[-1]
        for i in range(n - 1)[::-1]:
            if prev < nums[i]:
                l = i
            else:
                prev = nums[i]
        if l == n or r == 0:
            return 0

        return r - l + 1
