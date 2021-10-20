from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            visited[x][y] = True
            if dp[x][y] != 0:
                return dp[x][y]
            count = 1
            for newX, newY in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= newX < m and 0 <= newY < n:
                    if matrix[newX][newY] > matrix[x][y]:
                        if not visited[newX][newY]:
                            count = max(count, dfs(newX, newY) + 1)
                        else:
                            count = max(count, dp[newX][newY] + 1)
            dp[x][y] = count
            return count

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    dfs(i, j)

        answer = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] > answer:
                    answer = dp[i][j]
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath([[9, 9, 4],
                                          [6, 6, 8],
                                          [2, 1, 1]]))  # Expect 4
    print(solution.longestIncreasingPath([[3, 4, 5],
                                          [3, 2, 6],
                                          [2, 2, 1]]))  # Expect 4
