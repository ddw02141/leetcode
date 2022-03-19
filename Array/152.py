from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        answer = imax = imin = nums[0]
        for i in range(1, n):
            candidates = (imax * nums[i], imin * nums[i], nums[i])
            imax = max(candidates)
            imin = min(candidates)

            answer = max(answer, imax)

        return answer
