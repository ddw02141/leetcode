from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [0, 1, 0, 3, 2, 3]
        # [0, 1, 2, 3, float("-inf"), float("-inf")]
        answer = 0
        n = len(nums)
        tails = [float("inf") for _ in range(n)]

        #         tails[0] = nums[0]

        #         if nums[1] < tails[0]:
        #             tails[0] = nums[1]
        #         else:
        #             tails[1] = nums[1]

        #         if nums[2] < tails[0]:
        #             tails[0] = nums[2]
        #         elif nums[2] < tails[1]:
        #             tails[1] = nums[2]
        #         else:
        #             tails[2] = nums[2]
        for i, num in enumerate(nums):
            for j in range(i + 1):
                if num < tails[j]:
                    tails[j] = num
                    break
                elif num == tails[j]:
                    break
        for i, tail in enumerate(reversed(tails)):
            if tail != float("inf"):
                return n - i


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
