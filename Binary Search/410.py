from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0
        right = 10 ** 11
        maxNum = max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if mid < maxNum:
                left = mid + 1
                continue
            fold = self.getFold(mid, nums)
            if fold <= m:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def getFold(self, threshold, nums):
        fold = 0
        current = 0
        for num in nums:
            current += num
            if current > threshold:
                fold += 1
                current = num
        if current > 0:
            fold += 1
        return fold
