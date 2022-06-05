from typing import List

rowcol = [[-1, 0], [0, -1], [1, 0], [0, 1]]


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Solution:

    def __init__(self):
        self.parent = list()
        self.rank = list()
        self.n = 0
        self.m = 0

    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        # write your code here
        """
        union-find : Union by rank and path compression
        1 1 0
        0 0 0
        0 0 1
        """
        self.n, self.m = n, m
        maxIdx = n * m
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        self.parent = [i for i in range(maxIdx)]
        self.rank = [1 for _ in range(maxIdx)]
        answer = list()
        numIsland = 0
        for point in operators:
            x, y = point.x, point.y
            if not matrix[x][y]:
                for row, col in rowcol:
                    newX, newY = x + row, y + col
                    if newX < 0 or newX >= n or newY < 0 or newY >= m:
                        continue
                    if matrix[newX][newY]:
                        numIsland += self.union(self.getIdx(x, y), self.getIdx(newX, newY))
                matrix[x][y] = 1
                numIsland += 1
            answer.append(numIsland)

        return answer

    def getIdx(self, x, y):
        return x * self.m + y

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, n1, n2):
        r1 = self.find(n1)
        r2 = self.find(n2)
        if r1 == r2:
            return 0

        if self.rank[r1] < self.rank[r2]:
            self.parent[r2] = r1
        elif self.rank[r1] > self.rank[r2]:
            self.parent[r1] = r2
        else:  # self.rank[r1] == self.rank[r2]
            self.parent[r2] = r1
            self.rank[r2] += 1

        return -1
