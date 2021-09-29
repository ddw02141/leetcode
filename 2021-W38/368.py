# https://leetcode.com/problems/largest-divisible-subset/
# (a1, a2): divisible, (a2, a3): divisible => (a1, a3): divisible
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[nums[i]] for i in range(n)]
        # if nums[1] % nums[0] == 0:
        #     dp[1] = dp[0] + 1
        # if nums[2] % nums[0] == 0:
        #     dp[2] = max(dp[2], dp[0] + 1)
        # if nums[2] % nums[1] == 0:
        #     dp[2] = max(dp[2], dp[1] + 1)
        max_idx = n - 1
        maxi = -1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
                        if len(dp[i]) > maxi:
                            maxi = len(dp[i])
                            max_idx = i
        return dp[max_idx]
