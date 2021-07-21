# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            lteMid = self.lteTarget(nums, n, mid)
            if lteMid >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def lteTarget(self, nums, n, target):
        slow, fast, count = 0, 0, 0
        while slow < n or fast < n:
            while fast < n and nums[fast] - nums[slow] <= target:
                fast += 1
            count += fast - slow - 1
            slow += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDistancePair([1, 3, 1], 1))  # Expect 0
    print(solution.smallestDistancePair([1, 1, 1], 2))  # Expect 0
    print(solution.smallestDistancePair([1, 6, 1], 3))  # Expect 5
