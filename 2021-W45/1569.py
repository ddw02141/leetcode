from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = 1000

        def f(nums):
            if len(nums) <= 2:
                return 1
            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]

            return comb(len(left) + len(right), len(left)) * f(left) * f(right)

        return (f(nums) - 1) % MOD
