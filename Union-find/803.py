# https://leetcode.com/problems/bricks-falling-when-hit/discuss/195781/Union-find-Logical-Thinking
from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.m = 0
        self.n = 0
        self.parent = None
        self.size = None

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        if not grid:
            return [0 for _ in range(len(hits))]
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        maxIdx = self.m * self.n
        self.parent = [i for i in range(maxIdx + 1)]  # 0 indicates top of the grid, which is not visible
        self.size = [1 for _ in range(maxIdx + 1)]

        """
        Mark cells to hit as 2 if block exists
        """
        for x, y in hits:
            if self.grid[x][y] == 1:
                self.grid[x][y] = 2
        """
        Union around 1 cells
        """
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.unionAround(i, j)
        # print(self.parent)
        # print()
        # print(self.size)
        # num bricks after last erasure
        numBricksLeft = self.size[self.find(0)]
        reversedNumBricksDropped = [0 for _ in range(len(hits))]
        reversedHits = hits[::-1]
        for i, hit in enumerate(reversedHits):
            x, y = hit
            if self.grid[x][y] == 2:
                self.grid[x][y] = 1
                self.unionAround(x, y)
                newNumBricksLeft = self.size[self.find(0)]
                reversedNumBricksDropped[i] = max(0, newNumBricksLeft - numBricksLeft - 1)
                numBricksLeft = newNumBricksLeft

        return reversedNumBricksDropped[::-1]

    def unionAround(self, i, j):
        idx = self.getIdx(i, j)
        for newI, newJ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if newI < 0 or newI >= self.m or newJ < 0 or newJ >= self.n or self.grid[newI][newJ] != 1:
                continue
            self.union(idx, self.getIdx(newI, newJ))

        # Union to top of the grid(idx=0) if i == 0
        if i == 0:
            self.union(0, idx)

    def getIdx(self, i, j):
        return i * self.n + j + 1

    def union(self, idx1, idx2):
        root1 = self.find(idx1)
        root2 = self.find(idx2)

        if root1 != root2:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]


if __name__ == "__main__":
    # solution1 = Solution()
    # print(solution1.hitBricks([[1, 0, 0, 0],
    #                            [1, 1, 1, 0]], [[1, 0]]))
    # solution2 = Solution()
    # print(solution2.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]))
    solution3 = Solution()
    print(solution3.hitBricks([[1, 1, 1],
                               [0, 1, 0],
                               [0, 0, 0]],
                              [[0, 2], [2, 0], [0, 1], [1, 2]]))
