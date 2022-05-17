from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left, right = 0, 0
        n = len(nums)
        cur = nums[0]
        answer = float("inf")
        while left < n and right < n:
            if cur >= target:
                answer = min(answer, right - left + 1)
                if left == right:
                    right += 1
                    if right < n:
                        cur += nums[right]
                else:
                    cur -= nums[left]
                    left += 1
            else:
                right += 1
                if right < n:
                    cur += nums[right]

        return answer
