from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0
        numOne = sum(sum(row) for row in grid)
        if numOne == 0 or numOne == n ** 2:
            return -1
        visited = [[False for _ in range(n)] for _ in range(n)]
        q = set()
        numZero = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.add((i, j))
                    visited[i][j] = True
                else:
                    numZero += 1
        while numZero > 0:
            q, numZero = self.spread(n, numZero, q, grid, visited)
            answer += 1
        return answer

    def spread(self, n, numZero, q, grid, visited):
        newQ = set()
        for i, j in q:
            for newI, newJ in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= newI < n and 0 <= newJ < n and not visited[newI][newJ] and grid[newI][newJ] == 0:
                    visited[newI][newJ] = True
                    grid[newI][newJ] = 1
                    newQ.add((newI, newJ))
                    numZero -= 1
        return newQ, numZero


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(solution.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(solution.maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
