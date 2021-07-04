# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def first():
            for i in range(X):
                for j in range(Y):
                    if grid[i][j]:
                        return i, j
        borders = list()
        X = len(grid)
        Y = len(grid[0])
        answer = 0
        def dfs(x, y):
            grid[x][y] = -1
            borders.append((x,y))
            # adj = 0
            for newX, newY in ((x+1,y), (x,y+1),(x-1,y),(x,y-1)):
                if 0 <= newX < X and 0 <= newY < Y and grid[newX][newY] == 1:
                    # adj += 1
                    dfs(newX, newY)
            # if adj < 4:
            #     borders.append((x,y))
        dfs(*first())
        while borders:
            newBorders = []
            for x, y in borders:
                for newX, newY in ((x+1,y), (x,y+1),(x-1,y),(x,y-1)):
                    if 0 <= newX < X and 0 <= newY < Y:
                        if grid[newX][newY] == 1:
                            return answer
                        elif grid[newX][newY] == 0:
                            grid[newX][newY] = -1
                            newBorders.append((newX, newY))
            borders = newBorders
            answer += 1
