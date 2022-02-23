from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        nums = [1 for _ in range(n)]

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                nums[i + 1] = nums[i] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                nums[i - 1] = max(nums[i] + 1, nums[i - 1])

        return sum(nums)
