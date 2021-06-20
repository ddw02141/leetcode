# arr.length <= 2 * 10^4
from bisect import bisect_left

class Solution:

    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        orderedOddJump = [(arr[-1], n - 1)]
        orderedEvenJump = [(-arr[-1], n - 1)]
        higher, lower = [False for _ in range(n)], [False for _ in range(n)]
        higher[-1] = lower[-1] = True
        for i in range(n - 1)[::-1]:
            hi = bisect_left(orderedOddJump, (arr[i], i))
            if hi < len(orderedOddJump):
                higher[i] = lower[orderedOddJump[hi][1]]
            orderedOddJump.insert(hi, (arr[i], i))
            lo = bisect_left(orderedEvenJump, (-arr[i], i))
            if lo < len(orderedEvenJump):
                lower[i] = higher[orderedEvenJump[lo][1]]
            orderedEvenJump.insert(lo, (-arr[i], i))
        return sum(int(val) for val in higher)