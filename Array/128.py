from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        numSet = set(nums)
        for num in numSet:
            if num + 1 in numSet:
                continue
            count = 0
            while num in numSet:
                num -= 1
                count += 1
            answer = max(answer, count)
        return answer
