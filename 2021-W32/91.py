class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = i번째 string까지 decode 가능한 경우의 수
        slen = len(s)
        dp = [0 for _ in range(slen)]
        for i in range(slen):
            print(dp)
            if i == 0:
                if '1' <= s[i] <= '9':
                    dp[i] = 1
            elif i == 1:
                if '1' <= s[i] <= '9':
                    dp[i] = dp[i - 1]
                if '10' <= s[i - 1:i + 1] <= '26':
                    dp[i] = dp[i] + 1
            else:
                if '1' <= s[i] <= '9':
                    dp[i] = dp[i - 1]
                if '10' <= s[i - 1:i + 1] <= '26':
                    dp[i] = dp[i] + dp[i - 2]
        return dp[-1]
