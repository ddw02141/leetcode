class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        Input: steps = 4, arrLen = 2
        Output: 8
        s s s s

        l r s s
        s l r s
        s s l r
        l s r s
        l s s r
        s l s r

        l r l r
        dp[i][j]: Number of cases that can be located at j index after i steps
        answer = dp[steps][0]
        dp[i][j] = dp[i - 1][j] \ # step i: stay
            + dp[i - 1][j + 1] \ # step i: left
            + dp[i - 1][j - 1] \ # step i: right
        """
        MOD = 10 ** 9 + 7
        needed = min(arrLen, steps + 1)
        dp = [[0 for _ in range(needed + 1)] for _ in range(steps + 1)]
        dp[0][0] = 1
        for step in range(1, steps + 1):
            for pos in range(min(step + 1, needed)):
                if pos == 0:
                    dp[step][pos] = (dp[step - 1][pos] + dp[step - 1][pos + 1]) % MOD
                elif pos == needed - 1:
                    dp[step][pos] = (dp[step - 1][pos] + dp[step - 1][pos - 1]) % MOD
                else:
                    dp[step][pos] = (dp[step - 1][pos] + dp[step - 1][pos + 1] + dp[step - 1][pos - 1]) % MOD

        return dp[steps][0]
