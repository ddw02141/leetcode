from typing import List
from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        new_nums = nums[pivot:] + nums[:pivot]
        idx = bisect_left(new_nums, target)
        if idx >= n or new_nums[idx] != target:
            return -1
        return (idx + pivot) % n


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Expect 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], -1))  # Expect -1
    print(solution.search([1], 2))  # Expect -1
    print(solution.search([5, 1, 3], 1))  # Expect 1
