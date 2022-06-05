from typing import List

DIRECTIONS = [[-1, 0], [0, -1], [1, 0], [0, 1]]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        [
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ]
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            visited[x][y] = True
            if dp[x][y] != -1:
                return dp[x][y]
            ans = 1
            for dx, dy in DIRECTIONS:
                newX, newY = x + dx, y + dy
                if newX < 0 or newX >= m or newY < 0 or newY >= n:
                    continue
                if matrix[x][y] > matrix[newX][newY]:
                    if not visited[newX][newY]:
                        newAns = dfs(newX, newY) + 1
                    else:
                        newAns = dp[newX][newY] + 1

                    if ans < newAns:
                        ans = newAns
            dp[x][y] = ans
            return dp[x][y]

        answer = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    dfs(i, j)
                if answer < dp[i][j]:
                    answer = dp[i][j]

        return answer
