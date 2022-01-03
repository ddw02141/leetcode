from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0
        if self.isAllZero(n, grid) or self.isAllOne(n, grid):
            return -1
        q = list()
        numZero = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                else:
                    numZero += 1
        while numZero > 0:
            q, numZero = self.spread(n, numZero, q, grid)
            answer += 1
        return answer

    def isAllZero(self, n, grid):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return False
        return True

    def isAllOne(self, n, grid):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    return False
        return True

    def spread(self, n, numZero, q, grid):
        newQ = list()
        for i, j in q:
            for newI, newJ in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= newI < n and 0 <= newJ < n and grid[newI][newJ] == 0:
                    grid[newI][newJ] = 1
                    newQ.append((newI, newJ))
                    numZero -= 1
        return newQ, numZero


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(solution.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(solution.maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
