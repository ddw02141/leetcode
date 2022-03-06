from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        answer = 0
        d = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                d[n1 + n2] += 1

        for n3 in nums3:
            for n4 in nums4:
                if -n3 - n4 in d:
                    answer += d[-n3 - n4]

        return answer
