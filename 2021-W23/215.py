# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest = (n - k)th smallest
        h = []
        for num in nums:
            heappush(h, -num)
            if len(h) > len(nums) - k + 1:
                heappop(h)

        return -h[0]
