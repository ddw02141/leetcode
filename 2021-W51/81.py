from typing import List
from bisect import bisect_left


def get_pivot(left, right, nums):
    if left >= right:
        return left
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        return get_pivot(mid + 1, right, nums)
    elif nums[mid] == nums[right]:
        pivot1 = get_pivot(mid + 1, right, nums)
        pivot2 = get_pivot(left, mid, nums)
        if nums[pivot1 - 1] > nums[pivot1]:
            return pivot1
        return pivot2
    else:
        return get_pivot(left, mid, nums)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pivot = get_pivot(0, n - 1, nums)
        new_nums = nums[pivot:] + nums[:pivot]
        idx = bisect_left(new_nums, target)
        if idx >= n or new_nums[idx] != target:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2))  # Expect True
    print(solution.search([1, 0, 1, 1, 1], 0))  # Expect True
    print(solution.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13))  # Expect True
