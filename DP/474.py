from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        knapsack: m 0s and n 1s`
        """
        l = len(strs)
        zerosAndOnesCounts = []
        strToZerosAndOnesCount = dict()
        for s in strs:
            if s in strToZerosAndOnesCount:
                zerosAndOnesCounts.append(strToZerosAndOnesCount[s])
            else:
                zerosAndOnesCount = s.count("0"), s.count("1")
                zerosAndOnesCounts.append(zerosAndOnesCount)
                strToZerosAndOnesCount[s] = zerosAndOnesCount
        # dp[i][j][k]: maximum subset count when using strs[:i] with j 0s & k 1s
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            zerosAndOnesCount = zerosAndOnesCounts[i - 1]
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zerosAndOnesCount[0] and k >= zerosAndOnesCount[1]:
                        dp[i][j][k] = max(dp[i - 1][j][k],
                                          1 + dp[i - 1][j - zerosAndOnesCount[0]][k - zerosAndOnesCount[1]])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[l][m][n]
