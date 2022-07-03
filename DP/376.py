from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]
        up[0] = 1
        down[0] = 1
        for i, (prev, num) in enumerate(zip(nums, nums[1:])):
            if prev < num:
                up[i + 1] = max(up[i], down[i] + 1)
            elif prev > num:
                down[i + 1] = max(down[i], up[i] + 1)
            else:
                up[i + 1], down[i + 1] = up[i], down[i]

        return max(up[-1], down[-1])
