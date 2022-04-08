from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j] = matrix[0][0] ~ matrix[i][j]까지의 sum
        if dp[r2][c2] - dp[r1][c1] == (r2 - r1) * (c2 - c2)
        then update answer!
        """
        answer = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 0:
                    if j == 0:
                        dp[i][j] = int(matrix[i - 1][j - 1])
                    else:
                        dp[i][j] = dp[i][j - 1] + int(matrix[i - 1][j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + int(matrix[i - 1][j - 1])
                else:  # 0 < i and 0 < j
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + int(matrix[i - 1][j - 1])
        # for d in dp:
        #     print(d)

        for r1 in range(1, m + 1):
            for c1 in range(1, n + 1):
                for diff in range(min(m - r1, n - c1) + 1)[::-1]:
                    r2, c2 = r1 + diff, c1 + diff
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if area <= answer:
                        break
                    if dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1] == area:
                        # print("(%s, %s), (%s, %s) : %d" %(r1, c1, r2, c2, (r2 - r1 + 1) * (c2 - c1 + 1)))
                        answer = max(answer, area)
                        break

        return answer
