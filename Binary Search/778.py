from collections import deque


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        0 <= elevation <= 2500
        for elevation in range(2500, 0)
            dfs(0, 0)
            if meet bottom right square:
                update answer to elevation
            if not:
                return answer
        """
        n = len(grid)
        left = grid[0][0]
        right = n * n - 1
        while left < right:
            mid = (left + right) // 2
            if self.isReachable(n, mid, grid):
                right = mid
            else:
                left = mid + 1

        return right

    def isReachable(self, n, elevation, grid):
        q = deque([(0, 0)])
        visited = set()
        while q:
            x, y = q.popleft()
            if grid[x][y] > elevation or (x, y) in visited:
                continue
            visited.add((x, y))
            if x == n - 1 and y == n - 1:
                return True
            for newX, newY in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if newX < 0 or newX >= n or newY < 0 or newY >= n:
                    continue
                q.append((newX, newY))
        return False
