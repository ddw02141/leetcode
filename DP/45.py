from typing import List


class Solution:
    # O(len(nums) * max(nums)) solution
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [float("inf") for _ in range(n)]
    #     dp[0] = 0
    #     for i in range(n):
    #         for j in range(1, nums[i] + 1):
    #             if i + j >= n:
    #                 break
    #             dp[i + j] = min(dp[i + j], dp[i] + 1)
    #
    #     return dp[-1]

    # O(len(nums)) solution
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        left = 0
        right = nums[0]
        jumps = 1
        while right < n - 1:
            left, right = right, max(i + nums[i] for i in range(left, right + 1))
            jumps += 1
        return jumps
