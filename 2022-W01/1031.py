from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], l: int, m: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        maxl = maxm = summ = 0
        for i in range(m, len(prefix) - l):
            maxm = max(maxm, prefix[i] - prefix[i - m])
            summ = max(summ, maxm + prefix[i + l] - prefix[i])
        for i in range(l, len(prefix) - m):
            maxl = max(maxl, prefix[i] - prefix[i - l])
            summ = max(summ, maxl + prefix[i + m] - prefix[i])
        return summ
