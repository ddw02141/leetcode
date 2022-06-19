from typing import List
from collections import deque


class Solution:

    def shortest_distance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]
        buildings = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.add((i, j))

        def bfs(x, y):
            visited = [[False for _ in range(n)] for _ in range(m)]
            q = deque([(x, y, 0)])
            while q:
                x, y, d = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                dist[x][y] += d
                for newX, newY in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                    if newX < 0 or newX >= m or newY < 0 or newY >= n:
                        continue
                    if not visited[newX][newY] and grid[newX][newY] == 0:
                        q.append((newX, newY, d + 1))
            for i in range(m):
                for j in range(n):
                    # Not reachable empty land
                    # ex) 2 2
                    #     2 0
                    if not visited[i][j] and grid[i][j] == 0:
                        dist[i][j] = float("inf")

        for x, y in buildings:
            bfs(x, y)

        answer = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    answer = min(answer, dist[i][j])

        return answer
