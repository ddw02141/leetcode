from typing import List


class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        # dp[i]: possible max point starts from q[i]
        n = len(q)
        dp = [0 for _ in range(n + 1)]
        for i in range(n)[::-1]:
            if i + q[i][1] + 1 >= n:
                dp[i] = max(dp[i + 1], q[i][0])
            else:
                dp[i] = max(dp[i + 1], q[i][0] + dp[i + q[i][1] + 1])

        return dp[0]
