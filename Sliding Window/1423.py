from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        == Find min score subList that have length len(cardPoints) - k
        """
        # n = len(cardPoints)
        # sumPoints = sum(cardPoints)
        # minSum = float("inf")
        # w = n - k
        # if w == 0:
        #     return sumPoints
        # cur = sum(cardPoints[:w - 1])
        # for i in range(n - w + 1):  # (n - w) + w - 1 = n - 1
        #     cur += cardPoints[i + w - 1]
        #     # print("i: ", i, "cur:", cur)
        #     minSum = min(minSum, cur)
        #     cur -= cardPoints[i]
        #
        # return sumPoints - minSum

        n = len(cardPoints)
        minSum = float("inf")
        w = n - k
        sumPoints, cur = 0, 0
        i = 0
        for j, cardPoint in enumerate(cardPoints):
            cur += cardPoint
            sumPoints += cardPoint
            if j - i + 1 > w:
                cur -= cardPoints[i]
                i += 1
            if j - i + 1 == w:
                if cur < minSum:
                    minSum = cur

        return sumPoints - minSum
