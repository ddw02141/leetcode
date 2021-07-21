# https://leetcode.com/problems/next-greater-element-iii/
from bisect import bisect_right


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        INT_MAX = 2_147_483_647
        s = str(n)
        l = [int(ss) for ss in s[::-1]]
        sortedL = []
        idx1 = -1
        idx2 = -1
        for i, d in enumerate(l):
            if not sortedL:
                sortedL.append(d)
            elif sortedL[-1] <= d:
                sortedL.append(d)
            else:
                idx1 = len(s) - 1 - i
                idx2 = len(s) - 1 - bisect_right(sortedL, d)
                break
        if idx1 == -1:
            return -1
        answerList = list(s)
        answerList[idx1], answerList[idx2] = answerList[idx2], answerList[idx1]
        answerList[idx1+1:] = sorted(answerList[idx1+1:])
        answer = int("".join(answerList))
        if answer > INT_MAX:
            return -1
        return answer