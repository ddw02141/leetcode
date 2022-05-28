class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        # dp[i] is the number of ways to reach 0 starting from position 'i'
        """
        MOD = 10 ** 9 + 7
        needed = min(arrLen, steps + 1)
        dp = [0 for _ in range(needed + 1)]
        dp[0] = 1
        nextDp = [numWay for numWay in dp]
        for step in range(1, steps + 1):
            for pos in range(min(step + 1, needed)):
                if pos == 0:
                    nextDp[pos] = dp[pos] + dp[pos + 1]
                else:
                    nextDp[pos] = dp[pos - 1] + dp[pos] + dp[pos + 1]

            dp, nextDp = nextDp, dp

        return dp[0] % MOD
