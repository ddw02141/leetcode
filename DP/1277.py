from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        1. Brute Force
        When meet 1, +1
        Then check left, top, and left-top is 1 -> If yes, plus another 1Then check ...
        [0, 1, 1, 1]
        [1, 1, 2, 2]
        [0, 1, 2, 3] => 15
        2. DP
        Memoize max square size
        [0,1,1,1]
        [1,1,2,2]
        [0,1,2,3]
        if matrix[i][j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
        return sum(sum(row) for row in dp)
