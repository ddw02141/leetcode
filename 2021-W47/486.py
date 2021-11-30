# https://leetcode.com/problems/predict-the-winner/
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp[i][j]: i~j 까지의 숫자들 중에서 선택할 때 Player 1이 더 얻을 수 있는 점수
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        # dp[0][1] = abs(dp[0][0] - dp[1][1])
        # dp[0][2] = max(dp[0][0] - dp[1][2], dp[2][2] - dp[0][1])
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
