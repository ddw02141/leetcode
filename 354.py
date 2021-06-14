# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def bs(left, right, target):
            result = float("inf")
            while left <= right:
                mid = (left + right) // 2
                if target <= lis[mid]:
                    result = min(result, mid)
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        answer = 0
        for i, envelope in enumerate(envelopes):
            wi, hi = envelope
            if not lis or lis[-1] < hi:
                lis.append(hi)
                answer += 1
            else:
                idx = bs(0, len(lis) - 1, hi)
                if idx != float("inf"):
                    lis[idx] = hi

        return answer