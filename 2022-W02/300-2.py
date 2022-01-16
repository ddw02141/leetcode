from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = list()
        for num in nums:
            if not lis or lis[-1] < num:
                lis.append(num)
            else:
                idx = bisect_left(lis, num)
                lis[idx] = num
        return len(lis)
