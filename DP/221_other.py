from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        answer = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
                    if answer < dp[i + 1][j + 1]:
                        answer = dp[i + 1][j + 1]

        return answer * answer
