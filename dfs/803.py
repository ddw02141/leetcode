class Solution:
    def __init__(self):
        self.grid = None
        self.m = 0
        self.n = 0

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        if not grid:
            return [0 for _ in range(len(hits))]
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for x, y in hits:
            self.dfs(x, y)

    def dfs(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return
        if self.grid[x][y] == 0:
            return

        # for newX, newY in [(x + 1, y)]
