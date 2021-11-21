from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1


if __name__ == "__main__":
    solution = Solution()

    print("------------------ Test Case 1 ------------------")
    sol = solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    ans = 6
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution.longestOnes([0, 0, 1, 1, 1, 0, 0], 0)
    ans = 3
    assert ans == sol, f"Expected {ans} Actual {sol}"
